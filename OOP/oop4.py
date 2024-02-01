import calendar
class masti:
    def __init__(self,b_date,b_month,b_year):
        self.b_date = b_date
        self.b_month = b_month
        self.b_year = b_year

    def givetmin(self):
        m = 0
        for i in range(self.b_year,2024):
            m = m + 525600
            if self.b_year%4==0:
                m = m + 1440

        for i in range(1,self.b_month):
            _,days = calendar.monthrange(2024 , i)
            if days==28:
                m = m + 40320
            if days==30:
                m = m + 43200
            else:
                m = m + 44640

        for i in range(1,self.b_date+1):
            m = m + 1440 
        
        return print(m)

def main():
    b_date = int(input("enter your bith date: "))
    b_month = int(input("enter your bith month: "))
    b_year = int(input("enter your bith year: "))

    birth = masti(b_date,b_month,b_year)
    print(birth)
    birth.givetmin()

main()