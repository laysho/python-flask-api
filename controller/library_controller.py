from flask_restful import Resource
from flask import request
from service import LibraryService
from models import db


class LibraryListResource(Resource):
    def get(self):
        books = LibraryService.get_all()
        return [book.to_dict() for book in books], 200

    def post(self):
        try:
            data = request.get_json()
            # Validate required fields
            if 'isbn' not in data or 'title' not in data or 'author' not in data:
                return {"message": "ISBN, title, and author are required"}, 400

            book = LibraryService.create(data)
            return book.to_dict(), 201

        except Exception as e:
            db.session.rollback()
            return {"error": "Unexpected error occurred", "details": str(e)}, 500


class LibraryResource(Resource):
    def get(self, isbn):
        book = LibraryService.get_by_id(isbn)
        if not book:
            return {"message": "Book not found"}, 404
        return book.to_dict(), 200

    def put(self, isbn):
        try:
            data = request.get_json()
            book = LibraryService.update(isbn, data)
            if not book:
                return {"message": "Book not found"}, 404
            return book.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {"error": "Unexpected error occurred", "details": str(e)}, 500

    def delete(self, isbn):
        try:
            book = LibraryService.delete(isbn)
            if not book:
                return {"message": "Book not found"}, 404
            return {"message": f"Book with ISBN {isbn} deleted"}, 200
        except Exception as e:
            db.session.rollback()
            return {"error": "Unexpected error occurred", "details": str(e)}, 500