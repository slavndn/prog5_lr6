# Славный Даниил Михайлович - Лабораторная работа 6

Задача: Применить паттерн декоратор и реализуйте объектно-ориентированную версию программы получения курсов валют с сайта Центробанка таким образом, чтобы:
1. было возможно использовать базовую версию для получения информации о валютах (возвращает словарь со структурой, описанной в одной из предыдущих лабораторных работ) (class CurrenciesList);
2. было возможно применить декоратор к базовой версии и получить данные в формате JSON (class ConcreteDecoratorJSON);
3. было возможно использовать декоратор к базовой версии (CurrenciesList) или к другому декоратору (ConcreteDecoratorJSON) и получить данные в формате csv (class ConcreteDecoratorCSV).

Данные загружаются с веб-страницы Центрального банка России (http://www.cbr.ru/scripts/XML_daily.asp), и обрабатываются для двух валютных идентификаторов.

# Тесты

**1. Импорт `unittest`:**

```python
import unittest
```
Это значит, что мы будем использовать функциональность для тестирования из этого модуля.

**2. Класс `TestCurrencyList`:**

```python
class TestCurrencyList(unittest.TestCase):
```
Вот тут мы создаем класс с тестами. Он наследуется от `unittest.TestCase`, что дает нам всякие удобные штуки для тестирования.

**3. Метод `setUp`:**

```python
    def setUp(self):
        self.cur_list = CurrencyList()
        self.json_decorator = JSONDecorator(self.cur_list)
        self.csv_decorator = CSVDecorator(self.cur_list)
```
Это метод, который вызывается **перед каждым тестом**. Тут мы создаем:
    - `self.cur_list`: Объект, который, похоже, хранит и обрабатывает данные о валютах (скорее всего, это класс, который мы тестируем).
    - `self.json_decorator`: Объект, который умеет преобразовывать данные о валютах в JSON. Судя по названию, это паттерн "Декоратор".
    - `self.csv_decorator`: Объект, который умеет преобразовывать данные о валютах в CSV. Тоже декоратор.
    
**4. Тест `test_get_currencies_standard`:**

```python
    def test_get_currencies_standard(self):
        """Тест на получение данных в стандартном виде"""
        currencies = self.cur_list.get_currencies(['R01239', 'R01235'])
        self.assertIn('R01235', currencies)
```
Это тест для метода `get_currencies` класса `CurrencyList`, который должен возвращать данные в каком-то стандартном формате.
    - Мы запрашиваем данные по валютам с кодами `R01239` и `R01235`.
    - `self.assertIn('R01235', currencies)`: Это проверка, что среди полученных данных есть валюта с кодом `R01235` (скорее всего, доллар).

**5. Тест `test_get_currencies_json`:**

```python
    def test_get_currencies_json(self):
        """Тест на получение данных в формате JSON"""
        json_data = self.json_decorator.get_currencies(['R01239', 'R01235'])
        self.assertTrue(json_data.startswith("{"))
```
Это тест для метода `get_currencies` JSON-декоратора.
    - Мы запрашиваем данные по тем же валютам.
    - `self.assertTrue(json_data.startswith("{"))`: Проверка, что JSON-данные начинаются с фигурной скобки (т.е., выглядят как JSON).

**6. Тест `test_get_currencies_csv`:**

```python
    def test_get_currencies_csv(self):
        """Тест на получение данных в формате CSV"""
        csv_data = self.csv_decorator.get_currencies(['R01239', 'R01235'])
        self.assertTrue(csv_data.startswith("ID;Rate;Name"))
```
Это тест для CSV-декоратора.
    - То же самое, запрашиваем данные.
    - `self.assertTrue(csv_data.startswith("ID;Rate;Name"))`: Проверка, что CSV-данные начинаются с заголовка (то есть, выглядят как CSV).

**7. Тест `test_update_rates`:**

```python
    def test_update_rates(self):
        """Тест на обновление данных"""
        self.cur_list.get_currencies(['R01239', 'R01235'])
        self.cur_list.rates_available = False
        new_data = self.cur_list.get_currencies(['R01239', 'R01235'])
        self.assertNotEqual(new_data, {})
```
Это тест для обновления данных о валютах.
    - Сначала получаем данные один раз.
    - `self.cur_list.rates_available = False`: Выставляем флаг (какой-то атрибут в объекте `cur_list`), который, похоже, указывает, что данные не актуальны.
    - Мы снова запрашиваем данные.
    - `self.assertNotEqual(new_data, {})`: Проверка, что вернулись новые данные (т.е., обновление сработало).



**В итоге:**

*   Класс `CurrencyList` получает и хранит данные.
*   `JSONDecorator` и `CSVDecorator` форматируют данные в JSON и CSV соответственно.
*   Тесты проверяют, что данные получаются правильно в разных форматах и что данные обновляются, когда они устаревают.
