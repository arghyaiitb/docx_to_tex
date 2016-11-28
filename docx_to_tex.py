import Gui
import LatexDefinition as LatexDef
import UserInput as Ui
import WordFileExtract as WordFE
import TextFormatExtract as TextFE


def main():
    story_details, book, chapter_details = Gui.gui_func()
    # filename = 'test.docx'
    print(story_details)
    docx_file_instance = WordFE.OpenDocFile()
    text_formatting_instance = TextFE.DocxReading()
    LatexDef_instance = LatexDef.DocumentHeader()
    document_body =''.join(LatexDef_instance.title_page())
    for chapter in chapter_details:
        # print(chapter.C_Name)
        docx_instance = docx_file_instance.openfile(chapter.C_loc)
        document_body=''.join([document_body, LatexDef_instance.chapter_name(chapter.C_Name),
                             text_formatting_instance.chapter_execute(docx_instance)])
    # docx_instance = docx_file_instance.openfile(chapter_details[0].C_loc)
    # document_body = text_formatting_instance.chapter_execute(docx_instance)

    latex_font_class = LatexDef_instance.document_class(12, 'Book')
    # up = LatexDef_instance.usepackage('geometry','left=0.8in,right=0.8in,top=1in,bottom=1in')
    story_parameters = Ui.AboutTheBook().get_all_values(story_details)
    book_dimension = LatexDef_instance.paper_dimension(book.Page_width, book.Page_height, book.Page_margin)
    # book_dimension =
    content = LatexDef_instance.parent_header(['document', document_body])

    print(latex_font_class)
    print(book_dimension)
    for parameter in story_parameters:
        print(parameter)
    # for parameter in book_dimension:
    print(content)



if __name__=='__main__':
    main()