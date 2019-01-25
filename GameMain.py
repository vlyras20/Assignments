import time
import random

gameOver = False
inventory = []
distance = 0
sanity = 100
contacts = {}

def setting():
  print("Yeah so apparently im stuck in 1999")

 def Intro():
     print("[Incoming Message]")
     time.sleep(1)
     print("Connection Established with Traveller 017")
     time.sleep(1.5)
     print("..lo -")
     time.sleep(.5)
     print("Hello? Dam. is this th eve working")
     time.sleep(2)
     print("Hell- Do yo- copy? ")

     input("Enter Here:  ")

     print("Ok. I think I fixed it")
     time.sleep(1)
     print("Oh my god hi. yes ok. Thank you for responding, I've been trying to reach out to anyone for hours now.")
     time.sleep(3)
     print("I've uhh, I've been kinda stuck here, whenever this is, and I need help getting back.")
     Time.sleep(3)
     print("Where's here, exactly? [1]")
     print("Whenever?              [2]")
     print("What Happened?         [3]")

     answer1 = input("Enter here:  ")

     if answer1 in ["1",  "2", "3"]:
         setting()
     else:
         print("That was not an option pick again")

intro()
