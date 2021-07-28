import random


print("Dungeons and Dragons character creator version 0.1")
print("Created by ARK")


#Method to generate stat diceroll value
def statgen(minimum,maximum):
    attribute_value = 0
    roll_values = []
    roll_values.append(random.randint(minimum,maximum))
    roll_values.append(random.randint(minimum,maximum))
    roll_values.append(random.randint(minimum,maximum))
    roll_values.append(random.randint(minimum,maximum))
    roll_values.remove(min(roll_values))
    attribute_value += sum(roll_values)
    return attribute_value

#Method to modify stats as a result of race value
def applyrace(race):
    if race == "Dwarf":
        char_sheet_dict["Constitution"] += 2
        char_sheet_dict["Speed"] = 25
        char_sheet_dict["Vision"] = "Darkvision"
        char_sheet_dict["Weapon Proficiency"] = ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"]
        char_sheet_dict["Languages"] = ["Common", "Dwarvish"]
    elif race == "Elf":
        char_sheet_dict["Dexterity"] += 2
        char_sheet_dict["Speed"] = 30
        char_sheet_dict["Vision"] = "Darkvision"
        char_sheet_dict["Languages"] = ["Common", "Elvish"]
    elif race == "Halfling":
        char_sheet_dict["Dexterity"] += 2
        char_sheet_dict["Speed"] = 25
        char_sheet_dict["Languages"] = ["Common", "Halfling"]
    elif race == "Human":
        char_sheet_dict["Strength"] += 1
        char_sheet_dict["Dexterity"] += 1
        char_sheet_dict["Constitution"] += 1
        char_sheet_dict["Intelligence"] += 1
        char_sheet_dict["Wisdom"] += 1
        char_sheet_dict["Charisma"] += 1
        char_sheet_dict["Speed"] = 30
        char_sheet_dict["Languages"] = ["Common"]
    elif race == "Dragonborn":
        char_sheet_dict["Strength"] += 2
        char_sheet_dict["Charisma"] += 1
        char_sheet_dict["Speed"] = 30
        char_sheet_dict["Languages"] = ["Common","Draconic"]
    elif race == "Gnome":
        char_sheet_dict["Intelligence"] += 2
        char_sheet_dict["Speed"] = 25
        char_sheet_dict["Vision"] = "Darkvision"
        char_sheet_dict["Languages"] = ["Common", "Gnomish"]
    elif race == "Half-Elf":
        char_sheet_dict["Charisma"] += 2
        #add 1 to two other ability scores of player choice
        char_sheet_dict["Speed"] = 30
        char_sheet_dict["Vision"] = "Darkvision"
        char_sheet_dict["Languages"] = ["Common", "Elvish"]
        #add 1 other language
    elif race == "Half-Orc":
        char_sheet_dict["Strength"] += 2
        char_sheet_dict["Constitution"] += 1
        char_sheet_dict["Speed"] = 30
        char_sheet_dict["Vision"] = "Darkvision"
        char_sheet_dict["Languages"] = ["Common", "Orcish"]
    elif race == "Tiefling":
        char_sheet_dict["Charisma"] += 2
        char_sheet_dict["Intelligence"] += 1
        char_sheet_dict["Speed"] = 30
        char_sheet_dict["Vision"] = "Darkvision"
        char_sheet_dict["Languages"] = ["Common", "Infernal"]
    else:
        pass

#Methods to tabulate number of available feats

def racialfeatselect():



def featselect():
    #ask player to select between stat point increase or available feats

    #if player selects stat points, allocate desired stat point

    #if player selects feat, prompt for feat selection


#Create Dictionary for Character Sheet
char_sheet_dict = {}

#input character name to character sheet
char_name = input("Please enter the name of your character:")
char_sheet_dict['Character Name'] = char_name

#Generate Stat values for character
char_sheet_dict["Strength"] = statgen(1,6)
print("The Strength value for "+str(char_sheet_dict.get("Character Name"))+" is "+str(char_sheet_dict.get("Strength")))

char_sheet_dict["Dexterity"] = statgen(1,6)
print("The Dexterity value for "+str(char_sheet_dict.get("Character Name"))+" is "+str(char_sheet_dict.get("Dexterity")))

char_sheet_dict["Constitution"] = statgen(1,6)
print("The Constitution value for "+str(char_sheet_dict.get("Character Name"))+" is "+str(char_sheet_dict.get("Constitution")))

char_sheet_dict["Intelligence"] = statgen(1,6)
print("The Intelligence value for "+str(char_sheet_dict.get("Character Name"))+" is "+str(char_sheet_dict.get("Intelligence")))

char_sheet_dict["Wisdom"] = statgen(1,6)
print("The Wisdom value for "+str(char_sheet_dict.get("Character Name"))+" is "+str(char_sheet_dict.get("Wisdom")))

char_sheet_dict["Charisma"] = statgen(1,6)
print("The Charisma value for "+str(char_sheet_dict.get("Character Name"))+" is "+str(char_sheet_dict.get("Charisma")))

#Select character race, modify stats to account for racial bonuses
available_races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]


print("available races for this character include:")
print(available_races)
char_race = input("Please select a race for this character from the list above:")
while char_race.capitalize() not in available_races:
    print(char_race+ "is not an available race.  Please select a race from the list provided.")
    print(available_races)
    char_race = input("Please select a race for this character from the list above:")
else:
    char_sheet_dict['race'] = char_race.capitalize()

#call function to apply race values
applyrace(char_sheet_dict.get("race"))





print(char_sheet_dict)
