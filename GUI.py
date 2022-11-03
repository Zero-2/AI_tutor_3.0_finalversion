from tkinter import *
from PIL import Image, ImageTk
# from bert_intent_recognition.app import BertIntentModel
from bilstm_crf.app import MedicalNerModel

# BIM = BertIntentModel()  #实例化BertIntentModel
MNM = MedicalNerModel() #实例化MedicalNerModel
root = Tk()
root.title("AI Tutor")
root.geometry("1000x600")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "TimesNewRoman 14"
FONT_BOLD = "TimesNewRoman 13 bold"


# Send function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    input = e.get().lower()
    # intent_output = BIM.predict(input)
    entity_output = MNM.predict(input)
    print(entity_output)
    # if(intent_output == ""):

    # txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,command=send).grid(row=2, column=1)

photo = Image.open(r'C:\Users\86137\Desktop\R.jpg')
photo = photo.resize((400,400))
photo = ImageTk.PhotoImage(photo)
label = Label(image=photo)
label.image = photo
label.grid(row=0, column=2, columnspan=2, rowspan=3)

root.mainloop()
