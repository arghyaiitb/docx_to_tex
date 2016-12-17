from tkinter import simpledialog
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename,asksaveasfile
from collections import namedtuple as nt
root = Tk()
chapter_details = nt('chapter_details', 'C_Name C_loc', rename=True)
story_details = nt('story_details', 'Title Author Edition', rename=True)
book_details = nt('book_details', 'Page_width Page_height Bottom Inner_margin Outer_margin')
font_options = nt('font_options', 'Font Font_size Para_indent Para_space Line_space')

chapter_det = []
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.main()

    def title(self):
        ns = simpledialog.askstring('Title',
                                    'Title of the Book')
        self.author(ns)

    def author(self, title):
        ns = simpledialog.askstring('Author Name',
                                    'Tera naam dal de')
        self.edition(title,ns)

    def edition(self, title, author):
        ns = simpledialog.askstring('Edition',
                                    'First edition probably')
        global story
        story=story_details(Title=title, Author=author, Edition=ns)
        # print

    def page_wid(self):
        ns = simpledialog.askstring('Page width',
                                    'Book page(eg:5in)')
        self.page_hei(ns)

    def page_hei(self, page_width):
        ns = simpledialog.askstring('Page Height',
                                    'Book page(eg:8in)')
        self.inner_mar(page_width, ns)

    def inner_mar(self, page_width, page_height):
        ns = simpledialog.askstring('Inner Margin',
                                    'Limit kya hai(eg:0.75in)')
        self.outer_mar(page_width, page_height, ns)

    def outer_mar(self, page_width, page_height, inner_margin):
        ns = simpledialog.askstring('Outer Margin',
                                    'Limit kya hai(eg:0.625in)')
        self.paragraph_margin(page_width, page_height, inner_margin, ns)

    def paragraph_margin(self, page_width, page_height, inner_margin, outer_margin):
        ns = simpledialog.askstring('Bottom margin',
                                    'Jaldi bol(eg:0.8in)')
        global book_det
        book_det = book_details(Page_width=page_width,
                                Page_height=page_height,
                                Inner_margin=inner_margin,
                                Outer_margin=outer_margin,
                                Bottom=ns)

    def chapter_name(self):
        ns= simpledialog.askstring('Chapter Name',
                                   'Just Name or keep it blank and press Ok')
        self.open_file(ns)

    def open_file(self, ns):
        global chapter_det
        name = askopenfilename(filetypes =(("Word File", "*.docx"),
                                           ("All Files","*.*")),
                               title = "Choose the word File")
        chapter_det.append(chapter_details(C_Name=ns, C_loc=name))


    def no_action(self):
        label1 = Label(Toplevel(), text='peace maro \n argo will put it in next version (arghyasaha26@gmail.com)',)
        label1.pack()

    def font_option(self, font):
        self.font_size(font)

    def font_size(self,font):
        ns = simpledialog.askstring('Font size',
                                    'default is 6pt or 8pt.(do give pt at the end)')
        self.para_indent(font, ns)

    def para_indent(self, font, font_size):
        ns = simpledialog.askstring('Para indent',
                                    'First line of a new para indent(eg:4em)')
        self.para_space(font, font_size, ns)

    def para_space(self, font, font_size, para_indent):
        ns = simpledialog.askstring('Para spacing',
                                    'space between paragraphs(eg:1em)')
        self.line_spacing(font, font_size, para_indent, ns)

    def line_spacing(self, font, font_size, para_indent, para_spacing):
        ns = simpledialog.askstring('Line spacing',
                                    'space between lines (eg:1 or 1.2)')
        global font_format
        font_format = font_options(Font=font,
                                   Font_size=font_size,
                                   Para_indent=para_indent,
                                   Para_space=para_spacing,
                                   Line_space=ns)

    def file_save(self):
        global output_file
        output_file = asksaveasfile(mode='w',
                                    defaultextension=".tex")
        self.quit()

    def quit(self):
        global root
        root.quit()


    def main(self):
        root.title("docx_2_tex v0.2")
        label = ttk.Label(root,
                          text="docx_2_tex",
                          foreground="maroon",
                          font=("Times", 30,"bold"))
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

        button1 = Button(root, text="Story Details", command=self.title, bg="Blue", fg="white")
        button1.place(relx=.90, rely=0.15, anchor=CENTER)

        button2 = Button(root, text="Page Settings", command=self.page_wid, bg="Blue", fg="white")
        button2.place(relx=.90, rely=0.30, anchor=CENTER)

        button3 = Button(root, text="Add Chapter", command=self.chapter_name, bg="Blue",fg="white")
        button3.place(relx=.90, rely=0.45, anchor=CENTER)

        button4 = Button(root, height=2, width=10, text="exit", command=lambda: exit(),bg="red" ,font=("Times",13,"bold"))
        button4.place(relx=.13, rely=0.60, anchor=CENTER)

        options = ["Georgia", "Arial", "century school book", "Book Antiqua"]

        drop = OptionMenu(root, StringVar(), *options, command=self.font_option)
        drop.place(relx=.90, rely=0.60, anchor=CENTER)

        button5 = Button(root, text="Process", command=self.file_save, bg="Blue",fg="white")
        button5.place(relx=.90, rely=0.75, anchor=CENTER)

        # var =


def gui_func():

    app = Application(master=root)
    app.mainloop()
    try:
        return story, book_det, chapter_det, font_format, output_file.name
    except (NameError):
        raise NameError('it')
