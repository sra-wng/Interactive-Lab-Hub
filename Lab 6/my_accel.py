import time
import board
import busio
import adafruit_mpu6050

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect('farlab.infosci.cornell.edu', port=8883)

topic_accel = 'IDD/syw/c/accel'
topic_gyro = 'IDD/syw/c/gyro'
topic_temp = 'IDD/syw/c/temp'

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    accel = "Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration)
    gyro = "Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro)
    temp = "Temperature: %.2f C" % mpu.temperature
    client.publish(topic_accel, accel)
    client.publish(topic_gyro, gyro)
    client.publish(topic_temp, temp)
    time.sleep(1)