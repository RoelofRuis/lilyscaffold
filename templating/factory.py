from pipes import *
from io.input import *
from io.output import *
from fillers import *
from os.path import join

class LilypondFactory():
    def __init__(self, projectName):
        self.projectName = projectName
        self.versionFiller = VersionFiller()
        self.cleanupFiller = CleanupFiller()

    def buildProject(self):
        configReader = ProjectConfigReader(self.projectName)
        config       = configReader.getConfig()
        sourceFolder = join(self.projectName, config['meta']['sourceFolder'])
        self.createTemplate('options', join(sourceFolder, 'options.ly'), config['options']).run()
        for instrument in config['instruments']:
            self.createTemplate('instrument', join(sourceFolder, instrument['instrumentName'] + '.ly'), instrument).run()
        mainReplacements = config['general'].copy()
        mainReplacements.update({'instruments' : config['instruments']})
        self.createTemplate('main', join(sourceFolder, 'main.ly'), mainReplacements).run()

    def createTemplate(self, template, outPath, replacements):
        pipe = TemplatingPipe(
            TemplateFileReader(template),
            TemplateFileWriter(outPath)
        )
        pipe.setFillers([
            self.versionFiller,
            LoopingReplacementFiller(replacements),
            self.cleanupFiller,
        ])
        return pipe