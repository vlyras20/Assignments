import time
import random

inventory = {}
inventory_empty = "[Inventory Empty]"

daysLeft = 5  # DAYS LEFT UNTIL EXTRACTION
distance = 10000  # DISTANCE FROM EXTRACTION POINT

usr_name = ""   # Player Name

password = ["-", "-", "-", "-", "-", "-"]
password_answer = ["5", "7", "4", "2", "8", "6"]


def intro():  # 1 ) Beginning of game
    print("[Incoming Message]")
    time.sleep(1)
    print("[Connection Established with Traveller 017]")
    time.sleep(1.5)
    print("..lo -")
    time.sleep(.5)
    print("Hello? Damn is th- thing even working")
    time.sleep(2)
    print("Hell- Do yo- copy? ")
    print()

    input("Enter Here:  ")

    print()
    print("Ok. I think I fixed the microphone issue")
    time.sleep(2)
    print("Thank you for responding, I've been trying to reach out to anyone for hours now.")
    time.sleep(3)
    print("Well, short story, I've uhh, I've been kinda stuck here, whenever this is, and I need help getting back.")
    time.sleep(3)
    print()
    print("Where's here, exactly? [1]")
    print("Whenever?              [2]")
    print("What Happened?         [3]")
    print()

    answers = ["1",  "2", "3"]
    answer = ""

    while answer not in answers:  # Checking whether or not the player has answered one of the options
        answer = input("Enter here:  ")
    else:
        setting()
    return


def setting(): # 2) Setting of Game / current scenario
    answers = ["1", "2", "3"]
    answer = ""

    print()
    print('''Well long story, my mission in Kepler 11 was compromised and I have
5 days to make it to my extraction point before im stuck here indefinitely,
while also being hunted by the other traveler team.''')
    time.sleep(5)
    print()
    print("Hunted by other travelers for what?                               [1]")
    print("How far is the extraction point?                                  [2]")
    print("I don't know how to help, im just an intern at Nasa.              [3]")
    print()

    while answer not in answers:  # Checking whether or not the player has answered one of the options
        answer = input("Enter here:  ")
    else:
        if answer == answers[0]:
            print("I will tell you on the way, for now I need your help.")
            time.sleep(2)
            print('''So  in order for me to go North I have to either cross a frozen lake or go around the outskirts.
My issue is time because its slowly turning dark, and the only thing I see is mountains around me, a big lake,
and a bunch of trees at the other side,
but uhmm what do you think?''')
            time.sleep(5)
            print("I don't have to mention that everything is fully snowed in I hope")
            time.sleep(3)
            main()

        elif answer == answers[1]:
            print('''Basically, my team will be in planet orbit in 5 days time in order to beam me out of this planet
and into safe grounds. The extraction point is at a facility, 10km straight North from my location.''')

            print('''            ---> [DISTANCE] = 10.000m
            ---> [DAYS UNTIL EXTRACTION] = 5
            ---> [SANITY] = 98''')
            time.sleep(7)
            print()
            print('''So  in order for me to go North I have to either cross a frozen lake or go around the outskirts.
My issue is time because its slowly turning dark, and the only thing I see is mountains around me, a big lake,
and a bunch of trees at the other side,
but uhmm what do you think?''')
            time.sleep(5)
            print("I don't have to mention that everything is fully snowed in I hope")
            time.sleep(3)
            main()
        elif answer == answers[2]:
            print("Oh my. Well you are still the best chances I have of reaching the extraction point.")
            time.sleep(2)
            print('''So  in order for me to go North I have to either cross a frozen lake or go around the outskirts.
My issue is time because its slowly turning dark, and the only thing I see is mountains around me, a big lake,
and a bunch of trees at the other side,
but uhmm what do you think?''')
            time.sleep(5)
            print("I don't have to mention that everything is fully snowed in I hope")
            time.sleep(3)
            main()
    return


def main():  # 3) Start of main game play
    answers = ["1", "2", "3", "Yes", "No",  "no", "NO"]
    answer1 = ""
    answer2 = ""

    while answer1 not in answers:
        print()
        print("Is the lake frozen solid, or would you fall through?               [1]")
        print("Outskirts sounds like a better idea but it would slow you down.    [2]")
        print("Is this really the type of help you needed from a NASA employer?   [3]")
        print()
        answer1 = input("Enter here:  ")

        if answer1 == answers[0]:
            print()
            print('''Looks pretty solid but its a big frozen lake nevertheless.
However, I think see a small island close to the middle of it.''')
            time.sleep(1)
            print("So through the lake then?  [Yes]/[No]")
            print()
            answer2 = input("Enter here:  ")
            if answer2 in ["Yes", "yes", "YES"]:
                lake()
            elif answer2 in ["No", "no", "NO"]:
                main()

        if answer1 == answers[1]:
            print('''The sides look pretty clear. Wait, what. I think I see a cabin maybe,
just by the lake following the outskirt ''')
            time.sleep(1)
            print()
            print('''It would slow me a bit but it sounds good to me, I'll stay the night there and tomorrow we move early,"
what do you think?  [Yes]/[No]''')
            print()
            time.sleep(3)
            answer2 = input("Enter here:  ")
            if answer2 in ["Yes", "yes", "YES"]:
                outskirts()
            elif answer2 in ["No", "no", "NO"]:
                main()

        elif answer1 == answers[2]:
            print('''Very funny intern, but no. I will need your knowledge later, this is just your opinion
because I might be going insane in this place. So what's your name?
Figured since im going to talk to you for a while I might as well know who this person is''')
            time.sleep(5)
            print()
            global usr_name
            usr_name = str(input("Enter Here:  "))
            print()
            print(usr_name, "! Nice, well im Traveller 017 or just Joe I guess. But enough of that! Where am I going?")
            time.sleep(2)
            main()

    return


def lake():  # 4 ) Frozen lake in-game decision events
    print("Yeah, I guess you're right. gotta save as much time as I can.")
    time.sleep(2)
    print("Ok, I will keep in touch.")
    time.sleep(1)
    print(".")
    time.sleep(.5)
    print("..")
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    print("Ice is holding on decently for now, I think this can work.")
    time.sleep(1)
    print("I will let you know when I make it to the centre island")
    time.sleep(2)
    print(".")
    time.sleep(.5)
    print("..")
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    print("Getting pretty close, and this ice is getting pretty thin but its holding.")
    time.sleep(2)
    print("Okay ummm, I made it to the tiny island, more of a 2 by 2 of safe ground but it'll keep me safe.")
    time.sleep(3)

    print()
    print('''            [DISTANCE] = 9000
            [DAYS UNTIL EXTRACTION] = 5''')
    print()
    time.sleep(3)

    print('''Do I keep moving on the lake, make my way to the forest and camp there,
or should I turn to the outskirts towards this metal cabin I see? ''')
    time.sleep(4)

    print()
    print("Make it passed the lake and camp out.                [1]")
    print("Move and take shelter at the cabin for the night.    [2]")
    print()

    answers = ["1",  "2"]
    answer = ""

    while answer not in answers:
        answer = input("Enter here:  ")
    else:
        if answer == answers[0]:
            print('''You're probably right. I would waste a lot of time moving to the cabin,
I might as well risk it and sleep in the forest if I wanna get out of here''')
            time.sleep(4)
            print("I will let you know once I've reached the other side then.")
            time.sleep(2)
            print()
            print(".")
            time.sleep(2)
            print()
            print("..")
            time.sleep(2)
            print()
            print("...")
            time.sleep(2)
            print()
            print("Ice is a lot thinner this side.")
            time.sleep(2)
            print("Oh no! I see ice cracking up ahead!")
            time.sleep(2)
            print("Im running back!")
            time.sleep(1)
            print("Go! go! go!")
            time.sleep(1)
            print("Almost there come on! Nooo- I- f- it's so, -cold")
            time.sleep(2)
            death("DEATH -> FROZEN BY LAKE")
            lake()

        if answer == answers[1]:
            print("Good call! Get a good sleep and I might even find supplies in there as well.")
            time.sleep(2)
            print("I will let you know once I've reached the cabin then.")
            time.sleep(2)
            print(". . .")
            time.sleep(3)
            print('''I see some weird blue creatures to the left further away.
I'm glad I came through the lake so I didn't have to face them.''')
            time.sleep(4)
            cabin_calm()
    return


