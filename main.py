
import telebot
from telebot import types
import os
from datetime import datetime

token = "TOKEN"

bot = telebot.TeleBot(token)

text = ""
OPD = False
get_text = False
right = False
Programming = False
deleteOPD = False
deleteProg = False
change_OPD = False
flag = True
change_Prog = False
change_Prog1 = False
take_time = False
change_OPD1 = False
change_Prog2 = False
change_OPD2 = False
change_queue = False
skip_OPD = False
skip_Prog = False
take_rights = False
get_rights = False
change_pos_Prog = False
mins_open = ""
hours_open = ""
change_pos_OPD = False
clear_OPD = False
clear_Prog = False
time_open = ""
time_close = ""
person_to_change = ""
person1 = ""
person2 = ""
queue_OPD = []
queue_Prog = []
counter = 1
students = [
    "Абиш Диана",
    "Бегинина Анастасия",
    "Беляков Дмитрий",
    "Виноградов Глеб",
    "Голиков Денис",
    "Дробыш Дмитрий",
    "Е Хэн",
    "Зотов Леонид",
    "Климович Вадим",
    "Линь Пэн",
    "Маракушев Михаил",
    "Назирджанов Некруз",
    "Новиков Егор",
    "Павлова Анастасия",
    "Пономарев Иван",
    "Рудык Ярослав",
    "Румский Александр",
    "Савелов Артем",
    "Скворцова Дарья",
    "Сосновцев Григорий",
    "Трофимченко Владислав",
    "Тюрин Иван"
]
id_getter = ""
getX = 0
Id_of_admins = ["Новиков Егор"]
BD_time = [
    datetime(2022, 4, 26, 21, 30, 0)
]


def get_time():
    Date = str(datetime.now()).split()
    date1 = Date[0].split("-")
    date2 = Date[1].split(":")
    seconds = date2[2].split(".")
    return datetime(int(date1[0]), int(date1[1]), int(date1[2]), int(date2[0]), int(date2[1]), int(seconds[0]))


def check_time():
    global BD_time
    if BD_time[0] < get_time():
        return True
    else:
        return False


def set_time(month1, day1, hour1, min1):
    global BD_time
    Date = str(datetime.now()).split()
    date1 = Date[0].split("-")
    BD_time[0] = datetime(int(date1[0]), int(day1), int(month1), int(hour1), int(min1))


def clear_queue():
    global clear_OPD, clear_Prog, queue_OPD, queue_Prog
    if clear_OPD:
        queue_OPD = []
    if clear_Prog:
        queue_Prog = []


def checker(string):
    Person_username = str(string)
    if Person_username == "791402882":
        return "Пономарев Иван"
    elif Person_username == "455577525":
        return "Савелов Артем"
    elif Person_username == "613659674":
        return "Павлова Анастасия"
    elif Person_username == "601555809":
        return "Климович Вадим"
    elif Person_username == "952621452":
        return "Тюрин Иван"
    elif Person_username == "838822912":
        return "Назирджанов Некруз"
    elif Person_username == "738821177":
        return "Рудык Ярослав"
    elif Person_username == "5029071602":
        return "Новиков Егор"
    elif Person_username == "481760825":
        return "Бегинина Анастасия"
    elif Person_username == "1841248342":
        return "Линь Пэн"
    elif Person_username == "418620498":
        return "Дробыш Дмитрий"
    elif Person_username == "617945082":
        return "Скворцова Дарья"
    elif Person_username == "549528518":
        return "Маракушев Михаил"
    elif Person_username == "809811685":
        return "Зотов Леонид"
    elif Person_username == "1812917030":
        return "Е Хэн"
    elif Person_username == "425184209":
        return "Румский Александр"
    elif Person_username == "403565141":
        return "Голиков Денис"
    elif Person_username == "303681142":
        return "Беляков Дмитрий"
    elif Person_username == "947814855":
        return "Сосновцев Григорий"
    elif Person_username == "883972940":
        return "Виноградов Глеб"
    elif Person_username == "444999728":
        return "Абиш Диана"
    elif Person_username == "1042684016":
        return "Трофимченко Владислав"
    elif Person_username == "1014846611":
        return "Абрабоу Ахмед Елсаид"


