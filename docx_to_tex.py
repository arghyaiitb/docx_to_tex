import Gui
import LatexDefinition as LatexDef
import UserInput as Ui
import WordFileExtract as WordFE
import TextFormatExtract as TextFE


def main():
    story_details, book, chapter_details = Gui.gui_func()
    docx_file_instance = WordFE.OpenDocFile()
    text_formatting_instance = TextFE.DocxReading()
    latex_def_instance = LatexDef.DocumentHeader()
    latex_packages = LatexDef.LatexPackages()

    document_body = '\n'.join(['\\frontmatter',
                               '\\title{\\titlename}',
                               '\\author{\\authorname}',
                               '\\sloppy',
                               latex_def_instance.title_page(),
                               '\\tableofcontents',
                               '\\mainmatter'])

    for chapter in chapter_details:
        # print(chapter.C_Name)
        docx_instance = docx_file_instance.openfile(chapter.C_loc)
        document_body=''.join([document_body, latex_def_instance.chapter_name(chapter.C_Name),
                               text_formatting_instance.chapter_execute(docx_instance)])

    latex_font_class = latex_def_instance.document_class(12, 'Book')

    latex_usepackages = latex_packages.basic_packages()

    story_parameters = Ui.AboutTheBook().get_all_values(story_details)

    book_dimension = latex_def_instance.paper_dimension(book.Page_width,
                                                        book.Page_height,
                                                        book.Bottom,
                                                        book.Inner_margin,
                                                        book.Outer_margin)

    content = latex_def_instance.parent_header(['document', document_body])

    print(latex_font_class)
    print(latex_usepackages)
    print(book_dimension)
    print(story_parameters)
    print(content)



if __name__=='__main__':
    main()
