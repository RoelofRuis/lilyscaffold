from pipes import *
from io import *
from fillers import *

class LilypondFactory():
    def createTemplate(self, template, out, replacements):
        pipe = TemplatingPipe(
            TemplateFileReader(template),
            TemplateFileWriter(out)
        )
        pipe.setFillers([
            VersionFiller(),
            LoopingReplacementFiller(replacements),
            CleanupFiller(),
        ])
        return pipe