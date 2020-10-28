import next_day_calculator
def test_generate_next_date_1():
    calculated_date = next_day_calculator.generate_next_date(1,1,2020)
    expected_date = 2, 1, 2020
    assert expected_date == calculated_date
    
def test_generate_next_date_2():
    calculated_date = next_day_calculator.generate_next_date(29,2,2015)
    expected_date = 0, 0, 0
    assert expected_date == calculated_date
    
def test_generate_next_date_3():
    calculated_date = next_day_calculator.generate_next_date(28,2,1999)
    expected_date = 1, 3, 1999
    assert expected_date == calculated_date

def test_generate_next_date_14():
    calculated_date = next_day_calculator.generate_next_date(31,12,1815)
    expected_date = 1, 1, 1816
    assert expected_date == calculated_date
   
