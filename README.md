Myoelectric Prosthetic Arm: Affordable Innovation for All

Version: 1.0  
License: MIT  
       Authors: 
Pranav Ram && Shibi Kumar S

Introduction  
The Myoelectric Prosthetic Arm is an open-source project aimed at creating an affordable, functional prosthetic for individuals with limb differences. This arm responds to muscle signals using EMG sensors, is powered by an ESP32 microcontroller, and built with 3D-printed components.

Our goal is to make prosthetics more accessible, especially for communities where traditional prosthetics are too expensive. By combining affordable hardware with innovative software, this project offers a cost-effective alternative that’s easy to build and use.

What’s in the Build?

Key Hardware:  
- ESP32 Microcontroller – The central control unit  
- EMG Sensors – Detect muscle activity and send the data to the ESP32  
- Servo Motors – Control the arm's movements  
- 5V LiPo Battery – Powers the system  
- 3D-Printed Arm  – Custom-designed to fit servos and sensors  

Software Stack:  
- Python – Used for signal processing and controlling the servos  
- ESP-IDF – The development environment for the ESP32  
- FreeCad – For modeling the arm components  
- Slic3r – For preparing the 3D models for printing

Step-by-Step Build Guide

1. Design the Arm: We used FreeCad to design the structure of the arm, focusing on making it strong and functional. The components are designed to accommodate the servos and wiring while providing a natural range of movement. Once complete, export the design as an STL file.

2. 3D Print the Components: With the STL files ready, we sliced the design in Slic3r and printed the components on a 3D printer. The parts are made from durable materials to ensure they can handle everyday use.

3. Build the Circuit: The electronics are built around a custom-designed PCB. This board integrates the ESP32, EMG sensors, and servos. If you’re prototyping, you can use a breadboard initially. Once the PCB is ready, solder the components in place and test the connections.

4. Write the Python Code: The arm's movements are controlled by Python code, which processes the muscle signals detected by the EMG sensors. The code translates these signals into servo motor movements. Using ESP-IDF, we uploaded the code to the ESP32 and ran tests to fine-tune the responses.

5. Assemble the Arm: Now, assemble the 3D-printed parts and integrate the servo motors into the arm. Connect the servos and EMG sensors to the ESP32 via the PCB. Secure the wiring and ensure the battery is properly connected for consistent power.

6. Calibrate and Test: Attach the EMG sensors to the user’s forearm and test the system. The Python script will read the muscle signals and control the servo motors to move the prosthetic arm. Calibration may be needed to ensure the arm responds naturally to muscle contractions.

Diagrams and Visuals

- Final Prosthetic Arm:  ![proesthetic arm](https://github.com/user-attachments/assets/a5a47d0f-dabd-45ff-8e78-ed1763c8ff20)
- Final working video: ![PCB Schematic](link_to_video) 
- PCB Design: ![PCB Schematic](link_to_image) 

Building the System:  
1. Clone this repository to your local machine.  
2. Install the Python dependencies:  
    ```bash  
    pip install -r requirements.txt  
    ```  
3. Follow the hardware build steps and upload the code to the ESP32.


How to Use
1. Attach the EMG sensors to your forearm.  
2. Power the system with the LiPo battery.  
3. Run the Python script on the ESP32 to start the system.  
4. Test various muscle contractions and adjust the code for responsiveness if needed.


Support Us
If you find this project useful or inspiring, please consider giving it a star. It helps others discover the project and motivates us to keep improving it.

License
This project is released under the MIT License. You can find the full license details in the LICENSE file.
