class DocumentHeader(object):

    def __init__(self):
        self


    def wrapper_around_decorator(func):
        def func_wrapper(self, tag):
            return '\\begin{%s} \n%s \n\\end{%s}\n '%(func(tag[0]), func(tag[1]),func(tag[0]))
        return func_wrapper


    def document_class(self, font_size, class_name):
        doc_class = '\\documentclass[%din] {%s}\n ' %(font_size, class_name)
        return doc_class

    def paper_dimension(self, width, height, margin):
        paper_def = '\\usepackage[paperwidth=%sin, paperheight=%sin, margin=%sin]{geometry}' %(width, height, margin)
        return paper_def

    def chapter_name(self, name):
        return '\\chapter{%s}\n' % (name)


    @wrapper_around_decorator
    def parent_header(tag):
        return tag

    def usepackage(self, package_name, package_parameters ):
        return '\\usepackage[%s]{%s}'%(package_parameters, package_name)

    def title_page(self):
        return self.parent_header(['titlepage','\\maketitle'])



class LatexFormatting(object):

    def __init__(self):
        self

    def basic_format(self, type, words):
        return '\\%s{%s}' %(type, words)

    def new_keyword_definition(self,type, content):
        return '\\newcommand{\%s}{%s}\n '%(type,content)



