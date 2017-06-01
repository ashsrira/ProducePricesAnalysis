#!/usr/local/bin/python


import sys, traceback

def get_date_price_value(set_value):
    #function to parse and get the date from
    temp = set_value.translate(None,'()')
    city = temp.split(',')[0]
    date = temp.split(',')[1]
    city = city.translate(None,"'").translate(None,' ')
    date = date.translate(None,"'").translate(None,' ')
    return (city,date)


def get_month(date_value):
    return '-'.join(date_value.split('-')[:-1])
    
def main(separator='\t'):
    for line in sys.stdin:
        temp = line.split('\t')
        try:
            temp2 = temp[0].translate(None,'()')
            city = temp2.split(',')[0]
            date = temp2.split(',')[1]
        except:
            print line
            traceback.print_exc()
            return 0
        print temp[0] + temp[1]



if __name__ == "__main__":
    main()





