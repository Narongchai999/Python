temp=input("ป้อนอุณหภูมิ (องศา) :") #25c
degree=int(temp[:-1]) # การเอาทุกตัวในสตริง temp ยกเว้นตัวสุดท้าย
# และนำมาแปลงเป็น int
unit=temp[-1].upper() # เลือกข้อมูลตัวสุดท้าย #c,f
# .upper มาเพื่อแปลงตัวcหรือfเป็นพิมพ์ใหญ่กันกรณี พิมพ์ใหญ่พิมพ์เล็ก
if unit=="C":
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮน์"
if unit=="F":
    result=(degree-32)*5/9
    unit_result="เซลเซียส"
print("แปลงตัวเลข = ",temp," เป็น ",unit_result," = ",result)