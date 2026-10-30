import requests
import statistics
import re



#Reading the API
cats_api= 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
data = response.json()

#Filtering out the cats informations
def weightseperation(api):
  weight_name = {}
  for cats in api:
    weight_name[cats['name']] = cats['weight']['metric']
  return weight_name

def lifespanseperator(api):
  lifespan = {}
  for cats in api:
    lifespan[cats['name']] = cats['life_span']
  return lifespan

def average(filteredlist):
  regex_pattern = r'[0-9]+'
  updated_averages = {}

  for name, weight in filteredlist.items():
    filterout = re.findall(regex_pattern, weight)
    averages = (int(filterout[0]) + int(filterout[1])) / 2
    updated_averages[name] = averages

  return updated_averages

#Min Max Mean Median and Standard deviation of cats weight (metric units)

def metriccalculations(filters):

  total = []

  for cat in filters.values():
    total.append(cat)

  mean = statistics.mean(total)
  median = statistics.median(total)
  mode = statistics.mode(total)
  standard_deviation = statistics.stdev(total)

  return mean, median, mode, standard_deviation

#Min Max Mean Median and Standard deviation of cats lifespan (years)

def lifespancalculations(filters):

  total = []

  for cat in filters.values():
    total.append(cat)

  mean = statistics.mean(total)
  median = statistics.median(total)
  mode = statistics.mode(total)
  standard_deviation = statistics.stdev(total)

  return mean, median, mode, standard_deviation

#Frequeny table of country and breeds of cats

def frequencies(api):
  chart = {}

  for cats in api:
    if cats['origin'] not in chart:
      chart[cats['origin']] = {}

    if cats['name'] not in chart[cats['origin']]:
      chart[cats['origin']][cats['name']] = 0

    chart[cats['origin']][cats['name']] += 1

  return chart

seperated = lifespanseperator(data)
seperated = weightseperation(data)
averages = average(seperated)
metriccalculations(averages)
lifespancalculations(averages)
frequencies(data)
