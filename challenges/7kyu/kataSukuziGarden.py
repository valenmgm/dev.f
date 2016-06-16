'''
def rake_garden(garden):
    position = 0
    objects = garden.split(" ")

    while position < len(objects):
        if objects[position] != ("rock" or "gravel"):
            objects[position] = "gravel"
        position += 1

    print(" ".join(objects))
'''
def rake_garden(garden):




rake_garden("gravel rock ant gravel bug")
rake_garden("gravel gravel rock rock ant rock rock bug trash gravel rock poop gravel")
