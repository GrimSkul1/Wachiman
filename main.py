import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk


import cv2

class App(tk.Tk):
    def __init__(self, master):
        self.master = master
        self.master.title("Wachiman")

        self.master.title("Wachiman")
        self.master.geometry("600x450")

        self.create_widgets()

        # Hacer que la ventana no sea redimensionable
        self.master.resizable(False, False)

        # Frame principal
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.video_button = tk.Button(self.frame, text="Cargar video", command=self.load_file, bg="white")
        self.analyze_button = tk.Button(self.frame, text="Analizar", command=self.analyze_file, bg="white")
        self.instructions_button = tk.Button(self.frame, text="Instrucciones", command=self.display_instructions,bg="white")
        self.quit_button = tk.Button(self.frame, text="Salir", command=self.master.quit,bg="white")

        self.video_button.pack(side=tk.LEFT, padx=(10, 5))

        self.analyze_button.pack(side=tk.LEFT, padx=(5, 5))

        self.instructions_button.pack(side=tk.LEFT, padx=(5, 5))

        self.quit_button.pack(side=tk.LEFT, padx=(5, 10))


        # Caja de texto para mostrar el progreso de la lectura de frames
        self.textbox = tk.Text(self.master, height=10, width=50,bg="white")
        self.textbox.pack(side=tk.TOP, pady=(10, 20))

        # Barra de progreso para mostrar el progreso del análisis
        self.progress_bar = ttk.Progressbar(self.master, orient=tk.HORIZONTAL, mode="determinate", length=300)
        self.progress_bar.pack()

        # Label para mostrar el porcentaje de armas encontradas
        self.weapon_percentage = 0
        self.percentage_label = tk.Label(self.master, text="% de Violencia",fg="red",bg="white")
        self.percentage_label.pack()


    def create_widgets(self):

        # Crear Texto Principal
        wachiman_label = tk.Label(root, text="WACHIMAN", font=("Consolas", 24), fg="blue", bg="white")
        wachiman_label.pack(pady=10)

        # Cargar la imagen desde un archivo
        image = Image.open("wachiman.png")
        # Redimensionar la imagen
        image = image.resize((100, 80))

        # Convertir la imagen a un formato que Tkinter pueda manejar
        photo = ImageTk.PhotoImage(image)

        # Asignar la imagen a un Label
        image_label = tk.Label(self.master, image=photo,bg="white")
        image_label.image = photo  # Necesario para evitar que la imagen se pierda debido a la recolección de basura
        image_label.pack()

    def analyze_file(self):
        # Función para analizar el archivo
        pass


    def display_instructions(self):
        # Creamos una nueva ventana para mostrar las instrucciones
        instr_window = tk.Toplevel(self.master)
        instr_window.title("Instrucciones")
        instr_window.resizable(False, False)

        # Creamos un frame para el texto de las instrucciones
        instr_frame = tk.Frame(instr_window, padx=20, pady=20)
        instr_frame.pack()

        # Creamos un widget Text para mostrar el texto de las instrucciones
        instr_text = tk.Text(instr_frame, width=60, height=20)
        instr_text.pack(side=tk.LEFT, fill=tk.BOTH)

        # Agregamos el texto de las instrucciones
        instr_text.config(state=("normal"))
        instr_text.insert(tk.END, "Instrucciones:\n\n")
        instr_text.insert(tk.END, "1. Carga un video haciendo clic en el botón 'Cargar video'.\n")
        instr_text.insert(tk.END, "2. Selecciona el tipo de armas a analizar en el menú desplegable.\n")
        instr_text.insert(tk.END, "3. Selecciona la cantidad de frames a analizar en el menú desplegable.\n")
        instr_text.insert(tk.END, "4. Haz clic en el botón 'Analizar' para iniciar el análisis.\n")
        instr_text.insert(tk.END, "5. Los resultados del análisis se mostrarán en la consola.\n")
        instr_text.insert(tk.END, "6. Para salir del programa, haz clic en el botón 'Salir'.\n\n")
        instr_text.insert(tk.END,
                          "Nota: El análisis puede tardar unos minutos dependiendo del tamaño del video y la cantidad de frames seleccionados.")
        instr_text.config(state=("disabled"))

        # Creamos un botón para cerrar la ventana de instrucciones
        close_button = tk.Button(instr_frame, text="Cerrar", command=instr_window.destroy)
        close_button.pack(side=tk.BOTTOM)


    def load_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo de video",
                                                   filetypes=(("Archivos de video", "*.mp4"),))
        if self.filename:
            self.video = cv2.VideoCapture(self.filename)
            self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

            # Mostrar el nombre del archivo en la caja de texto
            self.textbox.config(state="normal")
            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, f"Archivo cargado: {self.filename}")
            self.textbox.config(state="disabled")

        else:
            messagebox.showerror("Error", "No se seleccionó ningún archivo.")


if __name__ == '__main__':
    root = tk.Tk()
    root.configure(background="white")
    app = App(root)
    root.mainloop()