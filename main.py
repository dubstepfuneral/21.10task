"""
- напишите функцию, которая принмает на вход произвольное количество аргументов и выдает сумму этих аргументов 
- сделaйте коммит
- допишите функцию так, чтобы она проверяла, что вы передали только числа. Если попадаются не числа, то напечатайте сообщение об ошибке 
- сделайте коммит 


- создайте новую ветку 
- переключитесь на нее 
- напишите функцию, которая определяет, является ли строка палиндромом 


- создайте новую ветку 
- переключитесь на нее 
- напишите функцию, которая удаляет из строки лишние пробелы
"""

def summ(*args):
    res = 0
    error = False
    for i in args:
        if type(i) is int:
            res = res + i
        else:
            error = True
    if error:
        return "Error: non-numeric arguments"
    return res