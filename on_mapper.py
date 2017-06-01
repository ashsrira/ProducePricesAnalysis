#!/usr/local/bin/python  
import sys
index = 0;
for line in sys.stdin:  
    if index == 0:
        index = index + 1
        continue
    keys = line.split(',')
    date = keys[0]
    #Flip the date to ensure sorted order is maintained
    temp = date.split('-')
    temp.reverse()
    date = '-'.join(temp)
    zone  = keys[1]
    centre =  keys[2]
    price = keys[3]
    key = centre
    price = price.replace('\r\n','')
    if 'NA' in str(price):
        continue
    else:   
        if '.' in price:
            price = price.replace('\r\n','')
            price = int(float(price))
            value = (date,price)
        value = (centre,date)
        print('{0}\t{1}'.format(value,str(price)))
