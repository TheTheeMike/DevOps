import unittest
from main import MyShop

class TestMyShop(unittest.TestCase):

    def setUp(self):
        self.test_db_name = 'test_shop_db'
        self.my_shop_instance = MyShop(database=self.test_db_name)
        self.my_shop_instance.create_shop()

    def tearDown(self):
        self.my_shop_instance.delete_shop()
        self.my_shop_instance.close_connection()

    def test_add_item(self):
        self.my_shop_instance.add_item("TestProduct", 39.99)
        query = "SELECT * FROM shop WHERE item = %s"
        params = ("TestProduct",)
        result = self.my_shop_instance.fetch_all(query, params)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "TestProduct")
        self.assertEqual(result[0][2], 39.99)

    def test_delete_item(self):
        self.my_shop_instance.add_item("TestProduct", 39.99)
        self.my_shop_instance.delete_item("TestProduct")
        query = "SELECT * FROM shop WHERE item = %s"
        params = ("TestProduct",)
        result = self.my_shop_instance.fetch_all(query, params)
        self.assertEqual(len(result), 0)

    def test_delete_shop(self):
        self.my_shop_instance.delete_shop()
        query = "SELECT * FROM shop"
        result = self.my_shop_instance.fetch_all(query)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()

