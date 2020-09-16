'''
 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 

Base cases:
 - he is given 0 or less cookies. Return 0.
 - he is given 1 cookie. Return 1.  |
 - he is given 2 cookies. Return 2. | if n == 1 or n == 2: return n
 - he is given 3 cookies. Return 4.

 - he is given 4 cookies. Return 4
 - he is given 5 cookies. Return 3 
 - he is given 6 cookies. Return 2

 The solution required appears to allow several sessions eating the cookies.
 The cookie monster can only eat three cookies at a time.
 For every three cookies there are four ways the cookie monster can eat them.


Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    """
    Each time he eats cookies this function is called.
    When this function is called, he eats cookies in all possible permutations. He is quantum after all.

    """
    # Your code here
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return eating_cookies(2) + eating_cookies(3)
    elif n == 5:
        print(eating_cookies(2) + eating_cookies(3) + eating_cookies(4))
        return eating_cookies(2) + eating_cookies(3) + eating_cookies(4)
    elif n == 6:
        return eating_cookies(3) + eating_cookies(4) + eating_cookies(5)
    elif n >= 7:
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
