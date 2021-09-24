import unittest
from worldPopulation import WorldPopulationGrowth

class WorldPopulationGrowthTest(unittest.TestCase):
    
    def test_cryptography_exists(self):
        crypto_world = WorldPopulationGrowth()
        self.assertIsNotNone(crypto_world)
        
    def test__replace_each_digit_with_the_result_of_adding_seven_to_the_digit__then_execute(self):
        crypto_world = WorldPopulationGrowth()
        crypto_world.four_numbers_encrypting(3, 57, 43, 2)
        self.assertIsNotNone(crypto_world)


if __name__ == '__main__':
    unittest.main()
