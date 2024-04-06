import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # Expected Results
    expected_results = [
        ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
        ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    ]

    """ ------------ Add the assertion below ------------ """
    for quote, expected_result in zip(quotes, expected_results):
        result = getDataPoint(quote)
        self.assertEqual(result, expected_result)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # Expected Results
    expected_results = [
        ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
        ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    ]

    """ ------------ Add the assertion below ------------ """
    for quote, expected_result in zip(quotes, expected_results):
        result = getDataPoint(quote)
        self.assertEqual(result, expected_result)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
      price_a = 10
      price_b = 5
      expected_result = 2.0
      result = getRatio(price_a, price_b)
      self.assertEqual(result, expected_result)

  def test_getRatio_withZeroDivision(self):
      price_a = 10
      price_b = 0
      result = getRatio(price_a, price_b)
      self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
