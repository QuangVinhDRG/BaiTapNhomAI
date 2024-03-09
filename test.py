import pandas
import matplotlib.pyplot as plt
import numpy
data = pandas.read_csv('weight-height.csv')
# file = open('test.txt', 'w', encoding='utf-8')
# file.write(str(data))
# file.close()
# data['Height'] = data['Height'].multiply(2.54)
# data['Weight'] = data['Weight'].multiply(0.45359237)
# print(data[data['Gender'] == 'Female']['Height'].head())
numbers = numpy.array([1, 2, 3, 4, 5, 6])
print(numbers)
print(numbers.reshape(3, 2))