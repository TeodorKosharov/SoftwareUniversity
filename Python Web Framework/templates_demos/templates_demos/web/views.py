from django import http
from django.shortcuts import render


class Student:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}'

    # def index(request):
    #     context = {
    #         'title': 'SoftUni Homepage',
    #         'value': random.random(),
    #         'info': {
    #             'address': 'Sofia'
    #         },
    #         'student': Student('Teodor', 21).get_info()
    #     }


def base(request):
    context = {
        'student': Student('Teodor', 21)
    }
    return render(request, 'base.html', context)


def index(request):
    return render(request, 'index.html')
