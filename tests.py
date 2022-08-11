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
        return c

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_successful(self, collector):
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    def test_add_new_book_add_book_already_exist_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_new_book_have_rating_1(self, collector):
        assert collector.books_rating['Гордость и предубеждение и зомби'] == 1

    def test_set_book_rating_set_rating_5_success(self, collector):
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
