import unittest
from main import CurrencyList, JSONDecorator, CSVDecorator  

class TestCurrencyList(unittest.TestCase):
    def setUp(self):
        self.cur_list = CurrencyList()
        self.json_decorator = JSONDecorator(self.cur_list)
        self.csv_decorator = CSVDecorator(self.cur_list)

    def test_get_currencies_standard(self):
        currencies = self.cur_list.get_currencies(['R01239', 'R01235'])
        self.assertIn('R01235', currencies)  
    def test_get_currencies_json(self):
        json_data = self.json_decorator.get_currencies(['R01239', 'R01235'])
        self.assertTrue(json_data.startswith("{")) 

    def test_get_currencies_csv(self):
        csv_data = self.csv_decorator.get_currencies(['R01239', 'R01235'])
        self.assertTrue(csv_data.startswith("ID;Rate;Name")) 

    def test_update_rates(self):
        self.cur_list.get_currencies(['R01239', 'R01235'])
        self.cur_list.rates_available = False  
        new_data = self.cur_list.get_currencies(['R01239', 'R01235'])
        self.assertNotEqual(new_data, {})  

if __name__ == '__main__':
    unittest.main()
