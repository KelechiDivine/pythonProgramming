import unittest
import Solution

class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual((0, 1), Solution.solution([1, 2, 3, 4, 5], 3))
        self.assertEqual((3, 4), Solution.solution([1, 2, 3, 4, 5], 9))
        self.assertEqual((0, 4), Solution.solution([20, 3, 4, 5, 10], 30))


if __name__ == '__main__':
    unittest.main()
