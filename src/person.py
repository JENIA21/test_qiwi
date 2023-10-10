from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, sex: str, skills: list):
        self._name = name
        self._sex = sex
        self._skills = skills

    def get_name(self) -> str:
        return self._name

    def get_sex(self) -> str:
        return self._sex

    def get_skills(self) -> list:
        return self._skills

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
