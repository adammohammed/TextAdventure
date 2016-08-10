def it_begins():
    ''' Prints meme adventure in ascii '''
    print ("_________________________________________________________________________________________")
    print ("    _   _                            __                                                  ")
    print ("    /  /|                           / |        /                                         ")
    print ("---/| /-|----__---_--_----__-------/__|----__-/---------__----__--_/_----------)__----__-")
    print ("  / |/  |  /___) / /  ) /___)     /   |  /   /   | /  /___) /   ) /    /   /  /   ) /___)")
    print ("_/__/___|_(___ _/_/__/_(___ _____/____|_(___/____|/__(___ _/___/_(_ __(___(__/_____(___ _")
    print ("\n")

def create_character():
    ''' We will probably make this into a class later if this goes anywhere lol'''
    print ("Welcome to Cralohines. You crash landed on this densely forested planet...")
    print ("You slowly get up from your horrific landing and look around...")
    print ("Somehow nothing is broken but your head is bleeding and you can't remember much...")
    name = str(input("Whispers come from the north, what are they saying? "))
    # you get input with raw_input("prompt")
    # you usually want to cast it to the type you want, e.g. int, str, etc.
    return name

if __name__ == "__main__":
    it_begins()
    name = create_character()
    print ("\n")
    print (" 'Hello " + name + ". I am Harambe.' ")
    print ("\n")
    print (" A large gorilla sporting a magnificient halo decends from the heavens to greet you.")
    print (" He gently touches your face ands whispers: ")
    print ("\n")
    print (" 'It is okay, my little "+ name + ". I will guide you.")
    print ("\n")
    # Do something with the name now
