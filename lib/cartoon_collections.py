def roll_call_dwarves(dwarf_list):
    for dwarf in dwarf_list:
        print(f"{dwarf_list.index(dwarf) + 1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [element.title() + "!" for element in planeteer_calls]

def long_planeteer_calls(word_list):
    words_over_4 = 0
    for word in word_list:
        if len(word) > 4:
            words_over_4 += 1
    if words_over_4 > 0:
        return True
    else : return False

def find_the_cheese(word_list):
    cheeses = []
    for word in word_list:
        if word == "cheddar" or word == "gouda" or word == "camembert":
            cheeses.append(word)
    if len(cheeses) == 0:
        return None
    else : return cheeses[0]