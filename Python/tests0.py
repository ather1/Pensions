from  prime import  is_prime

def test_is_prime(n, expected):
    if is_prime(n) == expected:
        print(f"Test Passed is_prime({n}) has matched expected result: {expected} ")
    else:
        print(f"Test Failed is_prime({n}) has not matched expected result:{expected}")