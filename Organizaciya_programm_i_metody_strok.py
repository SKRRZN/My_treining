
print('Привет! Я робот, с которым можно обсудить повышение вашей зарплаты.')
name = input('Давайте познакомимся. Как Вас зовут?: ')
surname = input("А как Ваша фамилия?: ")
post = input("На какой должности вы работаете?: ")
print("Ну привет, привет, лучший в мире", post.upper(), name.upper(), surname.upper(),".", "Давайте поговорим.")
year = 2024
while True:
    try:
        salary_2024 = int(input("Какой оклад у Вас был в 2024 году? (укажите сумму в рублях): "))
    except ValueError:
        print("Не бесите меня и введите только цифры!!! Иначе сниму баллы для повышения оклада!!!")
        continue
    else:
        break
while True:
    try:
        salary_2025 = int(input('Какой оклад Вы хотели бы в 2025 году? (укажите сумму в рублях): '))
    except ValueError:
        print("Очень прошу ввести только цифры! С Вас снимается балл для повышения!!!")
        continue
    else:
        break
salary_2024_2025 = salary_2025 - salary_2024
print("Нихерррра себе!!!! Это ж больше на целых", salary_2024_2025, "рублей" "!" ,"Да Вы издеваетесь что ли???!!!")
while True:
    try:
        work_experience = int(input("Я в шоке конечно, но ладно.... А в каком году Вы пришли к нам работать?: "))
    except ValueError:
        print("Снова за свое??? ЦИФРЫ БЛИН ВВЕДИ!!! Штраф 500 рублей!!!")
        continue
    else:
        break
experience = year - int(work_experience)
print("Угу..... Т.е. Вы работаете у нас уже почти, мммммм, ", experience, "лет. Хм.....")
print("Я подумал, и боюсь что смогу поднять вам всего на 500 руб, т.е. на один штраф.")
print("Если хотите больше - обратитесь к Сергею Анатольевичу.")
survey = input("Вы довольны общением со мной? (да/нет)?:" )
print("Да хотя, в принципе, пофиг.")
print("Не скажу что рад был познакомиться. До свидания.")
input('')




