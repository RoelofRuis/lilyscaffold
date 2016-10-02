from templating.factory import *

# Testing the system
factory = LilypondFactory()

factory.createTemplate('main', 'out.ly', {
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
}).run()