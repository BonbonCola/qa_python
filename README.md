# qa_python
qa_python - это второй проект в практикуме, он посвящен юнит-тестам.

## Тесты
1. на метод `add_new_book()`:
```python
test_add_new_book_add_two_books_successful(self):
```
проверяет добвление двух разных книг в словарь `books_rating` методом `add_new_book()`
```python
test_add_new_book_add_book_already_exist_not_added(self):
```
проверяет, что одну и ту же книгу можно добавить  в словарь `books_rating` только 1 раз методом `add_new_book()`
```python
test_add_new_book_new_book_have_rating_1(self):
```
проверяет, что у добавленной методом `add_new_book()` в словарь `books_rating` книги рейтинг по умолчанию равен 1
2. на метод `set_book_rating()`:
```python
test_set_book_rating_set_rating_5_success(self):
```
проверяет, что метод `set_book_rating()` устанавливает валидный рейтинг книги
```python
test_set_book_rating_invalid_rating_not_set(self, invalid_rating):
```
проверяет, что метод `set_book_rating()` не устанавливает не валидный рейтинг книги (значения параметров 0 и 11)
```python
test_set_book_rating_if_book_not_exist_valid_rating_not_set(self):
```
проверяет, что метод `set_book_rating()` не устанавливает валидный рейтинг несуществующей книге и не создает ее
3. на метод `get_book_rating()`:

