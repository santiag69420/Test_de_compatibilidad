from tkinter import * 
from tkinter import ttk

hobbies = [
    'Leer', 'Escribir', 'Dibujar', 'Pintar', 'Escuchar música', 'Bailar', 'Tocar un instrumento',
    'Futbol', 'Basket', 'Nadar', 'Correr', 'Cocinar', 'Repostería', 'Yoga', 'Meditación',
    'Ver películas', 'Ver series', 'Jugar videojuegos', 'Programar', 'Jardinería', 'Fotografiar',
    'Viajar', 'Senderismo', 'Ciclismo', 'Surf', 'Aprender idiomas', 'Jugar a juegos de mesa',
    'Hacer manualidades', 'Pinta caras', 'Padel', 'Petanca', 'Waterpolo'
]

usuarios = []

usuario1 = {}
usuario2 = {}

def mostrar_usuarios():
    lista_usuarios.delete(0, END)  # Limpiar la lista antes de agregar los usuarios
    for i, usuario in enumerate(usuarios, start=1):
        lista_usuarios.insert(END, f"Usuario {i}: {usuario['Nombre']}")


def seleccionar_usuarios():
    seleccionados = lista_usuarios.curselection()
    if len(seleccionados) == 2:
        usuario1.clear()
        usuario2.clear()
        for idx in seleccionados:
            if len(usuario1) == 0:
                usuario1.update(usuarios[idx])
            else:
                usuario2.update(usuarios[idx])
        calcular_y_mostrar_compatibilidad()
    else:
        print("Por favor, selecciona exactamente 2 usuarios.")

def calcular_compatibilidad(usuario1, usuario2):
    edad1 = int(usuario1['Edad'])
    edad2 = int(usuario2['Edad'])
    diferencia_edad = abs(edad1 - edad2)
    compatibilidad = 0
    
    if usuario1['Género'] == usuario2['Preferencias de género']:
        compatibilidad += 20
    elif usuario1['Preferencias de género'] == usuario2['Género']:
        compatibilidad += 20
    
    
    hobbies_comunes = set(usuario1['Hobbies']).intersection(usuario2['Hobbies'])
    compatibilidad += len(hobbies_comunes) * 10
    
    if diferencia_edad <= 4:
        compatibilidad += 15
    
    if compatibilidad > 100:
        compatibilidad = 100
    
    return compatibilidad

def calcular_y_mostrar_compatibilidad():
    compatibilidad = calcular_compatibilidad(usuario1, usuario2)
    texto_compatibilidad.config(text=f"La compatibilidad entre {usuario1['Nombre']} y {usuario2['Nombre']} es de {compatibilidad}%.")

def seleccionar_hobbies():
    seleccionados = lista_hobbies.curselection()
    if len(seleccionados) > 7:
        errorMsgHobbies.config(text="¡Selecciona un máximo de 7 hobbies!", bg="lavender", fg="red")
    else:
        seleccionados_hobbies = [hobbies[i] for i in seleccionados]
        errorMsgHobbies.config(text=", ".join(seleccionados_hobbies))

def validar_y_mostrar_error():
    errores = []

    nombre = txt1.get()
    if not nombre:
        errorMsgName.config(text="¡Por favor, introduce un nombre!", bg="lavender", fg="red")
        errores.append("Nombre")
    else:
        errorMsgName.config(text="", bg="hot pink")
    
    edad = txt2.get()
    if not edad.isdigit() or int(edad) < 18:
        errorMsgAge.config(text="¡Valor incorrecto, introduce una edad válida!", bg="lavender", fg="red")
        errores.append("Edad")
    else:
        errorMsgAge.config(text="", bg="hot pink")

    genero = lista.get()
    if not genero:
        errorMsgGender.config(text="¡Por favor, selecciona un género!", bg="lavender", fg="red")
        errores.append("Género")
    else:
        errorMsgGender.config(text="", bg="hot pink")

    pref_genero = lista2.get()
    if not pref_genero:
        errorMsgPrefGender.config(text="¡Por favor, selecciona tus preferencias de género!", bg="lavender", fg="red")
        errores.append("Preferencias de género")
    else:
        errorMsgPrefGender.config(text="", bg="hot pink")
    
    hobbies_seleccionados = [lista_hobbies.get(i) for i in lista_hobbies.curselection()]
    if len(hobbies_seleccionados) > 7:
        errorMsgHobbies.config(text="¡Selecciona un máximo de 7 hobbies!", bg="lavender", fg="red")
        errores.append("Hobbies")
    else:
        seleccionar_hobbies()
    
    if not errores:
        usuario = {
            "Nombre": nombre,
            "Edad": edad,
            "Género": genero,
            "Preferencias de género": pref_genero,
            "Hobbies": hobbies_seleccionados
        }
        usuarios.append(usuario)
        limpiar_interfaz()

