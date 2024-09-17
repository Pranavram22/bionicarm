import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import serial
import time

# Hardware configuration
num_channels = 8
sampling_rate = 200
servo_pin = 18
servo_freq = 50

# EMG sensor configuration
sensor_port = '/dev/ttyUSB0'
sensor_baudrate = 9600

# Servo motor control
def control_servo(angle):
    duty_cycle = (angle / 180) * 10 + 2.5
    pwm.ChangeDutyCycle(duty_cycle)

# EMG data acquisition and processing
def acquire_emg_data():
    ser = serial.Serial(sensor_port, sensor_baudrate)
    data = []
    for i in range(sampling_rate):
        raw_data = ser.readline().strip()
        emg_values = [float(value) for value in raw_data.split(',')]
        data.append(emg_values)
    ser.close()
    return np.array(data)

# Feature extraction
def extract_features(emg_data):
    features = []
    for channel in range(num_channels):
        features.append(np.mean(emg_data[:, channel]))
        features.append(np.var(emg_data[:, channel]))
        features.append(np.max(emg_data[:, channel]))
        features.append(np.min(emg_data[:, channel]))
    return features

# Classification (replace with your desired algorithm)
def classify_features(features):
   
    predicted_gesture = 0  # Replace with your prediction
    return predicted_gesture

# Main loop
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.PWM, frequency=servo_freq)
    pwm = GPIO.PWM(servo_pin, servo_freq)
    pwm.start(0)

    while True:
        emg_data = acquire_emg_data()
        features = extract_features(emg_data)
        predicted_gesture = classify_features(features)

        # Map predicted gesture to 
        servo_angle = 0  # Replace with your mapping logic

        control_servo(servo_angle)

        time.sleep(0.1)  # Adjust delay as needed

    pwm.stop()
    GPIO.cleanup()
