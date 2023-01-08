medida = float(input('Digite um distância em metros: '))
km = medida*0.001
hm = medida*0.01
dam = medida*0.1
dc = medida*10
cm = medida*100
mm = medida*1000

print('A medida de {} metros corresponde a {:.1f}cm, {:.1f}mm,{}dam, {}hm e {}km '.format(medida,cm,mm,dam,hm,km))

