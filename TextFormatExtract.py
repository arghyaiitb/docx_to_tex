from LatexDefinition import LatexFormatting as lf
from LatexDefinition import  DocumentHeader as dh

class DocxReading(object):
    def __init__(self):
        ParaReading.__init__(self)

    def chapter_execute(self, chapter):
        processed_chapter = '\\justify\n'
        for para in chapter.paragraphs:
            processed_chapter = ''.join([processed_chapter,ParaReading().run_execute(para), '\par \n'])
        return processed_chapter


class ParaReading(object):
    def __init__(self):
        self

    def run_execute(self, para):
        processed_run = ''
        for run in para.runs:
            processed_run = ''.join([processed_run,FormattingChecks().b_i_u(run)])
        return processed_run

class FormattingChecks(object):

    def __init__(self):
        self

    def b_i_u(self, words):
        """Bold Italic and Underline checks are performed"""
        final_word = words.text.replace('&','\&').replace('%','\%')
        if '*' in words.text:
            final_word = dh().parent_header(['center','****'])
        if words.bold:
            final_word = lf().basic_format('textbf', final_word)
        if words.italic:
            final_word = lf().basic_format('textit', final_word)
        if words.underline:
            final_word = lf().basic_format('underline', final_word)
        return final_word