def get_Id(string):
    Person_username = string
    if Person_username == "Пономарев Иван":
        return "791402882"
    elif Person_username == "Савелов Артем":
        return "455577525"
    elif Person_username == "Павлова Анастасия":
        return "613659674"
    elif Person_username == "Климович Вадим":
        return "601555809"
    elif Person_username == "Тюрин Иван":
        return "952621452"
    elif Person_username == "Назирджанов Некруз":
        return "838822912"
    elif Person_username == "Рудык Ярослав":
        return "738821177"
    elif Person_username == "Новиков Егор":
        return "5029071602"
    elif Person_username == "Бегинина Анастасия":
        return "481760825"
    elif Person_username == "Линь Пэн":
        return "1841248342"
    elif Person_username == "Дробыш Дмитрий":
        return "418620498"
    elif Person_username == "Скворцова Дарья":
        return "617945082"
    elif Person_username == "Маракушев Михаил":
        return "549528518"
    elif Person_username == "Зотов Леонид":
        return "809811685"
    elif Person_username == "Е Хэн":
        return "1812917030"
    elif Person_username == "Румский Александр":
        return "425184209"
    elif Person_username == "Голиков Денис":
        return "403565141"
    elif Person_username == "Беляков Дмитрий":
        return "303681142"
    elif Person_username == "Сосновцев Григорий":
        return "947814855"
    elif Person_username == "Виноградов Глеб":
        return "883972940"
    elif Person_username == "Абиш Диана":
        return "444999728"
    elif Person_username == "Трофимченко Владислав":
        return "1042684016"
    elif Person_username == "Абрабоу Ахмед Елсаид":
        return "1014846611"


def datetime_to_string(date_time_str):
    return datetime.strptime(date_time_str, '%y-%m-%d %H:%M:%S')


def get_queue(saver, getter):
    global queue_OPD, queue_Prog, Id_of_admins, BD_time
    if getter:
        with open("SaveQueue.txt", "r", encoding='UTF-8') as file:
            if os.stat("SaveQueue.txt").st_size != 0:
                queue_OPD = file.readline().split()
                queue_OPD = [int(i) for i in queue_OPD]
                queue_Prog = file.readline().split()
                queue_Prog = [int(i) for i in queue_Prog]
                Id_of_admins = file.readline().split()
                Id_of_admins = [int(i) for i in Id_of_admins]
                for i in range(len(queue_OPD)):
                    queue_OPD[i] = checker(queue_OPD[i])
                for i in range(len(queue_Prog)):
                    queue_Prog[i] = checker(queue_Prog[i])
                for i in range(len(Id_of_admins)):
                    Id_of_admins[i] = checker(Id_of_admins[i])
    if saver:
        with open("SaveQueue.txt", "w", encoding='UTF-8') as file:
            for k in queue_OPD:
                file.write(str(get_Id(k)) + " ")
            file.write("\n")
            for k in queue_Prog:
                file.write(str(get_Id(k)) + " ")
            file.write("\n")
            for k in Id_of_admins:
                file.write(str(get_Id(k)) + " ")


def checker_pos(item):
    temp = []
    if change_pos_OPD:
        for i in range(item, len(queue_OPD)):
            temp.append(queue_OPD[i])
    if change_pos_Prog:
        for i in range(item, len(queue_Prog)):
            temp.append(queue_Prog[i])
    return temp


def delete_person_from_queue():
    temp = []
    for i in range(len(students)):
        if (students[i] not in queue_OPD) and OPD:
            temp.append(students[i])
        if (students[i] not in queue_Prog) and Programming:
            temp.append(students[i])
    return temp


def delete_person(message):
    global queue_OPD, queue_Prog, deleteOPD, deleteProg
    if deleteOPD:
        queue_OPD.remove(message.text)
        deleteOPD = False
    elif deleteProg:
        queue_Prog.remove(message.text)
        deleteProg = False


def change_position(message):
    global getX, change_Prog, change_OPD
    if change_Prog:
        getX -= 1
        First_Person = queue_Prog[getX]
        for i in range(len(queue_Prog)):
            if check_person(message) == queue_Prog[i]:
                queue_Prog[i] = First_Person
        queue_Prog[getX] = check_person(message)
        bot.send_message(message.chat.id,
                         "Готово! Вы поменялись местами в очереди по Программированию с " + check_person(message))

    if change_OPD:
        getX -= 1
        First_Person = queue_OPD[getX]
        for i in range(len(queue_OPD)):
            if check_person(message) == queue_OPD[i]:
                queue_OPD[i] = First_Person
        queue_OPD[getX] = check_person(message)
        bot.send_message(message.chat.id, "Готово! Вы поменялись местами в очереди по ОПД с " + check_person(message))


def skip_one_person(message):
    global skip_OPD, skip_Prog
    if skip_OPD:
        if len(queue_OPD) < 2:
            bot.send_message(message.chat.id, "В очереди меньше 2 человек, вы никого не можете пропустить :)")
        else:
            if check_person(message) in queue_OPD:
                for i in range(len(queue_OPD) - 1):
                    if check_person(message) == queue_OPD[i] and i + 1 != len(queue_OPD):
                        queue_OPD[i] = queue_OPD[i + 1]
                        queue_OPD[i + 1] = check_person(message)
                        bot.send_message(message.chat.id, "Вы успешно пропустили " + queue_OPD[i])
                        bot.send_message(int(get_Id(queue_OPD[i])), "Тебя пропустили в ОПД!")
                        break
                    elif i + 1 == len(queue_OPD):
                        bot.send_message(message.chat.id, "Вы последний в очереди!")
                        break
            else:
                bot.send_message(message.chat.id, "Вас нет в очереди по ОПД!")
    elif skip_Prog:
        if len(queue_Prog) < 2:
            bot.send_message(message.chat.id, "В очереди меньше 2 человек, вы никого не можете пропустить :)")
        else:
            if check_person(message) in queue_Prog:
                for i in range(len(queue_Prog) - 1):
                    if check_person(message) == queue_Prog[i] and i + 1 != len(queue_Prog):
                        queue_Prog[i] = queue_Prog[i + 1]
                        queue_Prog[i + 1] = check_person(message)
                        bot.send_message(message.chat.id, "Вы успешно пропустили " + queue_Prog[i])
                        bot.send_message(int(get_Id(queue_Prog[i])), "Тебя пропустили в программировании!")
                        break
                    elif i + 1 == len(queue_Prog):
                        bot.send_message(message.chat.id, "Вы последний в очереди!")
                        break
            else:
                bot.send_message(message.chat.id, "Вас нет в очереди по Програмированию!")


