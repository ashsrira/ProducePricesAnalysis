#!/usr/local/bin/python  
import sys
import re, plotly
import matplotlib.pyplot as plt

def generate_graph():
    x = open('/Users/hadoop/python_files/monthly_avg_output.txt')
    temp = x.readlines()
    for item in temp:
        inner_dict= {}
        x_axis_list= []
        y_axis_list = []
        city = item.split('\t')[0]
        temp3  = item.split('\t')[1]
        temp4 =  re.findall("\(.*?\)", temp3)
        for value in temp4:
            year_month  = str(value.replace('(','').replace(')','').translate(None,"'").split(',')[0])
            price  = int(value.replace('(','').replace(')','').translate(None,"'").split(',')[1])
            if '99' in year_month:
                continue
            x_axis_list.append(year_month)
            y_axis_list.append(int(price))
        #plotting graph for city
        temp_x_axis = range(0,len(x_axis_list))
        print temp_x_axis
        print x_axis_list
        plt.xticks(temp_x_axis, x_axis_list,rotation='vertical',fontsize=9)
        plt.plot(temp_x_axis, y_axis_list)
        plt.ylabel('Price per Kg (Rs)')
        plt.xlabel('Year-Month (YY-MM)')
        plt.title('Monthly Average Price of Produce for  --  {0}'.format(city))
        ax = plt.subplot()
        ax.xaxis.get_children()[1].set_size(len(x_axis_list))
        for label in ax.xaxis.get_ticklabels()[::2]:  
            label.set_visible(False)  
        plt.show() 

if '__name__' == '__main__':
    generate_graph()
