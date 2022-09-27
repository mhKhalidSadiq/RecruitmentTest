#Written By: Khalid Sadiq (AI Engineer)
#Dated : 27/09/2022

def merge_lists(list1,list2):
  m = len(list1)
  n = len(list2)
  merged_list = [] # size m+n
  i,j = 0,0
  while i < m and j < n:
    if list1[i] < list2[j]:
       merged_list.append(list1[i])
       i+=1
    else:
       merged_list.append(list2[j])
       j+=1
  merged_list = merged_list + list1[i:] + list2[j:]

  return  merged_list

list1 = [1,3]
list2 = [2]
final_list = merge_lists(list1,list2)
n = len(final_list)
i = int(n/2)
if n%2 ==0: # even 
   res = (final_list[i] + final_list[i-1] ) / 2
else:
  res = final_list[i]
print("Final Merged and Sorted list is ", final_list)
print("Median is ", res)

#Time complexity for above funtion is O(m+n) as there is a linear loop for m/n lenth


##Output:
#Final Merged and Sorted list is  [1, 2, 3]
#Median is  2