def get_Admin(message):
    global Id_of_admins
    Id_of_admins.append(message.text)
    bot.send_message(message.chat.id, "Готово! Ты выдал права " + message.text)


def take_Admin(message):
    global Id_of_admins
    Id_of_admins.remove(message.text)
    bot.send_message(message.chat.id, "Готово! Ты забрал права у " + message.text)


def change_person_position(person_1, person_2):
    global change_OPD2, change_Prog2, change_pos_OPD, change_Prog
    temp1 = temp2 = 0
    if change_pos_OPD:
        for i in range(len(queue_OPD)):
            if queue_OPD[i] == person_1:
                temp1 = i
            if queue_OPD[i] == person_2:
                temp2 = i
        queue_OPD[temp1] = person_2
        queue_OPD[temp2] = person_1
        bot.send_message(int(get_Id(person_2)), "Тебе " + person_1 + " отдал свое место в очереди по ОПД.")
    if change_OPD2:
        for i in range(len(queue_OPD)):
            if queue_OPD[i] == person_1:
                temp1 = i
            if queue_OPD[i] == person_2:
                temp2 = i
        queue_OPD[temp1] = person_2
        queue_OPD[temp2] = person_1
        bot.send_message(int(get_Id(person_2)), "Администратор поменял местами тебя и " + person_1 + " в очереди по ОПД")
        bot.send_message(int(get_Id(person_1)), "Администратор поменял местами тебя и " + person_2 + " в очереди по ОПД")

    if change_pos_Prog:
        for i in range(len(queue_Prog)):
            if queue_Prog[i] == person_1:
                temp1 = i
            elif queue_Prog[i] == person_2:
                temp2 = i
            queue_Prog[temp1] = person_2
            queue_Prog[temp2] = person_1
        bot.send_message(int(get_Id(person_2)), "Тебе " + person_1 + " отдал свое место в очереди по Программированию.")
    if change_Prog2:
        for i in range(len(queue_Prog)):
            if queue_Prog[i] == person_1:
                temp1 = i
            if queue_Prog[i] == person_2:
                temp2 = i
        queue_Prog[temp1] = person_2
        queue_Prog[temp2] = person_1
        bot.send_message(int(get_Id(person_2)),
                         "Администратор поменял местами тебя и " + person_1 + " в очереди по Программированию")
        bot.send_message(int(get_Id(person_1)),
                         "Администратор поменял местами тебя и " + person_2 + " в очереди по Программированию")


def check_person(message):
    Person_username = str(message.from_user.id)
    if Person_username == "791402882":
        return "Пономарев Иван"
    elif Person_username == "455577525":
        return "Савелов Артем"
    elif Person_username == "613659674":
        return "Павлова Анастасия"
    elif Person_username == "601555809":
        return "Климович Вадим"
    elif Person_username == "952621452":
        return "Тюрин Иван"
    elif Person_username == "838822912":
        return "Назирджанов Некруз"
    elif Person_username == "738821177":
        return "Рудык Ярослав"
    elif Person_username == "5029071602":
        return "Новиков Егор"
    elif Person_username == "481760825":
        return "Бегинина Анастасия"
    elif Person_username == "1841248342":
        return "Линь Пэн"
    elif Person_username == "418620498":
        return "Дробыш Дмитрий"
    elif Person_username == "617945082":
        return "Скворцова Дарья"
    elif Person_username == "549528518":
        return "Маракушев Михаил"
    elif Person_username == "809811685":
        return "Зотов Леонид"
    elif Person_username == "1812917030":
        return "Е Хэн"
    elif Person_username == "425184209":
        return "Румский Александр"
    elif Person_username == "Denoske":
        return "Голиков Денис"
    elif Person_username == "303681142":
        return "Беляков Дмитрий"
    elif Person_username == "947814855":
        return "Сосновцев Григорий"
    elif Person_username == "883972940":
        return "Виноградов Глеб"
    elif Person_username == "444999728":
        return "Абиш Диана"
    elif Person_username == "1042684016":
        return "Трофимченко Владислав"
    elif Person_username == "1014846611":
        return "Абрабоу Ахмед Елсаид"


save = False
get = True
get_queue(save, get)
photo = open("dimases.jpg", 'rb')

