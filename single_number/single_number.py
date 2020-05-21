'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

#arr to hold numbers

def single_number(arr):
    no_dupes = []
#iterate through nums arr
    for x in arr:
        #check if number is already in no dupres list
        if x not in no_dupes:
            no_dupes.append(x)
            #if not append
        else:
            no_dupes.remove(x)
            #if is remove

            #when done iteratin, only number in no dupes is odd number out to return
    return no_dupes[0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")