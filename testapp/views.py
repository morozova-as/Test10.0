<<<<<<< HEAD
# -*- coding: utf-8 -*- 
=======
>>>>>>> 2cae5d9500de8a702edb212a406dfa7d10696f7c
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
import random
import numpy as np
import mimetypes, os
import socket
from .models import Question, Choice, User
from .forms import NameForm
<<<<<<< HEAD
from datetime import datetime, timedelta, time
from django.utils import timezone

import psycopg2
=======
from datetime import datetime, timedelta, timezone, time
>>>>>>> 2cae5d9500de8a702edb212a406dfa7d10696f7c

from django.core.files import File
from django.http import FileResponse
from wsgiref.util import FileWrapper

from testsite.settings import PATH_B, PATH_E

def index(request):
    #Mas.objects.all().delete()
    #p = User.objects.get(user_name="User")
    #p.corr_ans = 0
    #p.quest_now = 0
    #p.user_fio="NULL"
    #p.save()


    '''
    razm_users = User.objects.count()
    razm_users+=1
    razm = Question.objects.count()

    strr = "User" + str(razm_users)
    u = User(user_name=strr, user_fio="NULL")
    u.save()

    p = User.objects.get(user_name=strr)
    
    os.mkdir(PATH_B + str(p.user_name))
    file_name = PATH_B + str(p.user_name) + '/' + str(p.user_name) + PATH_E

    f = open(file_name, "w")

    file = File(f)

    file.close()

'''

    return render(request, "testapp/index.html", {"p": 'NULL', 'id':0})
    #return render(request, "testapp/form.html")


def fio(request):
    razm_users = User.objects.count()
    user_last = User.objects.get(pk = razm_users)
    razm_users = user_last.user_id + 1
    razm = Question.objects.count()

    strr = "User" + str(razm_users)
    u = User(user_name=strr, user_fio="NULL")
    u.save()

    p = User.objects.get(user_name=strr)
    
    os.mkdir(PATH_B + str(p.user_name))
    file_name = PATH_B + str(p.user_name) + '/' + str(p.user_name) + PATH_E

    f = open(file_name, "w")

    file = File(f)

    file.close()



    form = NameForm()
    return render(request, 'testapp/fio.html', {'form': form, 'id':p.user_id})

