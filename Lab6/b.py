s="Hello. This is Shashwat Kumar Trivedi!!!"
for i in s:
    if(not (i>='a' and i <='z') and not( i>='A' and i<='Z') and not(i==' ')):
        s=s.replace(i,'')
print(s)