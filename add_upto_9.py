def check_registration_number(reg_number):
    temp = reg_number
    result_sum = 0
    result = False
    if 1000 <= reg_number <= 9999:
        while temp > 0:
            rem = temp % 10
            result_sum += rem
            temp = temp//10
        if result_sum > 9:
            temp = result_sum
            rem = temp % 10
            temp = temp // 10
            result_sum = rem + temp
            if result_sum == 9:
                result = True
            else:
                result = False
        elif result_sum < 9:
            result = False
        else:
            result = True
    else:
        result = False
    return result

print(check_registration_number(9999))