def detail0(request, user_id, question_id):
    p = User.objects.get(user_id=user_id)

    file_mas = PATH_B + str(p.user_name) + '/' + str(p.user_name) + '_mas' + PATH_E
    f1 = open(file_mas, "w")
    file1 = File(f1)
    file1.close()


    file_mas = PATH_B + str(p.user_name) + '/' + str(p.user_name) + '_mas' + PATH_E
    fm = open(file_mas, "a")
    filem = File(fm)

    razm = Question.objects.count()
    l = np.random.permutation(razm)
    filem.write(','.join([str(i+1) for i in l]))
    filem.write('\r\n')
    filem.write('\n')
    filem.write(','.join(['0' for i in l]))
    '''
    for i in range(razm):
        filem.write(str(l[i]+1))
        if (i!=razm-1):
            filem.write(',')
        m = Mas (id_n = i+1, num = l[i]+1)
        m.save()
    filem.write('\n')
    filem.write('\r\n')
    for i in range(razm):
        filem.write(str(i+1))
        if (i!=razm-1):
            filem.write(',')
    filem.write('\n')
    filem.write('\r\n')
    for i in range(razm):
        filem.write('0')
        if (i!=razm-1):
            filem.write(',')
    '''


    filem.close()
    file_name = PATH_B + str(p.user_name) + '/' + str(p.user_name) + PATH_E
    if (p.user_fio == 'NULL'):
        if request.method == "POST":
            form = NameForm(request.POST)
            if form.is_valid() :
                p.user_fio = request.POST.get('name').encode('utf-8')
                p.save()

                f = open(file_name, "a")
                file = File(f)
                file.write("USER NAME: ")
                file.write(p.user_fio.decode('utf-8'))
            else:
                form = NameForm()
                return render(request, 'testapp/fio.html', {'form': form, 'id':user_id})
        else:
            form = NameForm()

    p.time_begin = datetime.now(timezone.utc)
    p.save()

    fm = open(file_mas, "r")
    filem = File(fm)

    #l = [line.strip() for line in filem]
    l = filem.readlines()
    mass = l[0].split(',')
    r = mass[p.quest_now]
    filem.close()

    file_name = PATH_B + str(p.user_name) + '/' + str(p.user_name) + PATH_E
    f = open(file_name, "a")
    file = File(f)

    file.write('\n')
    file.write('\r\n')
    file.write("BEGIN TIME: ")
    file.write(datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y"))
    file.write('\n')
    file.write('\r\n')
    file.write('------------------------------')
    file.write('\n')
    file.write('\r\n')
    file.close()


    #tr_name = translit(p.user_fio, "ru", reversed=True)
    return render(request, "testapp/detail.html", {"question": get_object_or_404(Question, pk=r), 'id':user_id, 't':p.time})


def detail(request, question_id, user_id):

    question = get_object_or_404(Question, pk=question_id)
    p = User.objects.get(user_id=user_id)
    file_mas = PATH_B + str(p.user_name) + '/' + str(p.user_name) + '_mas' + PATH_E
    #if (p.quest_now < p.kol_quest-1):
        #mass = Mas.objects.get(id_n=(p.quest_now+2))


    file_name = PATH_B + str(p.user_name) + '/' + str(p.user_name) + PATH_E
    f = open(file_name, "a")
    file = File(f)
    file.write("Question")
    file.write(str(p.quest_now+1))
    s = "-------"
    ss="-"
    s += ss*(2-len(str(p.quest_now+1)))
    file.write(s)

    try:
        option = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        p.quest_now+=1
        p.save()
        if (p.quest_now<p.kol_quest):

            file.write("WRONG")
            file.write('\n')
            file.write('\r\n')
            file.close()


            fm = open(file_mas, "r")
            filem = File(fm)
            l = filem.readlines()
            mass = l[0].split(',')
            r = mass[p.quest_now]
            filem.close()
            
            fm = open(file_mas, "r")
            filem = File(fm)
            text = filem.read()
            filem.close()

            fm = open(file_mas, "w")
            filem = File(fm)
<<<<<<< HEAD
            if (l[2] == '\r\n'):
            	h = 3
            else:
            	h = 2
            num_last = l[h].split(',')
            num_last[p.quest_now] = question_id
            text = text.replace(l[h],','.join([str(i) for i in num_last]))
=======
            num_last = l[3].split(',')
            num_last[p.quest_now] = question_id
            text = text.replace(l[3],','.join([str(i) for i in num_last]))
>>>>>>> 2cae5d9500de8a702edb212a406dfa7d10696f7c
            filem.write(text)
            filem.close()

            if (num_last[p.quest_now-1]!=0):
                if (mass[p.quest_now-1] != num_last[p.quest_now] ):
                    p.corr_ans = 0
                    p.quest_now = 0
                    p.save()
                    return render(request, "testapp/index.html", {"p": p.user_fio, "m":'Пройди сначала!', "m2":'Не будь читером!', 'id':user_id})

            return render(request, "testapp/detail.html", {"question": get_object_or_404(Question, pk=r), 'id':user_id, 't':p.time})
        elif (p.quest_now==p.kol_quest):
            p.time_end = datetime.now(timezone.utc)
            p.save()

            time_m = p.time_end-p.time_begin
            time_m = int(time_m.seconds)
            m = time_m//60
            time_m %= 60

            file.write("WRONG")
            file.write('\n')
            file.write('\r\n')
            file.write('------------------------------')
            file.write('\n')
            file.write('\r\n')
            file.write("END TIME: ")
            file.write(datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y"))
            file.write('\n')
            file.write('\r\n')
            file.write('\n')
            file.write('\r\n')


            file.write("RESULT: ")
            file.write(str(p.corr_ans))
            file.write('\n')
            file.write('\r\n')
            file.write('\n')
            file.write('\r\n')


            file.write("TIME: ")
            if(m!=0):
                file.write(str(m))
                file.write(" m. ")
            file.write(str(time_m+1))
            file.write(" s.")
            file.write('\n')
            file.write('\r\n')
            file.close()
            #Mas.objects.all().delete()

            os.rename(PATH_B + str(p.user_name), PATH_B + str(p.user_fio))
            return render(request, 'testapp/results.html', {'result': p.corr_ans, 'id':user_id, 'end': datetime.strftime(p.time_end, "%H:%M:%S %d.%m.%Y"), 'begin': datetime.strftime(p.time_begin, "%H:%M:%S %d.%m.%Y")})
        else:
            p.corr_ans = 0
            p.quest_now = 0
            p.save()
            return render(request, "testapp/index.html", {"p": p.user_fio, "m":'Пройди сначала!', "m2":'Не будь читером!', 'id':user_id})
    else:
        if option.correct:
            p.corr_ans+=1
            p.save()
            file.write("RIGHT")
            file.write('\n')
            file.write('\r\n')
        else:
            file.write("WRONG")
            file.write('\n')
            file.write('\r\n')

        p.quest_now+=1
        p.save()


        if (p.quest_now < p.kol_quest):
            fm = open(file_mas, "r")
            filem = File(fm)
            l = filem.readlines()
            mass = l[0].split(',')
            r = mass[p.quest_now]
            filem.close()


            fm = open(file_mas, "r")
            filem = File(fm)
            text = filem.read()
            filem.close()

            fm = open(file_mas, "w")
            filem = File(fm)
<<<<<<< HEAD

            if (l[2] == '\r\n'):
            	h = 3
            else:
            	h = 2
            num_last = l[h].split(',')
            num_last[p.quest_now] = question_id
            text = text.replace(l[h],','.join([str(i) for i in num_last]))
=======
            num_last = l[3].split(',')
            num_last[p.quest_now] = question_id
            text = text.replace(l[3],','.join([str(i) for i in num_last]))
>>>>>>> 2cae5d9500de8a702edb212a406dfa7d10696f7c
            filem.write(text)
            filem.close()


            if (num_last[p.quest_now-1]!=0):
                if (mass[p.quest_now-1] != num_last[p.quest_now] ):
                    p.corr_ans = 0
                    p.quest_now = 0
                    p.save()
                    return render(request, "testapp/index.html", {"p": p.user_fio, "m":'Пройди сначала!', "m2":'Не будь читером!', 'id':user_id})

            return render(request, "testapp/detail.html", {"question": get_object_or_404(Question, pk=r), 'id':user_id, 't':p.time})
        elif (p.quest_now==p.kol_quest):
            p.time_end = datetime.now(timezone.utc)
            p.save()

            time_m = p.time_end-p.time_begin
            time_m = int(time_m.seconds)
            m = time_m//60
            time_m %= 60


            file.write('------------------------------')
            file.write('\n')
            file.write('\n')
            file.write('\r\n')
            file.write('\r\n')
            file.write("END TIME: ")
            file.write(datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y"))
            file.write('\n')
            file.write('\n')
            file.write('\r\n')
            file.write('\r\n')
            file.write("RESULT: ")
            file.write(str(p.corr_ans))
            file.write('\n')
            file.write('\n')
            file.write('\r\n')
            file.write('\r\n')


            file.write("TIME: ")
            if(m!=0):
                file.write(str(m))
                file.write(" m. ")
            file.write(str(time_m+1))
            file.write(" s.")
            file.write('\n')
            file.write('\r\n')

            file.close()
            
            os.rename(PATH_B + str(p.user_name), PATH_B + str(p.user_fio))
            return render(request, 'testapp/results.html', {'result': p.corr_ans,'id':user_id, 'end': datetime.strftime(p.time_end, "%H:%M:%S %d.%m.%Y"), 'begin': datetime.strftime(p.time_begin, "%H:%M:%S %d.%m.%Y")})
        else:
            p.corr_ans = 0
            p.quest_now = 0
            p.save()
            return render(request, "testapp/index.html", {"p": p.user_fio, "m":'Пройди сначала!', "m2":'Не будь читером!', 'id':user_id})



def download_file(request, user_id):


    p = User.objects.get(user_id=user_id)
    my_file = PATH_B + str(p.user_fio) + '/' + str(p.user_name) + PATH_E
    response = HttpResponse(FixedFileWrapper(open(my_file, 'rb')), content_type=mimetypes.guess_type(my_file)[0])
    response['Content-Length'] = os.path.getsize(my_file)
    response['Content-Disposition'] = "attachment; filename=%s" % os.path.basename(my_file)
    return response



class FixedFileWrapper(FileWrapper):
    def __iter__(self):
        self.filelike.seek(0)
        return self

