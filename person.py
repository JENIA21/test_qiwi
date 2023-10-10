from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, sex: str, hip_hop_skill: bool, electro_skill: bool, pop_skill: bool,
                 house_skill: bool, rnb_skill: bool):
        self._name = name
        self._sex = sex
        self._rnb_skill = rnb_skill
        self._hip_hop_skill = hip_hop_skill
        self._electro_skill = electro_skill
        self._pop_skill = pop_skill
        self._house_skill = house_skill

    def get_name(self) -> str:
        return self._name

    def get_sex(self) -> str:
        return self._sex

    def get_rnb_skill(self) -> bool:
        return self._rnb_skill

    def get_hip_hop_skill(self) -> bool:
        return self._hip_hop_skill

    def get_electro_skill(self) -> bool:
        return self._electro_skill

    def get_pop_skill(self) -> bool:
        return self._pop_skill

    def get_house_skill(self) -> bool:
        return self._house_skill

    def drink(self) -> str:
        return f'{self._sex} {self._name} - пьет водку в баре'

    @abstractmethod
    def dance(self) -> None:
        pass


class RnbDance(Person):
    def dance(self) -> str:
        return f'{self._sex} {self._name} - танцует рнб'


class HipHopDance(Person):
    def dance(self) -> str:
        return f'{self._sex} {self._name} - танцует хип-хоп'


class ElectroDance(Person):
    def dance(self) -> str:
        return f'{self._sex} {self._name} - танцует электро'


class PopDance(Person):
    def dance(self) -> str:
        return f'{self._sex} {self._name} - танцует под поп-музыку'


class HouseDance(Person):
    def dance(self) -> str:
        return f'{self._sex} {self._name} - танцует хаус'
