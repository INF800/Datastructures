n_calls = 0
def fib(n):
    """
    TIME       : O(2^n) - EXPONENTIAL GROWTH
    """
    global n_calls
    n_calls += 1

    if n==0:
        return 0
    if n==1:
        return 1

    return fib(n-2) + fib(n-1) 

memo = {}
n_calls = 0
def _fib(n):
    global n_calls
    n_calls += 1

    # First, try to return from memo if possible
    if n in memo:
        return memo[n]
    
    # else,
    # Second, grow memo 
    if n==0:
        memo[n] = 0
        return 0
    if n==1:
        memo[n] = 1
        return 0

    ret = _fib(n-2) + _fib(n-1)    
    memo[n] = ret

    return ret

if __name__=='__main__':
    n = 100 #1000
    # with memoisation
    print(_fib(n), f'calls(n={n}): {n_calls}') # why calls x2 ? in text it is x1  