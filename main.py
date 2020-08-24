import config
import datetime
#import database
import os
from tinkoff_voicekit_client import ClientSTT

API_KEY = config.api_key
SECRET_KEY = config.secret_key

client = ClientSTT(API_KEY, SECRET_KEY)

audio_config = {
    "encoding": "LINEAR16",
    "sample_rate_hertz": 8000,
    "num_channels": 1
}

answering_machine = ["автоответчик", "сигнала"]
negative_words = ["нет", "неудобно"]
positive_words = ["говорите", "конечно", "слушаю"]

def ctime():
    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M")
    return time

def data_processing_step1(voice):
    for i in answering_machine:
        if i in voice.split(" "):
            return 0
    return 1
def data_processing_step2(voice):
    for i in positive_words:
        if i in voice.split(" "):
            return 1
    for i in negative_words:
        if i in voice.split(" "):
            return 0
    return "Error"

def send_log(res, action):
    f = open('log.txt')
    log = f.read()
    ID = len(log.split("\n"))
    f = open('log.txt', 'w')
    if flag != "Y":
        f.write(log + f"Дата и время: {ctime()}, ID: {ID}, Результат действия: {action}, Номер телефона: {phone}, "
                      f"Длительность: {res[0]['end_time']}, Результат распознания: {res[0]['alternatives'][0]['transcript']}\n")
        f.close()
    else:
        f.write(log + f"Дата и время: {ctime()}, ID: {ID}, Результат действия: {action}, Номер телефона: {phone}, "
                      f"Длительность: {res[0]['end_time']}, Результат распознания: {res[0]['alternatives'][0]['transcript']}\n")
        f.close()
        #database.add_info(ctime(), ID, action, phone, res[0]['end_time'], res[0]['alternatives'][0]['transcript'])
        print("Данные успешно записаны в базу данных!")

# recognise method call
path = input("Введите путь до файла: ")
phone = input("Введите номер телефона: ")
flag = input("Для добавление в базу данныйх введите Y, если это не нужно, то нажмите Enter: ")

response = client.recognize(path, audio_config)
res = data_processing_step1(response[0]['alternatives'][0]['transcript'])

if res == 1:
    res = data_processing_step2(response[0]['alternatives'][0]['transcript'])
    if res == 1:
        send_log(response, "Положительно")
    elif ress == 0:
        send_log(response, "Отрицательно")
    else:
        send_log(response, "Ошибка в определения реакции")
else:
    send_log(response, "Автоответчик")

os.remove(path)
print(f"\nРезультат: {res}\nСообщение: {response[0]['alternatives'][0]['transcript']}")