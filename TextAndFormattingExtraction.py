class DocxReading(object):
    def __init__(self):
        ParaReading.__init__(self)


    def chapter_execute(self, chapter):
        processed_chapter = ''
        for para in chapter.paragraphs:
            processed_chapter = ''.join([processed_chapter,ParaReading().run_execute(para)])
        return processed_chapter


class ParaReading(object):
    def __init__(self):
        self

    def run_execute(self, para):
        processed_run = ''
        for run in para.runs:
            processed_run = ''.join([processed_run,FormattingChecks().b_i_u(run)])
        return 'a'

class FormattingChecks(object):

    def __init__(self):
        self

    def b_i_u(self, words):
        """Bold Italic and Underline checks are performed"""

        if words.bold:
            print(words.text)
        if words.italic:
            print(words.text)
        if words.underline:
            print(words.text)
        return 'a'

