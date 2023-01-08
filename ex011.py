#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt=float(input('Informe a altura da parede: '))
lar=float(input('Informe a largura da parede: '))
area=alt*lar
tinta=area/2
print('Sua parede tem a dimensão de {} por {} que equivale a uma área de {}m². Você precisará de {} litros de tintas para pintá-la'.format(alt,lar,area,tinta))
