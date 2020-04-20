"""
    This file defines the tests for the random prediction model.
"""
import unittest

from src.models.neural_net import NeuralNetModel

class NeuralNetModelTester(unittest.TestCase):
    def test_classes_not_empty(self):
        model = NeuralNetModel()
        num_classes = model.num_classes
        self.assertTrue(num_classes > 0)

    def test_train_output_type(self):
        model = NeuralNetModel()
        output_type = model.train()
        self.assertIsInstance(output_type, float)


if __name__ == "__main__":
    unittest.main()