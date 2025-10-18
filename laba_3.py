# Создание списка квадратов чисел от 1 до 10
squares = [x**2 for x in range(1, 11)]
# print(squares)

#создание списка только четных чисел из диапазона от 1 до 20

honest = [x for x in range(0,20,2)][1::]
# print(honest)

words = ["python", "Java", "c++", "Rust", "go"]
up_words = [w.upper() for w in words if len(w) > 3]
# print(up_words)

class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        current = self.n
        while current >= 1:
            yield current
            current -= 1


# Пример использования
for x in Countdown(5):
    print(x)