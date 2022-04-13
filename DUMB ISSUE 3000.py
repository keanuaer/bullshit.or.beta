randomnum = 10

customnum= input ("Type in a number and i ll try guessing: ")


if customnum != randomnum:
    print ("Oh i was wrong. My Number was: " + str(randomnum))

if customnum == randomnum:
    print ("Yes i was right! That was our number:" + str(randomnum))


#Output:
#Type in a number and i ll try guessing: 10 <-- this is the right number
#Oh i was wrong. My Number was: 10 <-- Yes 10 is the right number