infoBasica = {"nombre":"Valentin",
    "apellidos":{"primero":"Martinez Gama","segundo":"Miranda"},
    "edad":18,
    "lenguajesCodigo":["python", "html-css", "mindstorme"]
    }
infoHobbies = {"deportes":["futbol", "bouldering", "lucha grecromana"]}

infoBasica["hobbies"] = infoHobbies

print(infoBasica["hobbies"])
print(infoBasica)
