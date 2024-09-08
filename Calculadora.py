import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Variable global para almacenar el historial de iteraciones
historial_global = []

# Función para el método de Newton-Raphson
def newton_raphson(f, df, x0, tol):
	"""
	Implementa el método de Newton-Raphson para encontrar la raíz de una función.
	
	Parámetros:
	f (función): La función de la cual se quiere encontrar la raíz.
	df (función): La derivada de la función f.
	x0 (float): El valor inicial para comenzar la iteración.
	tol (float): La tolerancia para el criterio de convergencia.
	
	Retorna:
	tuple: La raíz aproximada y el historial de iteraciones.
	"""
	historial = []
	x = x0
	while True:
		fx = f(x)
		dfx = df(x)
		if dfx == 0:
			raise ValueError("La derivada es cero.")
		x_new = x - fx / dfx
		historial.append((x, fx, dfx, x_new))
		if abs(x_new - x) < tol:
			break
		x = x_new
	return x_new, historial

# Función para ejecutar el método y mostrar el resultado
def ejecutar_metodo():
	"""
	Ejecuta el método de Newton-Raphson con los parámetros ingresados por el usuario
	y muestra el resultado en un cuadro de diálogo.
	"""
	try:
		f = eval("lambda x: " + entrada_funcion.get())
		df = eval("lambda x: " + entrada_derivada.get())
		x0 = float(entrada_x0.get())
		tol = float(entrada_tolerancia.get())
		resultado, historial = newton_raphson(f, df, x0, tol)
		messagebox.showinfo("Resultado", f"Raíz aproximada: {resultado}")
		global historial_global
		historial_global.extend(historial)
	except Exception as e:
		messagebox.showerror("Error", f"Entrada inválida: {str(e)}")

# Función para mostrar el historial
def mostrar_historial():
	"""
	Muestra una ventana con el historial de iteraciones del método de Newton-Raphson.
	"""
	historial_ventana = tk.Toplevel(root)
	historial_ventana.title("Historial")
	historial_ventana.geometry('800x900')
	historial_ventana.configure(bg='black')  # Establecer el fondo negro
	
 
	# Centrar la ventana de historial
	window_width = 800
	window_height = 700
	screen_width = historial_ventana.winfo_screenwidth()
	screen_height = historial_ventana.winfo_screenheight()
	position_top = int(screen_height / 2 - window_height / 2)
	position_right = int(screen_width / 2 - window_width / 2)
	historial_ventana.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
	
	# Crear la tabla
	tree = ttk.Treeview(historial_ventana, columns=("Iteración", "x", "f(x)", "f'(x)", "x_new"), show='headings')
	tree.heading("Iteración", text="Iteración")
	tree.heading("x", text="x")
	tree.heading("f(x)", text="f(x)")
	tree.heading("f'(x)", text="f'(x)")
	tree.heading("x_new", text="x_new")
	
	# Añadir los datos a la tabla
	for i, (x, fx, dfx, x_new) in enumerate(historial_global):
		tree.insert("", "end", values=(i+1, x, fx, dfx, x_new))
	
	tree.pack(expand=True, fill='both')

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Método de Newton-Raphson")
root.configure(bg='black')
root.geometry('500x600')

# Centrar la ventana principal
window_width = 500
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Crear y colocar los widgets en la ventana principal
tk.Label(root, text="Función f(x):", bg='black', fg='white').grid(row=0, column=0)
entrada_funcion = tk.Entry(root)
entrada_funcion.grid(row=0, column=1)

tk.Label(root, text="Derivada f'(x):", bg='black', fg='white').grid(row=1, column=0)
entrada_derivada = tk.Entry(root)
entrada_derivada.grid(row=1, column=1)

tk.Label(root, text="Valor inicial x0:", bg='black', fg='white').grid(row=2, column=0)
entrada_x0 = tk.Entry(root)
entrada_x0.grid(row=2, column=1)

tk.Label(root, text="Tolerancia:", bg='black', fg='white').grid(row=3, column=0)
entrada_tolerancia = tk.Entry(root)
entrada_tolerancia.grid(row=3, column=1)

tk.Button(root, text="Calcular", command=ejecutar_metodo).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Mostrar Historial", command=mostrar_historial).grid(row=5, column=0, columnspan=2)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()