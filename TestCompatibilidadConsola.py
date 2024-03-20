from tkinter import *

hobbies = [
    '1.-Leer',
    '2.-Escribir',
    '3.-Dibujar',
    '4.-Pintar',
    '5.-Escuchar música',
    '6.-Bailar',
    '7.-Tocar un instrumento musical',
    '8.-Futbol',
    '9.-Basket',
    '10.-Nadar',
    '11.-Correr',
    '12.-Cocinar',
    '13.-Hacer repostería',
    '14.-Practicar yoga',
    '15.-Hacer meditación',
    '16.-Ver películas',
    '17.-Ver series',
    '18.-Jugar videojuegos',
    '19.-Programar',
    '20.-Hacer jardinería',
    '21.-Fotografiar',
    '22.-Viajar',
    '23.-Practicar senderismo',
    '24.-Practicar ciclismo',
    '25.-Surf',
    '26.-Aprender idiomas',
    '27.-Jugar a juegos de mesa',
    '28.-Hacer manualidades',
    '29.-Practicar la pintura facial',
    '30.-Padel',
    '31.-Petanca',
    '32.-Waterpolo'
]

def calcular_compatibilidad(usuario1, usuario2):
 
   edad1 = int(usuario1['age'])
   edad2 = int(usuario2['age'])
   
   diferencia_edad = abs(edad1 - edad2)
   

   compatibilidad = 0
   

   if usuario1['genre'] == usuario2['prefGenre']:
       compatibilidad += 15
   elif usuario1['prefGenre'] == usuario2['genre']:
       compatibilidad += 15
   elif usuario1['prefGenre'] == usuario2['genre'] and usuario2['prefGenre'] == usuario1['genre']:
       compatibilidad += 15
   if usuario1['prefGenre'] == usuario2['genre'] or (usuario1['prefGenre'] == '3' and usuario2['prefGenre'] == '3') or (usuario1['prefGenre'] == '4' and usuario2['prefGenre'] == '4'):
       compatibilidad += 15
   
   
   
   hobbies_comunes = set(usuario1['hobbies']).intersection(usuario2['hobbies'])
   compatibilidad += len(hobbies_comunes) * 5
   
 
   if diferencia_edad <= 4:
       compatibilidad += 5
       

   if compatibilidad > 100:
       compatibilidad = 100
   
   return compatibilidad

def usuario(numero):
    print(f"Usuario {numero}: ")
    name = input("Introduce tu nombre: ")
    age = input("Introduce tu edad: ")
    if int(age) < 18:
        print("Lo siento, no puedes hacer este test si tienes menos de 18 años.")
        return None
    print("Cual és tu género?  \n1.-Hombre\n2.-Mujer\n 3.-Otro")
    genre = input("Eleccion (1, 2 o 3): ")    
    print("Cuales son tus preferencias de género?  \n1.-Hombre\n2.-Mujer\n3.-Ambos\n4.-Otros")
    prefGenre = input("Eleccion (1, 2, 3 o 4): ")
    
    print("Lista de hobbies: ")
    for hobby in hobbies:
        print(hobby)
    
    print(f"Usuario {numero}, escoge los hobbies que mas te gusten (máximo 7): ")
    selected_hobbies = []
    while len(selected_hobbies) < 7:
        hobby_choice = input(f"Escribe el número del hobby que te gusta o 'salir' para terminar (Usuario {numero}): ")
        if hobby_choice.lower() == 'salir':
            break
        else:
            hobby_choice = int(hobby_choice)
            if hobby_choice in range(1, len(hobbies) + 1):
                selected_hobbies.append(hobbies[hobby_choice - 1])
            else:
                print("Opción no válida. Intenta de nuevo.")
    
    return {
        'name': name,
        'age': age,
        'genre': genre,
        'prefGenre': prefGenre,
        'hobbies': [hobby.replace('.-', '') for hobby in selected_hobbies]
    }

usuario1 = usuario(1)
usuario2 = usuario(2)

compatibilidad = calcular_compatibilidad(usuario1, usuario2)

print(f"La compatibilidad entre {usuario1['name']} y {usuario2['name']} es de {compatibilidad}%.")

 







#def validar_edad():
 #   edad = txt2.get()
  #  if edad.isdigit() and int(edad) >= 18:
#        errorMsg.config()
#        return True
#    else:
#        return False
    
#def validar_nombre():
#    nombre = txt1.get()
#    if nombre.isalpha():
#        errorMsgName.config(text="", bg="hot pink")
#        return True
#    else:
#        errorMsgName.config(text="¡Nombre no puede contener números!", bg="lavender", fg="red")
#       return False