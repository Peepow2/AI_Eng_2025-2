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

### TODO#5

Plot loss and val_loss as a function of epochs.
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.plot(train_losses, label = 'Training Loss', color = 'blue', linestyle = 'solid')
plt.plot(val_losses, label = 'Validation Loss', color = 'red', linestyle = 'dashed')

plt.title('Training and Validation Loss over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.grid(True)
plt.show()
```
<hr>

### TODO#6

When does the model start to overfit?

**Ans:** <br>
เริ่ม Overfit เมื่อ Validation Loss เริ่มนิ่งหรือค่อยๆ ดีดตัวสูงขึ้น ในขณะที่ Training Loss ยังคงลดลง
<hr>

### TODO #7

Plot the learning rate as a function of the epochs.
```python
import matplotlib.pyplot as plt

epochs = range(1, len(learning_rates) + 1)

plt.figure(figsize=(8, 5))
plt.plot(epochs, learning_rates, marker='o', linestyle='-', color='green', label='Learning Rate')

#plt.yscale('log')

plt.title('Learning Rate Schedule over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Learning Rate (Log Scale)')
plt.xticks(epochs)
plt.grid(True, which = "both", ls = "-", alpha = 0.5)
plt.legend()

plt.show()
```
<hr>

### TODO #8

What makes the learning rate change?
(hint: try to understand the scheduler [ReduceLROnPlateau](https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.ReduceLROnPlateau.html))


**Ans:** <br>
ReduceLROnPlateau Scheduler ทำหน้าที่เป็นตัวปรับความเร็วในการเรียนรู้ของโมเดล โดยสังเกตค่า Validation Loss ในทุก ๆ Epoch หากพบว่าค่าความผิดพลาดหยุดลดลงหรือนิ่งอยู่ที่ระดับเดิม เป็นจำนวนรอบติดต่อกันตามที่ตั้งค่า patience ไว้ (ในที่นี้คือ 2 รอบ) ระบบจะถือว่าโมเดลไม่สามารถหาจุดที่แม่นยำกว่าเดิมได้ด้วยความเร็วปัจจุบัน Scheduler จึงลดค่า Learning Rate ลงตามสัดส่วนของ factor เพื่อบีบให้โมเดลค่อย ๆ ขยับ Weights ให้เข้าใกล้คำตอบที่ถูกต้องที่สุด
<hr>

