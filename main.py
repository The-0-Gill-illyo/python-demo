greeting = "Hello world!"
print(greeting)

fav_animal = input("What is your favorite animal? ")

valid_response = False

while valid_response == False:
    
    if fav_animal == "Zombie":
        print("I asked about an animal, but I'm glad you're ready for the apocalypse!")
        valid_response = True
    elif fav_animal == "Fish":
        print("I can tell you spend a lot of time in the water :)")
        valid_response = True
    elif fav_animal == "Turkey":
        print("And what does the turkey feel about Thanksgiving?")
        valid_response = True
    else:
        print("I don't think you know what an animal is, sorry!")