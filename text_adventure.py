from level_parser import display_level

def create_character():
    """ We will probably make this into a class later if this goes anywhere lol
        To avoid having a class with just __init__ Player will be a dictionary
        Player will have a name, age, race, health, and four item slots
    """
    player = {"name": '', "age": 0, "race": "human", "item_slot_1": None,
                "item_slot_2": None, "item_slot_3": None, "item_slot_4": None}

    display_level("levels/itbegins.txt", player)

    name = str(raw_input("  Whispers come from the north, what are they saying? "))
    print ""
    player["name"] = name
    # you get input with raw_input("prompt")
    # you usually want to cast it to the type you want, e.g. int, str, etc.
    return player

if __name__ == "__main__":
    p1 = create_character()
    # Print Greeting
    display_level("levels/harambe.txt", p1)
