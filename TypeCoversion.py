X=10
Y=3.1
Z="20"
#แปลงจาก str เป็น int
result1=X+int(Z)
#แปลงจาก int เป็น str
result2=str(X)+Z
#แปลงจาก int เป็น float
result3=Y+float(X)
print(result1)
print(result2)
print(result3)
Z=float(Z) 
Z=Z+50
print(Z)