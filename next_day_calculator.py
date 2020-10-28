# PF-Tryout

def generate_next_date(day, month, year):
    next_day = 0
    next_month = 0
    next_year = 0
    if 1 <= day <= 27:
        next_day = day + 1
        next_month = month
        next_year = year
        print(next_day, "-", next_month, "-", next_year)
        date = next_day, next_month, next_year
        return date
    elif day == 28:
        if month == 2:
            if year % 4 == 0:
                next_day = 29
                next_month = month
                next_year = year
                print(next_day, "-", next_month, "-", next_year)
                return next_day, next_month, next_year
            else:
                next_day = 1
                next_month = month + 1
                next_year = year
                print(next_day, "-", next_month, "-", next_year)
                return next_day, next_month, next_year
        else:
            next_day = day + 1
            next_month = month
            next_year = year
            print(next_day, "-", next_month, "-", next_year)
            return next_day, next_month, next_year
    elif day == 29:
        if month == 2:
            if year % 4 == 0:
                next_day = 1
                next_month = month + 1
                next_year = year
                print(next_day, "-", next_month, "-", next_year)
                return next_day, next_month, next_year
            else:
                print("[", day, "-", month, "-", year, "]      Not valid either date or month or year!")
                return next_day, next_month, next_year
        else:
            next_day = day + 1
            next_month = month
            next_year = year
            print(next_day, "-", next_month, "-", next_year)
            return next_day, next_month, next_year
    elif day == 30:
        if month % 2 == 0:
            if month == 8:
                next_day = day + 1
                next_month = month
                next_year = year
                print(next_day, "-", next_month, "-", next_year)
                return next_day, next_month, next_year
            elif month == 12:
                next_day = 1
                next_month = month + 1
                next_year = year + 1
                print(next_day, "-", next_month, "-", next_year)
                return next_day, next_month, next_year
            else:
                next_day = 1
                next_month = month + 1
                next_year = year
                print(next_day, "-", next_month, "-", next_year)
                return next_day, next_month, next_year
        else:
            next_day = day + 1
            next_month = month
            next_year = year
            print(next_day, "-", next_month, "-", next_year)
            return next_day, next_month, next_year
    elif day == 31:
        if month == 12:
            next_day = 1
            next_month = 1
            next_year = year + 1
            print(next_day, "-", next_month, "-", next_year)
            return next_day, next_month, next_year
        else:
            next_day = 1
            next_month = month + 1
            next_year = year
            print(next_day, "-", next_month, "-", next_year)
            return next_day, next_month, next_year


date = generate_next_date(21, 5, 2015)
print(date)
