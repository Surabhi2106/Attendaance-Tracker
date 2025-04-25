import pandas as pd
from datetime import datetime
import os

# Define folder and file path
folder_path = r"C:\Users\Aditya\Desktop\Attendance Tracker\content"
file_path = os.path.join(folder_path, "attendance.csv")

# Create folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Load attendance or create a new DataFrame if file is missing or empty
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    attendance_df = pd.read_csv(file_path)
else:
    attendance_df = pd.DataFrame(columns=["Name", "Date", "Time"])

# Function to mark attendance
def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    new_entry = pd.DataFrame([{"Name": name, "Date": date, "Time": time}])
    
    global attendance_df
    attendance_df = pd.concat([attendance_df, new_entry], ignore_index=True)
    attendance_df.to_csv(file_path, index=False)
    print(f"\n✅ Attendance marked for {name} at {time} on {date}.")

# Input
name_input = input("Enter your name to mark attendance: ").strip()
if name_input:
    mark_attendance(name_input)
else:
    print("❌ Name cannot be empty!")

# Show all records
print("\n📋 Current Attendance Records:")
print(attendance_df)
