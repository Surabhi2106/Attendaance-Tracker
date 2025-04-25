# Attendaance-Tracker
Sure! Here's a concise version under 350 characters:  > A simple Python-based attendance tracker that records names with date and time in a CSV file. It auto-creates the folder if missing and displays current records in the terminal. Built using `pandas` and `datetime`, it's great for basic logging tasks in labs or small groups.

# 🧑‍💻 Attendance Tracker (Python)

A simple terminal-based Python attendance system that records names, date, and time into a CSV file. Attendance entries are stored in a local `attendance.csv` file under a `content/` folder on your desktop.

---

## 📂 Project Structure
Attendance Tracker/
├── attendance.py        # Main script for marking attendance
└── content/             # Folder for storing attendance.csv
    └── attendance.csv   # CSV file for storing attendance data


---

## 🛠 Requirements

- Python 3.10+ (Tested with Python 3.11 / 3.13)
- [pandas](https://pypi.org/project/pandas/)

Install required Python library:

pip install pandas



🚀 How to Run
🔹 Step 1: Clone the Repository
git clone https://github.com/<your-username>/attendance-tracker.git
cd attendance-tracker


Or simply download the .zip and extract it to your desktop.

Step 2: Edit the Folder Path (Optional)
Inside attendance.py, make sure this path matches your system

folder_path = r"C:\Users\Aditya\Desktop\Attendance Tracker\content"

🔹 Step 3: Run the Script
You can run it via terminal, command prompt, or VS Code:
python attendance.py


✍️ Features
✅ Marks current date and time for each name entered

💾 Saves data to content/attendance.csv

🛡️ Automatically creates the folder if it doesn’t exist

📋 Prints current attendance log after marking



📸 Sample Output
Enter your name to mark attendance: John
✅ Attendance marked for Surabhi at 14:53:10 on 2025-04-25.

📋 Current Attendance Records:
    Name        Date      Time
1   Surabhi   2025-04-25   14:53:10

📌 Notes
The script does not prevent duplicate entries.

It will append every time a name is entered.

You can extend it with:

Duplicate prevention per day

Export to Excel

GUI using Tkinter


🧑‍💼 Author
Surabhi Karmarkar
Ronald lobo














