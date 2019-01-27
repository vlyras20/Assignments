import time
import random

gameOver = False
inventory = ["", "", ""]
inventory_empty = "[Inventory Empty]"
daysLeft = 5
distance = 10000
sanity = 100
contacts = {""}
usr_name = ""


def intro():
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

    while answer not in answers:
        answer = input("Enter here:  ")
    else:
        setting()
    return


def setting():
    answers = ["1", "2", "3"]
    answer = ""

    print()
    print('''Well long story, my mission in Kepler 11 was compromised and I have
5 days to make it to my extraction point before im stuck here indefinitely,
while also being hunted by the other traveler team.''')
    time.sleep(5)
    print()
    print("Kepler 11? How are you in Kepler 11?                              [1]")
    print("How far is the extraction point?                                  [2]")
    print("I don't know how to help, im just an intern at Nasa.              [3]")
    print()

    while answer not in answers:
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


def main():
    distance = 10000
    daysLeft = 5
    answers = ["1", "2", "3", "Yes", "No",  "no", "NO"]
    answer1 = ""

    while answer1 not in answers:
        print()
        print("Is the lake frozen solid, or would you fall through?        [1]")
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
            print('''It would slow me a bit but it sounds good to me, I'll stay the night there and tomorrow we move early,"
what do you think?  [Yes]/[No]''')
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


def lake():
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
    time.sleep(2)

    print()
    global sanity
    sanity -= 20
    print('''            [DISTANCE] = 9000
            [DAYS UNTIL EXTRACTION] = 5
            [SANITY] = 80''')
    print()

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
            death()
            lake()

        if answer == answers[1]:
            print("Good call! Get a good sleep and I might even find supplies in there as well.")
            time.sleep(2)
            print("I will let you know once I've reached the cabin then.")
            time.sleep(2)
            print('''I see some weird blue creatures to the left further away.
                  I'm glad I came through the lake so I didn't have to face them.''')
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

            answers2 = ["1", "2"]
            answer2 = ""

            while answer2 not in answers2:
                answer2 = input("Enter here:  ")
                print()
            else:
                if answer2 == answers2[0]:
                    print("Well I hope you're right. I'll keep you updated.")
                elif answer2 == answers2[1]:
                    print("Really? I mean, it kinda makes sense I guess. Ok, I will keep you updated.")
        elif answer == answers[1]:
            print('''Nothing but the frozen lake. I think my best chances are
dealing with these creatures fast and not waste time finding another way''')
            time.sleep(3)
            print("So do you have any knowledge of these things or should I just slowly pass them?")
            print()
            time.sleep(2)
            print("Well blue bears are deaf so as long as they don't see you, you should be fine.  ")
            time.sleep(2)
            print("Try maybe crawling through the snow so they can't see you.")
            print()
            time.sleep(1)
            print(usr_name, "I'm not sure about maybes in this situation. Do you have anything more certain than that?")
            time.sleep(2)

            print()
            print("--->Nope, that's your best bet at this moment. [1]")
            print("--->Run for it when you find a chance!         [2]")
            print()

            answers2 = ["1", "2"]
            answer2 = ""

            while answer2 not in answers2:
                answer2 = input("Enter here:  ")
                print()
            else:
                if answer2 == answers2[0]:
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

                    print()
                    print("If you're close enough go for it.        [1]")
                    print("No, stay hidden! Don't let them see you. [2]")
                    while answer2 not in answers2:
                        answer2 = input("Enter here:  ")
                        print()
                    else:
                        if answer2 == answers2[0]:
                            print()
                            cabin_calm()
                        elif answer2 == answers2[1]:
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
                elif answer2 == answers2[1]:
                    print("Really? I mean, it kinda makes sense I guess. Ok, I will keep you updated.")
                    time.sleep(2)
                    print("Ok. they've spread out enough! This is my chance and I'm going for it!")
                    time.sleep(2)
                    print("RUUUUUUUN!")
                    time.sleep(1)
                    print("Almost at the cabin!")
                    time.sleep(1)
                    print("Oh no! I see one looking at me! Im just running it! Go Go Go!")
                    time.sleep(2)
                    print("Made it to the door! ")
                    time.sleep(1)
                    print('''Phewww! Made it! that was close and I think they're circling the cabin outside
so Im trapped here for a while.''')
                    time.sleep(3)
                    cabin_surrounded()


def cabin_calm():
    global distance
    distance -= 920
    answer = ""
    answers = ["1", "2"]

    answer1 = ""
    answers1 = ["1", "2", "3"]

    time.sleep(2)
    print("Almost at the door.")
    time.sleep(1)
    print('''Phewww! Made it! Easy, Ok.''')
    time.sleep(2)
    print("I think the creatures haven't noticed me so I should be able to stay here until they leave.")
    time.sleep(3)
    print("I, I see nothing. It's pitch black. Let me see what I have on me.")
    time.sleep(2)
    print()
    print(inventory)
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
            [DAYS UNTIL EXTRACTION] = 4
            [SANITY] = 79''')
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
            print(usr_name, "...", usr_name, "Oh man it's freezing!")
            time.sleep(1)
            print('''Im glad I slept in here however, 
