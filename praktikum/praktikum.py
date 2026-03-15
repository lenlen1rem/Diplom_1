from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


def main():
    #инициализируем базу данных
    database: Database = Database()

    #создадим новый бургер
    burger: Burger = Burger()

    #считаем список доступных булок из базы данных
    buns: List[Bun] = database.available_buns()

    #считаем список доступных ингредиентов из базы данных
    ingredients: List[Ingredient] = database.available_ingredients()

    #соберём бургер
    burger.set_buns(buns[0])

    burger.add_ingredient(ingredients[1])
    burger.add_ingredient(ingredients[4])
    burger.add_ingredient(ingredients[3])
    burger.add_ingredient(ingredients[5])

    #переместим слой с ингредиентом
    burger.move_ingredient(2, 1)

    #удалим ингредиент
    burger.remove_ingredient(3)

    #распечатаем рецепт бургера
    print(burger.get_receipt())


if __name__ == "__main__":
    main()