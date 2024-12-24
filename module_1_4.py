greeting = ("Привет! Я очень хочу с Вами познакомиться! Меня зовут ROBBI.")
print(greeting)
name = input('А как Вас зовут? - ')
surname = input("А как Ваша фамилия? - ")
name_surname = name + " " + surname
print("Ооооо, в Вашем имени целых", len(name),", а в фамилии целых", len(surname),"симолов! Это круто!")
print("Я очень, очень рад, ", name_surname.upper(), "что мы познакомились!!!")
current_year = 2024
date_of_birth = input("В каком году Вы родились? - ")
age = current_year - int(date_of_birth)
print("Так Вы совсем еще молоды, хоть вам уже и целых ", age, "лет!!! Круто!!!")
print("Смотрите, как Ваши имя и фамилия будут выглядеть в нижнем регистре:", name_surname.lower())
print('А теперь в верхнем регистре:', name_surname.upper())
print("А если, вдруг, Вам интересно посмотреть мое приветствие без пробелов, то вот:", greeting.replace(' ',''))
print("Выводим первый символ строки -", greeting[0])
print("Выводим предпоследний символ строки -", greeting[-2])
print(greeting.replace('Привет! Я очень хочу с Вами познакомиться! Меня зовут ROBBI.','Ну все, пока! До новых встреч!'))

