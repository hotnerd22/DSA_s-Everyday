#Python Implementation for the selection sort.
arr = [64,25,12,22,11]
def selection_sort(arr): #defining the function
    for start in range(len(arr)): #outer for loop (first position and value are (0 and 64)
        print(start)
        minpos = start #assume first value as the minimum value. i.e minpos = start = 0
        for i in range(start+1, len(arr)): #loop from the next position of the start+1, first position and value of the second loop are(1 ans 25)
            if arr[i]<arr[minpos]: 
                minpos=i     #update minpos to i if above condition is true (main code for getting samllest value), for ex, arr[1] < arr[0] = 25 < 64 = yes
                #hence update minpos to 1 and so continue....
        (arr[start],arr[minpos])=(arr[minpos],arr[start])
        #here as we get the minimum value from the internal for loop, we will swap the positions (values) of the start and minpos.
        #again the same process will repeat from the next element. (which is 25)
        print(arr)
selection_sort(arr)

