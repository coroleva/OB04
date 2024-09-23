# Принцип инверсии зависимости (DIP, Dependency Inversion Principle)
# class Book:
#     def read(self):
#         print('Читать книгу')
#
# class StoryReader:
#     def __init__(self):
#         self.book = Book()
#
#     def read_story(self):
#         self.book.read()



from abc import ABC, abstractmethod
class StoryReader(ABC):
    @abstractmethod
    def read_story(self):
        pass
# Создадим несколько источников чтения историй:
class Book(StoryReader):
    def read_story(self):
        print('Читать книгу')

class AudioBook(StoryReader):
    def read_story(self):
        print('Слушать аудиокнигу')

# Создать класс в конструкторе указать источник чтения истории:
class Reader():
    def __init__(self, story_reader: StoryReader):  # передаем источник
        self.story_reader = story_reader
    def read_story(self):
        self.story_reader.read_story()

book = Book()
audio = AudioBook()


reader_book = Reader(book)
reader_audio_book = Reader(audio)

reader_book.read_story()
reader_audio_book.read_story()



# Этот код реализует шаблон проектирования "Стратегия" с использованием абстрактного класса для выбора источника чтения истории (книги или аудиокниги).
#
# Основные элементы:
# Абстрактный класс StoryReader:
#
# Это базовый класс, от которого будут наследоваться другие классы, представляющие разные способы чтения истории.
# Метод read_story объявлен как абстрактный, и любой класс, наследующий его, должен реализовать этот метод.
# Классы Book и AudioBook:
#
# Эти классы наследуются от StoryReader и реализуют метод read_story.
# Book выводит сообщение "Читать книгу", что символизирует чтение бумажной или электронной книги.
# AudioBook выводит "Слушать аудиокнигу", что означает прослушивание аудиокниги.
# Класс Reader:
#
# Этот класс принимает в конструкторе объект типа StoryReader, что позволяет указать способ чтения (книга или аудиокнига).
# В методе read_story вызывается соответствующий метод у переданного объекта story_reader.
# Логика программы:
# Создание источников:
#
# Создаются два объекта: book для чтения книги и audio для прослушивания аудиокниги.
# Создание читателя:
#
# Создаются два читателя: reader_book использует объект книги book, а reader_audio_book использует аудиокнигу audio.
# Чтение истории:
#
# При вызове reader_book.read_story() будет выполнен метод read_story объекта книги, и программа выведет сообщение "Читать книгу".
# При вызове reader_audio_book.read_story() будет выполнен метод аудиокниги, и программа выведет "Слушать аудиокнигу".
# Таким образом, класс Reader использует стратегию (чтение книги или прослушивание аудиокниги)
# в зависимости от переданного ему объекта, что делает его гибким и легко расширяемым для других типов чтения (например, чтение с экрана).