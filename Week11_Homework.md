### TODO #1

Explain each line of code in the function preprocess_for_ff()

**Ans:**

1.   reshape((-1, 5x5x3)) คือ การทำ Flatten ข้อมูลให้เป็นเวกเตอร์ขนาด 5x5x3 เพื่อป้อนเข้าสู่โมเดล โดยที่ 5x5 คือ grid around rain-measued station และ 3 คือ Color Channels
2.   reshape((-1, 1)) คือ การทำ Flatten ข้อมูลให้เป็นเวกเตอร์หนึ่งคอลัมน์

โดยที่ ตัวแปร train, val และ test เก็บข้อมูลในเดือน 6-8, 9 และ 10 ตามลำดับ
<hr>
### TODO #2

Why is the loss MSE?

**Ans:** <br>
เนื่องจากข้อมูลเป็นแบบ Regression เป็นการพยากรณ์ปริมาณน้ำฝนซึ่งเป็นตัวเลขต่อเนื่อง และต้องการความแม่นยำ โดยถ้าโมเดลพยากรณ์ผิดพลาดมาก (เช่น ฝนตกหนักแต่ทายว่าไม่มีฝน) ค่า Loss จะสูง
<hr>
### TODO #3

What is the activation function in the final dense layer? and why? Do you think there is a better activation function for the final layer?

**Ans:** <br>
ในโมเดล FeedForwardNN เลเยอร์สุดท้ายไม่มีการใส่ activation function <br>

งาน Regression นี้เป้าหมายคือการพยากรณ์ค่าปริมาณน้ำฝน ซึ่งเป็นตัวเลขต่อเนื่อง การไม่ใส่ activation function ทำให้โมเดลสามารถ Output ค่าออกมาเป็นตัวเลขใด ๆ ก็ได้โดยไม่ถูกจำกัด และความสอดคล้องกับ Loss เมื่อเราใช้ MSE การรับค่าจาก Linear Layer โดยตรงจะทำให้การคำนวณ Gradient เพื่อปรับ weight ดีขึ้น โดยที่อาจจะมี function ที่ดีกว่า เช่น ReLU ที่ป้องกันไม่ให้โมเดลพยากรณ์ค่าติดลบ
<hr>
### TODO#4

Explain why the first linear layer has number of parameters = 15200

**Ans:** <br>
Parameters = Input x Output + Output(Bias) = (75 x 200) + 200 = 15,000 + 200 = 15,200
<hr>