def outskirts():
    print()
    print("Okay Great, I will start moving now and keep you updated on the way")
    time.sleep(2)
    print(usr_name, usr_name, "I've got a problem. I see a group of animals between me and the cabin. ")
    time.sleep(2)
    print("What do you know about some blue, bear looking creatures here? Do they engage? Am I good to go through?")
    time.sleep(2)

    print()
    print("DO NOT APPROACH THEM! most animals in Kepler 11 are carnivores and will engage if alerted.     [1]")
    print("Is there another way around them?                                                              [2]")
    print()

    answers = ["1", "2"]
    answer = ""

    while answer not in answers:
        answer = input("Enter here:  ")
    else:
        if answer == answers[0]:
            print()
            print("Well, that's soothing, but this is why you're here! So what's my plan what do I do?")
            time.sleep(2)
            print()
            print("--->Blue bears are deaf so as long as they don't see you, you should be fine.  ")
            time.sleep(2)
            print("--->Try maybe crawling through the snow so they can't see you.")
            print()
            time.sleep(1)
            print(usr_name, "I'm not sure about maybes in this situation. Do you have anything more certain than that?")
            time.sleep(2)

            print()
            print("     --->Nope, that's your best bet at this moment. [1]")
            print("     --->Run for it when you find a chance!         [2]")
            print()

            answer2 = ""

            while answer2 not in answers:
                answer2 = input("Enter here:  ")
                print()
            else:
                if answer2 == answers[0]:
                    print("Well I hope you're right. I'll keep you updated.")
                    time.sleep(1)
                    print('''Just to let you know, this is terrifying. I'm currently crawling through a meter of snow
                    just to avoid some deaf bears. ''')
                    time.sleep(2)
                    print("I can't even see where I'm going, im just going straight towards the cabin.")
                    time.sleep(2)
                    print("I will keep you updated.")
                    time.sleep(1)
                    print("...")
                    time.sleep(2)
                    print("..")
                    time.sleep(2)
                    print(".")
                    time.sleep(2)
                    print('''Im close. I can run for it. Is that a good idea or is it just me?
                    what do you think''')
                    time.sleep(3)

                    print()
                    print("If you're close enough go for it.        [1]")
                    print("No, stay hidden! Don't let them see you. [2]")
                    print()

                    answer3 = ""

                    while answer3 not in answers:
                        answer3 = input("Enter here:  ")
                        print()
                    else:
                        if answer3 == answers[0]:
                            print()
                            cabin_calm()
                        if answer3 == answers[1]:
                            print("Ok still crawling then. Im close.")
                            time.sleep(1)
                            print("Oh no! I got to run! Quick!")
                            time.sleep(1)
                            print("Ahhh! Made it! He got me pretty bad though!")
                            time.sleep(2)
                            print('''One just turned the corner from the back of the cabin
                    and saw me right before I opened the door''')
                            time.sleep(3)
                            print("It was so fast! That was scary fast! Ah! That hurts.")
                            time.sleep(2)
                            print()
                            cabin_hurt()
                elif answer2 == answers[1]:
                    print("Really? I mean, it kinda makes sense I guess. Ok, I will keep you updated.")
                    time.sleep(4)
                    print("Ok. they've spread out enough! This is my chance and I'm going for it!")
                    time.sleep(4)
                    print("RUUUUUUUN!")
                    time.sleep(1)
                    print("Almost at the cabin!")
                    time.sleep(2)
                    print("Oh no! I see one looking at me! Im just running it! Go Go Go!")
                    time.sleep(3)
                    print("Made it to the door! ")
                    time.sleep(2)
                    print('''Phewww! Made it! that was close and I think they're circling the cabin outside
so Im trapped here for a while.''')
                    time.sleep(5)
                    cabin_calm()
        elif answer == answers[1]:
            print('''Nothing but the frozen lake. I think my best chances are
dealing with these creatures fast and not waste time finding another way''')
            time.sleep(4)
            print("So do you have any knowledge of these things or should I just slowly pass them?")
            print()
            time.sleep(3)
            print("--> Well blue bears are deaf so as long as they don't see you, you should be fine.  ")
            time.sleep(3)
            print("--> Try maybe crawling through the snow so they can't see you.")
            print()
            time.sleep(2)
            print(usr_name, "I'm not sure about maybes in this situation. Do you have anything more certain than that?")
            time.sleep(3)

            print()
            print("---> Nope, that's your best bet at this moment. [1]")
            print("---> Run for it when you find a chance!         [2]")
            print()

            answer2 = ""

            while answer2 not in answers:
                answer2 = input("Enter here:  ")
                print()
            else:
                if answer2 == answers[0]:
                    print("Well I hope you're right. I'll keep you updated.")
                    time.sleep(1)
                    print('''Just to let you know, this is terrifying. I'm currently crawling through a meter of snow
just to avoid some deaf bears. ''')
                    time.sleep(2)
                    print("I can't even see where I'm going, im just going straight towards the cabin.")
                    time.sleep(2)
                    print("I will keep you updated.")
                    time.sleep(1)
                    print("...")
                    time.sleep(2)
                    print("..")
                    time.sleep(2)
                    print(".")
                    time.sleep(2)
                    print('''Im close. I can run for it. Is that a good idea or is it just me?
what do you think''')
                    time.sleep(3)

                    print()
                    print("If you're close enough go for it.        [1]")
                    print("No, stay hidden! Don't let them see you. [2]")
                    print()

                    answer3 = ""

                    while answer3 not in answers:
                        answer3 = input("Enter here:  ")
                        print()
                    else:
                        if answer3 == answers[0]:
                            print()
                            cabin_calm()
                        if answer3 == answers[1]:
                            print("Ok still crawling then. Im close.")
                            time.sleep(1)
                            print("Oh no! I got to run! Quick!")
                            time.sleep(1)
                            print("Ahhh! Made it! He got me pretty bad though!")
                            time.sleep(2)
                            print('''One just turned the corner from the back of the cabin
and saw me right before I opened the door''')
                            time.sleep(3)
                            print("It was so fast! That was scary fast! Ah! That hurts.")
                            time.sleep(2)
                            print()
                            cabin_hurt()
                elif answer2 == answers[1]:
                    print("Really? I mean, it kinda makes sense I guess. Ok, I will keep you updated.")
                    time.sleep(3.5)
                    print("Ok. they've spread out enough! This is my chance and I'm going for it!")
                    time.sleep(3.5)
                    print("RUUUUUUUN!")
                    time.sleep(1.5)
                    print("Almost at the cabin!")
                    time.sleep(2)
                    print("Oh no! I see one looking at me! Im just running it! Go Go Go!")
                    time.sleep(3.5)
                    cabin_calm()


def cabin_calm():
    global distance
    distance -= 920

    answer = ""
    answers = ["1", "2"]

    answers1 = ["1", "2", "3"]

    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""
    answer5 = ""

    time.sleep(2)
    print("Almost at the door.")
    time.sleep(2)
    print('''Phewww! Made it! Easy, Ok.''')
    time.sleep(2)
    print("I think the creatures haven't noticed me so I should be able to stay here until they leave.")
    time.sleep(4)
    print("I, I see nothing. It's pitch black. Let me see what I have on me.")
    time.sleep(3)
    print()
    global inventory_empty
    print(inventory_empty)
    print()
    print('''Well I got nothing. I could just sleep in this corner
until morning comes I guess so I can see whats around. Sound Good?''')
    time.sleep(4)
    print("Sounds good!      [1]")

    while answer not in ["1"]:
        print()
        answer = input("Enter here:  ")
        print()
    else:
        if answer == "1":
            print("--> Sounds good.")
            time.sleep(1)
            print()
            print(".")
            time.sleep(2)
            print()
            print(".")
            time.sleep(2)
            print()
            print(".")
            time.sleep(2)
            print()
            print('''            [DISTANCE] = 9.080m
            [DAYS UNTIL EXTRACTION] = 4''')

            time.sleep(2)
            print()
            print(usr_name, "...", usr_name, "Oh man it's freezing!")
            time.sleep(1)
            print('''Im glad I slept in here however, 
I don't know if I would have made it camping at the forest in this cold.''')
            time.sleep(4)
            print("Better start searching around, see what I can find in this place.")
            time.sleep(3)
            print("I see a lot of cupboards but no supplies. That's not a good sign.")
            time.sleep(3)
            print("Oh, oh my, what is that smell?")
            time.sleep(2)
            print("Wooow! There's a corpse in the closet. Someone has been here recently.")
            time.sleep(3)

            print()
            print("Leave it! keep searching the room.      [1]")
            print("Search the body for supplies.           [2]")

            while answer2 not in answers:
                print()
                answer2 = input("Enter here:  ")
                print()
            else:
                if answer2 == answers[0]:
                    print("--> Leave it! keep searching the room.")
                    time.sleep(2)
                    print("Yeah, better not deal with this thing. I'll keep looking around.")
                    time.sleep(2)
                    print("I see books but nothing useful to take with me.")
                    time.sleep(2)
                    print("OHh! umm! I found a trapdoor.")
                    time.sleep(1)
                    print("It's sealed, I can't seem to break it open.")
                    time.sleep(2)
                    print("There must be a way to open it right?")
                    time.sleep(2)

                    print()
                    print("Search the body.                                      [1]")
                    print("Don't waste time and start heading towards the forest [2]")
                    print()

                    while answer3 not in answers:
                        print()
                        answer3 = input("Enter here:  ")
                        print()
                    else:
                        if answer3 == answers[0]:
                            print("--> Search the body.")
                            time.sleep(1)
                            print()
                            print("I was so sure you where going to say that. I guess it's worth a try then")
                            time.sleep(2)
                            print("I've got something.")
                            time.sleep(1)
                            print('''It's just some writing on a piece of paper. Something about a mineshaft underneath the cabin.
Could be interesting to investigate, but we still have 4 days left, so if I go searching I should do it fast.
There's also a few numbers written. 5 7 4 - 2 8 6
Any idea what they could mean? ''')
                            time.sleep(6)

                            print()
                            print("A password for the trapdoor maybe?                        [1]")
                            print("Leave it! You have a long way to go until the extraction. [2]")
                            print()

                            while answer4 not in answers:
                                print()
                                answer4 = input("Enter here:  ")
                                print()
                            else:
                                if answer4 == answers[0]:
                                    print("--> A password for the trapdoor maybe?")
                                    time.sleep(1)
                                    print()
                                    print("Why would a mineshaft require a password? Where would it lead?")
                                    time.sleep(2)
                                    print('''If it somehow leads me closer to my extraction, it could save me a lot of time though,
maybe even days worth of walking.''')
                                    time.sleep(3)
                                    print()
                                    print("Open the trapdoor.                       [1]")
                                    print("Ignore it! Leave for the forest now.     [2]")
                                    print()
                                    while answer5 not in answers:
                                        print()
                                        answer5 = input("Enter here:  ")
                                        print()
                                    else:
                                        if answer5 == answers[0]:
                                            print("--> Open the trapdoor. ")
                                            print()
                                            time.sleep(1)
                                            print('''I like your thinking! If it indeed leads to the facility,
 this might change everything''')
                                            time.sleep(2)
                                            mineshaft()
                                        if answer5 == answers[1]:
                                            print("--> Ignore it! Leave for the forest now.")
                                            print()
                                            time.sleep(2)
                                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                            time.sleep(3)
                                            forest()

                                if answer4 == answers[1]:
                                    print("--> Leave it! You have a long way to go until the extraction.")
                                    time.sleep(1)
                                    print()
                                    print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                    forest()
                        if answer3 == answers[1]:
                            print("You're right! I should just focus on getting back!")
                            time.sleep(3)
                            forest()
                if answer2 == answers[1]:
                    print("--> Search the body for supplies")
                    time.sleep(1)
                    print()
                    print("I was so sure you where going to say that. I guess it's worth a try then")
                    time.sleep(2)
                    print("I've got something.")
                    time.sleep(1)
                    print('''It's just some writing on a piece of paper. Something about a mineshaft underneath the cabin.
Could be interesting to investigate, but we still have 4 days left, so if I go searching I should do it fast.
There's also a few numbers written. 5 7 4 - 2 8 6
Any idea what they could mean? ''')
                    time.sleep(6)

                    print()
                    print("A password maybe?                                     [1]")
                    print("Find the entrance to the shaft.                       [2]")
                    print("Don't waste time and start heading towards the forest [3]")
                    print()

                    while answer4 not in answers1:
                        print()
                        answer4 = input("Enter here:  ")
                        print()
                    else:
                        if answer4 == answers1[0]:
                            print("--> A password maybe?")
                            time.sleep(1)
                            print()
                            print("Why would a mineshaft require a password? Where would it lead?")
                            time.sleep(2)
                            print('''If it somehow leads me closer to my extraction, it could save me a lot of time,
maybe even days worth of walking.''')
                            time.sleep(3)
                            print()
                            print("Find the entrance to the shaft.                       [1]")
                            print("Leave it, just start heading towards the forest       [2]")
                            print()
                            while answer5 not in answers:
                                print()
                                answer5 = input("Enter here:  ")
                                print()
                            else:
                                if answer5 == answers[0]:
                                    print()
                                    print('''I like your thinking! If it indeed leads to the facility,
this might change everything''')
                                    time.sleep(2)
                                    print("Well, I uh, I think I found it.")
                                    time.sleep(2)
                                    print("I found the trapdoor.")
                                    time.sleep(1)
                                    print("It's sealed, and I don't see any password input here.")
                                    time.sleep(2)
                                    mineshaft()
                                if answer5 == answers[1]:
                                    print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                    forest()

                        if answer4 == answers1[1]:
                            print("--> Find the entrance to the shaft.")
                            time.sleep(1)
                            print()
                            print('''I like your thinking! If it indeed leads to the facility,
this might change everything''')
                            time.sleep(3)
                            print("Well, I uh, I think I found it.")
                            time.sleep(2)
                            print("I found a trapdoor.")
                            time.sleep(1)
                            print("It's sealed, and I don't see any password input here.")
                            time.sleep(2)
                            mineshaft()
                        if answer4 == answers1[2]:
                            print("--> Don't waste time and start heading towards the forest")
                            time.sleep(1)
                            print()
                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                            forest()


