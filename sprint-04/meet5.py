# Мит #5: практика. Пиши решение под каждой задачей и запускай файл.
# Вывод сверяй с примером символ в символ. Решенное не стирай: этот файл уйдет в твой PR.

print("--- Задача 1. Автобусы")
people = 47
seats = 12
if people % seats == 0:
    bus = int(people / seats)
    free_seats = 0
    print(f"Автобусов: {bus}, свободных мест: {free_seats}")
else:
    bus = (people // seats) + 1
    free_seats = (bus * seats) - people
    print(f"Автобусов: {bus}, свободных мест: {free_seats}")
# Сколько автобусов нужно, чтобы увезти всех, и сколько мест останется свободными?
# Подсказка: // и %, потом if people % seats:
# Должно выйти:
# Автобусов: 4, свободных мест: 1
# Проверь на people = 48: Автобусов: 4, свободных мест: 0
# ⭐ Сделай без if.


print("--- Задача 2. Команда бота")
hours = ""
minutes = ""
desc = []
msg = "    /remind 90 купить хлеб    "
strip_msg = msg.strip()
split_msg = strip_msg.split()
time = 0
if split_msg[0].startswith("/") != True:
    print("Это не команда")
else:
    for n in split_msg:
        if n.isdigit():
            time = int(n)
            hours, minutes = divmod(time, 60)
        else:
            desc.append(n)
    desc.pop(0)

description = " ".join(desc)
if time == 0:
    print("Время - числом")
else:
    print(f"Напомню через {hours} ч {minutes} мин: {description}")
# Разбери команду: strip, split, startswith, isdigit, join.
# Должно выйти:
# Напомню через 90 мин: купить хлеб
# Проверь на msg = "привет": Это не команда
# Проверь на msg = "/remind завтра хлеб": Время - числом
# ⭐ Время через divmod: Напомню через 1 ч 30 мин: купить хлеб
