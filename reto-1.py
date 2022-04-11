name = input("country: ")

diccionario = {
    "Argentina":"Buenos Aires",
    "Chile":"Santiago",
    "Uruguay":"Montevideo",
    "Peru":"Lima",
    "Bolivia":"La Paz"

}

for country, capital in diccionario.items():
    if country == name and country[0] == "A":
        print(diccionario[country])
        print("El pais digitado esta seleccionado para donaciones")
    elif country == name:
        print(diccionario[country])

        
        
    

    
