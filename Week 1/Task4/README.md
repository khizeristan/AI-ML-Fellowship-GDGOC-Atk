
# Task 4 — Libraries, Packaging & Production Readiness

## Features
- Modular Programming
- Virtual Environments (venv)
- Dependency Management
- Custom Python Package
- Logging Support

## Folder Structure


Task4/
├── modules/
├── mypackage/
├── test_package.py
├── requirements.txt
└── README.md


## Setup
```bash
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt

Usage
Modules
from modules.calculator import add, subtract
from modules.utils import greet

print(add(2,3))
print(greet("Hizar"))

Custom Package
from mypackage import multiply, shout, log_info

print(multiply(4,5))
print(shout("hello"))
log_info("Task 4 running!")


---

## **8️⃣ How to Run in Visual Studio**

1. Open **Task4 folder** in Visual Studio  
2. Make sure **venv is selected** in Python Environments  
3. Right-click `main.py` or `test_package.py` → **Set as Startup File**  
4. Press **F5** → Output will show  
5. All **imports and packages will work perfectly**

---

Hizar, agar chaho to main **ye folder structure ready ZIP bana ke de doon**, jisme **sab files already arranged** ho aur **tum bas VS me open karke F5 run karo**, bina kisi error ke.  

Kya main ye ready ZIP bana doon?
::contentReference[oaicite:0]{index=0}