def cabin_hurt():
    global distance
    distance -= 920

    answer = ""
    answer1 = ""
    answers1 = ["1", "2", "3"]

    answers = ["1", "2"]
    answer2 = ""
    answer3 = ""
    answer4 = ""
    answer5 = ""
    answer6 = ""

    print("Blue bear bites are not poisonous right? ")
    print()
    time.sleep(1)
    print("No, but is it bad? How deep is the bite?             [1]")
    print("Yeah, you might not make the night my friend.        [2]")
    print()
    while answer1 not in answers:
        answer1 = input("Enter here:  ")
        print()
    else:
        if answer1 == answers[0]:
            print("--> No, but is it bad? How deep is the bite?")
            time.sleep(2)
            print()
            print("It's stable now, I tied it with some cloth I managed to rip.")

        elif answer1 == answers[1]:
            print("Wait. What? Don't freak me out", usr_name, "You serious?")
            print()
            time.sleep(2)
            print("--> No, calm down commando, I was joking, you'll be alright.     [1]")
            print("--> Well lets say fever is the last thing you should worry about.[2]")
            while answer2 not in answers:
                print()
                answer2 = input("Enter here:  ")
                print()
            else:
                if answer2 == answers1[0]:
                    print()
                if answer2 == answers[1]:
                    print("-> Well lets say fever is the last thing you should worry about.")
                    time.sleep(2)
                    print("-> Im joking by the way Mr. Traveler. I don't know if they have humour whenever you're from")
                    time.sleep(1)
                    print("Funny", usr_name, "Very funny indeed.")
    time.sleep(2)
    print("Well you know what. Ahh! I, I see nothing. It's pitch black and I'm exhausted.")
    time.sleep(2)
    print()
    print(inventory_empty)
    print()
    print('''Hopefully my wound doesn't get infected throughout night time. I could just sleep and rest in this corner
until morning comes so I can see whats around and move from there. Sound Good?''')
    time.sleep(5)
    print()
    print("Sounds good.      [1]")

    while answer not in ["1"]:
        print()
        answer = input("Enter here:  ")
        print()
    else:
        if answer == answers[0]:
            print("--> Sounds good.")
            time.sleep(1)
            print()
            print(".")
            time.sleep(2)
            print()
            print(".")
            time.sleep(2)
            print()
            print(".")
            time.sleep(2)
            print()
            print('''            [DISTANCE] = 9.080m
            [DAYS UNTIL EXTRACTION] = 4''')
            time.sleep(2)

            print()
            print(usr_name, "...", usr_name, "Oh man it's freezing!")
            time.sleep(1)
            print('''Im glad I slept in here however, 
I don't know if I would have made it camping at the forest in this cold.''')
            time.sleep(3)
            print("The bite is not looking good though.")
            time.sleep(2)
            print("Better start searching around, see what I can find in this place to help so I keep moving.")
            time.sleep(2)
            print("I see a lot of cupboards but no supplies. That's not a good sign.")
            time.sleep(2)

            time.sleep(2)
            print("Oh, oh my, what is that smell?")
            time.sleep(2)
            print("Wooow! There's a corpse in the closet. Someone has been here recently.")
            time.sleep(2)

            print()
            print("Leave it! keep searching the room.      [1]")
            print("Search the body for supplies.           [2]")

            while answer6 not in answers:
                print()
                answer6 = input("Enter here:  ")
                print()
            else:
                if answer6 == answers[0]:
                    print("--> Leave it! keep searching the room.")
                    time.sleep(2)
                    print("Yeah, better not deal with this thing. I'll keep looking around.")
                    time.sleep(2)
                    print("I see books but nothing useful to take with me.")
                    time.sleep(2)
                    print("OHh! umm! I found a trapdoor.")
                    time.sleep(1)
                    print("It's sealed, I can't seem to break it open.")
                    time.sleep(2)
                    print("There must be a way to open it right?")
                    time.sleep(2)

                    print()
                    print("Search the body.                                      [1]")
                    print("Don't waste time and start heading towards the forest [2]")
                    print()

                    while answer3 not in answers:
                        print()
                        answer3 = input("Enter here:  ")
                        print()
                    else:
                        if answer3 == answers[0]:
                            print("--> Search the body.")
                            time.sleep(1)
                            print()
                            print("I was so sure you where going to say that. I guess it's worth a try then")
                            time.sleep(2)
                            print("I've got something.")
                            time.sleep(1)
                            print('''It's just some writing on a piece of paper. Something about a mineshaft underneath the cabin.
Could be interesting to investigate, but we still have 4 days left, so if I go searching I should do it fast.
There's also a few numbers written. 5 7 4 - 2 8 6
Any idea what they could mean? ''')
                            time.sleep(6)

                            print()
                            print("A password for the trapdoor maybe?                        [1]")
                            print("Leave it! You have a long way to go until the extraction. [2]")
                            print()

                            while answer4 not in answers:
                                print()
                                answer4 = input("Enter here:  ")
                                print()
                            else:
                                if answer4 == answers[0]:
                                    print("--> A password for the trapdoor maybe?")
                                    time.sleep(1)
                                    print()
                                    print("Why would a mineshaft require a password? Where would it lead?")
                                    time.sleep(2)
                                    print('''If it somehow leads me closer to my extraction, it could save me a lot of time though,
maybe even days worth of walking.''')
                                    time.sleep(3)
                                    print()
                                    print("Open the trapdoor.                       [1]")
                                    print("Ignore it! Leave for the forest now.     [2]")
                                    print()
                                    while answer5 not in answers:
                                        print()
                                        answer5 = input("Enter here:  ")
                                        print()
                                    else:
                                        if answer5 == answers[0]:
                                            print("--> Open the trapdoor. ")
                                            print()
                                            time.sleep(1)
                                            print('''I like your thinking! If it indeed leads to the facility,
 this might change everything''')
                                            time.sleep(2)
                                            mineshaft()
                                        if answer5 == answers[1]:
                                            print("--> Ignore it! Leave for the forest now.")
                                            print()
                                            time.sleep(2)
                                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                            time.sleep(3)
                                            forest()

                                if answer4 == answers[1]:
                                    print("--> Leave it! You have a long way to go until the extraction.")
                                    time.sleep(1)
                                    print()
                                    print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                    forest()
                        if answer3 == answers[1]:
                            print("You're right! I should just focus on getting back!")
                            time.sleep(3)
                            forest()
                if answer2 == answers[1]:
                    print("--> Search the body for supplies")
                    time.sleep(1)
                    print()
                    print("I was so sure you where going to say that. I guess it's worth a try then")
                    time.sleep(2)
                    print("I've got something.")
                    time.sleep(1)
                    print('''It's just some writing on a piece of paper. Something about a mineshaft underneath the cabin.
Could be interesting to investigate, but we still have 4 days left, so if I go searching I should do it fast.
There's also a few numbers written. 5 7 4 - 2 8 6
Any idea what they could mean? ''')
                    time.sleep(6)

                    print()
                    print("A password maybe?                                     [1]")
                    print("Find the entrance to the shaft.                       [2]")
                    print("Don't waste time and start heading towards the forest [3]")
                    print()

                    while answer4 not in answers1:
                        print()
                        answer4 = input("Enter here:  ")
                        print()
                    else:
                        if answer4 == answers1[0]:
                            print("--> A password maybe?")
                            time.sleep(1)
                            print()
                            print("Why would a mineshaft require a password? Where would it lead?")
                            time.sleep(2)
                            print('''If it somehow leads me closer to my extraction, it could save me a lot of time,
maybe even days worth of walking.''')
                            time.sleep(3)
                            print()
                            print("Find the entrance to the shaft.                       [1]")
                            print("Leave it, just start heading towards the forest       [2]")
                            print()
                            while answer5 not in answers:
                                print()
                                answer5 = input("Enter here:  ")
                                print()
                            else:
                                if answer5 == answers[0]:
                                    print()
                                    print('''I like your thinking! If it indeed leads to the facility,
this might change everything''')
                                    time.sleep(2)
                                    print("Well, I uh, I think I found it.")
                                    time.sleep(2)
                                    print("I found the trapdoor.")
                                    time.sleep(1)
                                    print("It's sealed, and I don't see any password input here.")
                                    time.sleep(2)
                                    mineshaft()
                                if answer5 == answers[1]:
                                    print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                    forest()

                        if answer4 == answers1[1]:
                            print("--> Find the entrance to the shaft.")
                            time.sleep(1)
                            print()
                            print('''I like your thinking! If it indeed leads to the facility,
                            this might change everything''')
                            time.sleep(3)
                            print("Well, I uh, I think I found it.")
                            time.sleep(2)
                            print("I found a trapdoor.")
                            time.sleep(1)
                            print("It's sealed, and I don't see any password input here.")
                            time.sleep(2)
                            mineshaft()
                        if answer4 == answers1[2]:
                            print("--> Leave it, just start heading towards the forest")
                            time.sleep(1)
                            print()
                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                            forest()


