import readCsv
import char
import utils
import pandas as pd

def run():
  df = pd.read_csv('./data.csv')
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  countries = list(map(lambda x : x['Country'], data))
  percentage = list(map(lambda x : x['World Population Percentage'], data))
  '''
  

  #linea 8
  df = df[df['Continent'] == 'Africa']
  #linea 9 y 10
  countries=df['Country'].values
  percentage=df['World Population Percentage'].values
  df = pd.read_csv('./data.csv')
  char.generate_pie_chart(countries, percentage)
  data = readCsv.read_csv('./data.csv')
  country=input('ingrse el pais: ')
  country=country.title()
  result1=utils.population_by_country(data,country)
  if len(result1) > 0:
    labels,values=utils.get_population(result1[0])
    print(labels, values)
    char.generate_bar_chart(country, labels, values)

if __name__ == '__main__':
  run()