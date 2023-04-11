
class Person:
    def __init__(self, city_population, person_room):
        self.city_population = city_population
        self.person_room = person_room

    def get_person_room(self):
        return self.person_room

    def get_city_population(self):
        return self.city_population


person = Person(100000, 34)

print(person.person_room)
print(person.city_population)
