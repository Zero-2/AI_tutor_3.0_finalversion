from tkinter import *
from PIL import Image, ImageTk
from py2neo import Graph, Node, Relationship, NodeMatcher
from bert_intent_recognition.app import BertIntentModel
from bilstm_crf.app import MedicalNerModel

graph = Graph("http://localhost:7474", auth=("neo4j", "neo4j"))
node_matcher = NodeMatcher(graph)

BIM = BertIntentModel()  #实例化BertIntentModel
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
    input = e.get()
    intent_output = BIM.predict(input)
    print("intent_output:")
    print(intent_output)
    entity_output = MNM.predict([input])
    print("entity_output:")
    print(entity_output)
    if(len(entity_output) == 0):
        answer = "sorry I haven't learn that concept, please try some others.\n\n"
        txt.insert(END, "\n\n" + "AI Tutor ->" + answer)
        return
    intent_output = intent_output.get("name")
    entity_output = entity_output[0].get("entities")[0].get("word")
    entity_output = entity_output.strip()
    # print(intent_output)
    # print(entity_output)
    # print(entity_output.split('\n'))
    node1 = node_matcher.match("Nodes").where(name = entity_output.lower()).first()
    print(node1)
    if(node1 == None):
        answer = "sorry I haven't learn that concept, please try some others.\n\n"
        txt.insert(END, "\n\n" + "AI Tutor ->" + answer)
        return
    # print(node1)
    relationship = list(graph.match([node1], r_type = intent_output))
    print(relationship)
    if (len(relationship) == 0):
        answer = "sorry I haven't learn that relationship, please try some others.\n\n"
        txt.insert(END, "\n\n" + "AI Tutor ->" + answer)
        return
    # print(relationship)
    answer = ''
    for i in range(len(relationship)):
        print(relationship[i].end_node['name'])
        answer += str(i+1)+"." + relationship[i].end_node['name'] + "\n\n"
    txt.insert(END, "\n\n" + "AI Tutor ->"+ answer)
    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=70)
txt.grid(row=1, column=0, columnspan=2)
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=65)
e.grid(row=2, column=0)
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,command=send).grid(row=2, column=1)

photo = Image.open('./R.jpg')
photo = photo.resize((400,500))
photo = ImageTk.PhotoImage(photo)
label = Label(image=photo)
label.image = photo
label.grid(row=0, column=2, columnspan=2, rowspan=3)

root.mainloop()
