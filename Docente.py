from tkinter import messagebox
from tkinter.ttk import Label, Entry, Button, Frame
from Form import Form
import sqlite3
        
class TeacherForm(Form):

    def __init__(self, root, connection, form_type, *args, **kwargs):
        self.conn = connection

        self.teacherFrame = Frame(root, relief="groove", padding=(15,15))
        self.teacherFrame.grid(row=0, column=0, padx=10, pady=10)

        lbl_dni = Label(self.teacherFrame, text="DNI: ", width=10)
        lbl_dni.grid(row=1, column=0, columnspan=10)

        dni = Entry(self.teacherFrame, width=40)
        dni.grid(row=2, column=0, columnspan=40, pady=(0,15))

        lbl_name = Label(self.teacherFrame, text="Nombre: ", width=10)
        lbl_name.grid(row=3, column=0, columnspan=10)

        name = Entry(self.teacherFrame, width=40)
        name.grid(row=4, column=0, columnspan=40, pady=(0,15))

        lbl_surname = Label(self.teacherFrame, text="Apellido: ", width=10)
        lbl_surname.grid(row=5, column=0, columnspan=10)

        surname = Entry(self.teacherFrame, width=40)
        surname.grid(row=6, column=0, columnspan=40, pady=(0,15))

        lbl_email = Label(self.teacherFrame, text="Email: ", width=10)
        lbl_email.grid(row=7, column=0, columnspan=10)

        email = Entry(self.teacherFrame, width=40)
        email.grid(row=8, column=0, columnspan=40, pady=(0,15))

        lbl_phone = Label(self.teacherFrame, text="Teléfono: ", width=10)
        lbl_phone.grid(row=9, column=0, columnspan=10)

        phone = Entry(self.teacherFrame, width=40)
        phone.grid(row=10, column=0, columnspan=40, pady=(0,15))

        lbl_titulo = Label(self.teacherFrame, text="Título: ", width=10)
        lbl_titulo.grid(row=11, column=0, columnspan=10)

        titulo = Entry(self.teacherFrame, width=40)
        titulo.grid(row=12, column=0, columnspan=40, pady=(0,15))

        Form.__init__(self, {"dni":dni, "nombre":name, "apellido":surname, 
                             "email":email, "telefono":phone, "titulo":titulo})

        if form_type == "details":
            self.btn_modify = Button(self.teacherFrame, text="Modificar",
                                    command=self.update)
            self.btn_modify.grid(row=13, column=0, columnspan=20, pady=5)

            self.btn_delete = Button(self.teacherFrame, text="Eliminar",
                                    command=self.delete)
            self.btn_delete.grid(row=13, column=20, columnspan=20, pady=5)

        elif form_type == "create":
            lbl_newTeacher = Label(self.teacherFrame, text="Formulario de registro")
            lbl_newTeacher.grid(row=0, column=0, columnspan=18, pady=(5,10))

            self.btn_createStudent = Button(self.teacherFrame, text="Registrar",
                                            command=self.create)
            self.btn_createStudent.grid(row=13, column=0, columnspan=40, pady=5)

    def create(self):
        cur = self.conn.cursor()
        data = self.get_data()
        sql = """INSERT INTO `Docente` VALUES 
                  (NULL, ?, ?, ?, ?, ?, ?)"""

        try:
            cur.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print(e)

        self.modified = True
        self.clean_fields()
        messagebox.showinfo("Información", "El registro se ha creado con éxito!")

    def delete(self):
        if messagebox.askyesnocancel("Confimación", "Está seguro que desea eliminar \nlos datos del docente?"):
            cur = self.conn.cursor()
            sql = """DELETE FROM `Docente` 
                     WHERE codigo = ?"""
            
            try:
                cur.execute(sql, (self.id_register,))
                self.conn.commit()
            except Exception as e:
                print(e)
            
            self.modified = True
            messagebox.showinfo("Información", "El registro se ha eliminado con éxito!")
            

    def update(self):
        if messagebox.askyesnocancel("Confimación", "Está seguro que desea modificar \nlos datos del docente?"):
            cur = self.conn.cursor()
            data = self.get_data()
            data.append(self.id_register)
            sql = """UPDATE `Docente` 
                     SET dni = ?, nombre = ?, apellido = ?, email = ?, telefono = ?, titulo = ? 
                     WHERE codigo = ?"""

            try:
                cur.execute(sql, data)
                self.conn.commit()
            except Exception as e:
                print(e)

            self.modified = True
            messagebox.showinfo("Información", "El registro se ha modificado con éxito!")