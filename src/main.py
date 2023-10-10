import person
from night_club import NightClub, MusicType, DanceType


test = person.PopDance(name='Никита', sex='мальчик', skills=[DanceType.POP.value])
test_one = person.RnbDance(name='Настя', sex='девочка', skills=[DanceType.RNB.value])
test_two = person.PopDance(name='Женя', sex='мальчик', skills=[DanceType.POP.value])

club = NightClub()
club.add_person(person=test)
club.add_person(person=test_one)
club.add_person(person=test_two)

club.play_music(song=MusicType.rnb)
club.play_music(song=MusicType.electrohouse)
club.play_music(song=MusicType.pop)
