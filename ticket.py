a = int(input("Сколько билетов вы хотите приобрести?\n"))
tiq = range(0, a)
#  print(list(tiq)) # just checking what we've got
#  print(tiq[0] + tiq[1])  # just checking if they are integers
count_kids = 0  # counters for different ages
count_young = 0
count_full = 0
for i in tiq:
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        print("Вам повезло!!!\n(Наслаждайтесь всем бесплатно)")  # 'cause we're polite
        count_kids += 1
    if 18 < age < 25:
        print("Вам повезло!!!\n(Получили скидку - 400)")  # and we're still polite
        count_young += 1
    if age > 25:
        print("У вас МАКСИМАЛЬНЫЙ билет!!!\nКонечно за полную стоимость")
        count_full += 1
total = count_kids * 0 + count_young * 990 + count_full * 1390
#  print(total)  # just checking if sum works
if (count_kids + count_young + count_full) > 3:
    total = total - total//10
print("Ваша сумма: ", total)
print("Насладитесь конференцией в полной мере!")  # 'we still don't forget to be polite