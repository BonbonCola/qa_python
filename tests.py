from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # вынесла создание экземпляра класса и добавление первых 2х книг в фикстуру, так как это нужно в каждом тесте,
    # чтобы избежать копипасты и создавать для каждого теста новый экземпляр класса по условиям задачи
    @pytest.fixture
    def collector(self):
        # создаем экземпляр (объект) класса BooksCollector
        c = BooksCollector()
        # добавляем две книги
        c.add_new_book('Гордость и предубеждение и зомби')
        c.add_new_book('Что делать, если ваш кот хочет вас убить')
        c.add_new_book('Убить пересмешника')
        return c

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_successful(self, collector):
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_rating) == 3

    # напиши свои тесты ниже
    def test_add_new_book_add_book_already_exist_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_rating) == 3

    def test_add_new_book_new_book_have_rating_1(self, collector):
        assert collector.books_rating['Гордость и предубеждение и зомби'] == 1

    def test_set_book_rating_5_and_return_rating_5(self, collector):
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        assert collector.books_rating['Гордость и предубеждение и зомби'] == 5

    # тут нас надо проверить хотя бы 2 значения, так как валидный диапазон для рейтинга 1-10
    # чтобы не копипастить тесты и иметь возможность расширить тестовый набор еще значениями - параметризуем
    @pytest.mark.parametrize('invalid_rating', [0, 11])
    def test_set_book_rating_invalid_rating_not_set(self, invalid_rating, collector):
        collector.set_book_rating('Гордость и предубеждение и зомби', invalid_rating)
        assert collector.books_rating['Гордость и предубеждение и зомби'] == 1

    def test_set_book_rating_if_book_not_exist_valid_rating_not_set(self, collector):
        collector.set_book_rating('Тестовая книга', 5)
        assert collector.books_rating.get('Тестовая книга') is None

    def test_get_book_rating_set_rating_5_and_return_rating_5(self, collector):
        collector.books_rating['Гордость и предубеждение и зомби'] = 5
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 5

    def test_get_book_rating_if_book_not_exist_return_none(self, collector):
        assert collector.get_book_rating('Тестовая книга') is None

    @pytest.mark.parametrize('books, rating, result', [
        ({'Гордость и предубеждение и зомби': 8}, 8, 1),
        ({'Гордость и предубеждение и зомби': 8,
          'Что делать, если ваш кот хочет вас убить': 5,
          'Убить пересмешника': 5}, 5, 2),
        ({'Гордость и предубеждение и зомби': 4,
          'Что делать, если ваш кот хочет вас убить': 4,
          'Убить пересмешника': 4}, 4, 3)
    ])
    def test_get_books_with_specific_rating_return_books_with_requested_rating(self, collector, books, rating, result):
        for n, r in books.items():
            collector.books_rating[n] = r
        assert len(collector.get_books_with_specific_rating(rating)) == result

    def test_get_books_with_specific_rating_if_no_ratings_8_return_empty_list(self, collector):
        assert len(collector.get_books_with_specific_rating(8)) == 0

    @pytest.mark.parametrize('invalid_rating', [0, 11])
    def test_get_books_with_specific_rating_if_invalid_rating_return_empty_list(self, collector, invalid_rating):
        assert len(collector.get_books_with_specific_rating(invalid_rating)) == 0

    def test_get_books_with_specific_rating_if_books_rating_dict_is_empty_return_empty_list(self):
        collector = BooksCollector()
        assert len(collector.get_books_with_specific_rating(11)) == 0

    def test_get_books_rating_return_books_dict(self, collector):
        assert collector.get_books_rating() == collector.books_rating

    def test_get_books_rating_return_books_dict_empty(self):
        collector = BooksCollector()
        assert collector.get_books_rating() == collector.books_rating

    @pytest.mark.parametrize('books, favorites, result', [
        (['Гордость и предубеждение и зомби'],
         ['Гордость и предубеждение и зомби'],
         1),
        (['Гордость и предубеждение и зомби',
          'Что делать, если ваш кот хочет вас убить',
          'Убить пересмешника'],
         ['Что делать, если ваш кот хочет вас убить'],
         1),
        (['Гордость и предубеждение и зомби',
          'Что делать, если ваш кот хочет вас убить',
          'Убить пересмешника'],
         ['Что делать, если ваш кот хочет вас убить',
          'Гордость и предубеждение и зомби'],
         2)
    ])
    def test_add_book_in_favorites_add_existing_books_successful(self, collector, books, favorites, result):
        for n in books:
            collector.books_rating[n] = 1
        for f in favorites:
            collector.add_book_in_favorites(f)
        assert len(collector.favorites) == result

    def test_add_book_in_favorites_add_books_not_in_books_rating_return_empty_list(self, collector):
        collector.add_book_in_favorites('Тестовая книга')
        assert len(collector.favorites) == 0

    def test_add_book_in_favorites_book_already_exist_not_added(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 1

    @pytest.mark.parametrize('favorites, deleted, result', [
        (['Гордость и предубеждение и зомби'],
         ['Гордость и предубеждение и зомби'],
         0),
        (['Гордость и предубеждение и зомби',
          'Что делать, если ваш кот хочет вас убить',
          'Убить пересмешника'],
         ['Что делать, если ваш кот хочет вас убить'],
         2),
        (['Гордость и предубеждение и зомби',
          'Что делать, если ваш кот хочет вас убить',
          'Убить пересмешника'],
         ['Что делать, если ваш кот хочет вас убить',
          'Гордость и предубеждение и зомби'],
         1)
    ])
    def test_delete_book_from_favorites_delete_existing_books_successful(self, collector, favorites, deleted, result):
        for f in favorites:
            collector.favorites.append(f)
        for d in deleted:
            collector.delete_book_from_favorites(d)
        assert len(collector.favorites) == result

    def test_delete_book_from_favorites_delete_book_not_in_list_no_error(self, collector):
        collector.favorites.append('Гордость и предубеждение и зомби')
        assert collector.delete_book_from_favorites('Тестовая книга') == None

    @pytest.mark.parametrize('favorites, result', [
        (['Гордость и предубеждение и зомби'],
         1),
        (['Гордость и предубеждение и зомби',
          'Что делать, если ваш кот хочет вас убить',
          'Убить пересмешника'],
         3)
    ])
    def test_get_list_of_favorites_books_return_favorites_list_successful(self, collector, favorites, result):
        for f in favorites:
            collector.favorites.append(f)
        assert len(collector.get_list_of_favorites_books()) == result

    def test_get_list_of_favorites_books_return_empty_list_successful(self, collector):
        assert len(collector.get_list_of_favorites_books()) == 0
