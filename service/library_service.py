from repositories import LibraryRepository
from models import Library

class LibraryService:
    @staticmethod
    def get_all():
        return LibraryRepository.find_all()
    
    @staticmethod
    def get_by_id(isbn):
        return LibraryRepository.find_by_id(isbn)
    
    @staticmethod
    def create(data):
        
        book = Library(
            isbn = data['isbn'],
            title = data['title'],
            author = data['author']
        )
        return LibraryRepository.save(book)
    
    @staticmethod
    def update(isbn, data):
        return LibraryRepository.update(isbn, data)
    
    @staticmethod
    def delete(isbn):
        return LibraryRepository.delete(isbn)