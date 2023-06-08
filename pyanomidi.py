import pygame
import pygame.midi
import time


class MidiReader:
    ''' A class which reads midi input data from attached midi device. '''

    def read_chord(self):
        '''
        Reads and decodes note data from a set of keys all pressed
        within 3/4 second.
        '''
        pygame.init()
        pygame.midi.init()
        input_id = int(pygame.midi.get_default_input_id())
        self.midi_input = pygame.midi.Input(input_id)
        chord_timeout = 0
        chord = []
        while True:
            if chord:
                chord_timeout += 1
            if self.midi_input.poll():
                data = self.midi_input.read(1)
                action, note, velocity, _ = data[0][0]
                note_name = pygame.midi.midi_to_ansi_note(note)
                if action == 144:
                    chord.append(note_name)
                # print(str(pygame.midi.Input.read(1)))
            if chord_timeout > 75:
                # print(f'action: {action}, note: {note_name}, velocity: {velocity}')
                return chord
            time.sleep(0.01)
