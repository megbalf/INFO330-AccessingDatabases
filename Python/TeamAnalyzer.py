import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

# All the "against" column suffixes:
types = ["bug","dark","dragon","electric","fairy","fight",
    "fire","flying","ghost","grass","ground","ice","normal",
    "poison","psychic","rock","steel","water"]

conn = sqlite3.connect('../pokemon.sqlite')
cursor = conn.cursor()

# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()

team = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue

    name = cursor.execute("SELECT name FROM pokemon WHERE pokedex_number = " + arg).fetchall()
  

    pokename = name[0][0]
    print(pokename)

    name2 = cursor.execute("SELECT * FROM pokemon_types_view WHERE name = '" + pokename + "'").fetchone()

    pokename1 = name2[1]
    pokename2 = name2[2]
    # print(pokename1, pokename2)
   
    against = cursor.execute("SELECT * FROM pokemon_types_battle_view WHERE type1name = '" + pokename1 + "' and type2name = '" + pokename2 + "'").fetchone()
    # print(against)

    #creates clean tuple without the first two columns 
    clean_pokemon_types = against[2:]
    # print(clean_pokemon_types)

    stronger_than = []
    weaker_than = []

    count = 0
    
    for column in clean_pokemon_types:
        if column >= 1:
            stronger_than.append(types[count])
            
        else: 
            weaker_than.append(types[count]) 
        count += 1
        # print(count)
    print(pokename + "(" + pokename1 + ", " + pokename2 +  ") is strong againsgt:" + str(stronger_than) + "but weak against:" + str(weaker_than))
  


answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    teamName = input("Enter the team name: ")

    # Write the pokemon team to the "teams" table
    print("Saving " + teamName + " ...")
else:
    print("Bye for now!")
