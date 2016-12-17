import Gui
import LatexDefinition as LatexDef
import UserInput as Ui
import WordFileExtract as WordFE
import TextFormatExtract as TextFE
from subprocess import call
import os


def main():
    try:
        story_details, book, chapter_details, font_options, output_file = Gui.gui_func()
    except NameError:
        print ('Input Not Given Properly')
        raise NameError

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
                               '\\mainmatter\n'])

    for chapter in chapter_details:
        # print(chapter.C_Name)
        docx_instance = docx_file_instance.openfile(chapter.C_loc)
        document_body=''.join([document_body, latex_def_instance.chapter_name(chapter.C_Name),
                               text_formatting_instance.chapter_execute(docx_instance)])

    latex_font_class = latex_def_instance.document_class(12, 'Book')

    latex_usepackages = latex_packages.basic_packages()

    hard_coded_font_options = '''
\\setmainfont{%s}

\\changefontsizes{%s}
\\pagestyle{fancy}
\\thispagestyle{empty}


\\setlength{\\parindent}{%s}
\\setlength{\\parskip}{%s}
\\renewcommand{\\baselinestretch}{%s}

\\fancyhead[LO]{\\footnotesize \\textit{\\titlename}}
\\fancyhead[RE]{\\footnotesize \\textit{\\authorname}}
\\fancyfoot[C]{\\footnotesize \\thepage}

''' % (font_options.Font,
                                            font_options.Font_size,
                                            font_options.Para_indent,
                                            font_options.Para_space,
                                            font_options.Line_space)

    story_parameters = Ui.AboutTheBook().get_all_values(story_details)

    book_dimension = latex_def_instance.paper_dimension(book.Page_width,
                                                        book.Page_height,
                                                        book.Bottom,
                                                        book.Inner_margin,
                                                        book.Outer_margin)

    content = latex_def_instance.parent_header(['document', document_body])

    f = open(output_file, 'w', encoding='utf-8')
    f.write(latex_font_class)
    f.write(latex_usepackages)
    f.write(book_dimension)
    f.write(hard_coded_font_options)
    f.write(story_parameters)
    f.write(content)
    f.close()

    path = output_file[:output_file.rfind('/')]+'/output/'
    pdf_file = ''.join([path,
                       output_file[output_file.rfind('/')+1:-4],
                       '.pdf'])

    os.system('lualatex -output-directory="%s" "%s" && "%s"' %(path, output_file, pdf_file))



if __name__=='__main__':
    main()
