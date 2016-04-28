from tkinter import *


strings = {}


class Node:
    def __init__(self, node_num, letter):
        self.node_num = node_num
        self.letter = letter


class AdjNodes:
    def __init__(self, i, count):
        self.frame = Frame(root, height=2)
        row = 0
        column = 0
        self.adj_nodes = []
        for j in range(count):
            temp_frame = Frame(self.frame, height=1)
            temp_num = Label(temp_frame, text=str(j+1))
            temp_letter = Text(temp_frame, width=10, height=1)
            letters = temp_letter.get("1.0", END).strip().split()
            for letter in letters:
                self.adj_nodes.append(Node(j+1, letter))
            temp_num.grid(row=0, column=0)
            temp_letter.grid(row=0, column=1)
            temp_frame.grid(row=str(row), column=column)
            row += 1
            if (j+1) % 4 == 0:
                row = 0
                column += 1
        self.frame.grid(row=i, column=2)


class OneString:
    def __init__(self, i, count):
        delta = 3
        self.frame_for_check_boxes = Frame(root)
        self.checkbox = Checkbutton(self.frame_for_check_boxes)
        self.checkbox2 = Checkbutton(self.frame_for_check_boxes)
        self.textbox = Text(root, width=10, height=1)
        self.label = Label(root, text=str(i+1))
        self.adj_nodes = AdjNodes(2*i + delta + 1, count)
        self.label.grid(row=2*i+delta, column=0, padx=20)
        self.textbox.grid(row=2*i+delta, column=1)

        self.frame_for_check_boxes.grid(row=2*i+delta, column=2, sticky=W, columnspan=2)
        self.checkbox.grid(row=0, column=0)
        self.checkbox2.grid(row=0, column=1)


class Header:
    def __init__(self):
        self.num = Label(root, text="№")
        self.name = Label(root, text="Имя вершины")
        self.frame_for_checkboxes = Frame(root)
        self.checkBox = Label(self.frame_for_checkboxes, text="Начальное\n состояние")
        self.checkBox2 = Label(self.frame_for_checkboxes, text="Конечное\n состояние")
        self.num.grid(row=2, column=0)
        self.name.grid(row=2, column=1)
        self.frame_for_checkboxes.grid(row=2, column=2, sticky=W)
        self.checkBox.grid(row=0, column=0)
        self.checkBox2.grid(row=0, column=1)


def write_file(event):
    global strings
    with open("in.txt", 'w') as f:
        f.write(str(len(strings) - 1) + '\n')
        for string in strings.keys():
            f.write(string)
            for node_num in strings[string].adj_nodes.adj_nodes():
                pass


def set_button_ok(last_ind):
    butOk = Button(root, text="OK")
    butOk.grid(row=str(last_ind * 2 + 1), column=0, padx=10)
    butOk.bind("<Button-1>", write_file)
    root.mainloop()


def set_some_strings(count):
    global strings
    header = Header()
    # strings[header.name] = header
    for i in range(count):
        tempFrame = OneString(i, count)
        strings[tempFrame.textbox.get("1.0", END)] = tempFrame
    set_button_ok(count + 1)


def output(event):
    try:
        count = int(ent.get())
        ent.destroy()
        but.destroy()
        set_some_strings(count)
    except ValueError:
        pass

root = Tk()
root.minsize(width=450, height=400)

ent = Entry(root, width=3)
but = Button(root, text="Далее")

ent.grid(row=0, column=0, padx=20, pady=20)
but.grid(row=0, column=1)


but.bind("<Button-1>", output)

root.mainloop()
