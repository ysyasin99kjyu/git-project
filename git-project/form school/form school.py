# List kar ha
# 1- دریافت نام دانش آموز
# 2- دریافت سن
# 3- دریافت نمره نهایی کارنامه
# 4- دریافت نام پدر و مادر
# 5- دریافت کد ملی
# منطق
# سن دانش آموز از 13 بیشتر باشد
# نمره نهایی بالای 17 در غیر این صورت امتحان گرفته شود

import os

score = 0
errorList = []
exam = 0
ageStatus = 0
status = 'default'


student = {
    'name':'default',
    'age': 0,
    'father': 'default',
    'mother': 'default',
    'final score': 'default'
}



def get_creds():
    student['name'] = input('Name Danesh Amoz \n')
    student['age'] = int(input('Sen Danesh Amoz \n'))
    student['father'] = input('Name pedar Danesh Amoz \n')
    student['mother'] = input('Name madar Danesh Amoz \n')
    student['final score'] = int(input('Moadel Danesh Amoz \n'))


def check_creds():
    global score
    global errorList
    global ageStatus
    global exam
    global student
    global status
    if student['age'] >= 13:
        score = score + 1
    else:
        ageStatus = 1
        errorList.append('Sen danesh amoz kam ast')

    if student['final score'] >= 17:
        score = score + 1
    else:
        exam = 1
        errorList.append('Moadel Danesh Amoz Kam ast')

    if exam == 1 and ageStatus == 0:
        print('Danesh amoz Baraye sabt nam bayad Emtehan dahad')
        status = 'Danesh amoz Baraye sabt nam bayad Emtehan dahad'
    elif score == 2:
        print('Danesh Amooz Ba Movafaqiat sabt nam shod')
        status = 'Danesh Amooz Ba Movafaqiat sabt nam shod'
    else:
        print('Danesh Amooz Sabt Nam Nmisahvad Be Dalayel Zir => ')
        status = 'Danesh Amooz Sabt Nam Nmisahvad'
        for item in errorList:
            print(item)





def start_app():
    global student
    global status
    print('Be form sabt nam khosh amadid')
    get_creds()
    check_creds()
    print('Mamnon az entekhab shoma')
    with open('wwform.txt', 'w') as f:
        f.write('Name Danesh Amooz: {} \n'.format(student['name']))
        f.write('Name Pedar Danesh Amooz: {} \n'.format(student['father']))
        f.write('Name Madar Danesh Amooz: {} \n'.format(student['mother']))
        f.write('Sen Danesh Amooz: {} \n'.format(student['age']))
        f.write('Moadel Danesh Amooz: {} \n'.format(student['final score']))
        f.write('Vaziat Sabt Name Danesh Amooz: {} \n'.format(status))

start_app()