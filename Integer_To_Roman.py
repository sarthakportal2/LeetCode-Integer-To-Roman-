class Solution:
    def intToRoman(self, num: int) -> str:
        #new_approach
        #min. runtime (42ms)T(C(N))=O(N) and SC(N)=O(N) as it requires contigous memory allocation and level wise iteration
        d={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000,}#Dictionary declare
        out=[]#output array declare
        for k,v in reversed(d.items()):#dictionary bottom up iteration
            while num >0:#iterating from positive number
                if v<=num:out.append(k);num-=v#appending kth elem into the list 
                else:break#goto oper to next statement
        return "".join(out)#priniting Joined nullable string 

     #i=0;j=i+1;op=0
    #old_approach
       # for i in range(len(d)):
        #    for k in range(i-1,len(d)):
         #       if d[i]<d[j]:op=d[j]-d[i]
          #      elif d[j+1]<=d[j+2] and d[j+3]:op=d[j+2]-d[j+1]
           #     elif d[j+3]<=d[j+4] and d[j+5]:op=[j+4]-d[j+3]
            #    #if d[i]<len(d[j]-1):d[k]-=d[i]
        #return op
                    
