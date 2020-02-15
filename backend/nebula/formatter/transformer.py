from typing import List
from lxml import etree
from pprint import pprint
mandatory = ['id', 'currencyId', 'name', 'picture', 'categoryId', 'beginDate', 'endDate', 'price', 'model', 'vendor', 'vat', 'delivery']

elements = [{'expiry': {'value': 'NULL'},
'id': {'value': 1278788},
'name': {'value': 'Изготовление макета'},
'vendor': {'value': 'Неизвестен 2'},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Изготовление '
'полиграфической и '
'печатной продукции'},
'Вид товаров': {'is_param': True,
'value': 'Изготовление макетов'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}},
{'expiry': {'value': 'NULL'},
'id': {'value': 16622985},
'name': {'value': 'Доставка товара'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Перевозка (доставка) '
'грузов и корреспонденции'},
'Вид товаров': {'is_param': True,
'value': 'Внутригородская перевозка '
'(доставка) грузов и '
'корреспонденции'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}},
{'expiry': {'value': 'NULL'},
'id': {'value': 16239082},
'name': {'value': 'Техническое обслуживание '
'видеонаблюдения'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Техническое обслуживание '
'и текущий ремонт '
'оборудования, снаряжения, '
'инвентаря'},
'Вид товаров': {'is_param': True,
'value': 'Техническое обслуживание и '
'текущий ремонт систем '
'видеонаблюдения'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}},
{'expiry': {'value': 'NULL'},
'id': {'value': 1325384},
'name': {'value': 'Внутригородская перевозка '
'(доставка) грузов'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Перевозка (доставка) '
'грузов и корреспонденции'},
'Вид товаров': {'is_param': True,
'value': 'Внутригородская перевозка '
'(доставка) грузов и '
'корреспонденции'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}},
{'expiry': {'value': 'NULL'},
'id': {'value': 1413182},
'name': {'value': 'Монтаж, установка, сборка '
'оборудования'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Монтаж, установка, сборка '
'оборудования'},
'Вид товаров': {'is_param': True,
'value': 'Монтаж, установка, сборка '
'прочего оборудования'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}},
{'expiry': {'value': 'NULL'},
'id': {'value': 1291849},
'name': {'value': 'Услуги пультовой охраны, '
'мониторинг систем охранной и '
'аварийной сигнализации'},
'vendor': {'value': 'Неизвестен 2'},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Технические охранные, '
'противопожарные услуги '
'(мероприятия)'},
'Вид товаров': {'is_param': True,
'value': 'Услуги пультовой охраны, '
'мониторинг систем охранной '
'и аварийной сигнализации'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}},
{'expiry': {'value': 'NULL'},
'id': {'value': 19358682},
'name': {'value': 'Техническое обслуживание тревожной '
'сигнализации'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Техническое обслуживание '
'и текущий ремонт '
'оборудования, снаряжения, '
'инвентаря'},
'Вид товаров': {'is_param': True,
'value': 'Техническое обслуживание и '
'текущий ремонт охранного '
'оборудования'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}},
{'expiry': {'value': 'NULL'},
'id': {'value': 18324683},
'name': {'value': 'Техническое обслуживание АПС'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Техническое обслуживание '
'и текущий ремонт '
'оборудования, снаряжения, '
'инвентаря'},
'Вид товаров': {'is_param': True,
'value': 'Техническое обслуживание и '
'текущий ремонт '
'охранно-пожарных систем'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}},
{'expiry': {'value': 'NULL'},
'id': {'value': 20357598},
'name': {'value': 'Предварительный медицинский '
'осмотр'},
'vendor': {'value': None},
'weight': {'value': 'NULL'},
'Вид продукции': {'is_param': True,
'value': 'Медицинские осмотры'},
'Вид товаров': {'is_param': True,
'value': 'Медицинские '
'освидетельствования'},
'Высота': {'value': 'NULL'},
'Диаметр': {'is_param': True, 'value': 'NULL'},
'Длина': {'value': 'NULL'},
'Материал': {'is_param': True, 'value': 'NULL'},
'Объем': {'is_param': True, 'value': 'NULL'},
'Страна происхождения': {'is_param': True,
'value': 'NULL'},
'Цвет': {'is_param': True, 'value': 'NULL'},
'Ширина': {'value': 'NULL'}}]


def offer_transformer(offers: List):
    for offer in offers:
        for man in mandatory:
            if offer.get(man, None) is None:
                offer[man] = {'value': '🤔'}

        root = etree.Element("offer")

        params = []
        for key, value in offer.items():
            is_param = value.get('is_param', False)
            if is_param:
                params.append((key, value['value']))
            else:
                child = etree.SubElement(root, key)
                child.text = str(value['value'])

        for param in params:
            child = etree.SubElement(root, "param", name=param[0])
            child.text = str(param[1])
        print(etree.tostring(root, encoding='utf-8').decode())

offer_transformer(elements)

