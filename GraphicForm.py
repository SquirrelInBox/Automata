import tkinter as tk


class VerticalScrolledFrame(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!

    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)

        return


class StatusBar(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


class NodeFrame(tk.Frame):
    def __init__(self, parent, number, count):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.nodes = []
        self.number = number
        self.startPoint = tk.BooleanVar(False)
        self.endPoint = tk.BooleanVar(False)
        self.initNode(count)

    def initNode(self, count):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.numberLabel = tk.Label(self, text=str(self.number) + ":")
        self.nameEntry = tk.Entry(self)
        self.startCheck = tk.Checkbutton(self, variable=self.startPoint)
        self.endCheck = tk.Checkbutton(self, variable=self.endPoint)
        self.numberLabel.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1)
        self.startCheck.grid(row=0, column=2)
        self.endCheck.grid(row=0, column=3)

        for i in range(count):
            l = tk.Label(self, text=str(i)+":")
            e = tk.Entry(self)
            self.nodes.append((l, e))
            l.grid(row=i+1, column=1)
            e.grid(row=i+1, column=2)

    def info(self, names):
        if self.nameEntry.get() != "":
            info = self.nameEntry.get() + " "
        else:
            info = str(names[self.number]) + " "
        num = 0
        for i in self.nodes:
            vert = i[1].get()
            if vert != "":
                info += str(names[self.nodes.index(i)]) + " " + vert+" "
            num += 1
        return info + "\n"


class NodeHeader(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initHeader()

    def initHeader(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        tk.Label(self, text="Number").grid(row=0, column=0)
        tk.Label(self, text="Name").grid(row=0, column=1)
        tk.Label(self, text="Start").grid(row=0, column=2)
        tk.Label(self, text="End").grid(row=0, column=3)


class MainHeader(tk.Frame):
    def __init__(self, parent, statusbar):
        tk.Frame.__init__(self, parent, relief=tk.RIDGE, borderwidth=1)
        self.parent = parent
        self.main = None
        self.count = 0
        self.statusbar = statusbar
        self.fileName = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.nodeCountLabel = tk.Label(self, text="Count:")
        self.nodeCountEntry = tk.Entry(self)
        self.nodeCountButton = tk.Button(self,  text="Create", width=20)
        self.nodeSaveButton = tk.Button(self,  text="Save", width=20)
        self.fileOutputLabel = tk.Label(self, text="Output file's name:")
        self.fileOutputEntry = tk.Entry(self)
        self.nodeCountLabel.grid(row=0, column=0)
        self.nodeCountEntry.grid(row=0, column=1)
        self.nodeCountButton.grid(row=0, column=2)
        self.nodeSaveButton.grid(row=0, column=3)
        self.fileOutputLabel.grid(row=1, column=0)
        self.fileOutputEntry.grid(row=1, column=1)
        self.nodeSaveButton.config(state=tk.DISABLED)

        def create(event):
            if self.main:
                self.main.grid_forget()
                self.main.destroy()
                self.header.grid_forget()
                self.header.destroy()
            self.count = self.nodeCountEntry.get()
            self.fileName = self.fileOutputEntry.get()
            self.header = NodeHeader(self.parent)
            self.main = MainFrame(self.parent, int(self.count))
            self.header.pack(fill=tk.BOTH)
            self.main.pack(fill=tk.BOTH, expand=1)
            self.nodeSaveButton.config(state=tk.NORMAL)
            self.statusbar.set(
                "%s", "Fill fields what you need and press 'Save' button")

        def save(event):
            info = str(self.fileName) + "\n"
            info += str(self.count) + "\n"
            start = ""
            end = ""
            names = [i.nameEntry.get()
                     if i.nameEntry.get() != ""
                     else self.main.nodeFrames.index(i)
                     for i in self.main.nodeFrames]
            for i in self.main.nodeFrames:
                name = names[self.main.nodeFrames.index(i)]
                info += i.info(names)
                if i.startPoint.get():
                    start += str(name) + " "
                if i.endPoint.get():
                    end += str(name) + " "
            info += start + "\n"
            info += end + "\n"
            with open("in.txt", "w") as txt:
                txt.writelines(info)
            self.statusbar.set("%s", "Saved to in.txt")
            self.parent.destroy()

        self.nodeCountButton.bind("<Button-1>", create)
        self.nodeCountButton.bind("<Return>", create)
        self.nodeSaveButton.bind("<Button-1>", save)
        self.nodeSaveButton.bind("<Return>", save)


class MainFrame(VerticalScrolledFrame):
    def __init__(self, parent, count):
        VerticalScrolledFrame.__init__(self, parent)
        self.parent = parent
        self.nodeFrames = []
        self.initMain(count)

    def initMain(self, count):
        for i in range(count):
            node = NodeFrame(self.interior, i, count)
            node.pack(fill=tk.BOTH)
            self.nodeFrames.append(node)


def write_from_forms():
    root = tk.Tk()
    root.geometry("640x480+200+200")

    statusbar = StatusBar(root)
    header = MainHeader(root, statusbar)

    header.pack(side=tk.TOP, fill=tk.X, pady=20)

    statusbar.pack(side=tk.BOTTOM, fill=tk.X)
    statusbar.set('%s', "Type count and press button 'Create'")
    root.mainloop()
