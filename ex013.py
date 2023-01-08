sal=float(input('Informe o salário: R$ '))
ns=sal+(sal*15/100)
print('O funcionário  que recebia R${:.2f} de salário, com o aumento de 15% receberá R$ {:.2f}'.format(sal,ns))
