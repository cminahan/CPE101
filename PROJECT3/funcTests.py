# Project 4 - Word Puzzle
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: 101-03

#two tests for each function

import unittest
from funcs import*

class TestCases(unittest.TestCase):


    #makes the rows of the string into lists
    def test_make_rows(self):
        self.assertEqual(make_rows('WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), [['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'Z', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'W', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']])
        self.assertEqual(make_rows('EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'),  [['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']])

    #makes the columns of the string into lists
    def test_make_columns(self):
        self.assertEqual(make_columns('WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), [['W', 'C', 'A', 'L', 'P', 'O', 'L', 'Y', 'X', 'U'], ['A', 'B', 'Z', 'D', 'O', 'E', 'G', 'C', 'V', 'U'], ['Q', 'M', 'X', 'W', 'N', 'D', 'Q', 'S', 'D', 'I'], ['H', 'I', 'W', 'L', 'D', 'S', 'C', 'L', 'M', 'U'], ['G', 'V', 'K', 'F', 'T', 'O', 'K', 'O', 'G', 'N'], ['T', 'Q', 'W', 'X', 'M', 'Y', 'G', 'A', 'S', 'I'], ['T', 'Q', 'I', 'P', 'V', 'Q', 'M', 'C', 'X', 'X'], ['W', 'E', 'I', 'I', 'A', 'G', 'M', 'U', 'C', 'F'], ['E', 'L', 'I', 'P', 'M', 'O', 'C', 'Z', 'Y', 'N'], ['E', 'S', 'L', 'V', 'N', 'B', 'T', 'M', 'Z', 'U']])
        self.assertEqual(make_columns('EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'),  [['E', 'Z', 'A', 'A', 'C', 'B', 'E', 'A', 'B', 'B'], ['O', 'E', 'R', 'A', 'N', 'O', 'E', 'B', 'O', 'O'], ['A', 'B', 'R', 'C', 'A', 'N', 'R', 'C', 'I', 'A'], ['R', 'R', 'A', 'B', 'B', 'I', 'T', 'E', 'O', 'A'], ['B', 'A', 'C', 'R', 'O', 'R', 'C', 'R', 'R', 'K'], ['R', 'E', 'C', 'R', 'Z', 'B', 'B', 'I', 'O', 'R'], ['N', 'B', 'O', 'C', 'O', 'B', 'R', 'C', 'R', 'K'], ['I', 'R', 'O', 'H', 'B', 'N', 'A', 'R', 'C', 'E'], ['A', 'B', 'N', 'E', 'K', 'C', 'I', 'H', 'C', 'A'], ['B', 'H', 'R', 'C', 'A', 'A', 'A', 'R', 'O', 'R']])

    #searches for a word in the rows forward
    def test_find_horizontal_forward(self):
        self.assertEqual(find_horizontal_forward([['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'Z', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'W', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']], 'UNIX'), (True, 'UNIX: (FORWARD)  row:   9    column:   3'))
        self.assertEqual(find_horizontal_forward([['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']], 'RACOON'), (False, 'not in puzzle'))

    #searches for a word in the rows backward
    def test_find_horizontal_backwards(self):
        self.assertEqual(find_horizontal_backwards([['W', 'A', 'Q', 'H', 'G', 'T', 'T', 'W', 'E', 'E'], ['C', 'B', 'M', 'I', 'V', 'Q', 'Q', 'E', 'L', 'S'], ['A', 'Z', 'X', 'W', 'K', 'W', 'I', 'I', 'I', 'L'], ['L', 'D', 'W', 'L', 'F', 'X', 'P', 'I', 'P', 'V'], ['P', 'O', 'N', 'D', 'T', 'M', 'V', 'A', 'M', 'N'], ['O', 'E', 'D', 'S', 'O', 'Y', 'Q', 'G', 'O', 'B'], ['L', 'G', 'Q', 'C', 'K', 'G', 'M', 'M', 'C', 'T'], ['Y', 'C', 'S', 'L', 'O', 'A', 'C', 'U', 'Z', 'M'], ['X', 'V', 'D', 'M', 'G', 'S', 'X', 'C', 'Y', 'Z'], ['U', 'U', 'I', 'U', 'N', 'I', 'X', 'F', 'N', 'U']], 'VIM'), (True, 'VIM: (BACKWARD) row:  1    column:  4'))
        self.assertEqual(find_horizontal_backwards([['E', 'O', 'A', 'R', 'B', 'R', 'N', 'I', 'A', 'B'], ['Z', 'E', 'B', 'R', 'A', 'E', 'B', 'R', 'B', 'H'], ['A', 'R', 'R', 'A', 'C', 'C', 'O', 'O', 'N', 'R'], ['A', 'A', 'C', 'B', 'R', 'R', 'C', 'H', 'E', 'C'], ['C', 'N', 'A', 'B', 'O', 'Z', 'O', 'B', 'K', 'A'], ['B', 'O', 'N', 'I', 'R', 'B', 'B', 'N', 'C', 'A'], ['E', 'E', 'R', 'T', 'C', 'B', 'R', 'A', 'I', 'A'], ['A', 'B', 'C', 'E', 'R', 'I', 'C', 'R', 'H', 'R'], ['B', 'O', 'I', 'O', 'R', 'O', 'R', 'C', 'C', 'O'], ['B', 'O', 'A', 'A', 'K', 'R', 'K', 'E', 'A', 'R']], 'ZEBRA'), (False, 'not in puzzle'))

    #searchs for a word in the columns forward/down
    def test_find_vertical_down(self):
        self.assertEqual(find_vertical_down([['W', 'C', 'A', 'L', 'P', 'O', 'L', 'Y', 'X', 'U'], ['A', 'B', 'Z', 'D', 'O', 'E', 'G', 'C', 'V', 'U'], ['Q', 'M', 'X', 'W', 'N', 'D', 'Q', 'S', 'D', 'I'], ['H', 'I', 'W', 'L', 'D', 'S', 'C', 'L', 'M', 'U'], ['G', 'V', 'K', 'F', 'T', 'O', 'K', 'O', 'G', 'N'], ['T', 'Q', 'W', 'X', 'M', 'Y', 'G', 'A', 'S', 'I'], ['T', 'Q', 'I', 'P', 'V', 'Q', 'M', 'C', 'X', 'X'], ['W', 'E', 'I', 'I', 'A', 'G', 'M', 'U', 'C', 'F'], ['E', 'L', 'I', 'P', 'M', 'O', 'C', 'Z', 'Y', 'N'], ['E', 'S', 'L', 'V', 'N', 'B', 'T', 'M', 'Z', 'U']], 'CPE101'), (False, 'not in puzzle'))
        self.assertEqual(find_vertical_down([['E', 'Z', 'A', 'A', 'C', 'B', 'E', 'A', 'B', 'B'], ['O', 'E', 'R', 'A', 'N', 'O', 'E', 'B', 'O', 'O'], ['A', 'B', 'R', 'C', 'A', 'N', 'R', 'C', 'I', 'A'], ['R', 'R', 'A', 'B', 'B', 'I', 'T', 'E', 'O', 'A'], ['B', 'A', 'C', 'R', 'O', 'R', 'C', 'R', 'R', 'K'], ['R', 'E', 'C', 'R', 'Z', 'B', 'B', 'I', 'O', 'R'], ['N', 'B', 'O', 'C', 'O', 'B', 'R', 'C', 'R', 'K'], ['I', 'R', 'O', 'H', 'B', 'N', 'A', 'R', 'C', 'E'], ['A', 'B', 'N', 'E', 'K', 'C', 'I', 'H', 'C', 'A'], ['B', 'H', 'R', 'C', 'A', 'A', 'A', 'R', 'O', 'R']], 'RABBIT'), (True, 'RABBIT: (DOWN) row:   1    column:   3'))

    #searches for a word in the columns backwards/up
    def test_find_vertical_up(self):
        self.assertEqual(find_vertical_up([['W', 'C', 'A', 'L', 'P', 'O', 'L', 'Y', 'X', 'U'], ['A', 'B', 'Z', 'D', 'O', 'E', 'G', 'C', 'V', 'U'], ['Q', 'M', 'X', 'W', 'N', 'D', 'Q', 'S', 'D', 'I'], ['H', 'I', 'W', 'L', 'D', 'S', 'C', 'L', 'M', 'U'], ['G', 'V', 'K', 'F', 'T', 'O', 'K', 'O', 'G', 'N'], ['T', 'Q', 'W', 'X', 'M', 'Y', 'G', 'A', 'S', 'I'], ['T', 'Q', 'I', 'P', 'V', 'Q', 'M', 'C', 'X', 'X'], ['W', 'E', 'I', 'I', 'A', 'G', 'M', 'U', 'C', 'F'], ['E', 'L', 'I', 'P', 'M', 'O', 'C', 'Z', 'Y', 'N'], ['E', 'S', 'L', 'V', 'N', 'B', 'T', 'M', 'Z', 'U']], 'DONUT'), (False, 'not in puzzle'))
        self.assertEqual(find_vertical_up([['E', 'Z', 'A', 'A', 'C', 'B', 'E', 'A', 'B', 'B'], ['O', 'E', 'R', 'A', 'N', 'O', 'E', 'B', 'O', 'O'], ['A', 'B', 'R', 'C', 'A', 'N', 'R', 'C', 'I', 'A'], ['R', 'R', 'A', 'B', 'B', 'I', 'T', 'E', 'O', 'A'], ['B', 'A', 'C', 'R', 'O', 'R', 'C', 'R', 'R', 'K'], ['R', 'E', 'C', 'R', 'Z', 'B', 'B', 'I', 'O', 'R'], ['N', 'B', 'O', 'C', 'O', 'B', 'R', 'C', 'R', 'K'], ['I', 'R', 'O', 'H', 'B', 'N', 'A', 'R', 'C', 'E'], ['A', 'B', 'N', 'E', 'K', 'C', 'I', 'H', 'C', 'A'], ['B', 'H', 'R', 'C', 'A', 'A', 'A', 'R', 'O', 'R']], 'RAN'), (True, 'RAN: (UP) row:  7    column:  7'))

# Run the unittest
if __name__ == '__main__':
    unittest.main()