I don't know if I would have made it camping at the forest in this cold.''')
            time.sleep(3)
            print("Better start searching around, see what I can find in this place.")
            time.sleep(2)
            print("I see a lot of cupboards but no supplies. Thats not a good sign.")
            time.sleep(2)
            print("Oh, oh my, what is that smell?")
            time.sleep(2)
            print("Wooow! There's a corpse in the closet. Someone has been here recently.")
            time.sleep(2)

            print()
            print("Leave it! keep searching the room.      [1]")
            print("Search the body for supplies.           [2]")

            while answer not in answers:
                print()
                answer = input("Enter here:  ")
                print()
            else:
                if answer == answers[0]:
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

                    while answer not in answers:
                        print()
                        answer = input("Enter here:  ")
                        print()
                    else:
                        if answer == answers[0]:
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

                            while answer not in answers:
                                print()
                                answer = input("Enter here:  ")
                                print()
                            else:
                                if answer == answers[0]:
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
                                    while answer not in answers:
                                        print()
                                        answer = input("Enter here:  ")
                                        print()
                                    else:
                                        if answer == answers[0]:
                                            print("--> Open the trapdoor. ")
                                            print()
                                            time.sleep(1)
                                            print('''I like your thinking! If it indeed leads to the facility,
 this might change everything''')
                                            time.sleep(2)
                                            mineshaft()
                                        if answer == answers[1]:
                                            print("--> Ignore it! Leave for the forest now.")
                                            print()
                                            time.sleep(2)
                                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                            time.sleep(3)
                                            forest()

                                if answer == answers[1]:
                                    print("--> Leave it! You have a long way to go until the extraction.")
                                    time.sleep(1)
                                    print()
                                    print('''Yeah? I guess you're right. 
                            The mineshaft might take me completely out of my way.''')
                                    forest()
                if answer == answers[1]:
                    print("--> Search the body for supplies.")
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

                    while answer1 not in answers1:
                        print()
                        answer1 = input("Enter here:  ")
                        print()
                    else:
                        if answer1 == answers1[0]:
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
                            while answer not in answers:
                                print()
                                answer = input("Enter here:  ")
                                print()
                            else:
                                if answer == answers[0]:
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
                                if answer == answers[1]:
                                    print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                    forest()

                        if answer1 == answers1[1]:
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
                        if answer1 == answers1[2]:
                            print("--> Don't waste time and start heading towards the forest")
                            time.sleep(1)
                            print()
                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                            forest()


def cabin_surrounded():
    global distance
    distance -= 920

    answer1 = ""
    answers1 = ["1", "2", "3"]

    answer = ""
    answers = ["1", "2"]
    print("I, I see nothing. It's pitch black. Let me see what I have on me somehow.")
    time.sleep(2)
    print()
    print(inventory)
    print()
    print('''Well I got nothing. I could just sleep in this corner
until morning comes so I can see whats around. Sound Good?''')
    time.sleep(4)
    print("Sounds good.      [1]")

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
            [DAYS UNTIL EXTRACTION] = 4
            [SANITY] = 79''')
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
            print(usr_name, "...", usr_name, "Oh man it's freezing!")
            time.sleep(1)
            print('''Im glad I slept in here however, 
I don't know if I would have made it camping at the forest in this cold.''')
            time.sleep(3)
            print("Seems like the creatures have left, I don't hear anything outside.")
            time.sleep(2)
            print("Better start searching around quick, see what I can find in this place to help and start moving.")
            time.sleep(2)
            print("I see a lot of cupboards but no supplies. That's not a good sign.")
            time.sleep(2)
            print("Oh, oh my, what is that smell?")
            time.sleep(2)
            print("Wooow! There's a corpse in the closet. Someone has been here recently.")
            time.sleep(2)

            print()
            print("Leave it! keep searching the room.      [1]")
            print("Search the body for supplies.           [2]")

            while answer not in answers:
                print()
                answer = input("Enter here:  ")
                print()
            else:
                if answer == answers[0]:
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

                    while answer not in answers:
                        print()
                        answer = input("Enter here:  ")
                        print()
                    else:
                        if answer == answers[0]:
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

                            while answer not in answers:
                                print()
                                answer = input("Enter here:  ")
                                print()
                            else:
                                if answer == answers[0]:
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
                                    while answer not in answers:
                                        print()
                                        answer = input("Enter here:  ")
                                        print()
                                    else:
                                        if answer == answers[0]:
                                            print("--> Open the trapdoor. ")
                                            print()
                                            time.sleep(1)
                                            print('''I like your thinking! If it indeed leads to the facility,
 this might change everything''')
                                            time.sleep(2)
                                            mineshaft()
                                        if answer == answers[1]:
                                            print("--> Ignore it! Leave for the forest now.")
                                            print()
                                            time.sleep(2)
                                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                            time.sleep(3)
                                            forest()

                                if answer == answers[1]:
                                    print("--> Leave it! You have a long way to go until the extraction.")
                                    time.sleep(1)
                                    print()
                                    print('''Yeah? I guess you're right. 
                            The mineshaft might take me completely out of my way.''')
                                    forest()
                if answer == answers[1]:
                    print("--> Search the body for supplies.")
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

                    while answer1 not in answers1:
                        print()
                        answer1 = input("Enter here:  ")
                        print()
                    else:
                        if answer1 == answers1[0]:
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
                            while answer not in answers:
                                print()
                                answer = input("Enter here:  ")
                                print()
                            else:
                                if answer == answers[0]:
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
                                if answer == answers[1]:
                                    print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                    forest()

                        if answer1 == answers1[1]:
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
                        if answer1 == answers1[2]:
                            print("--> Don't waste time and start heading towards the forest")
                            time.sleep(1)
                            print()
                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                            forest()


