from pipes import *
from io import *
from fillers import *

class LilypondFactory():
    def createProject(self, general, options, instruments):
        self.versionFiller = VersionFiller()
        self.cleanupFiller = CleanupFiller()
        self.createTemplate('options', 'options.ly', options).run()
        for instrument in instruments:
            self.createTemplate('instrument', instrument['instrumentName'] + '.ly', instrument).run()
        mainReplacements = general.copy()
        mainReplacements.update({'instruments' : instruments})
        self.createTemplate('main', 'main.ly', mainReplacements).run()

    def createTemplate(self, template, out, replacements):
        pipe = TemplatingPipe(
            TemplateFileReader(template),
            TemplateFileWriter(out)
        )
        pipe.setFillers([
            self.versionFiller,
            LoopingReplacementFiller(replacements),
            self.cleanupFiller,
        ])
        return pipe