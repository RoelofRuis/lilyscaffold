from templating.factory import *

factory = LilypondFactory()

general = {
    'title'       : 'Title',
    'subtitle'    : 'Subtitle',
    'composer'    : 'Roelof Ruis',
}

options = {
    'time'    : '4/4',
    'tempo'   : '4 = 120',
    'key'     : 'c \minor',
}

instruments = [
    {
        'instrument'     : 'violin',
        'clef'           : 'treble',
        'instrumentName' : 'violin',
    },
    {
        'instrument'     : 'guitar',
        'clef'           : 'treble',
        'instrumentName' : 'guitar',
    }
]

factory.createProject(general, options, instruments)