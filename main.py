import person
from night_club import NightClub

test = person.PopDance(name='Никита', sex='мальчик', hip_hop_skill=False, electro_skill=False, pop_skill=True,
                       house_skill=False, rnb_skill=False)
test_one = person.RnbDance(name='Настя', sex='девочка', hip_hop_skill=False, electro_skill=False, pop_skill=False,
                           house_skill=False, rnb_skill=True)
test_two = person.PopDance(name='Женя', sex='мальчик', hip_hop_skill=False, electro_skill=False, pop_skill=True,
                           house_skill=False, rnb_skill=False)

club = NightClub()
club.add_person(person=test)
club.add_person(person=test_one)
club.add_person(person=test_two)

club.play_music(song="Rnb")
club.play_music(song="Electrohouse")
club.play_music(song="Pop-music")
