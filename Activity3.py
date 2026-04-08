list1=[4,5,6,1,2,9]
print(list1)
count=0
for i in list1:
    count+=i

average=count/len(list1)
print("The average is ",average)
print("The sum of charcters is ",count)
list1.sort()
print("The smallest number in the sequence is ",list1[0])
print("The largest number in the sequence is ",list1[-1])