class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Transport is moving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"


class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Beep beep!")

    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")

    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"

    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented


class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")

    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type}"


# 4. Практика использования
print("=== Создание объектов ===")
transport1 = Transport("Generic", 60)
car1 = Car("Toyota", 120, 5)
car2 = Car("Honda", 110, 4)
bike1 = Bike("Giant", 25, "mountain")

print("\n=== Вывод объектов (__str__) ===")
print(transport1)
print(car1)
print(car2)
print(bike1)

print("\n=== Проверка методов move() и honk() ===")
transport1.move()
car1.move()
car1.honk()
bike1.move()

print("\n=== Использование len(car) ===")
print(f"Количество мест в {car1.brand}: {len(car1)}")

print("\n=== Сравнение двух машин (car1 == car2) ===")
print(f"{car1.brand} == {car2.brand}: {car1 == car2}")

print("\n=== Сложение скоростей двух машин (car1 + car2) ===")
print(f"Суммарная скорость {car1.brand} и {car2.brand}: {car1 + car2} km/h")

print("\n=== Сложение машины и велосипеда (car1 + bike1) ===")
try:
    result = car1 + bike1
    print(result)
except TypeError as e:
    print(f"Ошибка: {e}")
print("Объяснение: При сложении car1 + bike1 вызывается метод __add__ класса Car.")
print("Поскольку bike1 не является объектом Car, метод возвращает NotImplemented,")
print("что приводит к TypeError - неподдерживаемая операция для данных типов.")

# 5. Дополнительное задание
print("\n=== Дополнительное задание ===")
vehicles = [
    Transport("Generic", 50),
    Car("BMW", 180, 4),
    Car("Ford", 160, 5),
    Bike("Trek", 30, "road"),
    Bike("Specialized", 35, "mountain")
]

print("Вызов метода move() для всех объектов в списке:")
for vehicle in vehicles:
    vehicle.move()

print("\nПринцип ООП, который тут демонстрируется: ПОЛИМОРФИЗМ")
print("Разные объекты (Transport, Car, Bike) по-разному реагируют на один и тот же метод move()")