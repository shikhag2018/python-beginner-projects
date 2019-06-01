day_31=[1,3,5,7,8,10,11]
day_30=[4,6,9,11]

def next_date(day,month,year):
    if (year%4)==0:
         if (year%100)==0:
              if (year%400)==0:
                  leap_yr=True
              else:
                  leap_yr=False
         else:
             leap_yr=True
    else:
        leap_yr=False
        
    if day==31:
        if month in day_31:
            next_day=1
            next_month=month+1
            next_year=year
        else:
            print("invalid date")
    
    elif day==30:
        if month in day_30:
            next_day=1
            next_month=month+1
            next_year=year
        else:
            print ("invalid date")
    elif  day==28 and leap_yr==True:
        next_day=day+1
        next_month=month
        next_yr=year
    elif month==12:
        next_day=1
        next_month=1
        next_year=year+1
    elif day==29 and month==2:
        next_day=1
        next_month=month+1
        next_year=year
    else:
        next_day=day+1
        next_month=month
        next_year=year
    try:
        print(next_day,"-",next_month,"-",next_year)
    except  NameError:
        pass
next_date(31,4,2019)
         
        

    
        
        
        
    
        
