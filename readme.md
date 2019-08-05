# Robotframework Live CPU stats

This repo consist of generating live CPU stats while execution is in progress

---
### Prerequisite:

 - Install [psutil](https://pypi.org/project/psutil/)
    > `pip install psutil`

---
### Steps to Use:

 - Step 1: Download or clone this repo
 
 - Step 2: Copy `MemoryStatsListener.py` to your project

 - Step 3: Execute test case/suites using LogListener
   > - `robot --listener MemoryStatsListener.py Tests` 

 - Step 4: A new browser will be opened with logs
   > Note: Page refresh's for every 100 seconds.
   > - Users can modify reload time from .py file
   > - `<meta http-equiv="refresh" content="100" >`

---
### Screenshot

<img src="/memoryStats.jpg" alt="memoryStats">