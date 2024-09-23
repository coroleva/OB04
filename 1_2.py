# class Reprt:
#     def __init__ (self, title, content):
#         self.title = title
#         self.content = content
#     def docPrinter(self):
#         print(f'Сформирован отчет: {self.title} - {self.content}')
#
# report = Reprt('Отчет', 'Текст отчета')
# report.docPrinter()

from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFomatted(Formatted):
    def format(self, report):
        print(f'Сформирован отчет: {report.title} - {report.content}')
class HTMLFomatted(Formatted):
    def format(self, report):
        print(f'<h1>Сформирован отчет: {report.title} - {report.content}</h1>')
class Report:
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)



report = Report('Отчет', 'Текст отчета', TextFomatted())
report.docPrinter()

report = Report('Отчет', 'Текст отчета', HTMLFomatted())
report.docPrinter()
