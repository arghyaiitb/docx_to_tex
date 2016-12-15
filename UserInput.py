from LatexDefinition import LatexFormatting as lf


class AboutTheBook(object):
    def __init__(self):
        self

    def title(self, title):
        return lf().new_keyword_definition('titlename',title)

    def author_name(self, author):
        return lf().new_keyword_definition('authorname',author)

    def edition(self, edition):
        return lf().new_keyword_definition('edition', edition)

    def get_all_values(self, story):
        values = ''.join([self.title(story.Title), self.author_name(story.Author), self.edition(story.Edition)])
        return values


class BookDimensions(object):
    def __init__(self):
        self

    def page_width(self):
        return input('Please enter the width of the pages: ')

    def page_height(self):
        return  input('Please enter the height of the pages: ')

    def page_margin(self):
        return input('Please enter the top margin of the document: ')

    def page_bottom_margin(self):
        return input('Please enter the bottom margin of the document: ')

    def get_all_values(self, book):
        values =self.page_width(book.Page_width), self.page_height(book.Page_height), self.page_margin(book.Page_margin)
        return values


class BookContent(object):
    def __init__(self):
        self

    def chapter_name(self):
        return '\\chapter{%s}'%input('Enter the Chapter name: ')
