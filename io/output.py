import os
from shutil  import copyfile
from os.path import join

from config  import GLOBAL_CONFIG

class ProjectFileWriter():
    def __init__(self, projectName):
        self.projectName = projectName

    def _setupFolderIfNotExists(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def setupProjectStructure(self):
        projectFolder = join(GLOBAL_CONFIG.get('projectFolder', 'out\\'), self.projectName)
        self._setupFolderIfNotExists(projectFolder)
        self._setupFolderIfNotExists(join(projectFolder, GLOBAL_CONFIG.get('metaFolderName', 'meta')))
        self._setupFolderIfNotExists(join(projectFolder, GLOBAL_CONFIG.get('sourceFolderName', 'src')))
        self._setupFolderIfNotExists(join(projectFolder, GLOBAL_CONFIG.get('outputFolderName', 'out')))

    def setupTemplate(self, templateName):
        src = join(
            GLOBAL_CONFIG.get('projectTemplateFolder','templates\\projects\\'),
            templateName + '.yml'
        )
        dst = join(
            GLOBAL_CONFIG.get('projectFolder', 'out\\'),
            self.projectName,
            GLOBAL_CONFIG.get('metaFolderName', 'meta') + '\\',
            GLOBAL_CONFIG.get('projectConfigFileName', 'config.yml')
        )
        copyfile(src, dst)
        
class TemplateFileWriter():
    def __init__(self, targetPath):
        self.targetPath = targetPath

    def outputLines(self, lines):
        with open(join(GLOBAL_CONFIG.get('projectFolder', 'out\\'), self.targetPath), 'w') as target:
            for line in lines:
                target.write(line)