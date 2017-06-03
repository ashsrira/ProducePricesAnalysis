#!/usr/local/bin/python
import sys
def get_date_city_value(set_value):
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
    for line in sys.stdin:
        line = line.split('\t')
        if len(line) != 2:
            print "NA"
        else:            
            current_city,date =get_date_city_value(line[0])
            if current_city == date == 'NA':
                continue
            if current_city == prev_city:
                value = line[1]
                price = line[1]
                date_value = get_month(date)
                if date_value == month_value:
                    value_list.append(price)
                else:
                    if month_value != None:                
                        total = sum(int(i) for i in value_list)
                        avg = total/len(value_list)
                        value_list = []
                        month_list.append((month_value,avg))
                        month_value = date_value
                        value_list.append(price)
                    else:
                        month_value = date_value
                        value_list.append(price)
            else:
                if prev_city != None:
                    if ((month_value != None) and (len(value_list) != 0)):
                        total = sum(int(i) for i in value_list)
                        avg = total/len(value_list)
                        month_list.append((month_value,avg))
                    print '{0}\t{1}'.format(prev_city,month_list)
                month_list = []
                value_list = []
                month_value = None
                value = line[1]
                current_city,date =get_date_city_value(line[0])
                price=line[1]
                month_value = get_month(date)
                value_list.append(price)
                prev_city = current_city

    if ((month_value != None) and (len(value_list) != 0)):
        total = sum(int(i) for i in value_list)
        avg = total/len(value_list)
        month_list.append((month_value,avg))
        print '{0}\t{1}'.format(current_city,month_list)



if __name__ == "__main__":
    main()





