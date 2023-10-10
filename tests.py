import unittest

import person


class TestNightClub(unittest.TestCase):
    def test_rnb(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует рнб
        :return:
        """
        test = person.RnbDance('Никита', 'мальчик', False, False, False, False, True)
        self.assertEqual(test.dance(), 'мальчик Никита - танцует рнб')

    def test_pop_dance(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует поп
        :return:
        """
        test = person.PopDance('Маша', 'девочка', False, False, True, False, False)
        self.assertEqual(test.dance(), 'девочка Маша - танцует под поп-музыку')

    def test_house(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует хаус
        :return:
        """
        test = person.HouseDance('Максим', 'мальчик', False, False, False, True, False)
        self.assertEqual(test.dance(), 'мальчик Максим - танцует хаус')

    def test_hip_hop(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует хип-хоп
        :return:
        """
        test = person.HipHopDance('Алеша', 'мальчик', True, False, False, False, False)
        self.assertEqual(test.dance(), 'мальчик Алеша - танцует хип-хоп')

    def test_electro(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует электро
        :return:
        """
        test = person.ElectroDance('Настя', 'девочка', False, True, False, False, False)
        self.assertEqual(test.dance(), 'девочка Настя - танцует электро')
