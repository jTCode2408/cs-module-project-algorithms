'''
Input: an integer
Returns: an integer
'''

#Memoization/caching (saving): save work so it doesnt have to be re-computed.
#need some data structure to save the data
#array/dictionary most common
#if we check cache & see answer we're looking for is already there, return answer
#if cache doesnt have answer, how do we add it?
#1st time answer is calculated, save in cache. then access cache in  future times

def eating_cookies(n, cache=None):
    #base case: no more cookies
    if n == 0:
        return 1
    elif n < 0:
        return 0
    #check cache
    elif cache and cache[n] > 0: #check for cache & n already in cache index position
        return cache[n]
    #init cache if we dont have it
    else:
        if not cache:
            cache = [0 for _ in range(n + 1)]
            #= {i: 0 for i in range(n + 1)} <--dict version
            #save answer to cache
            #recursive case where there are still some cookies to be eaten
            #can do empty dict for cache ={}& say 'elif cache and n in cache' to ccheck if n is in cache
        cache[n]= eating_cookies(n-1, cache) + eating_cookies (n-2, cache) + eating_cookies(n-3, cache) #adding answers to cache after calculated once 
        #eating 1 cookie
     #eating 2 cookies
     #eating 3 cookies
    return cache[n] 


    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
