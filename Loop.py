# โครงสร้างควบคุมแบบทำซ้ำ
#i=1 #ตัวนับจำนวนรอบ
#while i<=3: #ทุกคำสั่งภายใต้loop while จะทำซ้ำ
#    print("รอบที่ ",i)
#    i=i+1 # เพิ่มค่าของ i จนกว่าจะครบข้อกำหนด แล้วหยุดการทำงานของโปรแกรม
          # ถ้าไม่เพิ่มค่าของ i loopจะไม่มีจุดสิ้นสุด

#Loop while จะทำงานเมื่อเงื่อนไขเป็นจริง ยังไม่รู้จำนวนรอบที่ชัดเจน
#Loop for รู้จำนวนรอบที่ชัดเจน

#i=1
#summation=0
#averrage=0
#cout=int(input("ระบุจำนวรอบ : "))
#while i<=cout:
#    summation+=i # เก็บผลรวมของ i แต่ละรอบ 1+2+3
#    print("รอบที่  = ",i ,"ค่าsum = ",summation)
#    i+=1 # 1 2 3 4 5
#averrage=summation/cout
#print("ผลรวม = ", summation)
#print("เฉลี่ย = ", averrage)

#for i in range(3) # 0 1 2
#for i in range(1,11,2): # start,stop,step 

summation=0
for i in range(1,11): # summation
# ระบุจำนวนรอบการทำงานตั้งแต่รอบที่ 1 ถึง 11
    summation+=i
    print("รอบที่  = ",i,"ผลรวม",summation)
print("ผลรวม = ", summation)
print("เฉลี่ย = ", summation/10)

