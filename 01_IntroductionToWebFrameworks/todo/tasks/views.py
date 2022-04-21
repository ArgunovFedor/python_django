from django.http import HttpResponse

from django.views import View
import random


class ToDoView(View):
    def get(self, request, *args, **kwargs):
        tasks = ['<li>Установить python</li>',
                 '<li>Установить django</li>',
                 '<li>Запустить сервер</li>',
                 '<li>Порадоваться результату</li>']
        return HttpResponse('<ul>' +
                            ''.join([tasks.pop(random.randrange(len(tasks))) for _ in range(len(tasks))])
                            +
                            '</ul>')
