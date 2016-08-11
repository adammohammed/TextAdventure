""" Level Text Display module """
import time

def display_level(filepath, _player):
    """ Prints level text to STDOUT
        Includes formating for dictionary interactions
    """
    with open(filepath) as f:
        for line in f:
            #Removes Carriage Returns at end of lines
            text = line.rstrip()
            #Substitutes all player info into text
            text_new, sleeptime = substitute_player_data(text, _player)

            print text_new
            if sleeptime:
                _sleep = int(sleeptime)
                time.sleep(_sleep)

def find_between(sample, first_char, second_char):
    """ Searches string for two characters and returns whats in the middle"""
    try:
        start = sample.index(first_char)
        end = sample.index(second_char)
        return sample[start+1:end]
    except ValueError:
        # Returns a tuple of length 1 if characters are not found
        return ""

def substitute_player_data(in_text, _dict):
    """ Looks for all occurences of dict keys in as <dictkey> in text and replaces
        the <dictkey> with the corresponding value from the dictionary
        Example:
        Input: in_text = "Welcome to Cralohines, <name>! <3>"
        Input: _dict = {"name": "Adam"}
        Output: "Welcome to Cralohines, Adam!", 3
    """
    out_text = in_text
    for key, value in _dict.iteritems():
        out_text = out_text.replace("<"+ key +">", str(value))

    # Find and replace sleep time
    sleeptime = find_between(out_text, '<', '>')
    out_text = out_text.replace('<'+sleeptime+'>', '')
    return out_text, sleeptime
