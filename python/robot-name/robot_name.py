import random
import string
import time

class Robot(object):
  def __init__(self):
    self.set_name()

  def reset(self):
    self.set_name()

  def set_name(self):
    random.seed(time.time())
    self.name = ''.join(
        random.sample(string.ascii_uppercase, 2) + random.sample(string.digits, 3))

  