def forest():
    print("Ok time to leave the cabin then!")
    time.sleep(2)
    print("The decision has been made!")
    time.sleep(2)
    print("I will keep you updated ")
    time.sleep(2)
    print()
    print(". . .")
    print()
    time.sleep(1)
    print()
    print(". . .")
    print()
    time.sleep(1)
    print(usr_name, "Hey Hey! I see movement in the forest!")
    time.sleep(2)
    print("Looks like regular people. They must be the other travellers most likely.")
    time.sleep(3)
    print("I can't let them spot me.")
    time.sleep(2)
    print()
    print("Follow them               [1]")
    print("Take them out one by one. [2]")
    print()
    time.sleep(1)

    answer = ""
    answers = ["1", "2"]

    while answer not in answers:
        answer = input("Enter here:  ")
        print()
    else:
        if answer == answers[0]:
            print("--> Follow them.")
            time.sleep(1)
            print("I could do that actually, good idea", usr_name)
            time.sleep(2)
            print("In fact they could lead me straight to the facility")
            time.sleep(2)
            print("Or even my team if they're still alive.")
            time.sleep(2)
            print("Ok, I will keep following them and keep you updated partner.")
            time.sleep(2)
            print()
            print(". . .")
            print()
            time.sleep(1)
            print()
            print(". . .")
            print()
            time.sleep(1)
            print("Whoa! hey,", usr_name, "umm, so I see them loading cargo boxes on their spaceship.")
            time.sleep(2)
            print("That must be my way to the facility!")
            time.sleep(2)
            print("I have to free my team and get out of this place!")
            time.sleep(2)
            print("But first, I need a way onto that spaceship.")
            time.sleep(2)
            print("Any ideas?")
            time.sleep(1)

            print()
            print("Kill all of them and hijack the spaceship?  [1]")
            print("Hide in the boxes and sneak in.             [2]")
            print()
            time.sleep(2)

            answer1 = ""
            while answer1 not in answers:
                answer1 = input("Enter here:  ")
                print()
            else:
                if answer1 == answers[0]:
                    print("--> Kill all of them and hijack the spaceship?")
                    time.sleep(1)
                    print("I would love to do that but I can't drive a spaceship.")
                    time.sleep(2)
                    print("Wait a minute")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print("Okay umm! I'm inside a cargo box.")
                    time.sleep(2)
                    print("But it's full of explosives!")
                    time.sleep(2)
                    print("As long as I don't blow up I should be good.")
                    time.sleep(3)
                    print("All I need now is to be placed in the spaceship")
                    time.sleep(3)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print("Im in! It worked. I had to stay quiet there, I couldn't compromise myself.")
                    time.sleep(3)
                    print("Now I just have to wait or take off and I break out of here.")
                    time.sleep(3)
                    spaceship()
                if answer1 == answers[1]:
                    print("--> Hide in the boxes and sneak in.")
                    time.sleep(2)
                    print()
                    print("Smart, I'll see what I can do.")
                    time.sleep(2)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print("Okay umm! I'm inside a cargo box.")
                    time.sleep(2)
                    print("But it's full of explosives!")
                    time.sleep(2)
                    print("As long as I don't blow up I should be good.")
                    time.sleep(3)
                    print("All I need now is to be placed in the spaceship")
                    time.sleep(3)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print("Im in! It worked. I had to stay quiet there, I couldn't compromise myself.")
                    time.sleep(3)
                    print("Now I just have to wait for take off and I break out of here.")
                    time.sleep(3)
                    spaceship()
        if answer == answers[1]:
            print("--> Take them out one by one.")
            time.sleep(1)
            print("I see at least 5, and my only weapon is a shiv!")
            time.sleep(2)
            print("I don't like my chances but I will try and make this work.")
            time.sleep(2)
            print("One of them is alone. I could go for the kill but if he hears me or alerts his team, its over.")
            time.sleep(3)
            print("What do you think?")
            time.sleep(1)

            print()
            print("Take him out!             [1]")
            print("Find a different approach [2]")
            print()
            time.sleep(2)

            answer1 = ""

            while answer1 not in answers:
                answer1 = input("Enter here:  ")
                print()
            else:
                if answer1 == answers[0]:
                    print("--> Take him out!")
                    print()
                    time.sleep(1)
                    print(". .")
                    time.sleep(1)
                    print(". .")
                    time.sleep(1)
                    print(". .")
                    time.sleep(2)
                    print("Ok, ok, ok, it's done! First one down!")
                    time.sleep(2)
                    print("I found a key card and a ray gun on him with 3 shots.")
                    time.sleep(2)
                    global inventory
                    inventory["Key card"] = '1'
                    inventory["Ray Gun"] = '3'
                    print()
                    print(inventory)
                    print()
                    time.sleep(2)
                    print("Okay, I see another possible target!")
                    time.sleep(2)
                    print("The way up to the spaceship is safe. I can find somewhere to hide there.")
                    time.sleep(3.5)
                    print("Should I go for the spaceship, or maybe target the rest of the travellers?")
                    time.sleep(4)
                    print()
                    print("Go for the spaceship!    [1]")
                    print("Take out the travellers. [2]")
                    print()

                    answer2 = ""
                    while answer2 not in answers:
                        answer2 = input("Enter here:  ")
                    else:
                        if answer2 == answers[0] or answers[1]:
                            print(". .")
                            time.sleep(1)
                            print(". .")
                            time.sleep(1)
                            print('''Never mind, I uhh, I almost got spotted so I, I rushed to the spaceship 
and now im currently in a cabinet of some sorts.''')
                            time.sleep(4)
                            print("I'm fairly certain I wasn't seen, so I should be safe here for now.")
                            time.sleep(3)
                            print("Once we take off, I should be clear to investigate the spaceship.")
                            time.sleep(2)
                            print("But for now we wait.")
                            spaceship()

                if answer1 == answers[1]:
                    print("--> Find a different approach")
                    print()
                    time.sleep(1)
                    print("Ok, I think I found another way around this.")
                    time.sleep(2)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print("Im back! I'm inside a cargo box.")
                    time.sleep(2)
                    print("But it's full of explosives!")
                    time.sleep(2)
                    print("As long as I don't blow up I should be good.")
                    time.sleep(3)
                    print("All I need is to be placed in the spaceship and everything should be find from there.")
                    time.sleep(3)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    print("Im in! It worked. I had to stay quiet there, I couldn't compromise myself.")
                    time.sleep(3)
                    print("Now I just have to wait or take off and I break out of here.")
                    time.sleep(3)
                    spaceship()


