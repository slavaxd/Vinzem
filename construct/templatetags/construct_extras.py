# coding: utf-8
from django import template

register = template.Library()

@register.filter(name='month')
def month(value):
    m = [0, "Січ", "Лют", "Бер", "Кві", "Тра", "Чер", "Лип", "Серпень", "Вер", "Жов", "Лис", "Гру"]
    return m[value]

@register.filter(name='categ')
def categ(value):
    l = ['Землевиорні роботи', 'Землеоціночні роботи', 'Якісь ще роботи', 'Останні роботи']
    res = l[int(value)]
    return res

@register.filter(name='subt')
def subt(value):
    l = ['Опис землевиорних роботи', 'Опис землеоціночних роботи', 'Опис якісь ще роботи', 'Опис останні роботи']
    res = l[int(value)]
    return res

@register.filter(name='first_fifty')
def first_fifty(value):
    res = value[:50] + "..."
    return res