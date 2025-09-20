from models import Library, db

class LibraryRepository:
    @staticmethod
    def find_all():
        return Library.query.all()
    
    @staticmethod
    def find_by_id(isbn):
        return Library.query.get(isbn)
    
    @staticmethod
    def save(book):
        db.session.add(book)
        db.session.commit()
        return book
    
    @staticmethod
    def update(isbn, data: dict):
        book = Library.query.get(isbn)
        if not book:
            return None
        for key, value in data.items():
            if hasattr(book, key):
                setattr(book, key, value)

        db.session.commit()
        return book

    @staticmethod
    def delete(isbn):
        book = Library.query.get(isbn)
        if not book:
            return None
        db.session.delete(book)
        db.session.commit()
        return book