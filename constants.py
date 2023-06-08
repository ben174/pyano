BLACK_DOWN_ARROW = '\u25BC'
BLACK_UP_ARROW = '\u25B2'
WHITE_DOWN_ARROW = '\u25BD'
WHITE_UP_ARROW = '\u25B3'

PIANO_ASCII = ''' _______________________________________________________
|  |#| |#|  |  |#| |#| |#|  |  |#| |#|  |  |#| |#| |#|  |
|  |#| |#|  |  |#| |#| |#|  |  |#| |#|  |  |#| |#| |#|  |
|  |#| |#|  |  |#| |#| |#|  |  |#| |#|  |  |#| |#| |#|  |
|  |#| |#|  |  |#| |#| |#|  |  |#| |#|  |  |#| |#| |#|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|'''

PIANO_ASCII = PIANO_ASCII.replace('#', '\u2588')

NOTE_LOCATIONS = {
    'C#': [4, 32],
    'D#': [8, 36],
    'F#': [16, 44],
    'G#': [20, 48],
    'A#': [24, 52],
    'C': [2, 30],
    'D': [6, 34],
    'E': [10, 38],
    'F': [14, 42],
    'G': [18, 46],
    'B': [26, 54],
    'A': [22, 50],
}

NOTE_DATA = {
    'C': {'base': 'C', 'fifth': 'G', 'maj_tri': 'E', 'hint': 'corgie / computer graphics'},
    'C#': {'base': 'C#', 'fifth': 'G#', 'maj_tri': 'F', 'hint': 'corgie / computer graphics'},
    'D': {'base': 'D', 'fifth': 'A', 'maj_tri': 'F#', 'hint': 'district attorney'},
    'D#': {'base': 'D#', 'fifth': 'A#', 'maj_tri': 'G', 'hint': 'district attorney'},
    'E': {'base': 'E', 'fifth': 'B', 'maj_tri': 'G#', 'hint': 'everybody'},
    'F': {'base': 'F', 'fifth': 'C', 'maj_tri': 'A', 'hint': 'funco / funk cat'},
    'F#': {'base': 'F#', 'fifth': 'C#', 'maj_tri': 'A#', 'hint': 'funco / funk cat'},
    'G': {'base': 'G', 'fifth': 'D', 'maj_tri': 'B', 'hint': 'good day / gosh darn'},
    'G#': {'base': 'G#', 'fifth': 'D#', 'maj_tri': 'C', 'hint': 'good day / gosh darn'},
    'A': {'base': 'A', 'fifth': 'E', 'maj_tri': 'C#', 'hint': 'aeiou / titan ae / after effects'},
    'A#': {'base': 'A#', 'fifth': 'F', 'maj_tri': 'D', 'hint': 'aeiou / titan ae / after effects'},
    'B': {'base': 'B', 'fifth': 'F#', 'maj_tri': 'D#', 'hint': 'ben friedland is sharp'},
}