from tkinter import *
import english
 
root = Tk()
root.geometry("400x500")
root.title("学习是不可能学习的 这辈子都不可能学习的")
data = english.words()

def word_msg(*args):
    indexs = word.curselection()
    if indexs:
        index = int(indexs[0])
        text.delete('1.0','end' )
        temp = data[index][3]
        text.insert(END,temp)

def sentence_msg(*args):
    indexs = sentence.curselection()
    if indexs:
        index = int(indexs[0]) 
        translate.delete('1.0','end' )
        if len(data[index][5]) > 3:
            translate.insert(END,data[index][5])

def update():
    global data
    data = english.words()
    word.delete(0,  END )
    sentence.delete(0,END )    
    text.delete('1.0','end' )
    translate.delete('1.0','end' )
    for i in data:
        temp = "{:20s}  {}".format(i[1],i[2].split())
        print(temp)
        word.insert(END, temp)
        sentence.insert(END,i[4])


word = Listbox(root, width = 55, height = 5, selectforeground='#171717', selectbackground='#EEEEE0' )
text = Text(root, width = 55, height = 5)
sentence = Listbox(root, width = 55, height = 5, selectforeground='#171717', selectbackground='#EEEEE0' )
translate = Text(root, width = 55, height = 5)


word.pack(pady=10)
text.pack(pady=3 )
sentence.pack(pady=10)
translate.pack(pady = 3)
update()

word.bind("<<ListboxSelect>>",word_msg)
sentence.bind("<<ListboxSelect>>", sentence_msg)

b = Button(root, text = "获取新单词", width=10,command=update)
b.pack()

root.mainloop() 