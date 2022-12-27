portion = int(input("Укажите на какое количество порций расчитано: "))
your_portion = int(input("Укажите сколько порций вы хотите: "))
ingridients = int(input("Укажите количество ингридиентов для граммов: "))
pcs = int(input("Укажите количество ингридиентов для штук: "))

lst_ingridients_weight={}
ing_pcs = {}

while ingridients > 0:

    name = input("Введите название весового ингридиента: ")
    number = input(f'Укажите количество в граммах для ингридиента {name.upper()}: ')
    number = int(number) / int(portion) * int(your_portion)
    lst_ingridients_weight[name] = number
    ingridients = int(ingridients) - 1

while pcs > 0:

    name = input("Введите название штучного ингридиента: ")
    number = input(f'Укажите количество в штуках для ингридиента {name.upper()}: ')
    number = int(number) / int(portion) * int(your_portion)
    ing_pcs[name] = number
    pcs = int(pcs) - 1


print('\n')
for ingridient, quantity in lst_ingridients_weight.items():
    print(f"{ingridient} - грамм для ингридента {quantity}")

for name, pcs in ing_pcs.items():
    print('{} - {:.2F} шт'.format(name, pcs))