def cabin_hurt():
    answers = ["1", "2"]
    answer = ""
    answers1 = ["1", "2","3"]
    answer1 = ""

    global distance
    distance -= 920

    print("Blue bear bites are not poisonous right? ")
    print()
    time.sleep(1)
    print("No, but is it bad? How deep is the bite?             [1]")
    print("Yeah, you might not make the night my friend.        [2]")
    while answer not in answers:
        answer = input("Enter here:  ")
        print()
    else:
        if answer == answers[0]:
            print("It's stable now, I tied it with some cloth I managed to rip.")

        elif answer == answers[1]:
            print("Wait. What? Don't freak me out", usr_name, "You serious?")
            time.sleep(2)
            print("No, calm down commando, I was joking, you'll be alright.     [1]")
            print("Well lets say fever is the last thing you should worry about.[2]")
            while answer not in answers:
                print()
                answer = input("Enter here:  ")
                print()
            else:
                if answer == answers1[0]:
                    print()
                if answer == answers[1]:
                    print("-> Well lets say fever is the last thing you should worry about.")
                    time.sleep(2)
                    print("-> Im joking by the way Mr. Traveler. I don't know if they have humour whenever you're from ")
                    time.sleep(1)
                    print("Funny", usr_name, "Very funny indeed.")
    time.sleep(2)
    print("Well you know what. Ahh! I, I see nothing. It's pitch black and I'm exhausted.")
    time.sleep(2)
    print()
    print(inventory)
    print()
    print('''Hopefully my wound doesn't get infected throughout night time. I could just sleep and rest in this corner
until morning comes so I can see whats around and move from there. Sound Good?''')
    time.sleep(5)
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
            [DAYS UNTIL EXTRACTION] = 4
            [SANITY] = 67''')
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

            while answer not in answers:
                print()
                answer = input("Enter here:  ")
                print()
            else:
                if answer == answers[0]:
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

                    while answer not in answers:
                        print()
                        answer = input("Enter here:  ")
                        print()
                    else:
                        if answer == answers[0]:
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

                            while answer not in answers:
                                print()
                                answer = input("Enter here:  ")
                                print()
                            else:
                                if answer == answers[0]:
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
                                    while answer not in answers:
                                        print()
                                        answer = input("Enter here:  ")
                                        print()
                                    else:
                                        if answer == answers[0]:
                                            print("--> Open the trapdoor. ")
                                            print()
                                            time.sleep(1)
                                            print('''I like your thinking! If it indeed leads to the facility,
 this might change everything''')
                                            time.sleep(2)
                                            mineshaft_hurt()
                                        if answer == answers[1]:
                                            print("--> Ignore it! Leave for the forest now.")
                                            print()
                                            time.sleep(2)
                                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                            time.sleep(3)
                                            forest_hurt()

                                if answer == answers[1]:
                                    print("--> Leave it! You have a long way to go until the extraction.")
                                    time.sleep(1)
                                    print()
                                    print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                    forest_hurt()
                if answer == answers[1]:
                    print("--> Search the body for supplies.")
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

                    while answer1 not in answers1:
                        print()
                        answer1 = input("Enter here:  ")
                        print()
                    else:
                        if answer1 == answers1[0]:
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
                            while answer not in answers:
                                print()
                                answer = input("Enter here:  ")
                                print()
                            else:
                                if answer == answers[0]:
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
                                    mineshaft_hurt()
                                if answer == answers[1]:
                                    print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                                    forest_hurt()

                        if answer1 == answers1[1]:
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
                            mineshaft_hurt()
                        if answer1 == answers1[2]:
                            print("--> Don't waste time and start heading towards the forest")
                            time.sleep(1)
                            print()
                            print('''Yeah? I guess you're right. 
The mineshaft might take me completely out of my way.''')
                            forest_hurt()


def forest():
    print("")


def forest_hurt():
    print()


def mineshaft():
    answers = ["1", "2"]
    answer = ""

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
        elif answer == answers[1]:
            print()
            print("You know what! I think that was a wise choice. Lets just make it to the extraction safely.")
            time.sleep(1)
            forest()


def mineshaft_hurt():
    print()


def death():
    print()
    print("[Connection Signal Lost]")
    time.sleep(1)
    print("[Traveller 017 is now offline]")


intro()