def limpiar_interfaz():
    txt1.delete(0, END)
    txt2.delete(0, END)
    lista.set('')
    lista2.set('')
    lista_hobbies.selection_clear(0, END)
    errorMsgName.config(text="")
    errorMsgAge.config(text="")
    errorMsgGender.config(text="")
    errorMsgPrefGender.config(text="")
    errorMsgHobbies.config(text="")

test = Tk()
test.title("Test de compatibilidad")
test.geometry("860x800")
test.config(bg="red2")
test.config(relief="solid")
test.config(bd=4)

miFrame = Frame(test, width=650, height=600)
miFrame.config(bg="hot pink", bd=5, relief="groove", cursor="heart")
miFrame.pack(fill="y", expand="True")

title = Label(miFrame, text='Test de compatibilidad')
title.config(bg="hot pink", fg="gray1", font=("Times New Roman", 24))
title.place(relx=0.3, rely=0.02)

lbl1 = Label(miFrame, text='Nombre:')
lbl1.config(bg="gray1", fg="snow")
lbl1.place(relx=0.12, rely=0.1, relwidth=0.21, relheight=0.03)

txt1 = Entry(miFrame, bg="pink")
txt1.place(relx=0.35, rely=0.1, relwidth=0.23, relheight=0.029)

errorMsgName = Label(miFrame)
errorMsgName.place(relx=0.59, rely=0.099)
errorMsgName.config(bg="hot pink", text="")

lbl2 = Label(miFrame, text='Edad:')  
lbl2.config(bg="gray1", fg="snow")
lbl2.place(relx=0.12, rely=0.16, relwidth=0.21, relheight=0.029)

txt2 = Entry(miFrame, bg="pink")
txt2.place(relx=0.35, rely=0.16, relwidth=0.23, relheight=0.029)

errorMsgAge = Label(miFrame)
errorMsgAge.place(relx=0.59, rely=0.159)
errorMsgAge.config(bg="hot pink", text="")

lbl3 = Label(miFrame, text='Género:')
lbl3.config(bg="gray1", fg="snow")
lbl3.place(relx=0.12, rely=0.22, relwidth=0.21, relheight=0.03)

lista = ttk.Combobox(miFrame, state="readonly", values=["Hombre", "Mujer", "Otros"])
lista.place(relx=0.35, rely=0.22, relwidth=0.23, relheight=0.03)

errorMsgGender = Label(miFrame)
errorMsgGender.place(relx=0.59, rely=0.219)
errorMsgGender.config(bg="hot pink", text="")

lbl4 =Label(miFrame, text='Preferencias de género:')
lbl4.config(bg="gray1", fg="snow")
lbl4.place(relx=0.12, rely=0.28, relwidth=0.21, relheight=0.03)

lista2 = ttk.Combobox(miFrame, state="readonly", values=["Hombre", "Mujer", "Ambos", "Otros"])
lista2.place(relx=0.35, rely=0.28, relwidth=0.23, relheight=0.03)

errorMsgPrefGender = Label(miFrame)
errorMsgPrefGender.place(relx=0.59, rely=0.279)
errorMsgPrefGender.config(bg="hot pink", text="")

lbl5 = Label(miFrame, text='Hobbies:')
lbl5.config(bg="gray1", fg="snow")
lbl5.place(relx=0.12, rely=0.34, relwidth=0.21, relheight=0.03)

lista_hobbies = Listbox(miFrame, selectmode="multiple", exportselection=False)
lista_hobbies.config(bg="pink", fg="gray1")
for hobby in hobbies:
    lista_hobbies.insert(END, hobby)
lista_hobbies.place(relx=0.35, rely=0.34, relwidth=0.23, relheight=0.3)

errorMsgHobbies = Label(miFrame, text="")
errorMsgHobbies.config(bg="Hot Pink", fg="gray1")
errorMsgHobbies.place(relx=0.12, rely=0.64, relheight=0.03)

boton_validar = Button(miFrame, text="Validar Datos", command=validar_y_mostrar_error)
boton_validar.place(relx=0.12, rely=0.7)

lista_usuarios = Listbox(miFrame, selectmode="multiple", exportselection=False)
lista_usuarios.config(bg="pink", fg="gray1")
lista_usuarios.place(relx=0.6, rely=0.34, relwidth=0.3, relheight=0.3)

boton_mostrar_usuarios = Button(miFrame, text="Mostrar Usuarios", command=mostrar_usuarios)
boton_mostrar_usuarios.place(relx=0.34, rely=0.7)

boton_seleccionar = Button(miFrame, text="Seleccionar Usuarios", command=seleccionar_usuarios)
boton_seleccionar.place(relx=0.6, rely=0.65)

texto_compatibilidad = Label(miFrame, text="")
texto_compatibilidad.config(bg="pink", fg="gray1")
texto_compatibilidad.place(relx=0.6, rely=0.75)

test.mainloop()

