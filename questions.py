import random
categorias = {
        "words": [
            "python",
            "programa",
            "variable",
            "funcion",
            "bucle",
            "cadena",
            "entero",
            "lista",
        ],

        "frutas": [
            "manzana",
            "pera",
            "banana",
            "sandia",
            "uva",
            "frutilla",
        ],

        "libreria": [
            "lapiz",
            "cartuchera",
            "cuaderno",
            "lapicera",
            "resaltador",
        ],

        "ropa": [
            "remera",
            "pantalon",
            "pollera",
            "musculosa",
            "buzo",
        ]
}
#word = random.choice(words)
guessed = []
attempts = 6
puntaje = 6

print("¡Bienvenido al Ahorcado!")
print()

print ("Categorias disponibles: ")
for cat in categorias.keys():
    print (f"{cat}")
eleccion = input ("Escriba la categoria: ")

word = random.choice(categorias[eleccion])

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        print (f"Puntaje: {puntaje}")
        break
    
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ")

    if (len(letter) != 1) or not (letter>= 'a' and letter<= 'z'):
        print("Entrada no valida")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1
        print("Esa letra no está en la palabra.")
    
    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    print ("Su puntaje es 0")