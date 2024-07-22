# Задача "Developer - не только разработчик":
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if self.number_of_floors >= new_floor:
                print(i)
            else:
                print("Такого этажа не существует")
                break


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print('----------')
h1.go_to(5)
print('----------')
h2.go_to(10)


