from templating.factory import *

factory = LilypondFactory()

# Options file
factory.createTemplate('options', 'options.ly', {
    'version' : '2.18.2',
    'time'    : '4/4',
    'tempo'   : '4 = 120',
    'key'     : 'c \minor',
}).run()

factory.createTemplate('instrument', 'violin.ly', {
    'version'        : '2.18.2',
    'instrument'     : 'violin',
    'clef'           : 'treble',
    'instrumentName' : 'violin',
}).run()

factory.createTemplate('instrument', 'guitar.ly', {
    'version'        : '2.18.2',
    'instrument'     : 'guitar',
    'clef'           : 'treble',
    'instrumentName' : 'guitar',
}).run()

factory.createTemplate('main', 'main.ly', {
    'version'     : '2.18.2',
    'title'       : 'Title',
    'subtitle'    : 'Subtitle',
    'composer'    : 'Roelof Ruis',
    'meter'       : '',
    'piece'       : '',
    'instruments' : [
        {
            'instrumentName' : 'violin',
        },
        {
            'instrumentName' : 'guitar',
        }
    ]
}).run()