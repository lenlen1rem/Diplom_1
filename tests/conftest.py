import random
import pytest
import sys
import os

#добавляем путь к корневой папке проекта
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
import praktikum.ingredient_types as types

#импортируем из модуля tests
from tests.constants import bun_names, bun_prices, sauces, fillings


@pytest.fixture(scope="function")
def new_bun():
    """фикстура создания булки с реальным названием и ценой из Stellar Burgers"""
    bun_index = random.randint(0, len(bun_names) - 1)
    return Bun(bun_names[bun_index], bun_prices[bun_index])


@pytest.fixture(scope="function")
def new_ingredient():
    """фикстура создания нового рандомного ингредиента: соуса или начинки с реальными данными"""
    ingredient_type = random.choice([types.INGREDIENT_TYPE_SAUCE, types.INGREDIENT_TYPE_FILLING])
    
    if ingredient_type == types.INGREDIENT_TYPE_FILLING:
        ingredient_data = random.choice(fillings)
        ingredient_name, ingredient_price = ingredient_data
    else:
        ingredient_data = random.choice(sauces)
        ingredient_name, ingredient_price = ingredient_data
        
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_sauce():
    """фикстура создания соуса с реальным названием и ценой из Stellar Burgers"""
    ingredient_data = random.choice(sauces)
    ingredient_name, ingredient_price = ingredient_data
    return Ingredient(types.INGREDIENT_TYPE_SAUCE, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_filling():
    """фикстура создания начинки с реальным названием и ценой из Stellar Burgers"""
    ingredient_data = random.choice(fillings)
    ingredient_name, ingredient_price = ingredient_data
    return Ingredient(types.INGREDIENT_TYPE_FILLING, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_burger(new_bun, new_filling, new_sauce):
    """фикстура создания готового бургера с булкой, начинкой и соусом из реальных данных"""
    burger = Burger()
    burger.set_buns(new_bun)
    burger.add_ingredient(new_filling)
    burger.add_ingredient(new_sauce)
    return burger