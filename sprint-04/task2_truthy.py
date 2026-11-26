
# Вывод:False False False False False
print(bool(0.0), bool(()), bool({}), bool(set()), bool(None))
# Вывод:True True True True
print(bool("None"), bool(-1), bool(" "), bool([[]]))
# Вывод: True True False False
print(not 0, not "", not "0", not [0])
# Вывод:False False True True
print(None == 0, None == "", None == None, None is None)
# Вывод [1,2,3], None
x = [1, 2]
y = x.append(3)
print(x, y)
# Вывод 0, None, None
d = {"a": 0}
print(d.get("a"), d.get("b"), d.get("b", "нет"))
# если ключ не находится,то возвращает второй аргумент
# вывод:пусто,5,нет,да
print("" or "пусто", 0 or 5, None or "нет", "да" or "нет")
# Выйдет ошибка,нельзя использовать логик операторы с  None
score = None
# print(score > 5)

score = 0
if score:
    print("Результат:", score)
else:
    print("Еще не играл")
# Правильный код:
# score = 0
# if not score is None:
#    print("Результат:", score)
# else:
#    print("Еще не играл")

# Если текст состоит из пробелов выводит Есть Текст,так как пробелы это не None,значит для пайтона там есть символы
text = "   "
if text:
    print("Есть текст")
else:
    print("Пусто")

# Правильный код:
#text = "      "
#text = text.strip()
#print(text)
#if text:
#    print("Есть текст")
#else:
#    print("Пусто")
