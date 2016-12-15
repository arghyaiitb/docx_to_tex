class DocumentHeader(object):

    def __init__(self):
        self

    def wrapper_around_decorator(func):
        def func_wrapper(self, tag):
            return '\\begin{%s} \n%s \n\\end{%s}\n '%(func(tag[0]), func(tag[1]),func(tag[0]))
        return func_wrapper

    def chapter_name(self, name):
        return '\\chapter{%s}\n' % (name)

    def document_class(self, font_size, class_name):
        doc_class = '\\documentclass[%din] {%s}\n ' %(font_size, class_name)
        return doc_class

    def paper_dimension(self, width, height, bottom, inner_margin, outer_margin):
        paper_def = '\\usepackage[paperwidth=%s, paperheight=%s, bottom=%s, outer=%s,inner=%s]{geometry}' %(width,
                                                                                                            height,
                                                                                                            bottom,
                                                                                                            inner_margin,
                                                                                                            outer_margin)
        return paper_def



    @wrapper_around_decorator
    def parent_header(tag):
        return tag

    def title_page(self):
        return self.parent_header(['titlepage','\\maketitle'])

    def usepackage_with_parameters(package_name, package_parameters):
        return '\\usepackage[%s]{%s}'%(package_parameters, package_name)

    def usepackage_without_parameters(package):
        return '\\usepackage{%s}'%(package)




class LatexFormatting(object):

    def __init__(self):
        self

    def basic_format(self, type, words):
        return '\\%s{%s}' %(type, words)

    def new_keyword_definition(self,type, content):
        return '\\newcommand{\%s}{%s}\n '%(type,content)


class LatexPackages(object):

    def __init__(self):
        self.package_without_para = ['fancyhdr', 'fourier-orns', 'fontspec', 'lmodern', 'mathptmx', 'scrextend']

        self.package_with_para = {'ragged2e': 'document',
                                  'fontenc': 'T1',
                                  'babel': 'british,UKenglish,USenglish,english,american',
                                  'hyphenat': 'none'}

    def basic_packages(self):
        result = ''
        for p in self.package_without_para:
            result = '\n'.join([result, DocumentHeader.usepackage_without_parameters(p)])
        for p in self.package_with_para:
            result = '\n'.join([result, DocumentHeader.usepackage_with_parameters(p, self.package_with_para[p])])
        return result



