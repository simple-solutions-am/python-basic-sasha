# Мит #7 · break, continue и функции · 14.11
# Решение пиши под условием и запускай. Что должно выйти - в комментариях.
# Нейросеть только объясняет, код пишешь сам.


# ===================== Блок 1. break и continue =====================

# --- Что выведет? Сначала прогноз, потом запуск ---
# 81
n = 1
while n < 50:
    n *= 3
print(n)
# б о т(каждое  с новой строки)
for ch in "бот-2026":
    if ch == "-":
        break
    print(ch)
# 1 2 4 5
for n in range(1, 7):
    if n % 3 == 0:
        continue
    print(n)

# Ловушка: прогноз пиши, но НЕ запускай - зависнет (остановит Ctrl + C)
# i = 0
# while i < 3:
#     if i == 1:
#         continue
#     print(i)
#     i += 1


# --- Задача 1. Матч ---
# Посчитай убийства и смерти: afk пропускаем (continue), на end матч закончен (break).
events = ["kill", "kill", "afk", "death", "kill", "afk", "end", "kill"]

kill = 0
death = 0
for e in events:
    if e == "kill":
        kill += 1
    elif e == "death":
        death += 1
    elif e == "end":
        break

try:
    kd = kill / death
except ZeroDivisionError:
    kd = float(kill)

print(f"Убийств: {kill}, Смертей: {death}, K/D: {kd}")
# Должно выйти:
# Убийств: 3, смертей: 1
# K/D: 3.0
# ⭐ Если смертей 0, K/D = убийствам, без ZeroDivisionError


# ===================== Блок 2. Функции =====================

# --- Что выведет? Сначала прогноз, потом запуск ---
def hello(name):
    print("Привет,", name)

x = hello("Нео")
print(x)


def double(n):
    return n * 2
    print("после return")

print(double(4))


def minus(a, b):
    return a - b

print(minus(10, 3), minus(3, 10))


def bonus(kills):
    if kills >= 3:
        return "серия!"

print(bonus(5), bonus(1))


# --- Задача 2. K/D ---
# Напиши функцию kd(kills, deaths). Она возвращает K/D. Смертей 0 - K/D равно убийствам.
# Напишешь - раскомментируй проверку:
# print(kd(3, 1))
# print(kd(7, 2))
# print(kd(5, 0))
def kd(kills, deaths):
    if deaths == 0:
        return kills
    else:
        return kills / deaths

print(kd(3, 1)
,kd(7, 2)
,kd(5, 0))

# Должно выйти:
# 3.0
# 3.5
# 5

# ⭐ rank(x) возвращает звание: меньше 1 - "Новичок", меньше 3 - "Боец", иначе "Легенда"
# print(rank(kd(1, 2)))  # Новичок
# print(rank(kd(4, 2)))  # Боец
# print(rank(kd(3, 1)))  # Легенда


# --- Задача 3. Прокачка в функцию (дома) ---
# Возьми свое решение «Прокачки» из Спринта 5 и оберни в функцию level_from_xp(xp).
# Она возвращает уровень. Старт: уровень 1, на следующий нужно 100 опыта, дальше каждый раз вдвое больше.
# Напишешь - раскомментируй проверку:
# print(level_from_xp(1300))
# print(level_from_xp(100))
# print(level_from_xp(50))
def level_from_xp(xp):
    level = 1
    need = 100
    while xp >= need:
        xp -= need
        level += 1
        need *= 2
    return level

print(level_from_xp(1300))
print(level_from_xp(100))
print(level_from_xp(50))
# Должно выйти:
# 4
# 2
# 1
