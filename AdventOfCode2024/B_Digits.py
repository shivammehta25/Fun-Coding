def chatgpt(n, d):
    """
    Given:
      - n (positive integer)
      - d in {0,1,2,...,9}
    Returns:
      A list of odd digits in {1,3,5,7,9} that divide the number formed
      by writing digit 'd' exactly n! times in a row.
    """
    
    # We'll build a result list
    divisors = []
    
    # Check each odd digit from 1 to 9:
    for test_digit in [1, 3, 5, 7, 9]:
        if test_digit == 1:
            # 1 always divides anything
            divisors.append(1)
        
        elif test_digit == 3:
            # Divisible by 3 if sum of digits is multiple of 3.
            # sum of digits = d * (n!) => Check 3 | d*(n!)
            # => If n >= 3, then 3 | n!, so it's automatically divisible
            #    If n < 3, we need 3 | d
            if n >= 3:
                divisors.append(3)
            else:
                # n = 1 or 2
                if d in [3, 9]:
                    divisors.append(3)
        
        elif test_digit == 5:
            # Divisible by 5 iff last digit is 0 or 5 => repeated digit must be 5
            if d == 5:
                divisors.append(5)
        
        elif test_digit == 7:
            # From the analysis: if n >= 3 => always divides
            # If n = 1 => the number is just d => need d = 7
            # If n = 2 => the number is 11*d => need 7 | d => d=7
            if n >= 3:
                divisors.append(7)
            else:
                if d == 7:
                    divisors.append(7)
        
        elif test_digit == 9:
            # Divisible by 9 iff sum of digits is multiple of 9 => 9 | d*(n!)
            # If n >= 6 => n! has at least two factors of 3 => 9 | n!, so always
            # If 1 <= n < 6 => check smaller n case by case
            if n >= 6:
                divisors.append(9)
            else:
                # n in {1, 2, 3, 4, 5}
                if n == 1:
                    # number is just d => need d=9
                    if d == 9:
                        divisors.append(9)
                elif n == 2:
                    # number = 11*d => sum of digits = 2*d => not multiple of 9 unless 2*d=9 => impossible
                    pass
                else:
                    # n in {3,4,5}
                    # sum of digits = (n!) * d, but mod 9 we can reduce n!
                    # from the table => must be d in {3,9}
                    if d in [3, 9]:
                        divisors.append(9)
    
    return divisors


def solve(inp):
    n, d = inp
    
    ans = [1]
    to_check = [3, 5, 7, 9]
    
    print(chatgpt(n, d))

    
    


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        solve(map(int, input().split()))