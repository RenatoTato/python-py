import readCsv
import char

pais = input('Ingrese el pais: ')
pais=pais.title()
values=[]
labels=[]
data = readCsv.read_csv('./app/data.csv')
for i in data:
  if i['Country'] == pais:
    for key, value in i.items():
      if key.endswith('Population'):
        values.append(value)
        labels.append(key[:4])
print(values)
print(labels)
char.generate_bar_chart(labels, values)

