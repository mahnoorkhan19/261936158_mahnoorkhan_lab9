class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class House:
    def __init__(self, address, num_rooms):
        self.address = address
        self.num_rooms = num_rooms
        self.residents = []

    def add_resident(self, person):
        self.residents.append(person)

    def remove_resident(self, person):
        self.residents.remove(person)

    def print_residents(self):
        print(self.address)
        for resident in self.residents:
            print(resident.name,resident.age)

p1 = Person("Mahnoor", 77)
p2 = Person("Ayesha", 23)
p3 = Person("neha", 78)


house = House("fdttu", 2)
house.add_resident(p1)
house.add_resident(p2)
house.add_resident(p3)


house.print_residents()  

house.remove_resident(p2)
house.print_residents()  


    