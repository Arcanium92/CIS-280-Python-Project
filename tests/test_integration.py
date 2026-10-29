import pytest
from library_app.catalog import Catalog
from library_app.book import Book

def test_checkout_through_catalog_reduces_book_copies():
    # Arrange — wire Catalog and Book together
    catalog = Catalog()
    book = Book("Clean Code", "Martin", "111", 3)
    catalog.add_book(book)

    # Act — operate through Catalog (not directly on Book)
    catalog.check_out_book("111")

    # Assert — verify state on Book (the downstream component)
    assert book.available_copies == 2

""" #3 in the list """
def test_checkout_last_copy_makes_book_unavailable():
    # Arrange
    catalog = Catalog()
    book = Book("Clean Code", "Martin", "111", 1)
    catalog.add_book(book)
    
    # Act
    book.check_out()

    # Assert
    assert book.available_copies == False

""" #4 in the list """
def test_return_book_restores_available_status():
    # Arrange
    catalog = Catalog()
    book = Book("Clean Code", "Martin", "111", 0)
    catalog.add_book(book)
    
    # Act
    book.return_book()

    # Assert
    assert book.available_copies == True

""" #1 in the list """
def test_checkout_book_reduces_available_copies_by_1():
    # Arrange
    catalog = Catalog()
    book = Book("Clean Code", "Martin", "111", 3)
    catalog.add_book(book)
    
    # Act
    book.check_out()

    # Assert
    assert book.available_copies == 2

""" #2 in the list """
def test_return_book_increases_available_copies_by_1():
    # Arrange
    catalog = Catalog()
    book = Book("Clean Code", "Martin", "111", 3)
    catalog.add_book(book)
    catalog.check_out_book("111")
    
    # Act
    catalog.return_book("111")

    # Assert
    assert book.available_copies == 3