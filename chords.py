import os
import random

import datetime

from constants import PIANO_ASCII
from constants import BLACK_DOWN_ARROW, BLACK_UP_ARROW
from constants import WHITE_DOWN_ARROW, WHITE_UP_ARROW
from prompts import Prompter
from termutil import clear


class Note:
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

    flats = {
        'Db': [4, 32],
        'Eb': [8, 36],
        'Gb': [16, 44],
        'Ab': [20, 48],
        'Bb': [24, 52],
    }

    def __init__(self, key):
        self.key = key
        self.sharp = False
        self.flat = False
        self.wins = 0
        self.response_times = []

    def get_note_name(self):
        ret = self.key
        if self.sharp:
            ret += '#'
        return ret

    def get_locations(self):
        return self.NOTE_LOCATIONS[self.get_note_name()]

    def get_avg_response(self):
        if self.response_times:
            return round(sum(self.response_times) / len(self.response_times))


class Game:
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

    def __init__(self):
        self.high_score = 0
        if os.path.exists('topscores.txt'):
            try:
                with open('topscores.txt', 'r') as f:
                    for line in f:
                        pass
                    last_line = line.strip()
                    self.high_score = int(last_line)
            except:
                print('Corrupt top score data. Discarding file.')
                os.remove('topscores.txt')
                raise

        self.notes = {}
        for key, data in self.NOTE_DATA.items():
            note = Note(key)
            note.hint = data['hint']
            note.fifth = data['fifth']
            note.maj_tri = data['maj_tri']
            self.notes[key] = note
        self.total_wins = 0
        self.prompter = Prompter()


    def is_lost(self):
        for note in self.notes.values():
            if len(note.response_times) < 2:
                return False
            avg_response = note.get_avg_response()
            if avg_response is not None and avg_response > 3500:
                failure_message = f'Average response time exceeded. Game over.\n\n'
                failure_message += self.get_scoreboard()
                print(failure_message)
                write_log(failure_message)
                return True
        return False

    def write_log(self, failure_message):
        with open("log.txt", "a") as hiscores:
            hiscores.write(f'{datetime.datetime.now().ctime()}\n\n')
            hiscores.write(self.get_scoreboard())
            hiscores.write(f'\n{failure_message}\n')
            hiscores.write(f'\n\nFinal Score: {self.total_wins}\n')
            hiscores.write('-'*30 + '\n\n')
            hiscores.close()
        if game.total_wins > game.high_score:
            banner = '   HIGH SCORE  '
            print(f"{'-' * len(banner)}{banner}{'-' * len(banner)}")
            print(f'  - Old Score {self.high_score}')
            print(f'  - New Score: {self.total_wins}')
            print()
            try:
                with open('topscores.txt', 'a') as topscore:
                    line = str(self.total_wins) + '\n'
                    topscore.write(line)
                    topscore.close()
            except:
                print('Error saving high score file.')
                raise

    def start(self):
        challenge = None
        while True:
            if game.is_lost() == True:
                result = 'Game over because your average time exceeded 3.5 seconds.'
                print(f'Final Score: {game.total_wins}')
                game.write_log(result)
                exit()

            while True:
                new_challenge = random.choice(list(game.notes.values()))
                if new_challenge != challenge:
                    challenge = new_challenge
                    break
            clear()
            print(f'Score: {game.total_wins} | High Score: {game.high_score}')
            print(self.get_scoreboard())
            prompt = self.prompter.get_random_prompt()
            start_time = datetime.datetime.now()
            result = prompt(self, challenge)

            if result is not None:
                print(result)
                print(f'Final Score: {game.total_wins}')
                game.write_log(result)
                exit()

            response_ms = round((datetime.datetime.now() - start_time).total_seconds() * 1000)
            challenge.response_times.append(response_ms)
            game.total_wins += 1

        print(f'Final Score: {game.total_wins}')

    def get_scoreboard(self):
        ret = 'Key | Hits     | Avg Response (ms)\n'
        ret += '-' * len(ret) + '\n'
        for key, note in self.notes.items():
            hits = str(len(note.response_times)).rjust(2, ' ')
            avg_response = '-' if not note.response_times else note.get_avg_response()
            key_label = key.ljust(3, ' ')

            ret += f"{key_label} | Hits: {hits} | {avg_response}\n"
        return ret

    def draw_piano(self, locations):
        piano_lines = PIANO_ASCII.splitlines()
        line = list(piano_lines[0])
        for location in locations:
            line[location[0]] = BLACK_DOWN_ARROW if location[1] is True else WHITE_DOWN_ARROW
        piano_lines[0] = ''.join(line)
        line = list(piano_lines[-1])
        for location in locations:
            line[location[0]] = BLACK_UP_ARROW if location[1] is True else WHITE_UP_ARROW
        piano_lines[-1] = ''.join(line)

        return '\n'.join(piano_lines)


game = Game()
game.start()
