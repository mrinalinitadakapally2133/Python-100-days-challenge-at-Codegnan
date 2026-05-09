sum.py
#array opearations appened delete insert
print("Length of array:", len(arr))
arr.append(90)
print("array after append:", arr)
arr.insert(2, 25)
print("array after inserting:", arr)
arr.remove(30)
print("array after deleting:", arr)
arr.sort()
print("array after sorting:"< arr)
arr.sort(reverse=True)
print("array after sorting in descending order:", arr)
new arr= sorted(arr)
print("new sorted array:", new_arr)
arr[5] = 60
print("array after updating:", arr)