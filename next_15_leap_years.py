def cal_next_15_leap_years(year):
    list_of_nxt_15_yrs = []
    if year % 4 == 0:
        for var in range(1, 16):
            if year % 100 == 0:
                if year % 400 == 0:
                    list_of_nxt_15_yrs.append(year)
                else:
                    pass
            else:
                list_of_nxt_15_yrs.append(year)
            year = year + 4
        return list_of_nxt_15_yrs
    else:
        while year % 4 != 0:
            year = year + 1
        list_of_nxt_15_yrs = cal_next_15_leap_years(year)
        return list_of_nxt_15_yrs



test = cal_next_15_leap_years(2002)

