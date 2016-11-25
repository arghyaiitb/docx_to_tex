import docx


class OpenDocFile(object):
    def __init__(self):
        pass

    def openfile(self, filename):
        document = docx.Document(filename)
        return document

    



