import os
import pyautogui
import time
import random
import string
import psutil

# Function to generate a random 4-letter word
def generate_random_word(length=4):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Function to check if Edge is running
def is_edge_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] and 'msedge' in process.info['name'].lower():
            return True
    return False

# Open Microsoft Edge
application_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
os.startfile(application_path)

# Wait for the browser to open
time.sleep(5)  # Adjust this delay if necessary
iterations =0
# Perform searches while Edge is running
print("Automation started. Close Edge to stop.")
while is_edge_running():
    random_word = generate_random_word()  # Generate a random word
    pyautogui.typewrite(random_word)     # Type the word
    pyautogui.press('enter')   
    iterations+=1
    if iterations >=11:
        time.sleep(1)
        break          # Press Enter
    time.sleep(8)                        # Wait for 3 seconds

print("Edge closed. Automation stopped.")