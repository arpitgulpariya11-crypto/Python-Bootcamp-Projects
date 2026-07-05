# Python-Bootcamp-Projects
A collection of Python scripts developed during my Data Analyst bootcamp, 

markdown
# Python Automation & Health Tracking Basics

Welcome to my Python repository! This project contains foundational Python scripts developed during my data analytics training to demonstrate file automation, data handling, and custom conditional logic.

## 📁 Repository Contents

### 1. ⚙️ Automatic File Sorter
* **File:** `Automatic_File_Sorter.py`
* **Description:** An automated background script that scans a designated desktop directory and dynamically organizes files into corresponding folders based on their extensions (`.csv`, `.png`, `.jpg`, `.txt`).
* **Key Features:** Uses a `while True` loop and `time.sleep()` to constantly run quietly in the background without user intervention.

### 2. 🧮 Interactive BMI Calculator
* **File:** `BMI_Calculator.py`
* **Description:** A text-based application that prompts users for their personal data metrics (Name, Weight, Height) to instantly calculate their Body Mass Index.
* **Key Features:** Features optimized, non-overlapping `if-elif-else` conditional structures to accurately categorize user health risks across standard threshold groups.

---

## 🛠️ How To Run the Projects Locally

### Prerequisites
Make sure you have Python installed on your machine along with Jupyter Notebook or any standard IDE (VS Code, PyCharm).

### Setup Instructions
1. Clone or download this repository to your local machine.
2. For the **File Sorter**, open the script and update the `path` variable line with your specific target folder path:
   ```python
   path = r"C:/Your/Target/Folder/Path/"
   ```
3. Run the script, and drop mixed files into that directory to watch them auto-organize!
