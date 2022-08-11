# qa_python

qa_python - это второй проект в практикуме, он посвящен юнит-тестам.

## Тесты

```python
test_add_new_book_add_two_books_successful(self):
```

проверяет добавление двух разных книг в словарь `books_rating` методом `add_new_book()`

```python
test_add_new_book_add_book_already_exist_not_added(self):
```

проверяет, что одну и ту же книгу можно добавить в словарь `books_rating` только 1 раз методом `add_new_book()`

```python
test_add_new_book_new_book_have_rating_1(self):
```

проверяет, что у добавленной методом `add_new_book()` в словарь `books_rating` книги рейтинг по умолчанию равен 1

```python
test_set_book_rating_get_book_rating_set_rating_5_and_return_rating_5(self):
```

проверяет, что метод `set_book_rating()` устанавливает валидный рейтинг книги, а метод `get_book_rating()` возвращает
этот только что установленный рейтинг

```python
test_set_book_rating_invalid_rating_not_set(self, invalid_rating):
```

проверяет, что метод `set_book_rating()` не устанавливает не валидный рейтинг книги (значения параметра 0 и 11)

```python
test_set_book_rating_if_book_not_exist_valid_rating_not_set(self):
```

проверяет, что метод `set_book_rating()` не устанавливает валидный рейтинг несуществующей книге и не создает ее

```python
test_get_book_rating_set_rating_5_and_return_rating_5(self):
```

проверяет, что метод `get_book_rating()` возвращает рейтинг запрошенной книги

```python
test_get_book_rating_if_book_not_exist_return_none(self):
```

проверяет, что метод `get_book_rating()` возвращает none для несуществующей книги

```python
test_get_books_with_specific_rating_return_books_with_requested_rating(self, books, rating, result):
```

проверяет, что метод `get_books_with_specific_rating()` возвращает список книг с указанным рейтингом. Проверям 3 случая:
в списке из 3х книг всего 1 такая книга, в списке 2 таких книги и весь список состоит из книг с нужным нам рейтингом

```python
test_get_books_with_specific_rating_if_no_ratings_8_return_empty_list(self):
```

проверяет, что метод `get_books_with_specific_rating()` возвращает пустой list для запроса рейтинга, которого нет ни у
одной книги в списке

```python
test_get_books_with_specific_rating_if_invalid_rating_return_empty_list(self, invalid_rating):
```

проверяет, что метод `get_books_with_specific_rating()` возвращает пустой list для запроса невалидного рейтинга

```python
test_get_books_with_specific_rating_if_books_rating_dict_is_empty_return_empty_list(self, invalid_rating):
```

проверяет, что метод `get_books_with_specific_rating()` возвращает пустой list если словарь `books_rating`  пустой

```python
test_get_books_rating_return_books_dict()
и
test_get_books_rating_return_books_dict_empty():
```

проверяют, что метод `get_books_rating()` возвращает словарь `books_rating`

```python
test_add_book_in_favorites_add_existing_books_successful(books, favorites, result):
```

проверяет, что метод `add_book_in_favorites()` добавялет книги в избранное. Проверяем 3 кейса: усе книги в избранном, в
избранном только одна и две

```python
test_add_book_in_favorites_add_books_not_in_books_rating_return_empty_list():
```

проверяет, что метод `add_book_in_favorites()` не добавляет в избранное неизвестную книгу

```python
test_add_book_in_favorites_book_already_exist_not_added():
```

проверяет, что метод `add_book_in_favorites()` не добавляет в избранное уже добавленную туда книгу

```python
test_delete_book_from_favorites_delete_existing_books_successful(favorites, deleted, result):
```

проверяют, что метод `delete_book_from_favorites()` удаляет указанные книги из списка избранных. Проверяем 3 кейса:
удалили последнюю книгу из избранного, удалили одну из избранных и пару

```python
test_delete_book_from_favorites_delete_book_not_in_list_no_error():
```

проверяет, что метод `delete_book_from_favorites()` не падает с ошибкой при попытке удалить несуществующую книгу в
списке избранного

```python
test_get_list_of_favorites_books_return_favorites_list_successful(favorites, result):
```

проверяет, что метод `get_list_of_favorites_books()` возвращает список избранного

```python
test_get_list_of_favorites_books_return_empty_list_successful():
```

проверяет, что метод `get_list_of_favorites_books()` возвращает пустой список избранного

## Тестовое покрытие
```bash
coverage run -m pytest tests.py
coverage report -m  

Name       Stmts   Miss  Cover   Missing
----------------------------------------
main.py       30      0   100%
tests.py      81      0   100%
----------------------------------------
TOTAL        111      0   100%
```

