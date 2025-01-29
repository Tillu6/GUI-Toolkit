# GUI-Toolkit
# GUI Nmap Toolkit

![image](https://github.com/user-attachments/assets/c05e77b6-177b-466c-9fea-a5bb9524e50c)


A simple and intuitive **GUI-based Nmap Toolkit** built with **Python** and **Tkinter**, enabling users to perform port scanning efficiently.

## Features
- Perform **port scans** using Nmap with an easy-to-use graphical interface.
- View detailed results including **port states** and **running services**.
- Supports **customizable port ranges** for scanning.
- Handles errors and user interruptions gracefully.

## Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **Nmap** (Install via `sudo apt install nmap` or [Nmap official website](https://nmap.org/))
- **Python-Nmap** (`pip install python-nmap`)

## Installation
```bash
git clone https://github.com/yourusername/gui-nmap-toolkit.git
cd gui-nmap-toolkit
pip install -r requirements.txt
```

## Usage
Run the tool with:
```bash
python gui_nmap.py
```

## Code Overview
The toolkit leverages the `nmap` Python module to execute scans and display results in a Tkinter-based GUI.

```python
scanner = nmap.PortScanner()
scanner.scan(target, f"{start_port}-{end_port}", arguments='-Pn')
```

## Screenshot
![image](https://github.com/user-attachments/assets/a487816c-cda0-44b4-8641-4c92c153587d)


## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork, improve, and submit pull requests!

---
**Author:** SAKETH REDDY POREDDY | **GitHub:** [Tillu6](https://github.com/Tillu6)