@bot.message_handler(commands=['start'])
def start_message(message):
    global photo
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Салам амалекум\n"
                                      "Ты попал в группу очереди группы P3110\n"
                                      "С чего начнем нашу работу?")
    buttons_message(message)


@bot.message_handler(content_types='text')
def get_parametrs(message):
    global students, OPD, Programming, queue_OPD, queue_Prog, counter, deleteOPD, deleteProg, id_getter, change_Prog1, change_OPD1, getX, change_queue, skip_OPD, skip_Prog, get_rights, take_rights, change_OPD2, change_Prog2
    global Id_of_admins, change_OPD, change_Prog
    global person1, person2
    global change_pos_OPD, change_pos_Prog, person_to_change
    global clear_OPD, clear_Prog
    global take_time
    global BD_time
    global get_text, right, text
    id_getter = check_person(message)
    if check_time() or id_getter in Id_of_admins:
        # --------------------------------------------------------------------------------------------------------------
        # BASIC_COMMANDS_START
        # --------------------------------------------------------------------------------------------------------------
        # LOOKING_FOR_QUEUE_START
        # --------------------------------------------------------------------------------------------------------------
        if message.text == "Посмотреть очереди":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Посмотреть очередь по ОПД")
            item2 = types.KeyboardButton("Посмотреть очередь по Программированию")
            item3 = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, "Выберите предмет: ", reply_markup=markup)

        elif message.text == "Посмотреть очередь по Программированию":
            if len(queue_Prog) == 0:
                bot.send_message(message.chat.id, "Очередей пока нет :(")
            else:
                ochered_prog = "<b>!!! ОЧЕРЕДЬ ПО ПРОГРАММИРОВАНИЮ !!!</b> \n"
                ochered_prog += "------------------------- \n"
                for i in range(len(queue_Prog)):
                    temp = str(i + 1) + ") "
                    ochered_prog += temp + queue_Prog[i] + "\n"
                ochered_prog += "------------------------- \n"
                bot.send_message(message.chat.id, ochered_prog, parse_mode="html")

        elif message.text == "Посмотреть очередь по ОПД":
            if len(queue_OPD) == 0:
                bot.send_message(message.chat.id, "Очередей пока нет :(")
            else:
                ochered_OPD = "<b>!!! ОЧЕРЕДЬ ПО ОПД !!!</b> \n"
                ochered_OPD += "------------------------- \n"
                for i in range(len(queue_OPD)):
                    temp = str(i + 1) + ") "
                    ochered_OPD += temp + queue_OPD[i] + "\n"
                ochered_OPD += "------------------------- \n"
                bot.send_message(message.chat.id, ochered_OPD, parse_mode="html")
        # --------------------------------------------------------------------------------------------------------------
        # LOOKING_FOR_QUEUE_END
        # --------------------------------------------------------------------------------------------------------------
        # ADD_SELF_TO_QUEUE_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Добавить себя в очередь":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Записаться на ОПД")
            item2 = types.KeyboardButton("Записаться на Программирование")
            item3 = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, "Выберите предмет: ", reply_markup=markup)

        elif message.text == "Записаться на ОПД":
            if check_person(message) in queue_OPD:
                bot.send_message(message.chat.id, "Вы уже записаны в эту очередь!")
            else:
                queue_OPD.append(check_person(message))
                bot.send_message(message.chat.id, "Вы успешно записались в очередь по ОПД!")
                get = False
                save = True
                get_queue(save, get)

        elif message.text == "Записаться на Программирование":
            if check_person(message) in queue_Prog:
                bot.send_message(message.chat.id, "Вы уже записаны в эту очередь!")
            else:
                queue_Prog.append(check_person(message))
                bot.send_message(message.chat.id, "Вы успешно записались в очередь по Программированию")
                get = False
                save = True
                get_queue(save, get)
        # --------------------------------------------------------------------------------------------------------------
        # ADD_SELF_TO_QUEUE_END
        # --------------------------------------------------------------------------------------------------------------
        # PUT_SELF_IN_THE_END_OF_THE_QUEUE_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Переместить себя в конец очереди":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Переместить себя в конец по ОПД")
            item2 = types.KeyboardButton("Переместить себя в конец по Программирование")
            item3 = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, "Выберите предмет: ", reply_markup=markup)

        elif message.text == "Переместить себя в конец по ОПД":
            if check_person(message) in queue_OPD:
                queue_OPD.remove(check_person(message))
                queue_OPD.append(check_person(message))
                get = False
                save = True
                get_queue(save, get)
                bot.send_message(int(get_Id(queue_OPD[1])), "Ты следующий в очереди по ОПД, быстрее иди сдавать лабы и не забудь себя переместить в конец")
                bot.send_message(message.chat.id, "Вы переместили себя в конец очереди по ОПД!")
            else:
                bot.send_message(message.chat.id, "Вас нет в очереди по ОПД!")

        elif message.text == "Переместить себя в конец по Программирование":
            if check_person(message) in queue_Prog:
                queue_Prog.remove(check_person(message))
                queue_Prog.append(check_person(message))
                get = False
                save = True
                get_queue(save, get)
                bot.send_message(int(get_Id(queue_Prog[1])), "Ты следующий в очереди по Программированию, быстрее иди сдавать лабы и не забудь себя переместить в конец")
                bot.send_message(message.chat.id, "Вы переместили себя в конец очереди по Программированию!")
            else:
                bot.send_message(message.chat.id, "Вас нет в очереди по Программированию!")
        # --------------------------------------------------------------------------------------------------------------
        # PUT_SELF_IN_THE_END_OF_THE_QUEUE_END
        # --------------------------------------------------------------------------------------------------------------
        # SKIP_ONE_PERSON_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Пропустить одного человека":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Пропустить человека в ОПД")
            item2 = types.KeyboardButton("Пропустить человека в Программировании")
            item3 = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, "Выберите предмет: ", reply_markup=markup)

        elif message.text == "Пропустить человека в ОПД":
            if check_person(message) in queue_OPD:
                skip_OPD = True
                skip_one_person(message)
                get = False
                save = True
                get_queue(save, get)
            else:
                bot.send_message(message.chat.id, "Вас нет в очереди по ОПД!")

        elif message.text == "Пропустить человека в Программировании":
            if check_person(message) in queue_Prog:
                skip_Prog = True
                skip_one_person(message)
                get = False
                save = True
                get_queue(save, get)
            else:
                bot.send_message(message.chat.id, "Вас нет в очереди по Программированию!")
        # --------------------------------------------------------------------------------------------------------------
        # SKIP_ONE_PERSON_END
        # --------------------------------------------------------------------------------------------------------------
        # CHANGE_POSITION_WITH_PERSON_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Поменяться местами с человеком, который стоит позади вас":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Поменяться в ОПД")
            item2 = types.KeyboardButton("Поменяться в Программировании")
            item3 = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=markup)

        elif message.text == "Поменяться в ОПД":
            temp_num = 0
            for i in range(len(queue_OPD)):
                if queue_OPD[i] == check_person(message):
                    temp_num = i + 1
            if temp_num > 0 and temp_num != len(queue_OPD):
                getX = temp_num
                change_pos_OPD = True
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                backbutton = types.KeyboardButton("Вернуться к главному экрану")
                button_list = [types.KeyboardButton(text=x) for x in checker_pos(temp_num)]
                markup.add(*button_list, backbutton)
                bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
            elif temp_num == len(queue_OPD):
                bot.send_message(message.chat.id, "Вы последний в очереди по ОПД")
            else:
                bot.send_message(message.chat.id, "Вас нет в очереди по ОПД")

        elif message.text == "Поменяться в Программировании":
            temp_num = 0
            for i in range(len(queue_Prog)):
                if queue_Prog[i] == check_person(message):
                    temp_num = i + 1
            if temp_num > 0 and temp_num != len(queue_Prog):
                getX = temp_num
                change_pos_Prog = True
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                backbutton = types.KeyboardButton("Вернуться к главному экрану")
                button_list = [types.KeyboardButton(text=x) for x in checker_pos(temp_num)]
                markup.add(*button_list, backbutton)
                bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
            elif temp_num == len(queue_Prog):
                bot.send_message(message.chat.id, "Вы последний в очереди по Программированию")
            else:
                bot.send_message(message.chat.id, "Вас нет в очереди по Программированию")
        # --------------------------------------------------------------------------------------------------------------
        # CHANGE_POSITION_WITH_PERSON_END
        # --------------------------------------------------------------------------------------------------------------
        # BASIC_COMMANDS_END
        # --------------------------------------------------------------------------------------------------------------
        # ADMIN_COMMANDS_START
        # --------------------------------------------------------------------------------------------------------------
        # CREATE_QUEUE_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Создать очередь по предмету" and id_getter in Id_of_admins:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            sub1 = types.KeyboardButton("ОПД")
            sub2 = types.KeyboardButton("Программирование")
            markup.add(sub1, sub2)
            bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=markup)

        elif message.text == "ОПД" and id_getter in Id_of_admins:
            OPD = True
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            choice = types.KeyboardButton("Изменить очередь")
            markup.add(choice)
            bot.send_message(message.chat.id, "Хотите ли вы добавить человека?", reply_markup=markup)

        elif message.text == "Программирование" and id_getter in Id_of_admins:
            Programming = True
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            choice = types.KeyboardButton("Изменить очередь")
            markup.add(choice)
            bot.send_message(message.chat.id, "Хотите ли вы добавить человека?", reply_markup=markup)

        elif message.text == "Изменить очередь" and (OPD or Programming) and id_getter in Id_of_admins:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = [types.KeyboardButton(text=x) for x in delete_person_from_queue()]
            item2 = types.KeyboardButton("Вернуться к главному экрану")
            item3 = types.KeyboardButton("Изменить очередь")
            markup.add(*item1, item2)
            markup.add(item3)
            bot.send_message(message.chat.id, "Выберите студента ИТМО", reply_markup=markup)
            change_queue = True
        # --------------------------------------------------------------------------------------------------------------
        # CREATE_QUEUE_END
        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------
        # GLOBAL_CHANGE_QUEUE_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Редактировать очереди" and id_getter in Id_of_admins:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Создать очередь по предмету")
            item2 = types.KeyboardButton("Удалить человека из очереди")
            item3 = types.KeyboardButton("Переместить человека из его текущего положения в конкретное положение")
            item4 = types.KeyboardButton("Выдать права администратора")
            item5 = types.KeyboardButton("Забрать права администратора")
            item6 = types.KeyboardButton("Очистить очередь")
            item7 = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4, item5)
            markup.add(item6)
            markup.add(item7)
            bot.send_message(message.chat.id, "Выберите команду для редактирования: ", reply_markup=markup)
        # --------------------------------------------------------------------------------------------------------------
        # GLOBAL_CHANGE_QUEUE_END
        # --------------------------------------------------------------------------------------------------------------
        # DELETE_PERSON_FROM_QUEUE_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Удалить человека из очереди" and id_getter in Id_of_admins:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Очередь ОПД")
            item2 = types.KeyboardButton("Очередь Программирование")
            item3 = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(message.chat.id, "Выберите предмет, в котором хотите изменить очередь: ",
                             reply_markup=markup)

        elif message.text == "Очередь ОПД" and id_getter in Id_of_admins:
            if len(queue_OPD) > 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                backcommand = types.KeyboardButton("Вернуться к главному экрану")
                button_list = [types.KeyboardButton(text=x) for x in queue_OPD]
                markup.add(*button_list, backcommand)
                bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
                deleteOPD = True
            else:
                bot.send_message(message.chat.id, "В очереди по ОПД нет людей")

        elif message.text == "Очередь Программирование" and id_getter in Id_of_admins:
            if len(queue_Prog) > 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                backcommand = types.KeyboardButton("Вернуться к главному экрану")
                button_list = [types.KeyboardButton(text=x) for x in queue_Prog]
                markup.add(*button_list, backcommand)
                bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
                deleteProg = True
            else:
                bot.send_message(message.chat.id, "В очереди по программированию нет людей")
        # --------------------------------------------------------------------------------------------------------------
        # DELETE_PERSON_FROM_QUEUE_END
        # --------------------------------------------------------------------------------------------------------------
        # GLOBAL_STUDENT_BY_NAME_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text in students and id_getter in Id_of_admins:
            if OPD and (message.text not in queue_OPD):
                bot.send_message(message.chat.id, "Студент успешно добавлен в очередь по ОПД!")
                queue_OPD.append(message.text)
                get = False
                save = True
                get_queue(save, get)

            elif Programming and (message.text not in queue_Prog) and id_getter in Id_of_admins:
                bot.send_message(message.chat.id, "Студент успешно добавлен в очередь по Программированию")
                queue_Prog.append(message.text)
                get = False
                save = True
                get_queue(save, get)

            elif change_pos_Prog:
                person_to_change = message.text
                change_Prog2 = False
                change_person_position(check_person(message), person_to_change)
                change_pos_Prog = False
                bot.send_message(message.chat.id,
                                 "Готово! Ты поменялся местами в очереди по Программированию с " + person_to_change)
                buttons_message(message)
                get = False
                save = True
                get_queue(save, get)

            elif change_pos_OPD:
                person_to_change = message.text
                change_person_position(check_person(message), person_to_change)
                change_pos_OPD = False
                bot.send_message(message.chat.id,
                                 "Готово! Ты поменялся местами в очереди по ОПД с " + person_to_change)
                buttons_message(message)
                get = False
                save = True
                get_queue(save, get)

            elif OPD or Programming and change_queue:
                bot.send_message(message.chat.id, "Данный студент уже был введен в очередь")

            if deleteOPD:
                delete_person(message)
                deleteOPD = False
                bot.send_message(message.chat.id, "Вы успешно удалили из очереди по ОПД " + message.text)
                bot.send_message(int(get_Id(message.text)), "Администратор удалил вас из очереди по ОПД")
                buttons_message(message)
                get = False
                save = True
                get_queue(save, get)

            elif deleteProg:
                delete_person(message)
                deleteProg = False
                bot.send_message(message.chat.id,
                                 "Вы успешно удалили из очереди по программированию " + message.text)
                bot.send_message(int(get_Id(message.text)), "Администратор удалил вас из очереди по Программированию")
                buttons_message(message)
                get = False
                save = True
                get_queue(save, get)

            elif get_rights:
                get_Admin(message)
                get_rights = False
                bot.send_message(int(get_Id(message.text)),
                                 "Вам выдали права администратора очереди. Теперь вы можете редактировать очередь. Перезапустите бота, чтобы ваш статус активировался (/start)")
                buttons_message(message)
                get = False
                save = True
                get_queue(save, get)

            elif take_rights:
                take_Admin(message)
                take_rights = False
                bot.send_message(int(get_Id(message.text)),
                                 "У вас забрали права администратора очереди. Перезапустите бота, чтобы ваш статус активировался (/start)")
                buttons_message(message)
                get = False
                save = True
                get_queue(save, get)

            elif change_OPD1:
                person1 = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                backbutton = types.KeyboardButton("Вернуться к главному экрану")
                button_list = [types.KeyboardButton(text=x) for x in queue_OPD]
                markup.add(*button_list, backbutton)
                change_OPD2 = True
                bot.send_message(message.chat.id, "Выберите второго человека: ", reply_markup=markup)
                change_OPD1 = False

            elif change_Prog1:
                person1 = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                backbutton = types.KeyboardButton("Вернуться к главному экрану")
                button_list = [types.KeyboardButton(text=x) for x in queue_Prog]
                markup.add(*button_list, backbutton)
                change_Prog2 = True
                bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
                change_Prog1 = False

            elif change_OPD2:
                person2 = message.text
                if person2 != person1:
                    change_person_position(person1, person2)
                    bot.send_message(message.chat.id,
                                     "Готово! Ты поменял " + person1 + " и " + person2 + " местами в очереди по ОПД")
                    buttons_message(message)
                    get = False
                    save = True
                    get_queue(save, get)
                else:
                    bot.send_message(message.chat.id, "Вы выбрали одного и того же человека")

                change_OPD2 = False

            elif change_Prog2:
                person2 = message.text
                if person1 != person2:
                    change_person_position(person1, person2)
                    bot.send_message(message.chat.id,
                                     "Готово! Ты поменял " + person1 + " и " + person2 + " местами в очереди по Программированию")
                    buttons_message(message)
                    get = False
                    save = True
                    get_queue(save, get)
                else:
                    bot.send_message(message.chat.id, "Вы выбрали одного и того же человека")

                change_Prog2 = False
        # --------------------------------------------------------------------------------------------------------------
        # GLOBAL_STUDENT_BY_NAME_END
        # --------------------------------------------------------------------------------------------------------------
        # CHANGE_PERSON_POS_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Переместить человека из его текущего положения в конкретное положение" and id_getter in Id_of_admins:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Изменить ОПД")
            item2 = types.KeyboardButton("Изменить Программирование")
            backbutton = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            markup.add(item2)
            markup.add(backbutton)
            bot.send_message(message.chat.id, "Выберите предмет, в котором хотите изменить человека: ",
                             reply_markup=markup)
            get = False
            save = True
            get_queue(save, get)

        elif message.text == "Изменить ОПД" and id_getter in Id_of_admins:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            backbutton = types.KeyboardButton("Вернуться к главному экрану")
            button_list = [types.KeyboardButton(text=x) for x in queue_OPD]
            markup.add(*button_list, backbutton)
            change_OPD1 = True
            bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
            get = False
            save = True
            get_queue(save, get)

        elif message.text == "Изменить Программирование" and id_getter in Id_of_admins:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            backbutton = types.KeyboardButton("Вернуться к главному экрану")
            button_list = [types.KeyboardButton(text=x) for x in queue_Prog]
            markup.add(*button_list, backbutton)
            change_Prog1 = True
            bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
            get = False
            save = True
            get_queue(save, get)
        # --------------------------------------------------------------------------------------------------------------
        # CHANGE_PERSON_POS_END
        # --------------------------------------------------------------------------------------------------------------
        # GET_ADMIN_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Выдать права администратора" and check_person(message) == "Новиков Егор":
            stud_temp = []
            for i in range(len(students)):
                if students[i] != "Новиков Егор":
                    stud_temp.append(students[i])
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            backbutton = types.KeyboardButton("Вернуться к главному экрану")
            button_list = [types.KeyboardButton(text=x) for x in stud_temp]
            markup.add(*button_list, backbutton)
            bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
            get_rights = True
            get = False
            save = True
            get_queue(save, get)
        # --------------------------------------------------------------------------------------------------------------
        # GET_ADMIN_END
        # --------------------------------------------------------------------------------------------------------------
        # TAKE_ADMIN_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Забрать права администратора" and check_person(message) == "Новиков Егор":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            backbutton = types.KeyboardButton("Вернуться к главному экрану")
            button_list = [types.KeyboardButton(text=x) for x in Id_of_admins]
            markup.add(*button_list, backbutton)
            bot.send_message(message.chat.id, "Выберите человека: ", reply_markup=markup)
            take_rights = True
            get = False
            save = True
            get_queue(save, get)
        # --------------------------------------------------------------------------------------------------------------
        # TAKE_ADMIN_END
        # --------------------------------------------------------------------------------------------------------------
        # SAVE_FILE_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Сохранить очередь в файл" and id_getter in Id_of_admins:
            save = True
            get = False
            get_queue(save, get)
            bot.send_message(message.chat.id, "Очередь успешно сохранена")
        # --------------------------------------------------------------------------------------------------------------
        # SAVE_FILE_END
        # --------------------------------------------------------------------------------------------------------------
        # CLEAR_QUEUE_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Очистить очередь" and id_getter in Id_of_admins:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            backbutton = types.KeyboardButton("Вернуться к главному экрану")
            item1 = types.KeyboardButton("Очистить ОПД")
            item2 = types.KeyboardButton("Очистить Программирование")
            markup.add(item1, item2)
            markup.add(backbutton)
            bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=markup)
        elif message.text == "Очистить ОПД" and id_getter in Id_of_admins:
            clear_OPD = True
            clear_queue()
            clear_OPD = False
            bot.send_message(message.chat.id, "Вы успешно очистили очередь по ОПД")
        elif message.text == "Очистить Программирование" and id_getter in Id_of_admins:
            clear_Prog = True
            clear_queue()
            clear_Prog = False
            bot.send_message(message.chat.id, "Вы успешно очистили очередь по Программированию")
        # --------------------------------------------------------------------------------------------------------------
        # CLEAR_QUEUE_END
        # --------------------------------------------------------------------------------------------------------------
        # SET_TIME_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Назначить время для очереди" and id_getter in Id_of_admins:
            bot.send_message(message.chat.id, "Введите день, месяц, час и минуты через пробел")
            take_time = True
            bot.send_message(message.chat.id, "Текущее время такое:")
            bot.send_message(message.chat.id, str(BD_time[0]))
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Вернуться к главному экрану")
            markup.add(item1)
            bot.send_message(message.chat.id, "Если вы хотите выйти из изменения времени, нажмите кнопку",
                             reply_markup=markup)

        elif take_time and id_getter in Id_of_admins:
            if message.text != "Вернуться к главному экрану":
                dateTime = message.text.split()
                set_time(dateTime[0], dateTime[1], dateTime[2], dateTime[3])
                bot.send_message(message.chat.id, "Вы успешно изменили время!")
                buttons_message(message)
                take_time = False
            elif message.text == "Вернуться к главному экрану":
                buttons_message(message)

        # --------------------------------------------------------------------------------------------------------------
        # SET_TIME_END
        # --------------------------------------------------------------------------------------------------------------
        # SEND_NEWS_START
        # --------------------------------------------------------------------------------------------------------------
        elif message.text == "Выложить новость в боте":
            bot.send_message(message.chat.id, "Отправьте текст, который вы хотели бы отправить всем")
            get_text = True
        # --------------------------------------------------------------------------------------------------------------
        # SEND_NEWS_END
        # --------------------------------------------------------------------------------------------------------------
        # ADMIN_COMMANDS_END
        # --------------------------------------------------------------------------------------------------------------

        # BACK_TO_MAIN

        elif message.text == "Вернуться к главному экрану":
            get = False
            save = True
            get_queue(save, get)
            buttons_message(message)
            deleteProg = deleteOPD = change_queue = OPD = Programming = False
        elif id_getter in Id_of_admins and get_text:
            text = message.text
            bot.send_message(message.chat.id, message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да")
            item2 = types.KeyboardButton("Нет")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Вы уверены в написаном тексте?", reply_markup=markup)
            right = True
            get_text = False
        elif message.text == "Да" and right:
            for i in range(len(queue_OPD)):
                bot.send_message(int(get_Id(queue_OPD[i])), text)
            right = False
            buttons_message(message)
        elif message.text == "Нет" and right:
            right = False
            buttons_message(message)
    else:
        buttons_message(message)


@bot.message_handler(commands=['buttons'])
def buttons_message(message):
    global id_getter, Id_of_admins, flag
    id_getter = check_person(message)
    if id_getter in Id_of_admins:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Посмотреть очереди")
        item2 = types.KeyboardButton("Добавить себя в очередь")
        item3 = types.KeyboardButton("Переместить себя в конец очереди")
        item4 = types.KeyboardButton("Пропустить одного человека")
        item5 = types.KeyboardButton("Поменяться местами с человеком, который стоит позади вас")
        item6 = types.KeyboardButton("Редактировать очереди")
        item7 = types.KeyboardButton("Сохранить очередь в файл")
        item8 = types.KeyboardButton("Назначить время для очереди")
        item9 = types.KeyboardButton("Выложить новость в боте")
        markup.add(item1, item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        markup.add(item8)
        markup.add(item9)
        bot.send_message(message.chat.id, "Выберите команду : ", reply_markup=markup)
    elif check_time():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Посмотреть очереди")
        item2 = types.KeyboardButton("Добавить себя в очередь")
        item3 = types.KeyboardButton("Переместить себя в конец очереди")
        item4 = types.KeyboardButton("Пропустить одного человека")
        item5 = types.KeyboardButton("Поменяться местами с человеком, который стоит позади вас")
        markup.add(item1, item2)
        markup.add(item3, item4)
        markup.add(item5)
        bot.send_message(message.chat.id, "Выберите команду : ", reply_markup=markup)
    elif not check_time():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Кнопка")
        markup.add(item1)
        bot.send_message(message.chat.id, "Извините, очередь сейчас закрыта", reply_markup=markup)


bot.infinity_polling()
