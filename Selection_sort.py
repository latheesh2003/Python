def select_sort(my_list):
  n=len(my_list)
  for i in range(0,n-1):
    curt_min=i
    for j in range(i+1,n):
      if(my_list[j]>my_list[curt_min]):
        curt_min=j
    my_list[i],my_list[curt_min]=my_list[curt_min],my_list[i]


my_list=[2,6,5,1,3,4]
print('before the sorting',my_list)
select_sort(my_list)
print('sorted List',my_list)