def mineshaft():
    answers = ["1", "2"]
    answer = ""

    answers1 = ["1", "2", "3"]
    answer1 = ""

    print()
    print("I don't see the password input. I will look around, it must be hidden somewhere.")
    time.sleep(2)
    print("It's not on any wall or surface. Hmm, where would they hide a password input?")
    time.sleep(2)
    print("Never mind! Found it! Ok, it was behind the cupboard itself.")
    time.sleep(2)
    print("What was the code again? umm ")
    time.sleep(1)
    print("5 7 4 - 2 8 6 right?")
    print()
    usr_input = input("Enter here:  ")
    print()
    if usr_input in ["Yes", "yes", "right", "correct"]:
        print("-->", usr_input)
        time.sleep(1)
        print()
        print("Yeah its done! I heard the trapdoor unlock!")
    elif usr_input in ["No", "no", "wrong"]:
        print("-->", usr_input)
        time.sleep(1)
        print()
        print("Yes it is! my memory hasn't failed me yet!")
        time.sleep(1)
        print("There we go! I heard the trapdoor unlock!")
    else:
        print("Never mind I did it! I heard the trapdoor open I think.")

    time.sleep(2)
    print("No going back now! Are we sure about this? Do I go looking for this miracle mineshaft?")
    time.sleep(2)

    print()
    print("Yes! That might be the only way to the facility.                   [1]")
    print("No! Turn to the forest, we don't know for sure what is down there. [2]")
    print()

    while answer not in answers:
        answer = input("Enter here:  ")
    else:
        if answer == answers[0]:
            print()
            print("Ok! here goes this then!")
            time.sleep(2)
            print("I see some boxes at the bottom of this ladder.")
            time.sleep(2)
            print("Oh! Nice! Ok its just a bunch of light sticks!")
            time.sleep(2)
            print("This should come in useful in here I guess")
            time.sleep(2)
            print("Wooow! There's a box full of explosives here.")
            time.sleep(2)
            print("I'll grab a few of those as well for the way so lets go further!")
            time.sleep(2)

            global inventory
            print("'Picked up 4 light sticks'")
            print("'Picked up 3 explosives'")
            inventory["Light Sticks"] = 4
            inventory["Explosives"] = 3
            time.sleep(2)

            print()
            print(inventory)
            print()

            time.sleep(1)
            print("Damn, this place is like a maze.")
            time.sleep(1)
            print("I have to find a mine cart or a way out because I am definitely getting stuck here otherwise.")
            time.sleep(3)
            print(". . .")
            time.sleep(2)
            print("Hey so, are there any other creatures lurking in here from your knowledge or am I, safe.")
            time.sleep(2)

            print()
            print("Unless creatures had a way in the shaft, nothing should be alive down there.     [1]")
            print("Unless you're afraid of alien bats or fungi then you should be safe I guess.     [2]")
            print("No knowledge on that I'm afraid. So? what was your mission in Kepler 11?         [3]")
            print()

            while answer1 not in answers1:
                answer1 = input("Enter here:  ")
            else:
                if answer1 == answers1[0] or answers1[1]:
                    print()
                    print("Okay... I don't know what to think about that, I'll just keep moving forward.")
                    time.sleep(2)
                    print("I found what looks like cart tracks.")
                    time.sleep(2)
                    clickers()
                if answer1 == answers1[2]:
                    print("Well, if you want to know, Kepler 11 was the best suitable candidate for a second Earth.")
                    time.sleep(3)
                    print('''I was sent here with my team, which was recently captured, 
to gather intel of unauthorised activity by other travellers.''')
                    time.sleep(3)
                    print("More on that later though", usr_name)
                    time.sleep(2)
                    print("I need another light stick I cant see anything.")
                    time.sleep(2)
                    print("'Removed 1 light stick from inventory'")
                    inventory["Light Sticks"] = 3
                    time.sleep(2)
                    print()
                    print(inventory)
                    print()
                    time.sleep(1)
                    print("Wow! Much better!")
                    time.sleep(2)
                    clickers()
        elif answer == answers[1]:
            print()
            print("You know what! I think that was a wise choice. Lets just make it to the extraction safely.")
            time.sleep(1)
            forest()
    return


def clickers():
    answers = ["1", "2", "3"]
    answer = ""

    print("ohh, ohhh my what is that!!!")
    time.sleep(2)
    print("It's coming after me!")
    time.sleep(2)
    print("Ahhh! Die you filthy clicking abomination!!")
    time.sleep(3)
    print(". . .")
    time.sleep(2)
    print("Ummm. I think I killed it!", usr_name, "What the hell was that thing!")
    time.sleep(3)

    print()
    print("A Trikofungus? really? I have only read about them but we never had proof.[1]")
    print("Are you hurt?                                                             [2]")
    print("Careful! You might have attracted more by shouting!                       [3]")
    print()

    while answer not in answers:
        answer = input("Enter here:  ")
    else:
        if answer == answers[0]:
            print()
            print("--> A Trikofungus? really? I have only read about them but we never had proof.")
            time.sleep(2)
            print()
            print("A Trika what? What are they? I need you here! I hear more clicking approaching!")
            time.sleep(3)
            print("What do I do?")
            cart()

        if answer == answers[1] or answers[2]:
            print()
            print("Im not hurt thankfully, I managed to use my shiv to just nail this thing back to it's grave!")
            time.sleep(3)
            print("I hear more on the way!")
            print("What do I do?")
            cart()


def cart():
    answer = ""

    answer1 = ""
    answers1 = ["1", "2"]
    answer2 = ""

    print()
    print("--> Leave! Find a way out!                                           [1]")
    print("--> Trikofungi are like bats, they're blind so don't make a sound.   [2]")
    print()

    while answer1 not in answers1:
        answer1 = input("Enter here:  ")
        print()
    else:
        if answer1 == answers1[0]:
            print("--> Leave! Find a way out!")
            print()
            time.sleep(1)
            print("There's no time, this place is like a maze!")
            time.sleep(2)
            print("I would never make it out")
            time.sleep(1)
            print("I have to try though! Ahh! What do I do?")
            time.sleep(2)
            print("Im making a run back to the cabin.")
            time.sleep(2)
            print("Ohh! These things are fast!")
            time.sleep(2)
            print("Nooo!! Ahhh!")
            time.sleep(1)
            print("Get")
            time.sleep(1)
            print("Off Me!")
            time.sleep(1)
            print("Ahhhh!! ")
            time.sleep(1)
            death()
            cart()

        if answer1 == answers1[1]:
            print("--> Trikofungi are like bats, they're blind so don't make a sound.")
            print()
            time.sleep(2)
            print("So now what? I should stay still? are you crazy?")
            time.sleep(2)
            print("I will search around for a weapon because my shiv wont make it")
            time.sleep(3)
            print("If you think of anything let me know")
            time.sleep(2)
            print(".")
            time.sleep(.5)
            print(".")
            time.sleep(1)
            print()
            print("--> Is there a minecart or anything on the tracks? [1]")
            print()

            answer2 = ""

            while answer2 != "1":
                answer2 = input("Enter here:  ")
            else:
                if answer2 == "1":
                    print()
                    time.sleep(1)
                    print("--> Is there a minecart or anything on the tracks?")
                    time.sleep(1)
                    print()
                    print(". . .")
                    time.sleep(1)
                    print()
                    print(". . .")
                    time.sleep(1)
                    print()
                    print(". . .")
                    time.sleep(1)
                    print()
                    print("Ohh they heard me!")
                    time.sleep(2)
                    print("Go, Go!")
                    time.sleep(1)
                    print()
                    print(". . .")
                    print()
                    time.sleep(2)
                    print("The cart is not moving.")
                    time.sleep(1)
                    print("Wait! I got it! Moooove! ahh!")
                    time.sleep(2)
                    print()
                    print(". . .")
                    print()
                    time.sleep(2)
                    print("Okay, and we, are, off!")
                    time.sleep(1)
                    print("Wooooo! we did it!")
                    time.sleep(2)
                    print("Seems like you know your way around this planet")
                    time.sleep(3)
                    print("So I will be expecting help like this more often then.")
                    time.sleep(3)
                    print(". . .")
                    time.sleep(1)
                    print("So uhmm, I just realised while my adrenaline slows down.")
                    time.sleep(3)
                    print("That")
                    time.sleep(1)
                    print("I'm currently in a mine cart with no idea of the destination.")
                    time.sleep(3)
                    print("Ohhh hold whatever thought you're having I see lights ahead!")
                    time.sleep(3)

                    print()
                    random_event()
                    print()

                    print("Nice! It could have been a lot worse, but I'm alive still, that's what counts.")
                    time.sleep(3)
                    print()
                    print("So you think I will make it to the facility with this?")
                    print()
                    time.sleep(2)
                    print("Are you even going North?                                                [1]")
                    print("What else could it be? Kepler is supposed to be unexplored territory     [2]")
                    print()

                    answer3 = ""
                    while answer3 not in answers1:
                        answer3 = input("Enter here:  ")
                    else:
                        if answer3 in answers1:
                            print()
                            print("Well, I think I'm going North.")
                            time.sleep(2)
                            print("I can't do anything else, I'll wait it out see where this terminates")
                            time.sleep(3)
                            print("Hopefully not a dead end, or my death for that matter.")
                            time.sleep(3)
                            print("I might as well get comfortable and I will keep you updated")
                            time.sleep(2)
                    print()
                    random_event()
                    print()

                    print("Pheww! Thank god for you huh! I don't think I would have made it this far without you")
                    time.sleep(3)
                    print("We still have far to go, I think. We will never know until we get out of here I guess.")
                    time.sleep(3)
                    print("I hope we are close to an exit!")
                    time.sleep(2)
                    print("I don't know how many of those enemies I can handle")
                    time.sleep(3)
                    print("I'm just starting to get tired that's all.")
                    time.sleep(2)
                    print("Ok! Same thing then. I will let you know of anything new!")
                    time.sleep(3)
                    print(". . .")
                    time.sleep(1)
                    print(". . .")
                    time.sleep(1)
                    mineshaft_exit()


