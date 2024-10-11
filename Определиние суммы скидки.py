# Напишите программу, которая вычисляет сумму скидки в зависимости от суммы продажи.


sell_ = round(float(input('Введите сумму продажи:')),2)


if sell_ in range(1, 5000+1):
    per = 5
elif sell_ in range(5000+1,15000+1):
    per = 12
elif sell_ in range(15000+1, 25000+1):
    per = 20
else:
    per = 30

discount_ = sell_ / 100 * per
print("Сумма скидки:", discount_)
new_sell = sell_ - discount_
print("Сумма с учётом скидки:", new_sell)

