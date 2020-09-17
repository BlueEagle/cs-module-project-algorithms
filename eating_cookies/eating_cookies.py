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


def eating_cookies(n, cache=None):
    """
    Each time he eats cookies this function is called.
    When this function is called, he eats cookies in all possible permutations. He is quantum after all.

    """
    # Your code here
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(
            n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 0

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
