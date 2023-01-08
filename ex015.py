dias=int(input('Informe a quantidade de dias alugado: '))
km=float(input('Informe a quantidade de km percorridos: '))
pago=(dias*60)+(km*0.15)

print('O total a pagar é de R${}'.format(pago))

