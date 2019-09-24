def front_times(str,n):
    '''
    Given a string and a non-negative int n, we'll
    say that the front of the string is the first 3
    chars, or whatever is there if the string is less
    than length 3. Return n copies of the front;
   
    '''
    return str[:3] * n

Print(front_times('Chocolate', 2))
Print(front_times('Chocolate', 3))
Print(front_times('Abc', 3))