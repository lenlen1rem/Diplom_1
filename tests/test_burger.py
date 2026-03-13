import sys
import os

#добавляем путь к корневой папке проекта для импорта модулей
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
import constants


class TestBurger:

    #тесты для класса Burger с использованием данных из Stellar Burgers. класс Burger отвечает за сборку бургера, расчет стоимости и формирование чека.


    def test_burger_initialization_bun_is_none(self):

        #тест инициализации бургера - проверка что булка изначально None.

        burger = Burger()
        assert burger.bun is None

    def test_burger_initialization_ingredients_empty_list(self):

        #тест инициализации бургера - проверка что список ингредиентов пуст.

        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns(self):

        #тест установки булки в бургер.

        bun_mock = Mock()
        bun_mock.get_price.return_value = 1255
        
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):

        #тест добавления ингредиента в бургер.

        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 500
        
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self):

        #тест удаления ингредиента из бургера.

        ingredient_mock = Mock()
        
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert ingredient_mock not in burger.ingredients

    def test_move_ingredient(self):

        #тест перемещения ингредиента в списке.

        ingredient1 = Mock()
        ingredient2 = Mock()
        
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        #изначальный порядок: [ingredient1, ingredient2]
        burger.move_ingredient(0, 1)
        #новый порядок: [ingredient2, ingredient1]
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):

        #тест расчета стоимости бургера.

        bun_mock = Mock()
        bun_mock.get_price.return_value = 1000
        
        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 500
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        
        assert burger.get_price() == 1000 * 2 + 500

    @pytest.mark.parametrize("bun_price, sauce_price, filling_price", [
        (1255, 90, 1337),    #краторная булка + Spicy-X + мясо моллюсков
        (988, 15, 300),      #флюоресцентная булка + традиционный + кольца
    ])
    def test_get_price_parametrized(self, bun_price, sauce_price, filling_price):

        #параметризованный тест расчета стоимости.

        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        
        sauce_mock = Mock()
        sauce_mock.get_price.return_value = sauce_price
        
        filling_mock = Mock()
        filling_mock.get_price.return_value = filling_price
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        
        expected_price = bun_price * 2 + sauce_price + filling_price
        assert burger.get_price() == expected_price

    def test_get_receipt(self):

        #тест формирования чека.

        bun_mock = Mock()
        bun_mock.get_name.return_value = "Краторная булка"
        
        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = "Соус Spicy-X"
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        
        receipt = burger.get_receipt()
        assert isinstance(receipt, str)
        assert "Краторная булка" in receipt

    def test_remove_ingredient_invalid_index(self):

        #тест удаления ингредиента с неверным индексом.

        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient_invalid_index(self):

        #тест перемещения ингредиента с неверными индексами.

        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        
        with pytest.raises(IndexError):
            burger.move_ingredient(10, 0)