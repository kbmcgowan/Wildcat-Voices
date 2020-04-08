"""
    This file defines an interface for a random prediction model, used for a baseline.
"""
import random

from base_model import BaseModel

class RandomModel(BaseModel):
    def __init__(self):
        self.classes = []
    
    def train(self):
        pass

    def predict(self):
        return random.choice(self.classes)