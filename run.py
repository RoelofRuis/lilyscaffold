from templating.pipes import *
from templating.io import *
from templating.fillers import *

# Testing the system

pipe = TemplatingPipe(TemplateFileReader('main'), TemplateFileWriter('out.ly'))
pipe.setFillers([
    LoopingReplacementFiller({
        'version' : '2.18.2',
        'title' : 'Title',
        'subtitle' : 'Subtitle',
        'composer' : 'Roelof Ruis',
        'meter' : '',
        'piece' : '',
        'instruments' : [
            {
                'instrumentName' : 'violin',
            },
            {
                'instrumentName' : 'guitar',
            }
        ]
    }),
    CleanupFiller(),
])
pipe.run()