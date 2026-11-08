

# ===================== Блок 1. for: повторяем =====================

# --- Что выведет? Сначала прогноз, потом запуск ---
print(list(range(10, 0, -3)))
# тевирп
word = ""
for ch in "привет":
    word = ch + word
print(word)
# спам, привет
stats = {"спам": 3, "привет": 5}
for key in stats:
    print(key)
# 3
for n in [1, 2, 3]:
    total = 0
    total += n
print(total)


# --- Задача 1. Донаты ---
# Посчитай общую сумму, сколько донатов больше нуля и самый большой донат с ником.
donations = [
    ("max", 100),
    ("lena", 0),
    ("kir", 500),
    ("max", 250),
    ("anon", 50),
]
amount = 0
summ = 0
for i, value in donations:
    summ += value
    if value != 0:
        amount += 1

best_don = None
best = None
for i, value in donations:
    if best is None or best < value:
        best = value
        best_don = i

print(f"Сумма:{summ} \n Донатов:{amount} \n Топ:{best_don} {best}")



# Должно выйти:
# Сумма: 900
# Донатов: 4
# Топ: kir 500
# ⭐ Средний донат без нулевых: 225.0


# --- Задача 2. Цензор ---
# Замени запрещенные слова на ***, посчитай замены. Новый список собирай отдельно.
banned = {"спам", "реклама"}
msgs = "купи спам и реклама тут спам"
msgs = msgs.split()
new_msg = []
count = 0
for msg in msgs:
    if msg.lower() in banned:
        new_msg.append("***")
        count += 1
    else:
        new_msg.append(msg)
new_msg = " ".join(new_msg)
print(new_msg)
print("Заменено:", count)

# Должно выйти:
# купи *** и *** тут ***
# Заменено: 3
# ⭐ msg = "Спам и РЕКЛАМА" -> *** и ***  (подсказка: lower())


# ===================== Блок 2. while, break, continue =====================

# --- Что выведет? Сначала прогноз, потом запуск ---
# 81
n = 1
while n < 50:
    n *= 3
print(n)
# б
# о
# т
for ch in "бот-2026":
    if ch == "-":
        break
    print(ch)

# 1
# 2
# 4
# 5
for n in range(1, 7):
    if n % 3 == 0:
        continue
    print(n)
# после единицы цикл зависнет,так как к i добавляется 1 только в конце итерации,а проверка идет до этого
# Ловушка: прогноз пиши, но НЕ запускай - зависнет (остановит Ctrl + C)
# i = 0
# while i < 3:
#     if i == 1:
#         continue
#     print(i)
#     i += 1


# --- Задача 3. Прокачка ---
# На каждый следующий уровень нужно вдвое больше опыта. Сколько раз повторится цикл - заранее не знаем.
xp = 1300
level = 1
need = 100
while xp >= need:
    xp -= need
    level += 1
    need *= 2

print("Уровень:", level)
print("Опыт:", xp,"/",need)
# Должно выйти:
# Уровень: 4
# Опыт: 600 / 800


# --- Задача 4. Матч ---
# Посчитай убийства и смерти: afk пропускаем (continue), на end матч закончен (break).
events = ["kill", "kill", "afk", "death", "kill", "afk", "end", "kill"]
kills = 0
deaths = 0
for event in events:
    if event == "kill":
        kills += 1
    elif event == "death":
        deaths += 1
print(f"Убийств: {kills}, смертей: {deaths}")
try:
    print("K/D:", kills/deaths)
except ZeroDivisionError:
    print("K/D:", kills)


# Должно выйти:
# Убийств: 3, смертей: 1
# K/D: 3.0
# ⭐ Если смертей 0, K/D = убийствам, без ZeroDivisionError


# ===================== Финал =====================

# --- Лайвкодинг. Игровой магазин (пишем вместе) ---
shop = {"меч": 300, "щит": 200, "зелье": 50}
gold = 500
bag = []
# Шаг 1. Меню: for по shop.items()
# Шаг 2. while True + input("Что купить? "), на /stop - break
# Шаг 3. Нет такого товара - "Нет в магазине" и continue
# Шаг 4. Не хватает золота - "Не хватает N золота" и continue, иначе покупка
# Шаг 5. После цикла: что в сумке и сколько золота
#
# Ввод: меч, лук, щит, зелье, /stop
# Должно выйти:
# Магазин:
#   меч - 300
#   щит - 200
#   зелье - 50
# Что купить? меч
# Куплено: меч, золота осталось: 200
# Что купить? лук
# Нет в магазине
# Что купить? щит
# Куплено: щит, золота осталось: 0
# Что купить? зелье
# Не хватает 50 золота
# Что купить? /stop
# В сумке: меч, щит
# Золото: 0


# --- Задача 5. Свободный ник (сам) ---
# Ник занят - пробуем shadow1, shadow2, ... пока не найдем свободный.
taken = {"shadow", "shadow1", "shadow2", "shadow4"}
nick = "shadow3"
if not nick in taken:
    print(nick)
else:
    new_nick = nick
    for i in range(1, 999):
        possible_nick = f"{nick}{i}"
        if possible_nick not in taken:
            new_nick = possible_nick
            break

    print(new_nick)

# Должно выйти:
# shadow3
# ⭐ nick = "neo" -> neo (цикл не выполнится ни разу)
