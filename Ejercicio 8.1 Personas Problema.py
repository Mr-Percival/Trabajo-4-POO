import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar


class Persona:
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} - {self.apellidos} - {self.telefono} - {self.direccion}"


class ListaPersonas:
    def __init__(self):
        self.lista_personas = []

    def añadir_persona(self, persona):
        self.lista_personas.append(persona)

    def eliminar_persona(self, indice):
        if 0 <= indice < len(self.lista_personas):
            del self.lista_personas[indice]

    def borrar_lista(self):
        self.lista_personas.clear()


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.lista = ListaPersonas()

        self.title("Personas")
        self.geometry("370x350")  # Ventana más ancha
        self.resizable(False, False)

        self.nombre_label = tk.Label(self, text="Nombre:")
        self.nombre_label.place(x=20, y=20)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.place(x=130, y=20, width=200)  # Campo más ancho

        self.apellidos_label = tk.Label(self, text="Apellidos:")
        self.apellidos_label.place(x=20, y=50)
        self.apellidos_entry = tk.Entry(self)
        self.apellidos_entry.place(x=130, y=50, width=200)  # Campo más ancho

        self.telefono_label = tk.Label(self, text="Teléfono:")
        self.telefono_label.place(x=20, y=80)
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.place(x=130, y=80, width=200)  # Campo más ancho

        self.direccion_label = tk.Label(self, text="Dirección:")
        self.direccion_label.place(x=20, y=110)
        self.direccion_entry = tk.Entry(self)
        self.direccion_entry.place(x=130, y=110, width=200)  # Campo más ancho

        self.añadir_button = tk.Button(self, text="Añadir", command=self.añadir_persona)
        self.añadir_button.place(x=130, y=150)

        self.lista_nombres = Listbox(self, selectmode=tk.SINGLE)
        self.lista_nombres.place(x=20, y=190, width=310, height=80)  # Lista más ancha

        self.eliminar_button = tk.Button(self, text="Eliminar", command=self.eliminar_nombre)
        self.eliminar_button.place(x=20, y=280)

        self.borrar_lista_button = tk.Button(self, text="Borrar Lista", command=self.borrar_lista)
        self.borrar_lista_button.place(x=130, y=280)

    def añadir_persona(self):
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()

        persona = Persona(nombre, apellidos, telefono, direccion)
        self.lista.añadir_persona(persona)
        self.lista_nombres.insert(tk.END, str(persona))

        self.nombre_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)

    def eliminar_nombre(self):
        selected_index = self.lista_nombres.curselection()
        if selected_index:
            self.lista_nombres.delete(selected_index)
            self.lista.eliminar_persona(selected_index[0])
        else:
            messagebox.showerror("Error", "Debe seleccionar un elemento")

    def borrar_lista(self):
        self.lista.borrar_lista()
        self.lista_nombres.delete(0, tk.END)


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
