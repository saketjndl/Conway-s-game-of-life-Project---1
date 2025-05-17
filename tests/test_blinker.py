import unittest
from life import next_gen

class TestLifePatterns(unittest.TestCase):
    def test_blinker(self):
        initial_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_gen1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_gen2 = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        gen1 = next_gen(initial_board)
        self.assertEqual(gen1, expected_gen1)
        gen2 = next_gen(gen1)
        self.assertEqual(gen2, expected_gen2)
        
    def test_glider(self):
        initial_board = [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_gen1 = [
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_gen2 = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_gen3 = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        gen1 = next_gen(initial_board)
        self.assertEqual(gen1, expected_gen1)
        gen2 = next_gen(gen1)
        self.assertEqual(gen2, expected_gen2)
        gen3 = next_gen(gen2)
        self.assertEqual(gen3, expected_gen3)

if __name__ == '__main__':
    unittest.main()