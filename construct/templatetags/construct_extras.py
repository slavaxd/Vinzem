# coding: utf-8
from django import template

register = template.Library()

@register.filter(name='month')
def month(value):
    m = [0, "Січ", "Лют", "Бер", "Кві", "Тра", "Чер", "Лип", "Серпень", "Вер", "Жов", "Лис", "Гру"]
    return m[value]