from templating.pipes import *
from templating.io import *
from templating.fillers import *

# Testing the system

pipe = TemplatingPipe(TemplateFileReader('options'), TemplateFileWriter('optionstest.txt'))
pipe.setFillers([
    SimpleReplacementFiller({
        'version' : '2.18.2',
        'time' : '4/4',
        'tempo' : '4 = 120',
        'key' : 'c \major',
    }),
    CleanupFiller(),
])
pipe.run()