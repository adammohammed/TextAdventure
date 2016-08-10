from random import randint

def it_begins():
    # Prints meme adventure in ascii
    print "_________________________________________________________________________________________"
    print "    _   _                            __                                                  "
    print "    /  /|                           / |        /                                         "
    print "---/| /-|----__---_--_----__-------/__|----__-/---------__----__--_/_----------)__----__-"
    print "  / |/  |  /___) / /  ) /___)     /   |  /   /   | /  /___) /   ) /    /   /  /   ) /___)"
    print "_/__/___|_(___ _/_/__/_(___ _____/____|_(___/____|/__(___ _/___/_(_ __(___(__/_____(___ _"
    print "\n"

def create_character():
    # We will probably make this into a class later if this goes anywhere lol
    print "Welcome to Cralohines. You crash landed on this densely forested planet"
    print "You slowly get up from your horrific landing and look around"
    print "Somehow nothing is broken but your head is bleeding and you can't remember much"
    # To avoid having a class with just __init__ Player will be a dictionary
    # Player will have a name, age, race, health, and four item slots
    player = {"name": '', "age": 0, "race": "human", "item_slot_1": None,
                "item_slot_2": None, "item_slot_3": None, "item_slot_4": None}
    name = str(raw_input("Whispers come from the north, what are they saying? "))
    player["name"] = name
    # you get input with raw_input("prompt")
    # you usually want to cast it to the type you want, e.g. int, str, etc.
    return player


# FUCKING DRADNOM INDEX CAUSE EVENTUALLY
rWords = ['memes','dank','penis','fuck','balls','maps','cardinal','mutable','cats','rockls','FUCK','faro','pharrah','firetruck']

# There is what ghostcrawler would call mechanics.
def fuck_the_police_you_fucking_homosexual():
    print('AYYYY LMAO PICK A NUMBER')
    urDED = int(raw_input("NUMBER 1 TO FIVE "))
    trickedU = randint(0,13)
    if trickedU > 5 or trickedU < 1:
        print(str(trickedU)+"! WHAT THE FUCK. FUK U DED KID. GAME OVER BITCH. YOU SHOULDNT HAVE SAID "+rWords[trickedU])
    else: print("alright you win this time.")



print(rWords)


if __name__ == "__main__":
    it_begins()

# Set player 1
p1 = create_character()

# Print Greeting
print ("\n")
print (" 'Hello " + p1["name"] + ". I am Harambe.' ")
print ("\n")
print (" A large gorilla sporting a magnificient ERECTION decends from the heavens to greet you.")
print ("\n")
print (" He gently touches your face ands whispers: ")
print ("\n")
print (" 'It is okay, my little "+ p1["name"] + ". I will guide you.")
print ("\n")

fuck_the_police_you_fucking_homosexual()