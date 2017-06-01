#!/usr/local/bin/python  
import sys
import re, plotly
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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
            print "APPENDING"
            print year_month
            print price
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
        #img = mpimg.imread('{0}_monthly.png'.format(city))
        #mpimg.imsave('{0}_monthly.png'.format(city), img)
        #figure = plt.gcf()
        #figure.set_size_inches(8, 6)
        #plt.savefig('/Users/hadoop/python_files/output_monthly/{0}_monthly.png'.format(city),dpi = 200) 
        #plt.close()
        plt.show() 
        #savefig('{0}_monthly.png'.format(city))
        #plt.show()
        # #
        # trace0 = go.Scatter(
        #     x = random_x,
        #     y = random_y0,
        #     mode = 'lines',
        #     name = 'lines'
        # )
        # data = [trace0]
        # layout = dict(title = 'Monthly Average Prices',
        #     xaxis = dict(title = 'Year/Month'),
        #     yaxis = dict(title = 'Price in Rs per Kg'),
        # )
        # fig = dict(data=data, layout=layout)
        # py.iplot(fig, filename='styled-line')
