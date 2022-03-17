import random
coin = ["Head",
        "Tail"]
theads = 0
ttails = 0
 

for i in range(1,101):
  flip = random.randint(0, 1)  
  if coin[flip] == "Head":
      theads += 1
  elif coin[flip] == "Tail":
      ttails += 1    
 
print ("The number of heads are: ", theads)
print ("The number of tails are: ", ttails)