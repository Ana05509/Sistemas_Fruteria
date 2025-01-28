import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="3306",
        user="root",
        password='088266619Da.di',
        database='fruteria',)

# Función para agregar un producto
def agregar_producto():
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    stock = entry_stock.get()

    if nombre and precio and stock:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ventas_producto (nombre, precio, stock) VALUES (%s, %s, %s)",
                       (nombre, precio, stock))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
        limpiar_campos()
        mostrar_productos()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
# Función para actualizar un producto
def actualizar_producto():
    id_producto = entry_id.get()
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    stock = entry_stock.get()

    if id_producto and nombre and precio and stock:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("UPDATE ventas_producto SET nombre=%s, precio=%s, stock=%s WHERE id=%s",
                       (nombre, precio, stock, id_producto))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Producto actualizado correctamente")
        limpiar_campos()
        mostrar_productos()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
# Función para eliminar un producto
def eliminar_producto():
    id_producto = entry_id.get()
    if id_producto:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ventas_producto WHERE id=%s", (id_producto,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        limpiar_campos()
        mostrar_productos()
    else:
        messagebox.showerror("Error", "Ingrese un ID válido")

# Función para eliminar un producto
def eliminar_producto():
    id_producto = entry_id.get()
    if id_producto:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ventas_producto WHERE id=%s", (id_producto,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        limpiar_campos()
        mostrar_productos()
    else:
        messagebox.showerror("Error", "Ingrese un ID válido")
# Función para eliminar un producto
def eliminar_producto():
    id_producto = entry_id.get()
    if id_producto:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ventas_producto WHERE id=%s", (id_producto,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        limpiar_campos()
        mostrar_productos()
    else:
        messagebox.showerror("Error", "Ingrese un ID válido")
# Función para mostrar productos en la lista
def mostrar_productos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ventas_producto")
    rows = cursor.fetchall()
    conn.close()
    
    listbox_productos.delete(0, tk.END)
    for row in rows:
        listbox_productos.insert(tk.END, f"ID: {row[0]}, Nombre: {row[1]}, Precio: {row[2]}, Stock: {row[3]}")
# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_stock.delete(0, tk.END)



