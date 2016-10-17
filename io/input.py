from os.path import join
from yaml    import load
from config  import GLOBAL_CONFIG

class ProjectConfigReader():
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

class TemplateFileReader():
    def __init__(self, templateName):
        self.templatePath = join(GLOBAL_CONFIG.get('fileTemplateFolder', 'templates\\files\\'), templateName + '.lyt')

    def getLines(self):
        with open(self.templatePath, 'r') as template:
            lines = template.readlines()
        return lines