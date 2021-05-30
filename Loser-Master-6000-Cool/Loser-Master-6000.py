import serial
import time

last_mult_5 = 0;

while True:
    f = open(r"C:\Users\91959\Desktop\PONG-BOOSTER\Cata-Pong\Cata-Pong_Data\StreamingAssets\CPU_Score.txt", "r")
    CPU_Score_Read = f.read()
    f.close();
    print(CPU_Score_Read)

    if int(CPU_Score_Read)%5 == 0 and int(CPU_Score_Read) != last_mult_5:
        last_mult_5 = CPU_Score_Read;
        ser = serial.Serial('COM3', 9800, timeout=1)
        time.sleep(2)
        ser.write(b'F')
        ser.close()
    time.sleep(1)