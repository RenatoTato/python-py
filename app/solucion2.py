import readCsv
import char

values = []
labels = []
data = readCsv.read_csv('./app/data.csv')
for i in data:
  for key, value in i.items():
    if key.endswith('Country'):
      labels.append(value)
    if key.endswith('Population Percentage'): 
      value=float(value)
      values.append(value)
print(values)
print(labels)
char.generate_pie_chart(labels, values)
