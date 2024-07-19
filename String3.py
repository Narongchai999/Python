name=input("ชื่อ-นามสกุล(คำนำหน้าแบบเต็ม) : ")
# .startswith ใช้ในการค้นหาคำที่อยู่ข้างหน้าสุด
if name.startswith("นาย"):
    print("เพศชาย")
elif name.startswith("เด็กชาย"):
    print("เพศชาย")
elif name.startswith("นาง"):
    print("เพศหญิง")
elif name.startswith("นางสาว"):
    print("เพศหญิง")
elif name.startswith("เด็กหญิง"):
    print("เพศหญิง")
else : print("ไม่สามารถระบุได้")

Lottery=input("ระบุเบอร์ล็อตเตอร์รี่ของท่าน : ")
# .endswith ใช้ในการค้นหาคำที่อยู่ท้ายสุด
if Lottery.endswith("47"):
    print("ยินดีด้วยคุณถูกรางวัลเลขท้าย 2 ตัว")
else : print("เสียใจด้วยคุณไม่ถูกรางวัล")