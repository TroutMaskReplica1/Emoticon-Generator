import random

eyes = [':', ';,', ':,', ';']
noses = ['-', ' ', '^', '{']
mouths = [')', '(', '|', '/']
eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)
print(eye + nose + mouth)