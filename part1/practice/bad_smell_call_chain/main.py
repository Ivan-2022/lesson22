# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, city: str, street: str, room: int):
        self.city = city
        self.street = street
        self.room = room

    def get_person_room(self):
        return self.room

    def get_room_street(self):
        return self.street

    def get_city_population(self):
        return self.city


# person = Person('Chita', 'Lenina str', 1)
# print(person.get_city_population())
# print(person.get_room_street())
# print(person.get_person_room())
