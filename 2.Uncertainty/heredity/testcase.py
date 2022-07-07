""" Test case provided in the project description """
import unittest
from heredity import joint_probability

class TestJointProbability(unittest.TestCase):
    """ Class inheret from unittest testcase class """

    def test_joint_probability(self):
        """ Test the functionality of the joint_probability function """
        family = {
            'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
            'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
            'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
        }

        self.assertAlmostEqual(joint_probability(family, {"Harry"}, {"James"}, {"James"}),
                                0.0026643247488)

if __name__ == "__main__":
    unittest.main()
