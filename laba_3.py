from decimal import Decimal, getcontext
from fractions import Fraction

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
# for x in Countdown(5):
#     print(x)

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Пример использования
# for num in fibonacci(5):
#     print(num)



def deposit_calculator():
    # Устанавливаем высокую точность вычислений
    getcontext().prec = 10

    # Ввод данных
    print("=== Финансовый калькулятор вкладов ===")

    initial_amount = Decimal(input("Введите начальную сумму вклада (руб.): "))
    interest_rate = Decimal(input("Введите годовую процентную ставку (%): "))
    years = Decimal(input("Введите срок вклада (лет): "))

    # Расчет по формуле ежемесячной капитализации
    # S = P * (1 + r/(12*100))^(12*t)

    monthly_rate = interest_rate / Decimal('12') / Decimal('100')
    months = years * Decimal('12')

    final_amount = initial_amount * (Decimal('1') + monthly_rate) ** months

    # Округляем до копеек (2 знака после запятой)
    final_amount = final_amount.quantize(Decimal('0.01'))
    profit = final_amount - initial_amount

    # Вывод результатов
    print("\n=== Результаты расчета ===")
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Годовая ставка: {interest_rate}%")
    print(f"Срок вклада: {years} лет")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")


# Запуск калькулятора
# if __name__ == "__main__":
#     deposit_calculator()


# Создание дробей
fraction1 = Fraction(3, 4)
fraction2 = Fraction(5, 6)

# Выполнение операций
addition = fraction1 + fraction2
subtraction = fraction1 - fraction2
multiplication = fraction1 * fraction2
division = fraction1 / fraction2

# Вывод результатов
print(f"Дробь 1: {fraction1}")
print(f"Дробь 2: {fraction2}")
print(f"Сложение: {fraction1} + {fraction2} = {addition}")
print(f"Вычитание: {fraction1} - {fraction2} = {subtraction}")
print(f"Умножение: {fraction1} * {fraction2} = {multiplication}")
print(f"Деление: {fraction1} / {fraction2} = {division}")