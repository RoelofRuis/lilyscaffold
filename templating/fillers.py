from os.path import join
import re

# Defines a basic filler
class Filler():
    def fill(self, lines):
        raise NotImplementedError('Fillers should implement fill')

# Replaces simple statements from a list of replacements.
class SimpleReplacementFiller(Filler):
    def __init__(self, replacements = {}):
        self.replacements = replacements

    def fill(self, lines):
        linesOut = []
        for line in lines:
            linesOut.append(self.processLine(line))
        return linesOut
            
    def processLine(self, line):
        matches = re.findall(r'@(.+?)!', line)
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
    def fill(self, lines):
        linesOut = []
        for line in lines:
            linesOut.append(self.processLine(line))
        return linesOut
      
    def processLine(self, line):
        return re.sub(r'@(.+?)!', '', line)