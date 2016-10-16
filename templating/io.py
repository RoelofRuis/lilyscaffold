import os
from shutil import copyfile
from os.path import join
from os import walk
from yaml import load
from config import GLOBAL_CONFIG

def getAvailableProjects():
    (_,_, files) = walk(GLOBAL_CONFIG.get('projectTemplateFolder', 'templates\\projects\\')).next()
    filenames = [os.path.splitext(f)[0] for f in files]
    return filenames

# Input classes
class ProjectInput():
    def getConfig(self):
        raise NotImplementedError('Project Input should implement the getConfig() method')

class ProjectConfigReader(ProjectInput):
    def __init__(self, projectName):
        self.projectConfig = join(
            GLOBAL_CONFIG.get('projectFolder', 'out\\'),
            projectName,
            GLOBAL_CONFIG.get('metaFolderName', 'meta') + '\\',
            GLOBAL_CONFIG.get('projectConfigFileName', 'config.yml'))

    def getConfig(self):
        with open(self.projectConfig, 'r') as f:
            data = load(f)
        return data

class TemplateInput():
    def getLines(self):
        raise NotImplementedError('Template Input should implement the getLines() method')

class TemplateFileReader(TemplateInput):
    def __init__(self, templateName):
        self.templatePath = join(GLOBAL_CONFIG.get('fileTemplateFolder', 'templates\\files\\'), templateName + '.lyt')

    def getLines(self):
        with open(self.templatePath, 'r') as template:
            lines = template.readlines()
        return lines

# Defines output classes
class ProjectWriter():
    def setupProjectStructure(self):
        raise NotImplementedError('Project Writer should implement setupProject() method')

    def setupTemplate(self):
        raise NotImplementedError('Project Writer should implement setupTemplate() method')

class ProjectFileWriter(ProjectWriter):
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

class TemplateOutput():
    def outputLines(self):
        raise NotImplementedError('Template Output should implement outputLines() method')
        
class TemplateFileWriter(TemplateOutput):
    def __init__(self, targetPath):
        self.targetPath = targetPath

    def outputLines(self, lines):
        with open(join(GLOBAL_CONFIG.get('projectFolder', 'out\\'), self.targetPath), 'w') as target:
            for line in lines:
                target.write(line)