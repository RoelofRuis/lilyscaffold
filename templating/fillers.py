from os.path import join
from subprocess import Popen, PIPE
import re

class Filler():
    def fill(self, lines):
        linesOut = []
        for line in lines:
            linesOut.append(self.processLine(line))
        return linesOut

    def processLine(self, line):
        raise NotImplementedError('Fillers should implement process line.')


class LoopingReplacementFiller(Filler):
    def __init__(self, replacements = {}):
        self.replacements = replacements

    def fill(self, lines):
        return self.fillInner(lines, self.replacements)

    def fillInner(self, lines, replacements):
        linesOut  = []
        loop      = False
        loopLines = []
        for line in lines:
            if loop:
                noloop = re.search(r'!([a-zA-Z_]+?):', line)
                if noloop:
                    if loop in replacements:
                        for loopReplacement in replacements[loop]:
                            linesOut += self.fillInner(loopLines, loopReplacement)
                    loop      = False
                    loopLines = []
                else:
                    loopLines.append(line)
            else:
                loopName = re.search(r'@([a-zA-Z_]+?):', line)
                if not loopName:
                    linesOut.append(self.processLine(line, replacements))
                else:
                    loop = loopName.group(1)
        return linesOut

    def processLine(self, line, replacements):
        matches = re.findall(r'@([a-zA-Z_]+?)!', line)
        for match in matches:
            if match in replacements:
                line = re.sub(r'@' + match + '!', replacements[match], line)
        return line

class VersionFiller(Filler):
    def __init__(self):
        process = Popen(["lilypond", "--version"], stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        if exit_code == 0:
            versionMatch = re.search(r'GNU LilyPond ([0-9\.]+)', output)
            if versionMatch:
                self.version = versionMatch.group(1)
        else:
            self.version = False

    def processLine(self, line):
        match = re.search(r'\\version', line)
        if match:
            if self.version:
                return '\\version "' + self.version + "\"\n"
            else:
                return ''
        else:
            return line

class CleanupFiller(Filler):
    def processLine(self, line):
        match = re.search(r'@([a-zA-Z_]+?)!', line)
        if match:
            return ''
        else:
            return line