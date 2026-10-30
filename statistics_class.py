import math
#This project is the creation of the statistics built-in module in python

#Creating the Class
class Statistics():
  def __init__(self, lst):
    self.lst = lst

#Count object that counts each value in the list
  def count(self):
    return len(self.lst)

#Sum object that adds each value in the list together
  def sum(self):
    total = 0
    for num in self.lst:
      total += num

    return total

#Min object that determines the smallest value in the list
  def min(self):
    smallest = self.lst[0]
    for num in self.lst:
      if num < smallest:
        smallest = num

    return smallest

#Max object that determines the largest value in the list
  def max(self):
    largest = self.lst[0]
    for num in self.lst:
      if num > largest:
        largest = num

    return largest

#Range object that determines the range of the list
  def range(self):
    return self.max() - self.min()

#Mean object that determines the mean of the list
  def mean(self):
    return self.sum() / self.count()

#Median object that determines the mean of the list
  def median(self):
    sortedlst = sorted(self.lst)
    length = int(self.count()/2)
    if self.count() % 2 == 0:
      newmedian = (sortedlst[length - 1] + sortedlst[length]) / 2
      return newmedian
    return sortedlst[length]

#Mode object that determines the mode of the list
  def mode(self):
    compiled = {}
    for num in self.lst:
      if num not in compiled:
        compiled[num] = 0
      compiled[num] += 1

    largest = 0
    mode_val = None

    for key, value in compiled.items():
      if value > largest:
        largest = value
        mode_val = key

    return {'mode': mode_val, 'count': largest}

 #Variance object that determines the variance of the list   
  def var(self):
    avg = self.mean()
    squareddifference = [(num - avg)**2 for num in self.lst]
    
    sum = 0
    for num in squareddifference:
      sum += num
    
    return sum / (self.count() - 1)

#Standard deviation object that determines the standard deviation of the list
  def std(self):
    return math.sqrt(self.var())
    
  #Frequency Distribution object that determines the frequency of the object.
  def freq_dist(self):
    compiled = {}
    for num in self.lst:
      if num not in compiled:
        compiled[num] = 0
      compiled[num] += 1
    
    frequencies = []
    for num, num_times in compiled.items():
      percentages = (num_times / self.count()) * 100
      frequencies.append((percentages, num))

    return sorted(frequencies, key=lambda num: num[0], reverse= True)

#Initializing the Class and using its methods  
data = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 29.76
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.27
print('Variance: ', data.var()) # 18.27
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
