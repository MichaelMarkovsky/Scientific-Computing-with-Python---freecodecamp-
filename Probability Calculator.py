import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key,value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_balls):
    if num_balls > len(self.contents):
      return self.contents
    else:
      balls_drawn = []
      for i in range(num_balls):
        ball_drawn = random.choice(self.contents)
        balls_drawn.append(ball_drawn)
        self.contents.remove(ball_drawn)
      return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_success = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)  
    if all(balls_drawn.count(ball) >= expected_balls[ball] for ball in expected_balls):
      num_success += 1
  return num_success/num_experiments
    
  
  

  
