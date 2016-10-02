from templating.pipes import *
from templating.io import *
from templating.fillers import *

# Testing the system

pipe = TemplatingPipe(TemplateFileReader('instrument'), TemplateFileWriter('out.ly'))
pipe.setFillers([
    SimpleReplacementFiller({
        'version' : '2.18.2',
        'instrument' : 'violin',
        'instrumentName' : 'Violin',
        'clef' : 'treble',
    }),
    CleanupFiller(),
])
pipe.run()