er = 'error'
def okletsgo(oper):
    a = float(input('vvedite pervoe chislo\n'))
    b = float(input('vvedite vtoroe chislo\n'))
    if oper == '+':
        result = a + b
    elif oper == '-':
        result = a - b
    elif oper == '*':
        result = a * b
    else:
        if b == 0:
            result = er
        else :
            result = a/b
    return(f'resultat : {result}')

opers = ['+','-','*','/']
print(f'varianty operaciy : {opers}')
operand = str(input('kokuyu operaciyu vy hotite?\n'))
if operand in opers:
    print(okletsgo(operand))
else:
    print(er)