a:list=["Ahmer Ali",18 ,["Cricket", "Progrming" ,"Coding"] ]
print(a)
# To Find Length
print(len(a))
# To Find Type
print(type(a))
# Find By Positive index
print(a[2])
# To Find By Negitive index
print(a[-2])
# To find  between Numbers Positive
print(a[:3])
# To Find between Number by Negitive index
print(a[-3:-1])
# To find Skip
print(a[0:3:2])
# List Constructor()
a:list=(("Ahmer" , "Ali"))
print(a)
# Copy Method 
a:list=["a","b","c"]
print(a)
b= a.copy()
c= list(a)
print(c)
print(b)
# Change the Value
a[1]="ahmer"
print(a)
# Change Value by insert method 
a.insert(2 , "Mamoon")
print(a)
# Add value in list by append method 
d = ["Ahmer", "Ali", "Mamoon"];
print(d)
e=["Ahmer and Arooj is lover and fauter wife husband "]
d.append("mamoon is the brother of Ahmer Ali")
d.extend(e)
print(d);
# Remove method of the element
d.remove("Ahmer")
print(d)
# Pop meyhod for removing method
d.pop()
print(d)