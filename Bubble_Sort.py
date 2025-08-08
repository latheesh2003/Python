def Bubble_sort(my_list):
  n=len(my_list)
  for i in range(0,n):
    for j in range(0,n-i-1):
      if(my_list[j]<my_list[j+1]):
         my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
  print("this is Bubble sort: ",my_list)


my_list=[]
for i in range(0,7):
  num=int(input(f"enter{i} element in list: "))
  my_list.append(num)
  
#Number1=set(map(int,my_list.split()))
print("this is the original list: ",my_list)
Number1=set(my_list)
print("this is the Set elements: ",Number1)
my_list1=list(Number1)
print("it is before the bubble sort",my_list1)
Bubble_sort(my_list1)