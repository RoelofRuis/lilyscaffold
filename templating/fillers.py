from os.path import join
import re

# Defines a basic filler
class Filler():
    def fill(self, lines):
        linesOut = []
        for line in lines:
            linesOut.append(self.processLine(line))
        return linesOut

    def processLine(self, line):
        raise NotImplementedError('Fillers should implement process line.')

# Replaces simple statements from a list of replacements.
class SimpleReplacementFiller(Filler):
    def __init__(self, replacements = {}):
        self.replacements = replacements
            
    def processLine(self, line):
        matches = re.findall(r'@([a-z_]+?)!', line)
        for match in matches:
            replacement = self.findReplacement(match)
            if replacement:
                line = re.sub(r'@' + match + '!', replacement, line)
        return line
            
    def findReplacement(self, item):
        if item in self.replacements:
            return self.replacements[item]
        else:
            return False
            
# Cleans up simple statements
class CleanupFiller(Filler):
    def processLine(self, line):
        return re.sub(r'@([a-z_]+?)!', '', line)