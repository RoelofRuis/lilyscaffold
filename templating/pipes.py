# For piping input to output with the fillers in between
class TemplatingPipe():
    def __init__(self, input, output):
        self.input  = input
        self.output = output
        self.fillers = []
        
    def setFillers(self, fillers):
        self.fillers = fillers
        
    def run(self):
        lines = self.input.getLines()
        for filler in self.fillers:
            lines = filler.fill(lines)
        self.output.outputLines(lines)