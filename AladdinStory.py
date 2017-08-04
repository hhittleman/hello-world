start = '''
You are Aladdin.
As an orphan in the Arabian city of Agrabah
you are poor and hungry.
As you walk down the plaza
you see an apple stand that is unattended.
Do you steal the apple ot ignore your hunger?
'''

print(start)

print("Type 'steal' to steal the apple or 'ignore' to ignore hunger.")
user_input = input()
if user_input == "steal":
    print("The vender comes out and sees you. Do you return the apple or run away? Type 'return' to return the apple or 'run' to run away")
    user_input = input()
    if user_input == "return":
        print("The vender gets angry and kills you with the apple.")
    elif user_input == 'run':
        print("You run into an alley. Do you break the window to your left and go into a house or hop the fence? Type 'left' to go into your house or 'hop' to hop the fence.")
        user_input = input()
        if user_input == "left":
            print("You enter the home, see your refleciton in the mirror, and die from horror.")
        elif user_input == "hop":
            print("You find Jasmine. She gives you all the apples you ever wanted. You say 'I like them apples' and live happily.")
elif user_input == "ignore":
    print("You enter a dark state of mind, become depressed, continue to starve, and DIE!!!!!!!")
