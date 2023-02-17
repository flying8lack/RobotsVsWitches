import unittest

import GUI.Inventory
import Items.GunItem


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.inventory = GUI.Inventory.Inventory()
        self.item1 = Items.GunItem.GunItem()
        self.item2 = Items.GunItem.GunItem()

    def test_open_gui(self):
        self.assertEqual(self.inventory.is_open(), False)
        self.inventory.toggle_open()
        self.assertEqual(self.inventory.is_open(), True)
        self.inventory.set_open(False)
        self.assertEqual(self.inventory.is_open(), False)

    def test_item_management(self):
        self.assertEqual(self.inventory.is_full(), False)  # must be empty at first
        self.assertEqual(len(self.inventory.inventory), 0)  # must be empty at first

        self.inventory.insert_item(0, self.item1)
        self.assertIn(self.item1, self.inventory.inventory)

        self.inventory.insert_item(0, self.item2)
        self.assertEqual(self.inventory.inventory[0], self.item2)  # insert should replace old items with new items

        self.inventory.insert_item(1, self.item1)
        self.inventory.insert_item(2, self.item1)
        self.assertEqual(self.inventory.insert_item(3, self.item1), True)
        self.assertEqual(self.inventory.is_full(), True)

        self.assertEqual(self.inventory.insert_item(4, self.item1), False)
        self.assertEqual(self.inventory.is_full(), True)


if __name__ == '__main__':
    unittest.main()
