import time
import random

gameOver = False
inventory = []
daysLeft = 5
distance = 10000
sanity = 100
contacts = {""}
usr_name = ""


def intro():
    print("[Incoming Message]")
    time.sleep(1)
    print("Connection Established with Traveller 017")
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
            time.sleep(3)
            print("I don't have to mention that everything is fully snowed in I hope")
            time.sleep(3)
            main()

        elif answer == answers[1]:
            print('''Basically, my team will be in planet orbit in 5 days time in order to beam me out of this planet 
and into safe grounds. The extraction point is at a facility, 10km straight North from my location.''')

            print('''                ---> [DISTANCE] set to 10.000m 
            ---> [DAYS UNTIL EXTRACTION] set to 5 ''')
            time.sleep(5)
            print('''So  in order for me to go North I have to either cross a frozen lake or go around the outskirts. 
My issue is time because its slowly turning dark, and the only thing I see is mountains around me, a big lake, 
and a bunch of trees at the other side,
but uhmm what do you think?''')
            time.sleep(3)
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
            time.sleep(4)
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
what do you think?''')
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
    print('''Do I keep moving on the lake, make my way to the forest and camp there, 
or should I turn to the outskirts towards this metal cabin I see? ''')
    time.sleep(3)

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

        if answer == answers[1]:
            print("Good call! Get a good sleep and I might even find supplies in there as well.")
            time.sleep(2)
            print("I will let you know once I've reached the cabin then.")
            cabin()
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
            print("Blue bears are deaf so as long as they don't see you, you should be fine.  ")
            time.sleep(2)
            print("Try maybe crawling through the snow so they can't see you.")
            print()
            time.sleep(1)
            print(usr_name, "I'm not sure about maybes in this situation. Do you have anything more certain than that?")
            time.sleep(2)

            print()
            print("Nope, that's your best bet at this moment. [1]")
            print("Run for it when you find a chance!         [2]")
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
            print("Nope, that's your best bet at this moment. [1]")
            print("Run for it when you find a chance!         [2]")
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
                    print('''Just to let you know, this is terrifying. I'm currently crawling through  ''')
                elif answer2 == answers2[1]:
                    print("Really? I mean, it kinda makes sense I guess. Ok, I will keep you updated.")


def cabin():
    time.sleep(2)
    print("Alms")


def forest():
    print("")


def rdm_event():
    print()


intro()
