# เริ่มต้นเกม
import random
number_answer = random.randint(1, 100)


# รับค่าตัวเลขที่ผู้เล่นทายและแปลงเป็น int
guess_player = int(input("Enter Number : "))
if guess_player == number_answer :
    print("You Won")
else:
    print("You Lose")


# ตรวจสอบว่าผู้เล่นทายถูก
