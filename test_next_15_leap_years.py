import next_15_leap_years

def test_cal_next_15_leap_years1():
    result=next_15_leap_years.cal_next_15_leap_years(2002)
    assert result==[2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060]

def test_cal_next_15_leap_years2():
    result=next_15_leap_years.cal_next_15_leap_years(2015)
    assert result==[2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072]

def test_cal_next_15_leap_years3():
    result=next_15_leap_years.cal_next_15_leap_years(1999)
    assert result==[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056]

def test_cal_next_15_leap_years4():
    result=next_15_leap_years.cal_next_15_leap_years(1845)
    assert result==[1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1900, 1904]
    
                   
