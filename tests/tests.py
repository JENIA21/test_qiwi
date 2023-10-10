from src import person
from src.night_club import DanceType


class TestNightClub:
    def test_rnb(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует рнб
        :return:
        """
        test = person.RnbDance(name='Никита', sex='мальчик', skills=[DanceType.RNB.value])
        assert test.dance() == 'мальчик Никита - танцует рнб'

    def test_pop_dance(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует поп
        :return:
        """
        test = person.PopDance(name='Маша', sex='девочка', skills=[DanceType.POP.value])
        assert test.dance() == 'девочка Маша - танцует под поп-музыку'

    def test_house(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует хаус
        :return:
        """
        test = person.HouseDance(name='Максим', sex='мальчик', skills=[DanceType.HOUSE.value])
        assert test.dance() == 'мальчик Максим - танцует хаус'

    def test_hip_hop(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует хип-хоп
        :return:
        """
        test = person.HipHopDance(name='Алеша', sex='мальчик', skills=[DanceType.HIPHOP.value])
        assert test.dance() == 'мальчик Алеша - танцует хип-хоп'

    def test_electro(self):
        """
        Тестируем абстрактный метод dance, для персонажа, который танцует электро
        :return:
        """
        test = person.ElectroDance(name='Настя', sex='девочка', skills=[DanceType.ELECTRO.value])
        assert test.dance() == 'девочка Настя - танцует электро'
