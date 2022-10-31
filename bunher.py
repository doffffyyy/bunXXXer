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

with open('move_card.txt', 'r', encoding = 'utf-8') as filehandle:
        move_cards = [current_move_cards.rstrip() for current_move_cards in filehandle.readlines()]
        #print(move_cards)

with open('job.txt', 'r', encoding = 'utf-8') as filehandle:
        job = [current_job.rstrip() for current_job in filehandle.readlines()]
        #print(job)

with open('health.txt', 'r', encoding = 'utf-8') as filehandle:
        health = [current_health.rstrip() for current_health in filehandle.readlines()]
        #print(health)

with open('phobia.txt', 'r', encoding = 'utf-8') as filehandle:
        phobia = [current_phobia.rstrip() for current_phobia in filehandle.readlines()]
        #print(phobia)

with open('hobby.txt', 'r', encoding = 'utf-8') as filehandle:
        hobby = [current_hobby.rstrip() for current_hobby in filehandle.readlines()]
        #print(hobby)

with open('bag.txt', 'r', encoding = 'utf-8') as filehandle:
        bag = [current_bag.rstrip() for current_bag in filehandle.readlines()]
        #print(bag)

with open('trait.txt', 'r', encoding = 'utf-8') as filehandle:
        trait = [current_trait.rstrip() for current_trait in filehandle.readlines()]
        #print(trait)

with open('more_info.txt', 'r', encoding = 'utf-8') as filehandle:
        more_info = [current_more_info.rstrip() for current_more_info in filehandle.readlines()]
        #print(more_info)

with open('crash.txt', 'r', encoding = 'utf-8') as filehandle:
        crash = [current_crash.rstrip() for current_crash in filehandle.readlines()]
        #print(crash)
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


        job_id = random.randint(0, len(job)-1)
        #print(job_id)

        if job[job_id] == None:
                while job[job_id] == None:
                        job_id = random.randint(0, len(job)-1)
                print('Профессия: ' + job[job_id])
                job[job_id] = None
        else:
                print('Профессия: ' + job[job_id])
                job[job_id] = None

        xp_job = random.randint(0, age-18)

        if xp_job == 0:
                xp_job = None
                print('Только начал(')
        else:
                print('Опыт работы:', xp_job, 'лет(год(а))' )


        health_id = random.randint(0, len(health)-1)
        
        if health[health_id] == None:
                while health[health_id] == None:
                        health_id = random.randint(0, len(health)-1)
                print('Состояние здоровья: ' + health[health_id])
                health[health_id] = None
        else:
                print('Состояние здоровья: ' + health[health_id])
                health[health_id] = None

        step_health = random.randint(1, 10) * 10
        print(step_health, '%')
        #print(health_id)


        phobia_id = random.randint(0, len(phobia)-1)

        if phobia[phobia_id] == None:
                while phobia[phobia_id] == None:
                        phobia_id = random.randint(0, len(phobia)-1)
                print('Фобия: ' + phobia[phobia_id])
                phobia[phobia_id] = None
        else:
                print('Фобия: ' + phobia[phobia_id])
                phobia[phobia_id] = None

        if phobia_id != 0:
                step_phobia = random.randint(1, 10) * 10
                print(step_phobia, '%')
        #print(phobia_id)


        hobby_id = random.randint(0, len(hobby)-1)

        if hobby[hobby_id] == None:
                while hobby[hobby_id] == None:
                        hobby_id = random.randint(0, len(hobby)-1)
                print('Хобби: ' + hobby[hobby_id])
                my_hobby = hobby[hobby_id]
                hobby[hobby_id] = None
        else:
                print('Хобби: ' + hobby[hobby_id])
                my_hobby = hobby[hobby_id]
                hobby[hobby_id] = None
        #print(hobby_id)

        xp_hobby = random.randint(0, age-10)

        if xp_hobby == 0:
                xp_hobby = None
                print('Только начал(')
        else: 
                print('Занимается', my_hobby +':', xp_hobby, 'лет(год(а))' )


        bag_id = random.randint(0, len(bag)-1)
    
        if bag[bag_id] == None:
                while bag[bag_id] == None:
                        bag_id = random.randint(0, len(bag)-1)
                print('В багаже: ' + bag[bag_id])
                bag[bag_id] = None
        else:
                print('В багаже: ' + bag[bag_id])
                bag[bag_id] = None
        #print(bag_id)

        
        trait_id = random.randint(0, len(trait)-1)
        
        if trait[trait_id] == None:
                while trait[trait_id] == None:
                        trait_id = random.randint(0, len(trait)-1)
                print('Человеческая черта: ' + trait[trait_id])
                trait[trait_id] = None
        else:
                print('Человеческая черта: ' + trait[trait_id])
                trait[trait_id] = None
        #print(trait_id)


        more_info_id = random.randint(0, len(more_info)-1)

        if more_info[more_info_id] == None:
                while more_info[more_info_id] == None:
                        more_info_id = random.randint(0, len(more_info)-1)
                print('Дополнительная информация: ' + more_info[more_info_id])
        else:
                print('Дополнительная информация: ' + more_info[more_info_id])
                more_info[more_info_id] = None
        #print(trait_id)


        '''move_cards_id = random.randint(0, len(move_cards)-1)
        print(move_cards[move_cards_id])
        #print(move_cards_id)
        
        move_cards[move_cards_id] = None'''
        for j in range(2):

                move_cards_id = random.randint(0, len(move_cards)-1)

                if move_cards[move_cards_id] == None:
                        while move_cards[move_cards_id] == None:
                                move_cards_id = random.randint(0, len(move_cards)-1)
                        print('Карта действия', str(j + 1) + ': ' + move_cards[move_cards_id])
                        move_cards[move_cards_id] = None
                else:
                        print('Карта действия', str(j + 1) + ': ' + move_cards[move_cards_id])
                        move_cards[move_cards_id] = None

        print(' ')
        print(Fore.LIGHTCYAN_EX + '______________________________')
        print(Fore.WHITE)
        print(' ')
print('███████████████████████████████▄██')
print('█▄─▄─█▄─▄▄─█─▄─█▄─▄─█▄─▄─█─█─█─█─█')
print('██─████─▄█▀█─█─██─▄▄██─███─█─█─█─█')
print('▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀')