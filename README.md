# LibraryApp — Python Starter Project

This is your starting point for the team project. It's a small console app that
models a library book checkout system, with pytest already wired up
and one example test in place.

## What's in here

```
main.py                         ← run this to start the console app
library_app/
  book.py                       ← a single book title, tracks copies available
  catalog.py                    ← manages the collection of books (add, search, checkout, return)
tests/
  test_book.py                  ← one example unit test — use this as a pattern
requirements.txt                ← run `pip install -r requirements.txt` to get pytest
pytest.ini                      ← pytest configuration (don't need to touch this)
```

## Setup (one time)

From the project root, install dependencies:
```
pip install -r requirements.txt
```

## Running the app

```
python main.py
```
You should see the catalog print out, a book get checked out, and an updated count.

## Running the tests

From the project root:
```
pytest
```
You should see `tests/test_book.py::test_check_out_reduces_available_copies_by_one PASSED`.

## What you'll do with this

Over the semester you'll come back to this project to:
- Add more unit tests (Week 7)
- Add integration tests across `Catalog` and `Book` working together (Week 9)
- Add a smoke test confirming the app runs end-to-end without crashing (Week 10)
- Add a performance test (e.g., checking out many books quickly) (Week 13)
- Wire up GitHub Actions to run your tests automatically on every push (Week 11)

You're free to extend the `Catalog` and `Book` classes with new features as your
team project requires — this starter is meant to be a foundation, not a final product.

Set up by: Nick Morgan