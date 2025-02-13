# QR Code-Based Gate Opening System using Raspberry Pi

This project is a **QR Code-Based Gate Opening System** developed using a Raspberry Pi. The system scans a QR code and automatically opens the gate if the code is verified. The project aims to create a secure and automated gate control solution.

## Features
- QR code scanning for authentication
- Real-time QR code verification
- Automated gate control using Raspberry Pi
- Python-based implementation for seamless control
- User-friendly and secure system

## Technologies Used
- **Hardware:** Raspberry Pi  
- **Programming Language:** Python  
- **Libraries:** OpenCV, pyzbar (for QR code scanning and decoding)  
- **Additional Tools:** GPIO for controlling the gate motor  

## Prerequisites
Ensure you have the following installed on your Raspberry Pi:  
- Python 3.x  
- OpenCV (`pip install opencv-python`)  
- pyzbar (`pip install pyzbar`)  
- RPi.GPIO (`pip install RPi.GPIO`)  

## Project Setup
1. **Connect the Hardware:**
   - Connect the gate motor to the Raspberry Pi GPIO pins.
   - Ensure the camera module is connected for QR code scanning.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/qr-code-gate-system.git
   cd qr-code-gate-system
3.**Install the Required Packages:**

```bash
pip install -r requirements.txt
```
4.**Run the Project:**

```bash
python main.py
```

# How It Works
- 1.The system continuously scans for a QR code using the camera.
- 2.Once a QR code is detected, it is verified against the predefined valid codes.
- 3.If the QR code is valid, the Raspberry Pi triggers the motor to open the gate.
- 4.The gate closes automatically after a set duration.
# Project Structure
```
qr-code-gate-system/
│
├── main.py             # Main Python script to run the project
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── images/             # Sample images for testing
```
# Future Improvements
- 1.Add a web-based interface for managing QR codes.
- 2.Implement notification alerts via email or SMS.
- 3.Integrate with cloud services for logging and monitoring.

# Author
**Abhirup Mohapatra**
*B.Tech in Electronics and Communication Engineering (Silicon University, Bhubaneswar)*
