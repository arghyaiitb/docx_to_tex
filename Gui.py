from tkinter import simpledialog
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfilename
from collections import namedtuple as nt
root = Tk()
chapter_details = nt('chapter_details', 'C_Name C_loc', rename=True)
story_details = nt('story_details', 'Title Author Edition', rename=True)
book_details = nt('book_details', 'Page_width Page_height Page_margin')

chapter_det = []
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.main()

    def title(self):
        ns = simpledialog.askstring('Title', 'Kuch bhi naam bol de')
        self.author(ns)

    def author(self, title):
        ns = simpledialog.askstring('Author Name', 'Tera naam dal de')
        self.edition(title,ns)

    def edition(self, title, author):
        ns = simpledialog.askstring('Chapter Name', 'Just Name')
        global story
        story=story_details(Title=title, Author=author, Edition=ns)
        # print

    def page_wid(self):
        ns = simpledialog.askstring('Page width', 'The fat one')
        self.page_hei(ns)

    def page_hei(self, page_width):
        ns = simpledialog.askstring('Page Height', 'The tall one')
        self.page_mar(page_width, ns)

    def page_mar(self, page_width, page_height):
        ns = simpledialog.askstring('Page Margin', 'Limit kya hai')
        global book_det
        book_det = book_details(Page_width=page_width, Page_height=page_height, Page_margin=ns)

    def chapter_name(self):
        ns= simpledialog.askstring('Chapter Name','Just Name')
        self.open_file(ns)

    def open_file(self, ns):
        global chapter_det
        name = askopenfilename(filetypes =(("Word File", "*.docx"),("All Files","*.*")),title = "Choose the word File")
        chapter_det.append(chapter_details(C_Name=ns, C_loc=name))


    def no_action(self):
        print('Chill hai')

    def main(self):
        root.title("docx_2_tex v0.1")
        label = ttk.Label(root, text="docx_2_tex", foreground="maroon", font=("Times", 30,"bold"))
        label.pack()

        menubar = Menu(root)
        story = Menu(menubar, tearoff=0)
        story.add_command(label="Title", command=self.no_action)
        story.add_command(label="Author", command=self.no_action)
        story.add_command(label="Edition", command=self.no_action)
        menubar.add_cascade(label="Story", menu=story)

        book = Menu(menubar, tearoff= 0)
        book.add_command(label='Page Width', command=self.no_action )
        book.add_command(label='Page Height', command= self.no_action)
        book.add_command(label='Page Margin', command= self.no_action)
        menubar.add_cascade(label= 'Page Settings', menu=story )

        chapter=Menu(menubar,tearoff=0)
        chapter.add_command(label='Chapter Name', command=self.no_action)
        chapter.add_command(label='Chapter source', command=self.no_action)
        menubar.add_cascade(label='Chapter', menu=chapter)

        root.geometry("740x680")
        # root.resizable(width=False, height=False)
        root.config(menu=menubar)

        # button1 = Button(root, text="Add Chapter", command=self.chapter_name, bg="Blue",fg="white")
        # button1.place(relx=.87, rely=0.75, anchor=CENTER)

        button3 = Button(root, text="Story Details", command=self.title, bg="Blue", fg="white")
        button3.place(relx=.90, rely=0.15, anchor=CENTER)

        button3 = Button(root, text="Page Settings", command=self.page_wid, bg="Blue", fg="white")
        button3.place(relx=.90, rely=0.35, anchor=CENTER)

        button2 = Button(root, text="Add Chapter", command=self.chapter_name, bg="Blue",fg="white")
        button2.place(relx=.90, rely=0.55, anchor=CENTER)

        button4 = Button(root, height=2, width=10, text="exit", command=lambda: exit(),bg="red" ,font=("Times",13,"bold"))
        button4.place(relx=.13, rely=0.75, anchor=CENTER)

        button1 = Button(root, text="Process", command=self.no_action, bg="Blue",fg="white")
        button1.place(relx=.90, rely=0.75, anchor=CENTER)




def gui_func():
    img = PhotoImage(file="story_mirror_logo.png")
    panel = Label(root, image=img)
    panel.place(relx=0.5, rely=0.5, anchor=CENTER)
    panel.pack(side="bottom", fill="both", expand="yes")

    app = Application(master=root)
    app.mainloop()
    return story, book_det, chapter_det
