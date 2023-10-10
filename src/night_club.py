from enum import Enum, unique


@unique
class DanceType(Enum):
    RNB = "rnb"
    HOUSE = "house"
    POP = "pop"
    ELECTRO = "electro"
    HIPHOP = "hip-hop"


@unique
class MusicType(Enum):
    rnb = ["rnb", "hip-hop"]
    electrohouse = ["electro", "house"]
    pop = ["pop"]


class NightClub:
    def __init__(self):
        self.people = []

    def add_person(self, person: object) -> None:
        """
        Эмулируем вход в клуб персонажей
        :param person:
        :return None:
        """
        self.people.append(person)

    def play_music(self, song: object) -> None:
        """
        метод, который моделирует ночной клуб, в зависимости от музыки персонажи выполняют некоторые действия: танцуют или пьют
        :param song:
        :return None:
        """
        print(f"Сейчас играет {song.name}!")
        for person in self.people:
            if len(list(set(song.value) & set(person.get_skills()))) != 0:
                print(person.dance())
            else:
                print(person.drink())
