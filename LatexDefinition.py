class DocumentHeader(object):

    def __init__(self):
        self

    def document_class(self, font_size, class_name):
        doc_class = '\\documentclass[%din] {%s}' %(font_size, class_name)
        return doc_class

    def paper_dimension(self, width, height, margin):
        paper_def = '\\usepackage[paperwidth=%din, paperheight=%din, margin=%din]{geometry}' %(width, height, margin)
        return paper_def

    def start_header(self, header):
        return '\\begin{%s}' %(header)

    def end_header(self, header):
        return '\\end{%s}' %(header)
