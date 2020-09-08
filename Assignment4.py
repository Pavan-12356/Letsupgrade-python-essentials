low=1042000
high=702648265
for num in range(low,high+1):
   x=len(str(num))
   sum=0
   temp=num
   while temp>0:
       digit=temp%10
       sum+=digit**x
       temp//= 10
   if num==sum:
       print("The first armstrong number is:",num)
       break
