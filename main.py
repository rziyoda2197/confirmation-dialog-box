from tkinter import Tk, messagebox

def confirmation_dialog():
    root = Tk()
    root.withdraw()  # Dialogni ko'rinishini yashirib qo'yamiz
    response = messagebox.askyesno("Tasdiqlash", "Bu xabarni tasdiqlaysizmi?", icon='error')
    root.destroy()  # Dialogni yashirib qo'yganidan keyin uni yo'q qilamiz
    return response

print(confirmation_dialog())
