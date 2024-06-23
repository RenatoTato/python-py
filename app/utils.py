def get_population(i):
  values=[]
  labels=[]
  for key, value in i.items():
    if key.endswith('Population'):
      values.append(int(value))
      labels.append(key[:4])
  return labels,values
  
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result
