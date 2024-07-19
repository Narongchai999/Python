fname="narongchai"
lname="chobarsa"
age="16"
salary=55555.555555
#text="ชื่อ : {0}\tนามสกุล : {1}\tอายุ : {2}\nอาชีพ : {3}\tเงินเดือน : {4:.2f}"#สามารถระบุตำแหน่งใน{}ได้
text="ชื่อ : {}\tนามสกุล : {}\tอายุ : {}\nอาชีพ : {}\tเงินเดือน : {:.2f}" #:.2f คือการปัดทศนิยมให้เหลือ 2 ตำแหน่ง
print(text.format(fname,lname,age,"Programmer",salary))