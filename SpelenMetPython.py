import random 
import time

while True:     
     print(''' 1. roll the dice             2. exit     ''')    
     user = int(input("what you want to do\n"))     
     if user==1:  
        print("")       
        number = random.randint(1,6)
        print("Het getal is.....")         
        print(number)
        print("")
     if user==2:
         print("oke tot ziens") 
         time.sleep(2)
         break    
     else:         
        break