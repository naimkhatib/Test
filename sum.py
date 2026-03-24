print ("Lets Do Some Math .....")
count=0
sum=0
max=0
m=input("Enter x: ")
while m !='9999':
    #for i in range(4):
        count+=1
        sum+=int(m)
        if max<=int(m):
         max=int(m)
        m=input("Enter x: ")
print("count=",count,"sum=",sum, "max=",max)
print("avg=",sum/count)
      
