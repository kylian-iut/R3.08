def division(a,b):
    try:
        c=a/b
    except TypeError:
        return "Au moins un des argument n'est pas un réel"
    except ValueError:
        return "Au moins un des argument n'est pas un réel"
    except ZeroDivisionError:
        return "b ne peut pas être 0 pour une division"
    else:
        return c

print(division("8","9"))