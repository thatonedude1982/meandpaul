import subprocess
import time
import os

proc = " "
stat = " "
cron = " "

while True:
    with open("tasklist.txt", "r+") as proc_file:  # top lines creates file and header for ps aspect
        os.system("cls")
        proc_file.write("----------------------------------------------------------------------------------\n")
        proc_file.flush()  # clears contents of buffer to prevent writing above header
        subprocess.Popen(["tasklist"], stdout=proc_file, stderr=proc_file)  # passes tasklist cmd to host
        print("Pulling new process data.")
        time.sleep(5)  # adding pause and "loading" screen so user knows script is still running
        print("Done!")
        subprocess.Popen(["type", "tasklist.txt"])  # will return no data to screen if sleep is removed.
        """
        code block to handle storing inputs as separate variables and comparing. if files are different, print
        difference and continue, if same, continue
        """

        time.sleep(2)  # will change to 55 when program is finished to make each separate aspect of script take 1 min
        os.system("cls")  # clears screen

    with open("stat.txt", "r+") as stat_file:  # creates file and header for netstat aspect
        os.system("cls")
        stat_file.write("----------------------------------------------------------------------------------\n")
        stat_file.flush()
        stat = subprocess.Popen(["netstat", "-ano"], stdout=stat_file , stderr=stat_file)
        print("Pulling new netstat data.")
        time.sleep(5)  # adding pause and "loading" screen so user knows script is still running
        print("Done!")
        stat = subprocess.Popen(["type", "stat.txt"])
        """
        code block to handle storing inputs as separate variables and comparing. if files are different, print
        difference and continue, if same, continue
        """

        time.sleep(2)  # change to 55 when finished. left shorted to test cycles of program
        os.system("cls")

    with open("sch_tasks.txt", "r+") as sch_tasks_file:  # creates file and header for scheduled tasks aspect
        os.system("cls")
        cron_file.write("-----------------------------------------------------------------------------------\n")
        cron_file.flush()
        cron = subprocess.Popen(["schtasks", "/query", "/v", "/fo CSV"], stdout=sch_tasks_file, stderr=sch_tasks_file)
        print("Pulling new scheduled tasks data.")
        time.sleep(5)  # adding pause and "loading" screen so user knows script is still running
        print("Done!")
        cron = subprocess.Popen(["type", "sch_tasks.txt"])
        """
        code block to handle storing inputs as separate variables and comparing. if files are different, print
        difference and continue, if same, continue
        """

        time.sleep(5)
        os.system("cls")

print("-----------------------------------------------------------------------------------")
