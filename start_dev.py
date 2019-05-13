import psutil
import automate_dev as atd
import subprocess

process_name = "Dev-C++ IDE (32 bit)"
if process_name in (p.name for p in psutil.process_iter()):
    print(process_name + " is already executing ")
else:
    print("Preparing to start the process requested")
    subprocess.Popen(["C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"])
    print("Process started ")

atd.perform_automation()
