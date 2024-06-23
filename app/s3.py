import readCsv
import char
values=[]
[]
data = readCsv.read_csv('./app/data.csv')
for i in data:  
  labels=[ i.keys(),value for  in i if 'Country' in a]
    if 'Country' in :  
      labels.append(i.vaules())
    if 'Population Percentage'in i.keys():                   values.append(i.vaules())
print(values)
print(labels)
char.generate_pie_chart(labels, values)