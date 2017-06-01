#!/usr/local/bin/python


import sys

def get_date_price_value(set_value):
    #function to parse and get the date from
    date  = set_value.replace(')','').replace('(','').split(',')[0]
    date = date.replace("'",'')
    price  = set_value.replace(')','').replace('(','').split(',')[1]
    #price = int(price.replace('\n','').replace("'",''))
    #alternative implementation
    import string
    all=string.maketrans('','')
    nodigs=all.translate(all, string.digits)
    price = price.translate(all, nodigs)
    if price  == '':
        price = 0
    return (date,price)

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
        current_city =line[0]
        #print "CURRENT CITY::>" + str(current_city)
        if current_city == prev_city:
            value = line[1]
            #print "VALUE IS " + str(value)
            (date,price) = get_date_price_value(value)
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
            (date,price) = get_date_price_value(value)
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





