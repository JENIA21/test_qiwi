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

    def play_music(self, song: str) -> None:
        """
        метод, который моделирует ночной клуб, в зависимости от музыки персонажи выполняют некоторые действия: танцуют или пьют
        :param song:
        :return None:
        """
        print(f"Сейчас играет {song}!")
        for person in self.people:
            if song == "Rnb" and (person.get_rnb_skill() or person.get_hip_hop_skill()):
                print(person.dance())
            elif song == "Electrohouse" and (person.get_house_skill() or person.get_electro_skill()):
                print(person.dance())
            elif song == "Pop-music" and person.get_pop_skill():
                print(person.dance())
            else:
                print(person.drink())
