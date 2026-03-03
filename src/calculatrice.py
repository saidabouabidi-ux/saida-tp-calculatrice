def division(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def puissance(a, n):
    if n < 0:
        raise ValueError
    return a ** n


def moyenne(notes):
    if len(notes) == 0:
        raise ValueError
    return sum(notes) / len(notes)
