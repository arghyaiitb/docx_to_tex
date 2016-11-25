import docx

import Gui
import LatexDefinition
import UserInput
import WordFileExtract
import TextAndFormattingExtraction


def main():
    filename = 'test.docx'
    docx_file_instance = WordFileExtract.OpenDocFile()
    docx_instance = docx_file_instance.openfile(filename)

    text_formatting_instance = TextAndFormattingExtraction.DocxReading()
    document_body = text_formatting_instance.chapter_execute(docx_instance)


    LatexDefinition_instance = LatexDefinition.DocumentHeader()
    latex_document_instance = LatexDefinition_instance.document_class(12, 'Book')
    l = LatexDefinition_instance.paper_dimension(12,12,1)
    y = LatexDefinition_instance.start_header('cool')
    z = LatexDefinition_instance.end_header('cool')
    print(latex_document_instance,l,y,z)



if __name__=='__main__':
    main()