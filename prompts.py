import random
import re

from pyanomidi import MidiReader
from termutil import getch


class Prompter:
    def __init__(self):
        self.midi_reader = MidiReader()

    def get_random_prompt(self):
        return random.choice([self.piano_prompt, self.fifth_prompt, self.chord_prompt])

    def piano_prompt(self, game, note):
        location = random.choice(note.get_locations())
        print(game.draw_piano([(location, True)]))
        print('What note is it?')
        print('   * Use upper case for sharp notes')
        response = getch()
        sharp_response = response[0].isupper()
        response = response.upper()
        if sharp_response:
            response += '#'
        if response != note.key:
            return f'\n - Incorrect response. You indicated {response}, but the note was {note.key}.'

    def fifth_prompt(self, game, note):
        print()
        print(f'Triad for note: {note.key} -> ?')
        print('   * Use upper case for sharp notes')
        response = getch()
        sharp_response = response[0].isupper()
        response = response.upper()
        if not response[0].isalpha():
            return 'Invalid character'
        if sharp_response:
            response += '#'

        if response != note.fifth:
            ret = f'\n - Wrong fifth for note: {note.key}, you indicated: {response}, but the correct fifth is {note.fifth}.\n'
            ret += f' - Hint: {note.hint}\n'
            locations = note.get_locations()
            key_locations = [(loc, True) for loc in locations]
            key_locations.extend([(loc, False) for loc in game.notes[note.fifth].get_locations()])
            key_locations.extend([(loc, False) for loc in game.notes[note.maj_tri].get_locations()])
            ret += '\n' + game.draw_piano(key_locations)
            return ret

    def chord_prompt(self, game, note):
        print()
        print(f'Enter major chord for note: {note.key}')
        print(f'   * Use attached MIDI keyboard')
        response = self.midi_reader.read_chord()
        notes = [re.sub(r'\d', '', r) for r in response]
        correct_chord = set([note.key, note.fifth, note.maj_tri])
        guess_chord = set(notes)
        if correct_chord != guess_chord:
            ret = '\nIncorrect answer!\n'
            ret += f" - Your Input: {', '.join(guess_chord)}\n"
            ret += f" - Correct Chord: {', '.join(correct_chord)}\n"
            return ret
