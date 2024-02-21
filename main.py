# Код написан 02.11.2023
# Автор: Кучук Милан Михайлович
print("\t\tПрограмма Кучук")
print("Кто твой папа\n")

family = {"MILAN": "MISHA"}
choice = None
while choice != 0:
    print("""
          Меню
          1 - Узнать кто отец
          2 - Добавить сына/отца
          3 - Изменить сына/отца
          4 - Удалть сына/отца  
        """)
    choice = int(input("Что вы хотите выбрать?\n"))

    if choice == 0:
        print("До свидания!")

    elif choice == 1:
        son = input("Введите имя сына\n")
        son = son.upper()
        if son in family:
            father = family[son]
            print("\n", son, "явился из смени", father)
        else:
            print("Это имя мне не знакомо")

    elif choice == 2:
        son = input("Введите имя ребнка\n")
        son = son.upper()
        if son not in family:
            father = input("Введите имя отца\n")
            father = father.upper()
            family[son] = father
            print("Новый сын/отец добавлен в список")
        else:
            print("Такое имя уже использовано")

    elif choice == 3:
        son = input("Введите имя ребенка, который хочет поменять своего отца\n")
        son = son.upper()
        if son in family:
            father = input("Введите имя нового отца\n")
            father = father.upper()
            family[son] = father
            print("Вы сменили отца")
        else:
            print("Такого имени не существует")

    elif choice == 4:
        son = input("Введите имя сына, вместе с отцом которого вы хотите умереть\n")
        son = son.upper()
        if son in family:
            del family[son]
            print("Семья была удалена")

    else:
        print("Возможно вы что-то сделали не так")