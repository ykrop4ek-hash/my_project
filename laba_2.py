from collections import Counter
import random
import string


def table():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i * j, end='\t')
        print()


def sum_nech_1_to_100():
    s = 0
    for x in range(1, 101):
        if x % 2 == 1:
            s += x
    return s


def deliteli(n):
    d = []
    for i in range(1, n + 1):
        if n % i == 0:
            d.append(i)
    return d


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


# table()
# print('Таблица умножения от 1 до 9')

# print('Сумма нечётных от 1 до 100:', sum_nech_1_to_100())

# n = int(input('Введите число для делителей: '))
# print('Делители:', deliteli(n))

# n_fact = int(input('Введите число для факториала: '))
# print('Факториал:', factorial(n_fact))

# n_fib = int(input('Введите длину последовательности Фибоначчи: '))
# print('Фибоначчи:', fibonacci_sequence(n_fib))


def chet_elem(nums):
    n = []
    for x in nums:
        if x % 2 == 0:
            n.append(x)
    print('Чётные элементы:', n)


def max_min(nums):
    return max(nums), min(nums)


def input_and_sort():
    user_nums = []
    for i in range(5):
        n = int(input('Введите число: '))
        user_nums.append(n)
    user_nums.sort()
    print('Отсортированный список:', user_nums)


def remove_duplicates(nums):
    unique = []
    for x in nums:
        if x not in unique:
            unique.append(x)
    return unique


def reverse(nums):
    if len(nums) > 1:
        nums[0], nums[-1] = nums[-1], nums[0]
    return nums


numbers = [random.randint(-50, 50) for _ in range(10)]


# print('Исходный список:', numbers)
# chet_elem(numbers)

# maximum, minimum = max_min(numbers)
# print('Исходный список:', numbers)
# print(f'Максимум: {maximum}, минимум: {minimum}')

# input_and_sort()

# unique_nums = remove_duplicates(numbers)
# print('Исходный список:', numbers)
# print('Список без дубликатов:', unique_nums)

# print('Исходный список:', numbers)
# chi = reverse(numbers)
# print('После замены первого и последнего элемента:', chi)


def average_score(students_scores):
    s = sum(students_scores.values())
    count = len(students_scores)
    average = s / count
    print(f'Средний балл: {average:.2f}')


def count_letters():
    text = input('Введите строку: ')
    letter_counts = {}
    for ch in text:
        if ch.isalpha():
            letter_counts[ch] = letter_counts.get(ch, 0) + 1
    return letter_counts


def squares_dict():
    s = {i: i ** 2
         for i in range(1, 11)}
    return s


def from_lists(keys, values):
    return dict(zip(keys, values))


# students = {'Иван': 85, 'Мария': 90, 'Саша': 78, 'Костя': 56, 'Елена': 88}
# average_score(students)

# counts = count_letters()
# print('Количество букв:', counts)

# sq = squares_dict()
# print('Квадраты чисел:', sq)

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# d = from_lists(keys, values)
# print('Словарь из списков:', d)

def per_ob():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    per = set1 & set2
    ob = set1 | set2
    print('Пересечение:', per)
    print('Объединение:', ob)


def unique_words():
    text = input('Введите текст: ')
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    words = clean_text.lower().split()
    unique = set(words)
    print('Уникальные слова:', unique)


def per_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    per = set1 & set2
    print('Общие элементы:', per)


def mn_in_mn(mn1, mn2):
    result = mn1.issubset(mn2)
    if result == True:
        print(f'Множество {mn1} является подмножеством {mn2}')
    else:
        print(f'Множество {mn1} не является подмножеством {mn2}')


def remove_less_than(s, threshold):
    otfiltrovan = set()
    for x in s:
        if x > threshold:
            otfiltrovan.add(x)
    print(f'Множество после удаления элементов меньше {threshold}:', otfiltrovan)


# per_ob()

# unique_words()

# per_elements([1, 2, 3, 4], [3, 4, 5, 6])

# mn_in_mn({1, 2}, {1, 2, 3, 4})

# remove_less_than({1, 5, 7, 2, 0, 9}, 5)


def unique_random_numbers():
    nums = [random.randint(1, 100) for _ in range(20)]
    unique_nums = set(nums)
    print('Список:', nums)
    print('Уникальные значения:', unique_nums)


def count_repetitions():
    lst = [20, 54, 21, 20, 87, -2]
    counts = {}
    for x in lst:
        counts[x] = counts.get(x, 0) + 1
    print('Исходный список:', lst)
    print('Количество повторений:', counts)


def long_words_set(words):
    long_words = set()
    for i in words:
        if len(i) > 5:
            long_words.add(i)
    print('Слова длиной > 5:', long_words)


def word_occurrences():
    text = input('Введите предложение: ')
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    words = clean_text.lower().split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    print('Вхождения слов:', counts)


def remove_duplicates(lst):
    unique_list = list(set(lst))
    print('Исходный список:', lst)
    print('Список без дубликатов:', unique_list)


def most_expensive_product(products):
    max_price = max(products.values())
    for product, price in products.items():
        if price == max_price:
            print(f'Самый дорогой товар: {product} с ценой {price}')


def repeated_names(names):
    counts = Counter(names)
    # print(counts)
    repeated = set()
    for name, count in counts.items():
        if count > 1:
            repeated.add(name)
    most_common = counts.most_common(1)[0][0]
    print('Повторяющиеся имена:', repeated)
    print('Имя с наибольшей частотой:', most_common)


def char_first_index():
    text = input('Введите строку: ')
    char_indices = {}
    for i, ch in enumerate(text):
        if ch not in char_indices:
            char_indices[ch] = i
    print('Индексы первых вхождений символов:', char_indices)

# unique_random_numbers()

# count_repetitions()

# words = ['apple', 'banana', 'cherry', 'blueberry', 'kiwi', 'peach', 'grapes']
# long_words_set(words)

# word_occurrences()

# remove_duplicates([1,2,2,3,4,4,5])

# products = {'Хлеб': 28, 'Молоко': 150, 'Яблоки': 70, 'Булочка Гата': 30, 'Сливочное масло': 400}
# most_expensive_product(products)

# names = ['Иван', 'Саша', 'Иван', 'Пётр', 'Саша', 'Костя', 'Саша']
# repeated_names(names)

# char_first_index()
