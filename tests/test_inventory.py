import unittest

import GUI.Inventory
import Items.GunItem
import Items.baseItem
import os


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.inventory = GUI.Inventory.Inventory()
        os.chdir(
            "C:\\Users\\flyin\\OneDrive - Northumbria University - Production Azure AD\\Desktop\\CyberFun\\RPG game in 7 days")
        self.item1 = Items.GunItem.GunItem()
        self.item2 = Items.GunItem.GunItem()

    def test_open_gui(self):
        self.assertEqual(self.inventory.is_open(), False)
        self.inventory.toggle_open()
        self.assertEqual(self.inventory.is_open(), True)
        self.inventory.set_open(False)
        self.assertEqual(self.inventory.is_open(), False)

    def test_item_management(self):
        self.assertEqual(self.inventory.inventory, [None, None, None, None])  # must be empty at first
        self.assertEqual(len(self.inventory.inventory), 4)  # must be empty at first

        self.inventory.insert_item(0, self.item1)
        self.assertIn(self.item1, self.inventory.inventory)

        self.inventory.insert_item(0, self.item2)
        self.assertEqual(self.inventory.inventory[0], self.item2)  # insert should replace old items with new items

        self.inventory.insert_item(1, self.item1)
        self.inventory.insert_item(2, self.item1)
        self.assertEqual(self.inventory.insert_item(3, self.item1), True)
        self.assertEqual(self.inventory.inventory[3], self.item1)

        self.assertRaises(IndexError, self.inventory.insert_item, -23, self.item1)
        self.assertRaises(IndexError, self.inventory.insert_item, 23, self.item1)

    def test_main_hand(self):
        self.assertIsNone(self.inventory.main_hand)
        self.inventory.main_hand = self.item1
        self.assertTrue(self.inventory.main_hand == self.item1, "They are equal")
        self.assertIsInstance(self.inventory.main_hand, Items.baseItem.BaseItem)
        del self.inventory.main_hand
        self.assertIsNone(self.inventory.main_hand)


if __name__ == '__main__':
    unittest.main()
