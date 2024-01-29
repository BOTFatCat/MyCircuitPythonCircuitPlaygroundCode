import random
import time

my_number = 5

while my_number > 0:
  print(my_number)
  my_number *= int(random.randint(1, 10))
  time.sleep(.2)
  if (my_number > 9999999999999999999999999999999999999999999999):
    print(my_number)
    break
print("done")
    