def random_event():  # Trigger events called at random for the minecart sequence in game
    choices = (1, 2, 3)
    event_1 = random.choice(choices)

    answers = ["1", "2"]
    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""

    if event_1 == 1:
        print("Wow okay, I see a Trikafungus on the tracks!")
        time.sleep(2)
        print("Surely this thing cart will obliterate him right?")
        time.sleep(2)
        print()
        print("--> Take cover in the cart and let it ram it.                      [1]")
        print("--> Stab it in the neck with the shiv if in combat!                [2]")
        print()

        while answer1 not in answers:
            answer1 = input("Enter here:  ")
        else:
            if answer1 == answers[0]:
                print("--> Take cover in the cart and let it ram it.")
                time.sleep(1)
                print()
                print("Will do then! I guess staying silent and avoiding these guys might be the way to go.")
                time.sleep(3)
                print("Wooo that's disgusting! That exploded everywhere.")
                time.sleep(2)
                print("I'm clear though, I just stayed hidden in the cart so I'm fine for now.")
            if answer1 == answers[1]:
                print("--> Stab it in the neck with the shiv if in combat!")
                time.sleep(1)
                print()
                print("Okay, I'll remember that!")
                time.sleep(1)
                print("Wooo that's disgusting! That exploded everywhere.")
                time.sleep(2)
                print("I think I might throw up.")
                time.sleep(2)
                print("Oh my god I feel sick.")
                time.sleep(2)
                print()
        choices = (x for x in choices if x != 1)  # Remove played choice from choices, so player does not repeat events.
        return choices

    elif event_1 == 2:
        print(usr_name, "Hey, Hey I got something up ahead.")
        time.sleep(2)
        print("The tracks split left and right but the right side is blocked by debris!")
        time.sleep(3)
        print("Should I keep going through the left path or maybe get out and blow up the debris.")
        time.sleep(3)
        print("It could maybe open up to another mineshaft, or another path to the facility")
        time.sleep(3)
        print("What are you thinking?")
        time.sleep(1)
        print()
        print("Don't take any risks if creatures are involved. Stay on the clear path. [1]")
        print("Could be a way out of the mines. Blow up the debris!                    [2]")
        print()
        time.sleep(3)
        while answer2 not in answers:
            answer2 = input("Enter here:  ")
        else:
            if answer2 == answers[0]:
                print()
                print("--> Don't take any risks if creatures are involved. Stay on the clear path.")
                time.sleep(1)
                print()
                print("I agree! No distractions! Lets see where this track takes us!")
                time.sleep(3)
                print("Uhmmm,", usr_name, usr_name.upper(), '''I see an opening far ahead 
with a bunch of creepy crawling creatures lurking.''')
                time.sleep(4)
                print("What do I do? Do I throw an explosive?")
                time.sleep(2)
                print("Sounds about right, I wont bother you for this one, I'll try take care of them.")
                time.sleep(4)
                print("Aaand BOOM!")
                time.sleep(1)
                print("WOOO! That should do it! There is no way anything survives that!")
                time.sleep(3)
                print("Ohh one made it on the cart alive!")
                time.sleep(2)
                print("Ahhh! Die you creepy crawly!")
                choices = (x for x in choices if x != 2)  # Remove played choice from choices
                return choices

            if answer2 == answers[1]:
                print()
                print("--> Could be a way out of the mines. Blow up the debris!")
                time.sleep(1)
                print("Agreed! I want to get out of here as fast as possible.")
                time.sleep(3)
                print("Placing explosives.")
                time.sleep(1)
                inventory["Explosives"] -= 1
                print("Removed 1 Explosive from Inventory")
                print()
                print(inventory)
                print()
                print("I feel like this is going to attract a lot of them clickers")
                time.sleep(2)
                print("So I have to be quick")
                time.sleep(2)
                print("Ok. Its time. Exploding in")
                time.sleep(2)
                print()
                print("3")
                time.sleep(1)
                print()
                print("2")
                time.sleep(1)
                print()
                print("1")
                time.sleep(1)
                print()
                print(".")
                time.sleep(1)
                print()
                print(".")
                time.sleep(1)
                print("Ah- th- w-s a st-ng explo-ion.")
                time.sleep(2)
                print()
                print("O- M- GOD! th- it..")
                time.sleep(2)
                print("Th- so m-any o- them")
                time.sleep(2)
                print()
                print(". . .")
                print()
                time.sleep(1)
                print("I a-m n-t m-o mov-ing.")
                time.sleep(2)
                print()

                print("I cant understand anything you're saying.        [1]")
                print("Return to the cart quick!                        [2]")
                print()
                time.sleep(2)
                while answer3 not in answers:
                    answer3 = input("Enter here:  ")
                else:
                    if answer3 == answers[0]:
                        print()
                        print("--> I can't understand anything you're saying.")
                        print()
                        time.sleep(1)
                        print("O-,u- uhh.")
                        time.sleep(1)
                        print("Explosion shook my microphone. Should be good now. ")
                        time.sleep(2)
                        print(usr_name, "They don't now my location and I see them lurking around the explosion.")
                        time.sleep(2)
                        print("I will try throw another explosive maybe killing all of them. And then running.")
                        time.sleep(3)
                        print("Fine with you? Im running out of options looking at them closing in. ")
                        print()
                        time.sleep(3)
                        print("Blow them up!                             [1]")
                        print("Run to the cart and leave quick!          [2]")
                        print()
                        time.sleep(2)
                        while answer4 not in answers:
                            answer4 = input("Enter here:  ")
                        else:
                            if answer4 == answers[0]:
                                print("--> Blow them up!")
                                print()
                                time.sleep(1)
                                print("Clever right? Ok lighting the explosive then.")
                                time.sleep(2)
                                inventory["Explosives"] -= 1
                                print("Removed 1 Explosive from Inventory")
                                print()
                                print(inventory)
                                print()
                                print("I threw it right in the middle of them, now I run!")
                                time.sleep(2)
                                print("Wooo! That should do it! There is no way anything survives that!")
                                time.sleep(2)
                                print("Made it to the cart. Time to go!")
                                choices = (x for x in choices if x != 2)  # Remove played choice from choices
                                return choices

                            if answer4 == answers[1]:
                                print()
                                print("--> Run to the cart and leave quick!")
                                print()
                                time.sleep(1)
                                print("Oh boy! They are closing in.")
                                time.sleep(1)
                                print("I'm running in")
                                print("3")
                                time.sleep(.5)
                                print("2")
                                time.sleep(.7)
                                print("1")
                                time.sleep(1)
                                print()
                                print(". . .")
                                print()
                                time.sleep(1)
                                print("Made it to the cart! I think they heard me though.")
                                time.sleep(2)
                                print("Yeah they definitely heard me!")
                                time.sleep(2)
                                print("Gotta go fast!")
                                time.sleep(2)
                                print("Oh no! One is trying to climb in!")
                                time.sleep(2)
                                print("Get out of here filthy clicker!")
                                time.sleep(2)
                                print(". . .")
                                time.sleep(1)
                                print("I got him! Sliced his neck right through and he's gone")
                                time.sleep(2)
                                choices = (x for x in choices if x != 2)  # Remove played choice from choices
                                return choices

                    if answer3 == answers[1]:
                        print()
                        print("--> Return to the cart!")
                        print()
                        time.sleep(1)
                        print("Oh boy! They are closing in.")
                        time.sleep(1)
                        print("I'm running in")
                        print("3")
                        time.sleep(.5)
                        print("2")
                        time.sleep(.7)
                        print("1")
                        time.sleep(1)
                        print()
                        print(". . .")
                        print()
                        time.sleep(1)
                        print("Made it to the cart! I think they heard me though.")
                        time.sleep(2)
                        print("Yeah they definitely heard me!")
                        time.sleep(2)
                        print("Gotta go fast!")
                        time.sleep(2)
                        print("Oh no! One is trying to climb in!")
                        time.sleep(2)
                        print("Get out of here filthy clicker!")
                        time.sleep(2)
                        print(". . .")
                        time.sleep(1)
                        choices = (x for x in choices if x != 2)  # Remove played choice from choices
                        return choices

    elif event_1 == 3:
        print()
        print("Is, is that sunlight?")
        time.sleep(2)
        print("Ohh my! the tracks surface!")
        time.sleep(2)
        print("Okay! I have good news and bad news!")
        time.sleep(2)
        print("Which do you want first?")
        time.sleep(2)
        print()
        print("Good news first!  [1]")
        print("Bad news first!   [2]")
        print()
        time.sleep(1)
        while answer2 not in answers:
            answer2 = input("Enter here:  ")
        else:
            if answer2 == answers[0]:
                print()
                print("--> Good news first!")
                time.sleep(1)
                print("Well good news is, this is definitely the way to the facility.")
                time.sleep(3)
                print("I see the facility in the far distance. Maybe even less than 3km away with 3 days left.")
                time.sleep(3)
                print("So I still have plenty of time to make it to the extraction.")
                time.sleep(2)
                print("Bad news, I can see ahead that I am going underground again!")
                time.sleep(2)
                print("Hopefully to an exit!")
                time.sleep(2)
                print("Oh no! there is a small rubble blockage at the left of the entrance.")
                time.sleep(2)
                print("I don't know if the cart fits.")
                time.sleep(2)
                print()
                print("Can you avoid if by tilting the cart?  [1]")
                print("Brace yourself.                        [2]")
                print()
                time.sleep(2)
                while answer3 not in answers:
                    answer3 = input("Enter here:  ")
                else:
                    if answer3 == answers[0]:
                        print()
                        print("--> Can you avoid if by tilting the cart?")
                        print()
                        time.sleep(1)
                        print("Good idea! Lets see if it works.")
                        time.sleep(2)
                        print("Woooo! worked like a charm! nice job!")
                        time.sleep(2)
                        choices = (x for x in choices if x != 3)  # Remove played choice from choices
                        return choices
                    if answer3 == answers[1]:
                        print()
                        print("--> Brace yourself.")
                        print()
                        time.sleep(1)
                        print("Well, you've gotten me this far!")
                        time.sleep(2)
                        print("I have faith in you so here goes nothing!")
                        time.sleep(2)
                        print()
                        print(". . . ")
                        print()
                        time.sleep(1)
                        choices = (x for x in choices if x != 3)  # Remove played choice from choices
                        return choices

            if answer2 == answers[1]:
                print()
                print("--> Bad news first!")
                time.sleep(1)
                print("Really? bad news first, who does that?")
                time.sleep(2)
                print("Anyways, the bad news is, I can see ahead that I am going underground again in a bit!")
                time.sleep(3)
                print("Hopefully to another exit though!")
                time.sleep(2)
                print("Good news on the other hand.")
                time.sleep(2)
                print("This is definitely the way to the facility.")
                time.sleep(2)
                print("I see the facility in the far distance. Maybe even less than 3km away with 3 days left.")
                time.sleep(3)
                print("So I still have plenty of time to make it to the extraction.")
                time.sleep(2)
                print("Oh no! there is a small rubble blockage at the left of the entrance.")
                time.sleep(2)
                print("I don't know if the cart fits.")
                time.sleep(2)
                print()
                print("Can you avoid if by tilting the cart?  [1]")
                print("Brace yourself.                        [2]")
                print()
                time.sleep(2)
                while answer3 not in answers:
                    answer3 = input("Enter here:  ")
                else:
                    if answer3 == answers[0]:
                        print()
                        print("--> Can you avoid if by tilting the cart?")
                        print()
                        time.sleep(1)
                        print("Good idea! Lets see if it works.")
                        time.sleep(2)
                        print("Woooo! worked like a charm! nice job!")
                        time.sleep(2)
                        choices = (x for x in choices if x != 3)  # Remove played choice from choices
                        return choices
                    if answer3 == answers[1]:
                        print()
                        print("--> Brace yourself.")
                        print()
                        time.sleep(1)
                        print("Well, you've gotten me this far!")
                        time.sleep(2)
                        print("I have faith in you so here goes nothing!")
                        time.sleep(2)
                        print()
                        print(". . . ")
                        print()
                        time.sleep(1)
                        choices = (x for x in choices if x != 3)  # Remove played choice from choices
                        return choices


