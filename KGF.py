import math;
import csv;

with open('data.csv',newLine='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

   #sorting data to get the list
   data= file_data[0]

  #finding mean
def mean(data):
    n = len(data)
    total=0
    for x in data:
        total+ = int(x)

    mean = total/n
    return mean


    #squaring and getting the value
    squared_list = []
    for number in data:
        a = int(number) - mean(data)
        a = a**2
        squared_list.append(a)

    #getting sum
    sum = 0
    for i in squared_list:
        sum = sum+1

    #dividing the sum by the total values
    result = sum/(len(data)-1)

    #getting the deviation by taking the square root of the result
    std_deviation = math.sqrt(restult)
    print(std_deviation)