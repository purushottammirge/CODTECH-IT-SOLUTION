
import time



def introduction():
    print("Welcome to the Mysterious Forest Adventure!")
    time.sleep(1)
    print("You find yourself at the edge of a dense and enchanting forest.")
    time.sleep(1)
    print("Your goal is to reach the magical waterfall hidden deep within.")
    time.sleep(1)
    print("Let your choices guide your destiny!")



    

def make_choice(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


            

def forest_path():
    print("You start your journey through the forest.")
    time.sleep(1)
    
    choices = ["Follow the sparkling butterflies", "Take the dark and mysterious path"]
    choice = make_choice("Which path do you choose?", choices)

    if choice == 1:
        print("The butterflies guide you to a clearing with a magical fountain.")
        time.sleep(1)
        print("You feel refreshed. Continue your journey.")

    else:
        print("The dark path leads you to a talking tree.")
        time.sleep(1)
        print("The tree offers you a magical lantern.")
        time.sleep(1)
        print("Do you accept the lantern?")

        choices = ["Accept the lantern", "Decline and continue without it"]
        choice = make_choice("What do you do?", choices)

        if choice == 1:
            print("You accept the lantern and illuminate your path.")
        else:
            print("You decline the lantern and venture into the darkness.")



            

def encounter_wildlife():
    print("As you continue, you encounter mystical creatures in the forest.")
    time.sleep(1)

    choices = ["Befriend the creatures", "Avoid them and continue quietly"]
    choice = make_choice("How do you approach the creatures?", choices)

    if choice == 1:
        print("The creatures become your allies and guide you to a hidden shortcut.")
    else:
        print("You cautiously move past the creatures and continue on your way.")



        

def magical_waterfall():
    print("You hear the sound of a distant waterfall.")
    time.sleep(1)
    print("You finally reach the magical waterfall, surrounded by ancient stones.")
    time.sleep(1)
    print("Congratulations! You've completed your journey.")



    

def main():
    introduction()
    forest_path()
    encounter_wildlife()
    magical_waterfall()
    

if __name__ == "__main__":
    main()
