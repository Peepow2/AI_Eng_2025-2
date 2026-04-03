### TODO #1

Explain each line of code in the function preprocess_for_ff()

**Ans:**

1.   reshape((-1, 5x5x3)) คือ การทำ Flatten ข้อมูลให้เป็นเวกเตอร์ขนาด 5x5x3 เพื่อป้อนเข้าสู่โมเดล โดยที่ 5x5 คือ grid around rain-measued station และ 3 คือ Color Channels
2.   reshape((-1, 1)) คือ การทำ Flatten ข้อมูลให้เป็นเวกเตอร์หนึ่งคอลัมน์

โดยที่ ตัวแปร train, val และ test เก็บข้อมูลในเดือน 6-8, 9 และ 10 ตามลำดับ

### TODO #2

Why is the loss MSE?

**Ans:** <br>
เนื่องจากข้อมูลเป็นแบบ Regression เป็นการพยากรณ์ปริมาณน้ำฝนซึ่งเป็นตัวเลขต่อเนื่อง และต้องการความแม่นยำ โดยถ้าโมเดลพยากรณ์ผิดพลาดมาก (เช่น ฝนตกหนักแต่ทายว่าไม่มีฝน) ค่า Loss จะสูง
