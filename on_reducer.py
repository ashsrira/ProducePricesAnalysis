#!/usr/local/bin/python


import sys

def get_date_city_value(set_value):
    #function to parse and get the date from
    #print set_value
    #date  = set_value.replace(')','').replace('(','').split(',')[1]
    #date = date.replace("'",'')
    #city  = set_value.replace(')','').replace('(','').split(',')[0]
    #city = city.replace("'",'')
    #city = city.replace(" ",'')

    #alternate implementations
    temp = set_value.translate(None,'()')
    temp = temp.split(',')
    if len(temp) != 2:
        return ('NA','NA')
    city = temp[0]
    date = temp[1]
    city = city.translate(None,"'").translate(None,' ')
    date = date.translate(None,"'").translate(None,' ')
    return (city,date)

def get_month(date_value):
    return '-'.join(date_value.split('-')[:-1])
    
def main(separator='\t'):
    # input comes from STDIN (standard input)
    last_key = None 
    running_total = 0
    prev_city = None
    key_dict = {}
    # vars needed for monthly avg
    month_value = None
    month_list = []
    value_list = []
    #data = read_input(sys.stdin)
    for line in sys.stdin:
        #print "LINE GOT is :"
        #print line
        line = line.split('\t')
        if len(line) != 2:
            print "NA"
        else:            
            current_city,date =get_date_city_value(line[0])
            if current_city == date == 'NA':
                continue
            #print "CURRENT CITY::>" + str(current_city)
            if current_city == prev_city:
                value = line[1]
                #print "VALUE IS " + str(value)
                price = line[1]
                date_value = get_month(date)
                #print "DATE VALUE::> " + str(date_value)
                if date_value == month_value:
                    value_list.append(price)
                else:
                    #print "DATE VALUE IS NOT THE SAME AS MONTH VALUE"
                    if month_value != None:                
                        total = sum(int(i) for i in value_list)
                        avg = total/len(value_list)
                        value_list = []
                        month_list.append((month_value,avg))
                        #print "MONTH LIST :::> " + str(month_list)
                        month_value = date_value
                        value_list.append(price)
                    else:
                        month_value = date_value
                        value_list.append(price)
                #print "Value LIST :::> " + str(value_list)
            else:
                if prev_city != None:
                    #print "Moving to next city"
                    if ((month_value != None) and (len(value_list) != 0)):
                        total = sum(int(i) for i in value_list)
                        avg = total/len(value_list)
                        month_list.append((month_value,avg))
                    print '{0}\t{1}'.format(prev_city,month_list)
                month_list = []
                value_list = []
                month_value = None
                value = line[1]
                #print "VALUE ::>" + str(value)
                value = line[1]
                current_city,date =get_date_city_value(line[0])
                price=line[1]
                #print "DATE::>" + date
                #print "PRICE::>" + str(price)
                month_value = get_month(date)
                #print "MONTH_VALUE::>" + str(month_value)
                value_list.append(price)
                #print value_list
                prev_city = current_city
                #print "PREV CITY::>" + str(prev_city)

    if ((month_value != None) and (len(value_list) != 0)):
        total = sum(int(i) for i in value_list)
        avg = total/len(value_list)
        month_list.append((month_value,avg))
        print '{0}\t{1}'.format(current_city,month_list)



if __name__ == "__main__":
    main()





