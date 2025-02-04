# Error Detection Techniques

## Description

This project contains implementations of two error detection techniques: Two-Dimensional Parity Check and Cyclic Redundancy Check (CRC). These techniques are used to detect errors in transmitted data and ensure data integrity.

### Two-Dimensional Parity Check
- Organizes a binary message into a matrix format and calculates parity bits for both rows and columns.
- Introduces a bit corruption and detects the exact position of the corrupted bit.

### Cyclic Redundancy Check (CRC)
- Uses polynomial division to generate a CRC code.
- Detects errors in the transmitted message by computing and verifying the CRC remainder.

## Technologies Used

* Python.

## Installation and Usage

### Prerequisites

* Python.
* Python IDE (e.g., PyCharm, VS Code, or IDLE).

**1. Clone the repository**  
git clone https://github.com/AndreiCIlies/Error_Detection_Techniques.git

**2. Open the project in the IDE**

**3. Run the application**  
### Two-Dimensional Parity Check  
- python TwoDimensionalParity.py
- Enter a binary message of length multiple of 7 when prompted.

### Cyclic Redundancy Check (CRC)  
- python CyclicRedundancyCheck.py
- Enter a binary message and a polynomial when prompted.
