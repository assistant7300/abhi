#Pascal Triangle

n=int(input("enter no of rows:"))
li=[]
for i in range(0,n):
   tem_list=[]
   for j in range(0,i+1):
      if j==0 or j==i:
       tem_list.append(1)
      else:
         tem_list.append(li[i-1][j]+li[i-1][j-1])
   li.append(tem_list)
   print(tem_list) 
