def welcome():
    # print the welcome to the game
    print()
    print('Welcome to Wacky Willy\'s Funtime Play World... the game!')
    print()


welcome()


# introduction to game theme and rules to win
def briefIntroductionToGame():
    user_name = input('What\'s your name? ')
    print()
    print("Oh man, {}. You just knew taking this job as the nighttime janitor at this haunted children\'s \namusement "
          "place was a bad idea!".format(user_name), end='')
    print(" This is turning out to be just like the last time! Oh well, looks like \nyou\'ll have to gather a bunch of "
          "weapons so you can destroy Willy the evil animatronic groundhog before \nit powers on and begins it's "
          "murder spree. Some first shift this is turning out to be!")
    print()
    print("You're going to need all the firepower you can get to take Willy down, so be sure to collect all SIX "
          "\nweapons (one in each room) in Wacky Willy\'s Funtime Play World before entering the Animatronics \nStorage"
          " room and facing Willy head to head.")
    print()
    print('"Another day, another dollar.", you say under your breath.')
    print()
    print("You are in the Janitor's Office.")
    print()


briefIntroductionToGame()


# a simple divider to make the game more readable
def divider():
    print('-----------------------------------------------------------------------------------------------------------')


# this is the main game
def main():
    # initially the player's inventory is an empty list
    inventory = []
    # this is a dictionary of the rooms, directions, and items in each room
    rooms = {
        'the Janitor\'s Office': {'South': 'Main Game Room'},
        'the Main Game Room': {'North': 'Janitor\'s Office', 'South': 'Gender Neutral Bathroom', 'East': 'Ball Pit',
                               'West': 'Laser Tag Registration', 'Get item': 'Nunchucks'},
        'the Gender Neutral Bathroom': {'North': 'Main Game Room', 'Get item': 'Piece of Broken Glass'},
        'the Ball Pit': {'West': 'the Main Game Room', 'North': 'the Super Secret Firearm Room',
                         'Get item': 'Rusty Screwdriver'},
        'the Super Secret Firearm Room': {'South': 'Ball Pit', 'Get item': 'Heavy Machine Gun'},
        'Laser Tag Registration': {'North': 'Laser Tag Arena', 'East': 'Main Game Room', 'West': 'Animatronics Storage',
                                   'Get item': 'Roll of Quarters in a Sock'},
        'the Laser Tag Arena': {'South': 'Laser Tag Registration', 'Get item': 'More Nunchucks'},
        'Animatronics Storage': {'East': 'Laser Tag Registration', 'Get item': 'Wacky Willy'},
    }

    # this updates the player's status throughout the game so the player can track their progress
    def playerStatus():
        print()
        divider()
        print('You are now in {}.'.format(currentRoom))
        print()
        print('Inventory = ', inventory)
        print()

    # initially the player starts in their office
    currentRoom = 'the Janitor\'s Office'

    # this is the first input, it also outlines what a player's options are in the game
    print("You can type North, South, East, or West to move from room to room, \"Get item\" to get the item in the "
          "room, \nor \"exit\" at any time to exit the game.")
    print()
    input_command = input("From this room you can only go south. What\'s your move?: ")

    # this while loop is the loop the player stays in while playing the game unless they type 'exit'
    while input_command != 'exit':
        # Janitor's office
        if currentRoom == 'the Janitor\'s Office':
            if input_command in rooms['the Janitor\'s Office'].keys():
                currentRoom = 'the Main Game Room'
                playerStatus()
                input_command = input("Make a move: ")
            elif input_command == 'exit':
                print('exiting...')
                break
            elif input_command == 'Get item':
                print()
                print("There are no usable weapons in this room, better venture out to the other rooms to look for "
                      "anything useful.")
                input_command = input("Try typing just \"South\", it\'s the only way out of here. You can also type "
                                      "\'exit\' to quit: ")
            elif input_command not in rooms['the Janitor\'s Office'].keys():
                print()
                print("You must be tired from staying up all night, that\'s not a valid direction.")
                input_command = input("Try typing just \"South\", it\'s the only way out of here. You can also type "
                                      "\'exit\' to quit: ")
        # Main Game Room
        if currentRoom == 'the Main Game Room':
            if input_command in rooms['the Main Game Room'].keys():
                if input_command == 'North':
                    currentRoom = 'the Janitor\'s Office'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'East':
                    currentRoom = 'the Ball Pit'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'South':
                    currentRoom = 'the Gender Neutral Bathroom'
                    playerStatus()
                    input_command = input("Make a movement (or enter a command): ")
                elif input_command == 'West':
                    currentRoom = 'Laser Tag Registration'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'Get item':
                    print()
                    print("Nice! You knew you\'d need these nunchucks someday, good thing you stored them under the "
                          "vending machine. \nGotta watch a quick YouTube video on how to use these babies.")
                    inventory.append(rooms['the Main Game Room']['Get item'])
                    rooms['the Main Game Room'].pop('Get item')
                    playerStatus()
                    input_command = input("Make a move: ")
            elif input_command not in rooms['the Main Game Room'].keys():
                print()
                print("Come on man, this is life or death. Pick a valid move!")
                input_command = input("You have six choices, try typing just \"North\", \"South\", \"East\", "
                                      "\"West\", \"Get item\" (unless you\'ve already \nfound your nunchucks), "
                                      "or \"exit\": ")
        # Laser Tag Arena
        if currentRoom == 'the Laser Tag Arena':
            if input_command in rooms['the Laser Tag Arena'].keys():
                if input_command == 'South':
                    currentRoom = 'Laser Tag Registration'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'Get item':
                    print()
                    print("I knew I hid another pair of nunchucks in here! You can never have enough nunchucks.")
                    inventory.append(rooms['the Laser Tag Arena']['Get item'])
                    rooms['the Laser Tag Arena'].pop('Get item')
                    playerStatus()
                    input_command = input("Make a move: ")
            elif input_command == 'exit':
                print('exiting...')
                break
            elif input_command not in rooms['the Laser Tag Arena'].keys():
                print()
                print("Let me be more specific. Make a VALID move: ")
                input_command = input('Try typing \"North\", \"East\", \"West\", \"Get item\", or \"exit\".')
        # Gender Neutral Bathroom
        if currentRoom == 'the Gender Neutral Bathroom':
            if input_command in rooms['the Gender Neutral Bathroom'].keys():
                if input_command == 'North':
                    currentRoom = 'the Main Game Room'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'Get item':
                    print()
                    print("Ouch! Who leaves broken glass on the floor of the bathroom? Who\'s "
                          "the janitor at this place?? Oh, wait a \nsecond, that\'s my job.")
                    inventory.append(rooms['the Gender Neutral Bathroom']['Get item'])
                    rooms['the Gender Neutral Bathroom'].pop('Get item')
                    playerStatus()
                    input_command = input("Make a movement (or enter a command): ")
            elif input_command == 'exit':
                print('exiting...')
                break
            elif input_command == 'Movement':
                print()
                print('**flushing noises**')
                playerStatus()
                input_command = input('You\'ve made a movement, now make a move: ')
            elif input_command not in rooms['the Gender Neutral Bathroom'].keys():
                print()
                print('Come on man, Willy\'s coming to life out there! Make a valid move: ')
                input_command = input("Try typing \"North\", \"Get item\", or type \"exit\" to exit the game: ")
        # Ball Pit
        if currentRoom == 'the Ball Pit':
            if input_command in rooms['the Ball Pit'].keys():
                if input_command == 'West':
                    currentRoom = 'the Main Game Room'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'North':
                    currentRoom = 'the Super Secret Firearm Room'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'Get item':
                    print()
                    print(
                        "Ouch! Who left this rusty screwdriver in the ball pit? Eh, whatever, I guess I can use this.")
                    inventory.append(rooms['the Ball Pit']['Get item'])
                    rooms['the Ball Pit'].pop('Get item')
                    playerStatus()
                    input_command = input("Make a move: ")
            elif input_command == 'exit':
                print('exiting...')
                break
            elif input_command not in rooms['the Ball Pit'].keys():
                print()
                print("That\'s not a valid move silly!")
                input_command = input("Try typing just \"North\", \"West\", or \"Get item\": ")
        # Super Secret Firearm Room
        if currentRoom == 'the Super Secret Firearm Room':
            if input_command in rooms['the Super Secret Firearm Room'].keys():
                if input_command == 'South':
                    currentRoom = 'the Ball Pit'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'Get item':
                    print()
                    print("Wait what? Is that a fully loaded machine gun? In the secret firearm room below the ball "
                          "bit of a children's \nplayplace? I\'m not going to question it.")
                    inventory.append(rooms['the Super Secret Firearm Room']['Get item'])
                    rooms['the Super Secret Firearm Room'].pop('Get item')
                    playerStatus()
                    input_command = input("Make a move: ")
            elif input_command == 'exit':
                print('exiting...')
                break
            elif input_command not in rooms['the Super Secret Firearm Room'].keys():
                print()
                print("Come on soldier, you\'ve got an animatronic groundhog to kill, get your head in the game!")
                input_command = input("Try typing just \"South\", it\'s the only way out of here. You can also type "
                                      "\"Get item\", or \'exit\' to quit: ")
        # Laser Tag Registration
        if currentRoom == 'Laser Tag Registration':
            if input_command in rooms['Laser Tag Registration'].keys():
                if input_command == 'East':
                    currentRoom = 'the Main Game Room'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'North':
                    currentRoom = 'the Laser Tag Arena'
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'Get item':
                    print()
                    print("\"Hmm, no item in this room. Better improvise.\" you mumble. You take off your sock and put"
                          " a bunch of change \nfrom the register in it. \"This\'ll do.\" you think to yourself.")
                    inventory.append(rooms['Laser Tag Registration']['Get item'])
                    rooms['Laser Tag Registration'].pop('Get item')
                    playerStatus()
                    input_command = input("Make a move: ")
                elif input_command == 'West':
                    # Animatronics storage and Willy showdown
                    currentRoom = 'Animatronics Storage'
                    playerStatus()
                    print("You can see Willy\'s eyes glowing in the dark and the whir of evil machinery.")
                    print()
                    input_decision = input("Face Willy? (Yes/No) ")
                    if input_decision == 'Yes':
                        # if player tries to face Willy without gathering all weapons they lose
                        if len(inventory) < 6:
                            print()
                            print('------------------------------------------------------------------------------------'
                                  '--------------------------')
                            print('Willy\'s machinery begins to whir faster and his red eyes roll back in his head. '
                                  'Frightened, you fumble through\nyour inventory for the weapons you\'ve collected. '
                                  'Just as you realize what items you\'re missing, Willy comes\nto life and grabs you '
                                  'by the throat. He pulls you close so you can smell his stinking, evil breath. '
                                  '\"Didn\'t \nyou read the introductory paragraph to the game?\", he snarls. \"It said'
                                  ' you need ALL SIX items to defeat me. \nPay more attention next time, mortal.\"')
                            print()
                            input('***You\'ve lost the game. Next time be sure to prepare before taking Willy on!***')
                            break
                        # if player faces Willy with all weapons the showdown scenario is presented to them
                        # the showdown code features inputs instead of printing statements so the player can read each
                        # line incrementally rather than just having a paragraph of text shoved in their faces
                        elif len(inventory) == 6:
                            print()
                            print('------------------------------------------------------------------------------------'
                                  '--------------------------')
                            input('Willy\'s machinery begins to whir faster and his red eyes roll back in his head. '
                                  'Before he fully awakens you \npull out the heavy machine gun you found and pull the '
                                  'trigger. ')
                            print()
                            input('\"Dammit, jammed.\", you mutter.')
                            print()
                            input('Time for plan B. You pull out both sets of nunchucks you found and realize you '
                                  'forgot to watch that YouTube \nvideo on how to use them. ')
                            print()
                            input('\"I\'m going to harvest your soul.\", Willy says as you drop the nunchucks to the '
                                  'floor.')
                            print()
                            input('You pull out that piece of broken glass you found and cut yourself. \"I don\'t '
                                  'really know what I was expecting.\", \nyou say. ')
                            print()
                            input('What about that roll of quarters in a sock? You pull it out and all the change falls'
                                  ' out of a hole in the \ntoe. ')
                            print()
                            input('You say your final prayers and pull out that rusty screwdriver you stepped on in '
                                  'the ball pit.')
                            print()
                            input('\"Screw you, Willy.\" you say, jumping at the mechanized abomination with your '
                                  'screwdriver.')
                            print()
                            print('------------------------------------------------------------------------------------'
                                  '--------------------------')
                            print('You walk out of the playplace into the light of day, your clothes covered in '
                                  'grease. You take a sigh and drag \non a cigarette. Your phone rings. Its your boss '
                                  'from Willy\'s. You pick up.')
                            print()
                            input('\"Hey, kiddo. So I\'m gonna need you to stay for a couple more hours. Turns out '
                                  'we\'re getting in a new shipment \nof animatronics for the playplace. You think you '
                                  'could handle that for me?\", says your boss.')
                            print()
                            print()
                            input('\"Oh I\'ll handle it alright.\", you say, clenching the grease-covered rusty '
                                  'screwdriver in your hand.')
                            print()
                            print()
                            print()
                            input('***Congratulations! You\'ve bested Willy and saved the playplace! Next time pick a '
                                  'different career path.***')
                            break
                    # if player chooses no to face Willy they are taunted
                    elif input_decision == 'No':
                        currentRoom = 'Laser Tag Registration'
                        print()
                        print('It\'s okay, not like this is important we\'re just talking about children\'s lives '
                              'here after all.')
                        playerStatus()
                        input_command = input("Make a move: ")
                    # if player does not make a viable decision they are placed back in Laser Tag Reg
                    else:
                        print("You failed to make a viable decision, try typing \"Yes\", or \"No\".")
                        currentRoom = 'Laser Tag Registration'
                        playerStatus()
                        input_command = input("Make a move: ")
            elif input_command == 'exit':
                print('exiting...')
                break
            elif input_command not in rooms['Laser Tag Registration'].keys():
                print()
                print("Get your head back in the game, you\'ve got a children\'s playplace to save!")
                input_command = input('Try typing \"North\", \"East\", \"West\", \"Get item\", or \"exit\": ')

    # This is the exit to the game.
    if input_command == 'exit':
        print()
        print("-------------------------------------------------------------------------")
        print("You\'ve exited the game, it was nice playing with you!")


main()
