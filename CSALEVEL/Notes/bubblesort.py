#revision No.1
array=[1,8,6,9,0,4,5,3,10,2,7]
def bubble_sort(array):

	length=len(array)-1
	swapped = True

	 # If zero swaps occur in a loop, then it's already sorted
	while swapped == True:
		swapped = False
		# Iterate through the list n times, ignoring last items as they have already been sorte
		for i in range(length):
			if array[i+1] < array[i]:
				temp = array[i+1]
				array[i+1] = array[i]
				array[i] = temp
				swapped = True
		length -= 1
	return array

print(bubble_sort(array))
