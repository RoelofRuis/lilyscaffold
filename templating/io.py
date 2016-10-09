from os.path import join

# Defines input classes
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