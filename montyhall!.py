import random

def thegame(numberoftests):
    switch = 0
    stay = 0
    doors = {1: "ZONK!", 2: "ZONK!", 3: "ZONK!"}

    for i in range(numberoftests):

        #creating random car door
        car = random.randint(1,3)
        doors[car]= "car!"
        original = {}
        original.update(doors)

        #picking a random door
        pickdoor = random.randint(1,3)




        #remove zonk value for one two doors not picked
        pickdoorvalue = doors[pickdoor]
        del doors[pickdoor]

        #get remaining door to chose from
        for i in doors:
            if doors[i] == "ZONK!":
                del doors[i]
                break
        #print(doors)

        doors[pickdoor] = pickdoorvalue

        #print(doors)

        #switching from original pick to new pick
        newpickdoor = 0
        for i in doors:
            #print(pickdoor)
            if i != pickdoor:
                newpickdoor = i
            #print(f"{pickdoor} +  end")

        #counting values for switch and stay

        #print((original))
        if original[newpickdoor] == "car!":
            switch += 1
        elif original[pickdoor] == "car!":
            stay += 1


        #resetting door values
        doors = {1: "ZONK!", 2: "ZONK!", 3: "ZONK!"}


    #printing out the results
    print(f"If you would have swtiched, you would have got the car {switch} times out of {numberoftests}")
    print(f"If you would have stayed, you would have got the car {stay} times out of {numberoftests}")



def main():
    thegame(100000)


main()