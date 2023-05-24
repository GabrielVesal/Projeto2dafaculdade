'''
input velocidade
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
print "Não levou multa" 
if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10:
print "Levou multa leve"
if velocidade > velocidade_maxima +11 e velocidade <= velocidade_maxima + 20:
print "Levou multa grave"
if velocidade > velocidade_maxima + 20:
print "Levou multa gravíssima"
'''

velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
  print('Levou multa leve')
elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
  print('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
  print('Levou multa gravíssima')
