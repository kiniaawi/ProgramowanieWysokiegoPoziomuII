# poprawiony kod biblioteki
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    books = relationship('Book', back_populates='author')


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')


class Library:
    def __init__(self, database_url='sqlite:///library.db'):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_author(self, name):
        author = Author(name=name)
        self.session.add(author)
        self.session.commit()
        return author

    def add_book(self, title, author_name):
        author = self.session.query(Author).filter_by(name=author_name).first()
        if not author:
            author = self.add_author(author_name)
        book = Book(title=title, author=author)
        self.session.add(book)
        self.session.commit()
        return book

    def get_books_by_author(self, author_name):
        author = self.session.query(Author).filter_by(name=author_name).first()
        if author:
            return [book.title for book in author.books]
        return []


if __name__ == '__main__':
    library = Library()

    library.add_book('Harry Potter', 'J.K. Rowling')
    library.add_book('Fantastic Beasts', 'J.K. Rowling')

    print(library.get_books_by_author('J.K. Rowling'))