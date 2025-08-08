def insertion_sort(my_list):
  n=len(my_list)
  for i in range(1,n):
    j=i
    while my_list[j-1]>my_list[j] and j>0:
      my_list[j-1],my_list[j]=my_list[j],my_list[j-1]
      j-=1
      
my_list=[3,1,7,-1,9,5]
print("before sorting: ",my_list)
insertion_sort(my_list)
print("after sorting: ",my_list)
