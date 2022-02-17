#*not working


print("""


""")
print("DigiButtonTapper *BETA by Keanu_aer")
print("""


""")

#Inputs:

#User Choose Digi Command: 
choosecommand = input("""DigiKeyboard.write (Tap Single Buttons) = 1

DigiKeyboard.sendKeyStroke (Tab Multiple Buttons at the same time) = 2

DigiKeyboard.print (Print Text) = 3

...choose wise:""")
print("""


""")
#ButtonName in DigiScript Language
buttoncommand = input("Key you want to use (In Digiscript Language (Example: /t )): ")
print("""


""")
#Amount of Lines
num = input ("Choose Amount of Lines: ")
print("You choose DigiButtonTapper for " + num +""" times. Here we go: 




""")


#VariableDefinitions
dskbwr = print("""
DigiKeyboard.write('""" + buttoncommand + """');
""")

dsksks = print("""
DigiKeyboard.sendKeyStroke('""" + buttoncommand + """');
""")

dkbpr = print("""
DigiKeyboard.print(" """ + buttoncommand + """ ");
""")


#Selection:

#ChooseCommand Selector

if choosecommand == 1:
    print(dskbwr *int(num)) 
if choosecommand == 2:
    print(dsksks *int(num))
if choosecommand == 3:
    print(dkbpr *int(num))
else:
    print("Ur first answer is out of my imagination. Please restart.")

print("""




""")

input('Press ENTER to exit')
