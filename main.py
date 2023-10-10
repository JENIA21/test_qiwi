import person
from night_club import NightClub

test = person.PopDance('Никита', 'мальчик', False, False, True, False, False)
test_one = person.RnbDance('Настя', 'девочка', False, False, False, False, True)
test_two = person.PopDance('Женя', 'мальчик', False, False, True, False, False)

club = NightClub()
club.add_person(test)
club.add_person(test_one)
club.add_person(test_two)

club.play_music("Rnb")
club.play_music("Electrohouse")
club.play_music("Pop-music")
