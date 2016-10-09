import os
from shutil import copyfile
from os.path import join
from os import walk
from yaml import load

def getAvailableProjects():
    (_,_, files) = walk('templates\\projects\\').next()
    filenames = [os.path.splitext(f)[0] for f in files]
    return filenames

# Input classes
class ProjectInput():
    def getConfig(self):
        raise NotImplementedError('Project Input should implement the getConfig() method')

class ProjectConfigReader(ProjectInput):
    def __init__(self, projectName):
        self.projectConfig = join('out\\', projectName, 'meta\\', 'config.yml')

    def getConfig(self):
        with open(self.projectConfig, 'r') as f:
            data = load(f)
        return data

class TemplateInput():
    def getLines(self):
        raise NotImplementedError('Template Input should implement the getLines() method')

class TemplateFileReader(TemplateInput):
    def __init__(self, templateName):
        self.templatePath = join('templates\\files\\', templateName + '.lyt')

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
        projectFolder = join('out\\', self.projectName)
        self._setupFolderIfNotExists(projectFolder)
        self._setupFolderIfNotExists(join(projectFolder, 'meta'))
        self._setupFolderIfNotExists(join(projectFolder, 'src'))
        self._setupFolderIfNotExists(join(projectFolder, 'out'))

    def setupTemplate(self, templateName):
        src = join('templates\\projects\\', templateName + '.yml')
        dst = join('out\\', self.projectName, 'meta\\', 'config.yml')
        copyfile(src, dst)

class TemplateOutput():
    def outputLines(self):
        raise NotImplementedError('Template Output should implement outputLines() method');
        
class TemplateFileWriter(TemplateOutput):
    def __init__(self, targetPath):
        self.targetPath = targetPath

    def outputLines(self, lines):
        with open(join('out\\', self.targetPath), 'w') as target:
            for line in lines:
                target.write(line)