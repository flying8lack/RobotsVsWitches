import unittest

import GUI.Inventory


class MyTestCase(unittest.TestCase):
    def test_open_gui(self):
        self.inventory = GUI.Inventory.Inventory()
        self.assertEqual(self.inventory.is_open(), False)
        self.inventory.toggle_open()
        self.assertEqual(self.inventory.is_open(), True)
        self.inventory.set_open(False)
        self.assertEqual(self.inventory.is_open(), False)


if __name__ == '__main__':
    unittest.main()
