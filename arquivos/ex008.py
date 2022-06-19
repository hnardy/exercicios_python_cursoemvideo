#faça um programa que pergunte um valor em metros e mostre seu valor em km,hm,dam,dm,cm,mm
n = float(input('digite um valor em metros'))
print ('{} metros equicavale há \n {} km \n {} hm \n {} dam \n {} m \n {} dm \n {} cm \n {} mm '.format(n,n/1000,n/100,n/10,n,n*10,n*100,n*1000))