def spaceship():
    time.sleep(2)
    print("Oh! Engines have started.")
    time.sleep(2)
    print("It's time! Once we are up in the air, I can change hiding spot.")
    time.sleep(3)
    print()
    print("Stay put!        [1]")
    print("Search the ship. [2]")
    print()

    answer = ""
    answers = ["1", "2"]
    while answer not in answers:
        answer = input("Enter here:  ")
    else:
        if answer == answers[0]:
            print()
            print("--> Stay put!")
            time.sleep(1)
            print("You sure?")
            time.sleep(2)
            print("I guess, I have to wait until we land so I might as well get comfortable here.")
            time.sleep(3)
            print(". . .")
            time.sleep(1)
            print("Someone just entered the cargo room!")
            time.sleep(2)
            print(". . .")
            time.sleep(1)
            print("He's close!")
            time.sleep(1)
            print("Oh no! I think he- ")
            time.sleep(2)
            print("Get OFF OF ME! Ahh!! ")
            time.sleep(2)
            print(".")
            death("DEATH -> SHOT BY TRAVELLER")
            spaceship()
        if answer == answers[1]:
            print()
            print("--> Search the ship.")
            time.sleep(1)
            print("Exactly my plan!")
            time.sleep(1)
            print("Ok, I'm currently at the cargo area and there's no one here that I see.")
            time.sleep(2)
            print("I can see people circling the hallways. If I want to search the ship I will have to blend in!")
            time.sleep(3)
            print("Doors seem to require a key card to open!")
            print()
            time.sleep(2)

            if "Key card" in inventory:  # Checks if player has already pickup up the key card to proceed
                print("Im glad I picked this up from the traveller outside.")
                time.sleep(2)
                print()
                print("Used Key card")
                print()
                time.sleep(1)
                print("It worked!")
                time.sleep(1)
                print("Ok, okay, umm, I see a total of 2 guards, do I sneak passed them or take them out?")
                time.sleep(3)

                print()
                print("Sneak to another room.    [1]")
                print("Shoot them!               [2]")
                print()
                answer1 = ""

                while answer1 not in answers:
                    answer1 = input("Enter here:  ")
                else:
                    if answer1 == answers[0]:
                        print()
                        print("--> Sneak to another room.")
                        print()
                        time.sleep(1)
                        print("Good call, I'm not sure I want to alert myself yet.")
                        time.sleep(2)
                        print("On my way.")
                        time.sleep(1)
                        print(". . .")
                        time.sleep(1)
                        print(". . .")
                        time.sleep(1)
                        print("Used Key card")
                        time.sleep(1)
                        print('''I'm in! I found an outfit which should hopefully,
give me enough time for a disguise in order to escape when I get to the facility.''')
                        time.sleep(4)
                        print("I should head back to the cargo room now and hide until we arrive, right?")
                        time.sleep(3)
                        print("I have everything I need to escape, I just need to land safely now.")
                        facility()
                    if answer1 == answers[1]:
                        print()
                        print("--> Shoot them! ")
                        print()
                        time.sleep(1)
                        print("Well then, I guess we are taking over the spaceship!")
                        time.sleep(1)
                        print("Used Ray Gun")
                        time.sleep(1)
                        print(". . .")
                        time.sleep(1)
                        print("Two down. I hear more coming! This gun is really loud!")
                        print()
                        inventory["Ray Gun"] = 1
                        print(inventory)
                        time.sleep(2)
                        print()
                        answer2 = ""
                        print("Run back to the cargo area!  [1]")
                        print("Hide.                        [2]")
                        print()

                        while answer2 not in answers:
                            answer2 = input("Enter here:  ")
                        else:
                            if answer2 == answers[0]:
                                print()
                                print("--> Run back to the cargo area!")
                                print()
                                time.sleep(1)
                                print("Way ahead of you buddy im already here!")
                                time.sleep(2)
                                print("They will find me here I should think of something!")
                                time.sleep(3)
                                print("I'm not sure I can make it out of this one my friend")
                                time.sleep(3)
                                print("It was a hell of an adventure!")
                                time.sleep(2)

                                print()
                                print("What? So you're quitting now? At the end?    [1]")
                                print("Hide.                                        [2]")
                                print()

                                answer3 = ""
                                while answer3 not in answers:
                                    answer3 = input("Enter here:  ")
                                else:
                                    if answer3 == answers[0] or answers[1]:
                                        ending_1()

                            if answer2 == answers[1]:
                                print()
                                print("--> Hide")
                                print()
                                time.sleep(1)
                                print("Way ahead of you buddy!")
                                time.sleep(1)
                                print("I'm back in the prev-")
                                time.sleep(1)
                                print("Oh no-")
                                time.sleep(1)
                                print("No No! Let me go!")
                                time.sleep(1)
                                print("AHH!")
                                time.sleep(1)
                                print("What are you going to do to me?")
                                time.sleep(1)
                                print("l-Larry?")
                                time.sleep(1)
                                print("I thought you were captured wh- what is going on here?")
                                time.sleep(1)
                                print("You work for these guys? What happened to OUR team and OUR orders?")
                                time.sleep(1)
                                print("TALK GOD DAMMIT! WHY WON'T YOU SAY SOMETHING!")
                                time.sleep(1)
                                print("WHAT DID YOU- -")
                                death("DEATH -> SHOT BY LARRY")
                                spaceship()

            else:
                print("If I could only get my hands on a key card!")
                time.sleep(2)
                print("For now I guess I have to wait here.")
                time.sleep(2)
                print("Oh no! Someone's coming in the cargo room")
                time.sleep(2)

                print()
                print("Hide!            [1]")
                print("Take him out!    [2]")
                print()
                answer1 = ""

                while answer1 not in answers:
                    answer1 = input("Enter here:  ")
                else:
                    if answer1 == answers[0]:
                        print()
                        time.sleep(1)
                        print("--> Hide")
                        time.sleep(1)
                        print("On it!")
                        time.sleep(1)
                        print(". . .")
                        time.sleep(1)
                        print("He's coming close, I think I may have a chance to take him out!")
                        time.sleep(3)
                        print(". . .")
                        time.sleep(2)
                        print(". . .")
                        time.sleep(2)
                        print("ah! ahhh! come on!! .. don't, fight, it!")
                        time.sleep(2)
                        print("WOO! Got him! okay!")
                        time.sleep(1)
                        print("Yes! we got the key card, and I found a ray gun as well.")
                        time.sleep(3)
                        inventory["Key card"] = '1'  # Updating Inventory
                        inventory["Ray Gun"] = '3'   # Updating Inventory
                        print()
                        print(inventory)
                        print()
                        time.sleep(2)
                        print("Off to search the spaceship then. I will let you know what I see.")
                        time.sleep(2)
                        print()
                        print("Used Key card")
                        print()
                        time.sleep(1)
                        print("It worked!")
                        time.sleep(1)
                        print("Ok, okay, umm, I see a total of 2 guards, do I sneak passed them or take them out?")
                        time.sleep(3)

                        print()
                        print("Sneak to another room.    [1]")
                        print("Shoot them!               [2]")
                        print()
                        answer2 = ""

                        while answer2 not in answers:
                            answer2 = input("Enter here:  ")
                        else:
                            if answer2 == answers[0]:
                                print()
                                print("--> Sneak to another room.")
                                print()
                                time.sleep(1)
                                print("Good call, I'm not sure I want to alert myself yet.")
                                time.sleep(2)
                                print("On my way.")
                                time.sleep(1)
                                print(". . .")
                                time.sleep(1)
                                print(". . .")
                                time.sleep(1)
                                print("Used Key card")
                                time.sleep(1)
                                print('''I'm in! I found an outfit which should hopefully,
give me enough time for a disguise in order to escape when I get to the facility.''')
                                time.sleep(4)
                                print("I should head back to the cargo room now and hide until we arrive, right?")
                                time.sleep(3)
                                print('''I have everything I need to escape, I just need to get back to hiding 
and wait to land safely.''')
                                time.sleep(3)
                                print(". . .")
                                time.sleep(1)
                                print(". . .")
                                time.sleep(1)
                                print("I'm back in hiding")
                                facility()
                            if answer2 == answers[1]:
                                print()
                                print("--> Shoot them! ")
                                print()
                                time.sleep(1)
                                print("Well then, I guess we are taking over the spaceship!")
                                time.sleep(1)
                                print("Used Ray Gun")
                                time.sleep(1)
                                print(". . .")
                                time.sleep(1)
                                print("Two down. I hear more coming! This gun is really loud!")
                                print()
                                inventory["Ray Gun"] = 1
                                print(inventory)
                                time.sleep(2)
                                print()

                                answer3 = ""

                                print("Run back to the cargo area!  [1]")
                                print("Hide.                        [2]")
                                print()

                                while answer3 not in answers:
                                    answer3 = input("Enter here:  ")
                                else:
                                    if answer3 == answers[0]:
                                        print()
                                        print("--> Run back to the cargo area!")
                                        print()
                                        time.sleep(1)
                                        print("Way ahead of you buddy im already here!")
                                        time.sleep(2)
                                        print("They will find me here I should think of something!")
                                        time.sleep(3)
                                        print("I'm not sure I can make it out of this one my friend")
                                        time.sleep(3)
                                        print("It was a hell of an adventure!")
                                        time.sleep(2)

                                        print()
                                        print("What? So you're quitting now? At the end?    [1]")
                                        print("Hide.                                        [2]")
                                        print()

                                        answer4 = ""
                                        while answer4 not in answers:
                                            answer4 = input("Enter here:  ")
                                        else:
                                            if answer4 == answers[0] or answers[1]:
                                                ending_1()

                    if answer1 == answers[1]:
                        print()
                        time.sleep(1)
                        print("--> Take him out")
                        time.sleep(1)
                        print("Yeah I have to don't I.")
                        time.sleep(1)
                        print("Here he comes.")
                        time.sleep(1)
                        print(". . .")
                        time.sleep(1)
                        print(". . .")
                        time.sleep(1)
                        print("Ahh!")
                        time.sleep(1)
                        print(". . .")
                        time.sleep(1)
                        print("No! No! AHH!")
                        death("DEATH -> CHOKED TO DEATH")
                        spaceship()


