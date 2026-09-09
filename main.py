import customtkinter as ctk

app = ctk.CTk()
app.title("Bem vindo ao sistema de teste")
app.geometry("370x150")

label = ctk.CTkLabel(app, text="Bem vindo ao sistema de teste", font=("Arial", 24))
label.pack(padx=20, pady=50)

app.mainloop()
