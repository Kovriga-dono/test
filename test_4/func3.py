def attack(target, attacker):
    def calculate_damage(damage, armor):
        return damage + armor


    player={'name': target, 'health': 100, 'damage': 50, 'armor': 1.2}
    enemy={'name': attacker, 'health': 80, 'damage': 30, 'armor': 1.2}
    calculated_damage = float(calculate_damage(int(enemy['damage']), float(player['armor'])))
    player['health'] -= calculated_damage
    return(f"{enemy['name']} атаковал {player['name']}! У {player['name']} осталось {player['health']} здоровья.")


player=input("Введите имя игрока: ")
enemy=input("Введите имя врага: ")
print(attack(player,enemy))


# Задача
# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. 
# Поэкспериментируйте с значениями урона и жизней по желанию. 
# Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. 
# Функция в качестве аргумента будет принимать атакующего и атакуемого. 
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.