def mineshaft_exit():  # Exit function from the mineshaft location in game.
    print(usr_name, usr_name, "Hey, are you there? I have good news I think.")
    time.sleep(3)
    print("I fell asleep on the cart but it seems like we made it to the end!")
    time.sleep(3)
    print("Time to get out of here and out of this planet!")
    time.sleep(2)
    print("I see the exit!")
    time.sleep(1)
    print("It's the same trapdoor as in the cabin!")
    time.sleep(2)
    print("I don't remember the key code, I must have lost the piece of paper along the way!")
    time.sleep(3)
    print("5  4  5  2  5  7")
    time.sleep(2)
    print("Wrong!")
    time.sleep(1)
    print("Umm 5 7 4 2 5 8")
    time.sleep(1)
    print("Wrong again!")
    time.sleep(1)
    print("Ahh! Dammit I don't remember! My brain can't function right now.")
    time.sleep(2)
    print("You must remember right? You have to!")
    time.sleep(2)

    time.sleep(1.5)
    answer = ""
    while answer != password_answer:  # Checking whether passsword typed by player is correct password
        print()
        print(password)
        print()

        answer = input("Type Password: ").split()
    else:
        if answer == password_answer:
            print("Correct! The trapdoor opened!")
            time.sleep(1)
            print("Ha HAA! You remembered!")
            time.sleep(1)
            print("Thank god!")
            time.sleep(1)
            print("Now lets see where we are!")
            facility()


def facility():  # One of three final endings for the player.
    print()
    time.sleep(2)
    print("I, I made it!")
    time.sleep(1)
    print("We Made it!!")
    time.sleep(1)
    print("I think I can take it from here partner!")
    time.sleep(2)
    print("We made it to the extraction point with 2 days to spare! ")
    time.sleep(3)
    print("I'll let you get back to your work then! Thank you for being part of this awesome but terrifying adventure")
    time.sleep(4)
    print()
    print()
    print("[GAME OVER]")
    print("[REACHED ENDING 'C']")


def ending_1():  # Two of three possible endings for the player.
    print()
    print("No! No more waiting around, or quitting, or hiding!")
    print('''There are enough explosives to blow up this spaceship 
    and everyone in it''')
    time.sleep(5)
    print("Including me!")
    time.sleep(2)
    print('''I will stop those travellers 
    from causing any more damage to this planet''')
    time.sleep(4)
    print("Even if its the last thing I do!")
    time.sleep(3)
    print("I hope you agree because I've set up the explosives while talking.")
    time.sleep(3)
    print("Here they come!")
    time.sleep(1)
    print(". . .")
    time.sleep(1)
    print(". . .")
    time.sleep(1.5)
    print(". . .")
    time.sleep(2)
    print("l- Lary?")
    time.sleep(1)
    print("Tonya, Michael, wh-what is going on?")
    time.sleep(3)
    print("I thought you guys were captured wh- what is going on here?")
    time.sleep(3)
    print("I was coming back to rescue you and bring you home.")
    time.sleep(3)
    print("You work for these guys? What happened to OUR team and OUR orders?")
    time.sleep(3)
    print()
    print("Michael: JOE! put, the detonator down, and we will explain everything.")
    time.sleep(4)
    print()
    print('''Joe: You don't make the rules now, I
    will blow up this ship If you don't start talking, NOW''')
    time.sleep(5)
    print()
    print("Larry: Okay, Joe, calm down, you don't won't to do this.")
    time.sleep(3)
    print("Let me explain.")
    time.sleep(1)
    print('''3 years ago, 
    we came to this planet to test the potential of a second Earth''')
    time.sleep(4)
    print("Remember that?")
    time.sleep(1)
    print('''Well turns out, this planet was discovered before we were here. 
    These people have been trying to eradicate infestations of creatures and infected that make this planet, 
    well, dangerous really.''')
    time.sleep(7)
    print('''Joe! These people are from an alternate Earth!
    That's why our mission was to investigate anomalies with Kepler 11, because travellers from our Earth had never been 
    authorised to work here!''')
    time.sleep(8)
    print()
    print('''Tanya: It's true Joe! You have to believe us! 
    we never wanted to put you in this situation''')
    time.sleep(4)
    print()
    print("Joe: But, you guys were captured supposedly.")
    time.sleep(3)
    print("Why didn't you make contact with me?")
    time.sleep(2)
    print()
    print("Larry: We thought you were dead! We thought this planet took you!")
    time.sleep(3)
    print("Now come on Joe! Put the detonator down and lets have the team back! New and Improved!")
    time.sleep(3)
    print()
    print("Joe: I don't know what to say now Larry.")
    time.sleep(2)
    print(usr_name, '''Hey you still here partner? 
    Im not making this decision without you! You've helped more than anyone these few days,
     so I am happy to leave this on you''')
    time.sleep(6)
    print("What do you think I should do?")
    print()
    print("Join the other Travellers.   [1]")
    print("Blow up the plane.           [2]")
    print()

    answer = ""
    answers = ["1", "2"]
    while answer not in answers:
        answer = input("Enter decision:  ")
    else:
        if answer == answers[0]:
            print()
            print("--> Join the other Travellers.")
            print("--> It was an honour to be in this adventure with you Joe! Now go be with you team!")
            print()
            time.sleep(2)
            print("*Puts detonator down*")
            time.sleep(1)
            print("Joe: It's good to see you guys!")
            print()
            print("Michael: It's good to have you back buddy!")
            time.sleep(3)
            print("We have a lot to tell you man!")
            time.sleep(1.5)
            print(". . .")
            time.sleep(2)
            print(". . .")
            time.sleep(2)
            print("[GAME OVER]")
            print("[REACHED ENDING 'A']")
        if answer == answers[1]:
            print()
            print("--> Blow up the plane")
            print("--> It was an honour to be in this adventure with you Joe! I will remember you!")
            print()
            time.sleep(2)
            print("Damn, intern, we've got the same ideas after all!")
            time.sleep(3)
            print("Goodbye my friend.")
            time.sleep(2)
            print("As for you guys.")
            time.sleep(1)
            print("I lost my team three years ago Larry. Nothing is bringing them back. ")
            time.sleep(3)
            print(". . .")
            time.sleep(1)
            print(". . .")
            time.sleep(2)
            print("[GAME OVER]")
            print("[REACHED ENDING 'B']")
            death("DEATH -> BOMB EXPLOSION")
            return


def death(reason):  # death function that explains the type of death.
    print()
    print("[Connection Signal Lost]")
    time.sleep(1)
    print("[Traveller 017 is now offline]")
    print()
    print(reason)
    print("[CONSOLE RESTARTING]")
    time.sleep(3)
    print()
    print()


intro()  # Game Begins and runs from intro
