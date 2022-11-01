import random
from colorama import init, Fore

print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⡄⠄⠄⠄⠄⠄⣠⠄⠄⠄⠄⢀⠄⠄⠄')
print('⠄⠄⠄⠄⠄⠄⠄⢠⠄⢀⠄⠄⠄⠄⢸⣷⢀⡆⠄⠄⣰⣿⣼⠄⠄⣰⡏⠄⠄⡀')
print('⠄⠄⠄⠄⠄⠄⠄⠄⢷⡜⣆⠄⠄⠄⢸⣿⣾⣿⠄⣠⣿⣿⣿⠄⣰⣿⠄⣠⠎⠄')
print('⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣿⣆⠄⠄⢸⣿⣿⣿⣰⣿⣿⣿⡇⣰⣿⢣⣾⠃⠄⠄')
print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣷⣄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄')
print('⠄⠒⢤⣠⣀⠄⠄⠄⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄')
print('⠄⠄⠄⠙⠿⣿⣷⣦⣄⣀⢻⣿⠿⠛⠋⠉⠄⠄⠄⠄⠈⠉⠛⠿⣿⡟⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⡿⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠁⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠄⠄⠄⠈⢙⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
print('⠐⠒⠶⣶⣶⣶⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⠾⠗⠄⠄')
print('⠄⠄⠄⠄⠄⠉⠙⠛⣿⡇⠄⠄⠄⠄⣤⣤⠄⠄⠄⠄⠄⠄⠄⠠⣽⡟⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠄⢀⣴⣿⣿⣧⠄⠄⠄⠈⠰⠟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⢀⣠⡄')
print('⠄⠄⢀⣠⣾⣿⣿⣿⢿⣿⣆⠄⠄⠄⣦⣀⣀⣤⠄⠄⠄⠄⠄⠄⢠⣾⣿⣉⡋⠄')
print('⠄⠖⢋⠵⠟⠋⠁⣰⣿⣿⣿⣆⠄⠄⠘⣿⣿⣿⠄⠄⠄⠄⠄⠄⠈⠄⠈⣉⡷⠄')
print('⠄⠄⠄⠄⠄⠄⣴⣿⠿⠋⢸⣿⠄⠄⠄⠈⠻⠿⠄⣀⣤⣀⣀⠄⠄⠄⠈⠛⠇⠄')
print('⠄⠄⠄⠄⢀⡼⠛⠁⠄⠄⣼⠏⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣷⡶⠶⠾⠋⠄')
print('⠄⠄⠄⠄⠈⠄⠄⠄⠄⠼⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠁⠄⠄⠄⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
print('⠄⠄⠄⢰⡀⡀⢀⣠⠤⠖⠒⢶⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄')
print('⠄⠄⠄⣸⣷⠚⠉⠁⠄⢀⣴⡿⠁⠄⠄⠄⠄⠄⠄⢠⠄⠄⢀⠄⣿⡄⠄⠄⠄⠄')
print('⠠⠢⠊⢿⡇⠄⠄⣄⣼⠿⠋⠄⢠⣦⠄⠄⠄⡷⠄⣽⠂⢠⡟⠄⠈⢀⣠⣤⡀⠄')
print('⠄⠄⠄⣼⣗⣠⠞⠋⠄⠄⠄⠄⠈⣿⣆⠄⠄⣿⠄⣿⣠⣿⠃⠄⢰⣟⡉⠄⠄⠄')
print('⠄⠄⠄⣿⡟⠁⢸⡆⠄⠄⣾⠃⢸⡿⣯⡄⠄⡟⢐⣿⡿⡧⡀⠄⠄⠉⠛⢷⣄⠄')
print('⠄⠄⠄⣿⡇⠄⣾⡇⠄⢀⣿⠄⢸⡿⠸⣇⢰⡧⢸⣿⠇⢣⢡⠄⠄⠄⠄⠈⣿⡆')
print('⠄⠄⠄⣿⡇⠄⢸⡇⠄⣼⡿⠄⢸⡧⠄⢻⣼⡟⢸⣿⠄⠄⢿⣇⠄⣠⠄⠄⣿⣷')
print('⠄⠄⠄⣿⡇⠄⢸⡇⣼⣿⠃⠄⠾⡇⠄⠘⣿⡇⢸⣿⠄⠄⢸⣿⠄⣿⣾⣄⣿⡟')
print('⠄⠄⠄⠻⠄⠄⠈⠛⠉⠁⣶⠄⠄⣾⡆⠄⢉⡀⠈⠁⢰⡀⠸⠿⠇⠈⠻⠿⠟⠁')
print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣧⠄⣿⣧⢠⣿⣧⣌⠉⢻⡟⠛⠛⠄⠄⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠹⣧⣿⡿⢸⣿⠈⢻⣷⢻⡇⠄⠄⠄⠄⠄⠄⠄⠄')
print('⠄⠄⢀⠄⠄⠄⠄⠄⠄⢰⣿⠄⠹⣿⡇⢸⣿⣤⣾⠃⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄')
print('⠄⠄⠸⣧⣤⣤⣤⡀⠄⠈⣛⣀⣀⣛⠃⠄⢍⠉⡁⠄⠚⠃⢀⣤⣤⣤⣤⣄⠄⠄')
print('⠄⣰⢾⡏⠄⠄⠈⢻⣦⠄⣿⡏⠛⠉⠄⠄⠘⣿⡇⠄⠄⠐⠛⢻⡏⠉⠉⠻⣷⡀')
print('⠚⠁⢸⣿⠄⠄⠄⠄⢻⡄⣿⡷⠶⣤⠄⠄⢀⣿⣇⠄⠄⠄⠄⢸⣷⠄⠄⠄⠹⡇')
print('⠄⠄⢸⣿⠄⠄⠄⢀⣾⠇⣿⡇⠄⠄⠄⢀⣾⠃⣻⣆⠄⠄⠄⢸⣿⠄⠄⠄⢀⡿')
print('⠄⠄⢸⣿⠄⣀⣤⣾⡟⠄⣿⡇⠄⠄⠄⣼⡿⠛⠛⣿⡀⠄⠄⣾⡏⠄⠄⠄⣸⡇')
print('⠄⣠⣼⣿⡿⠿⠛⠉⠄⠄⣿⣇⣀⠄⣸⣿⠄⠄⠄⢹⣧⠄⠄⣿⡇⣀⣠⣼⠏⠄')
print('⠸⠟⠉⠁⠄⠄⠄⠄⠄⠄⠛⠛⠛⠄⠛⠃⠄⠄⠄⠈⠻⠂⡾⠿⠿⠟⠋⠄⠄⠄')
print(' ')

coun = int(input())

print(' ')
print(Fore.LIGHTCYAN_EX + '______________________________')
print(Fore.WHITE)
print(' ')


def OpenFile(file, file_list):

        with open(file, 'r', encoding = 'utf-8') as filehandle:
                file_list = [current_file_list.rstrip() for current_file_list in filehandle.readlines()]
                #print(file_list)

        return(file_list)

def Some_filter(some_list):
        
        some_list_id = random.randint(0, len(some_list)-1)

        if some_list[some_list_id] == None:
                while some_list[some_list_id] == None:
                        some_list_id = random.randint(0, len(some_list)-1)
                 
        return(some_list_id)


health = OpenFile('health.txt', [])
job = OpenFile('job.txt', [])
phobia = OpenFile('phobia.txt', [])
hobby = OpenFile('hobby.txt', [])
bag = OpenFile('bag.txt', [])
move_card = OpenFile('move_card.txt', [])
trait = OpenFile('trait.txt', [])
more_info = OpenFile('more_info.txt', [])
crash = OpenFile('crash.txt', [])


crash_id = random.randint(0, len(crash)-1)
crash_pop = random.randint(1, 9) * 5
crash_effects = random.randint(9, 19) *5
print(Fore.MAGENTA + 'Катастрофа: ' + crash[crash_id])
print(' ')
print(Fore.MAGENTA + 'Остаток выжившего населения: ' + str(crash_pop))
print(Fore.MAGENTA + 'Разрушения на поверхности: ' + str(crash_effects))
print(' ')
print(Fore.WHITE)


for i in range(coun):
        
        print(Fore.RED + 'Игрок №', i+1)
        print(Fore.WHITE)
        print(' ')

        age = random.randint(18, 80)
        print('Возраст: ' + str(age))


        sex = random.randint(0, 1)
        if sex == 1:
                sex = 'Мужчина'
        else:
                sex = 'Женщина'
        print('Пол: ' + sex)


        child_free_id = random.randint(1, 10)
        if (1 <= child_free_id <= 3) or (age >= 46 and sex == 'Женщина'):
                child_free = 'Не может иметь детей'
        else:
                child_free = 'Может иметь детей'
        print('Способность к деторождению: ' + child_free)


        job_id = Some_filter(job)
        print('Профессия: ' + job[job_id])
        job[job_id] = None

        xp_job = random.randint(0, age-18)

        if xp_job == 0:
                xp_job = None
                print('Только начал(')
        else:
                print('Опыт работы:', xp_job, 'лет(год(а))' )


        health_id = Some_filter(health)
        print('Состояние здоровья: ' + health[health_id])
        health[health_id] = None

        step_health = random.randint(1, 10) * 10
        print(step_health, '%')
        #print(health_id)


        phobia_id = Some_filter(phobia)
        print('Фобия: ' + phobia[phobia_id])
        phobia[phobia_id] = None

        if phobia_id != 0:
                step_phobia = random.randint(1, 10) * 10
                print(step_phobia, '%')
        #print(phobia_id)


        hobby_id = Some_filter(hobby)
        print('Хобби: ' + hobby[hobby_id])
        my_hobby = hobby[hobby_id]
        hobby[hobby_id] = None

        xp_hobby = random.randint(0, age-10)

        if xp_hobby == 0:
                xp_hobby = None
                print('Только начал(')
        else: 
                print('Занимается', my_hobby +':', xp_hobby, 'лет(год(а))' )


        bag_id = Some_filter(bag)
        print('В багаже: ' + bag[bag_id])
        bag[bag_id] = None
        

        trait_id = Some_filter(trait)
        print('Человеческая черта: ' + trait[trait_id])
        trait[trait_id] = None


        more_info_id = Some_filter(more_info)
        print('Дополнительная информация: ' + more_info[more_info_id])
        more_info[more_info_id] = None


        for j in range(2):

                move_card_id = Some_filter(move_card)
                print('Карта действия', str(j + 1) + ': ' + move_card[move_card_id])
                move_card[move_card_id] = None

        print(' ')
        print(Fore.LIGHTCYAN_EX + '______________________________')
        print(Fore.WHITE)
        print(' ')
print('███████████████████████████████▄██')
print('█▄─▄─█▄─▄▄─█─▄─█▄─▄─█▄─▄─█─█─█─█─█')
print('██─████─▄█▀█─█─██─▄▄██─███─█─█─█─█')
print('▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀')