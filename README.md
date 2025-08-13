# SmartExcelCracker

**SmartExcelCracker** is an intelligent, customizable Python tool for unlocking encrypted Excel files. It supports staged brute-force strategies, flexible password patterns, and real-time GUI monitoring of password attempts.

---

## Features

- **Custom Fixed Arrays**: Specify known number sequences or character patterns (e.g., "135").  
- **Array Position Priority**: Attempt fixed arrays first at the start, end, or middle of passwords.  
- **Flexible Password Lengths**: Configure minimum and maximum password lengths.  
- **Multiple Modes**:
  - Mode 1: Digits only  
  - Mode 2: Digits + Letters  
  - Mode 3: Digits + Letters + Special Characters  
- **Short Password Priority**: Attempts shorter passwords first to improve success probability.  
- **Custom Dictionary**: Insert predefined words into password attempts.  
- **GUI Real-Time Display**: Monitor current password attempts in a simple Tkinter window.  
- **Phase-Based Strategy**: Tries high probability combinations first, then lower probability ones.  

---

## Cracking Strategy

**SmartExcelCracker** uses a multi-phase, priority-based approach to optimize password recovery efficiency:

1. **High Probability Phase**  
   - Passwords with the fixed array at prioritized positions (start > end > middle)  
   - Shortest lengths first  
   - Simpler character modes (digits only)  

2. **Medium Probability Phase**  
   - Passwords with the fixed array in non-prioritized positions  
   - Medium length passwords  
   - Expanded character sets (digits + letters)  

3. **Low Probability Phase**  
   - Longer passwords with complex character sets (digits + letters + special characters)  
   - Custom dictionary words inserted into generated passwords  
   - Full brute-force over remaining combinations  

**Key Principles**:

- **Short passwords first**: Reduces expected search time for typical passwords.  
- **Fixed array constraints**: Significantly narrows search space.  
- **Mode prioritization**: Attempts simpler character sets before moving to complex ones.  
- **Stage separation**: Ensures high probability combinations are fully attempted before low probability brute-force.  

**ASCII Flowchart:**

'''
+----------------------------+
|  Start Password Cracking   |
+------------+---------------+
             |
             v
+----------------------------+
|  High Probability Phase    |
|  - Fixed array at         |
|    prioritized positions  |
|  - Short passwords first  |
|  - Simple mode (digits)   |
+------------+---------------+
             |
             v
+----------------------------+
|  Medium Probability Phase  |
|  - Fixed array in non-    |
|    prioritized positions   |
|  - Medium length passwords|
|  - Mode: digits + letters |
+------------+---------------+
             |
             v
+----------------------------+
|  Low Probability Phase     |
|  - Longer passwords       |
|  - Complex modes: digits +|
|    letters + special chars|
|  - Insert custom dict     |
|  - Full brute-force       |
+------------+---------------+
             |
             v
+----------------------------+
|  Password Found?           |
+------------+---------------+
     | Yes                     | No
     v                         |
+----------------+              |
| Display Password|<-------------+
+----------------+
'''

---

## Installation

1. Clone the repository or download the script.  
2. Install required Python package:

```bash
pip install msoffcrypto-tool
````

---

## Configuration

All user-customizable parameters are located in `config.py`. Modify them according to your files and preferences.

```python
# config.py

encrypted_file = "/path/to/encrypted.xlsx"      # Path to your encrypted Excel file
output_file = "/path/to/unlocked.xlsx"         # Path for decrypted output

fixed_array = "135"                             # Fixed number/letter sequence
array_positions_priority = ["start","end","middle"] # Order to try fixed array positions
min_length = 4
max_length = 11
mode_priority = [1, 2, 3]                       # 1=Digits, 2=Digits+Letters, 3=Digits+Letters+Special
custom_dict = ["2025", "abcd"]                 # Optional custom dictionary
```

> **Note:** Replace `/path/to/...` with your actual file paths.

---

## Usage

Run the main script:

```bash
python SmartExcelCracker.py
```

* A GUI window will appear showing the currently attempted password.
* When the password is found, it will display:

```
Password correct! Password is: <password>
```

---

## Notes

* For long passwords or complex character sets, brute-force attempts may take significant time.
* Recommended to start with short passwords and high probability modes.
* Ensure you have sufficient memory and disk space when attempting large combinations.

---

## License

This project is open-source and free to use. Use responsibly and only on files you are authorized to access.