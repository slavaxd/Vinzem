# coding: utf-8
from django import template

from HTMLParser import HTMLParser

register = template.Library()

@register.filter(name='month')
def month(value):
    m = [0, "Січ", "Лют", "Бер", "Кві", "Тра", "Чер", "Лип", "Серпень", "Вер", "Жов", "Лис", "Гру"]
    return m[value]

@register.filter(name='categ')
def categ(value):
    l = ['Землевпорядні роботи', 'Землеоціночні роботи', 'Геодезичні роботи', 'Інші послуги']
    res = l[int(value)]
    return res

@register.filter(name='subt')
def subt(value):
    l = ['Опис землевпорядних роботи', 'Опис землеоціночних роботи', 'Опис геодезичних роботи', 'Опис інших послуг']
    res = l[int(value)]
    return res

@register.filter(name='fifty')
def fifty(value):
    res = value[:50] + "..."
    return res

@register.filter(name='slider_text')
def slider_text(value):
    if len(value) > 400:
        return value[:400] + '...'
    return value


@register.filter(name='unescape')
def unescape(value):
    h = HTMLParser()
    res = h.unescape(value)
    return res
