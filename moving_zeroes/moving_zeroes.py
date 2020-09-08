'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #2 pointers for either direction
    #zeroes to left
    #if not zero, should be right
    left = 0
    right = len(arr) -1 #whole array to traverse

    while left <= right:
        if arr[left] ==0 and arr[right] != 0: #if left pointer sees zero and right is not a zero
            arr[left], arr[right] = arr[right], arr[left] #swap 
            left +=1
            right -=1
        else:
            if arr[left] !=0:
                left +=1
            if arr[right] == 0:
                    right -=1

    return arr

    

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")