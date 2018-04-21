import subprocess
import time
import os

proc = " "
stat = " "
cron = " "

while True:
    with open("proc.txt", "w") as proc_file:  #top lines creates file and header for ps aspect
        os.system('clear')
        proc_file.write("----------------------------------------------------------------------------------\n")
        proc_file.flush()  #clears contents of buffer to prevent writing above header
        proc = subprocess.Popen(['ps' , '-A'] , stdout=proc_file , stderr = proc_file)  #passes ps -A to host
        print("Pulling new process data.")
        time.sleep(5)  # adding pause and "loading" screen so user knows script is still running
        print("Done!")
        proc = subprocess.Popen(['cat' , 'proc.txt'])  # will return no data to screen if sleep is removed.
        """
        code block to handle storing inputs as separate variables and comparing. if files are different, print
        difference and continue, if same, continue
        """

        time.sleep(2)  # will change to 55 when program is finished to make each separate aspect of script take one minute
        os.system('clear')  # clears screen

    with open("stat.txt", "w") as stat_file:  #creates file and header for netstat aspect
        os.system('clear')
        stat_file.write("----------------------------------------------------------------------------------\n")
        stat_file.flush()
        stat = subprocess.Popen(['netstat' , '-plantu' , '|' , 'sort'] , stdout=stat_file , stderr = stat_file)
        print("Pulling new netstat data.")
        time.sleep(5)  # adding pause and "loading" screen so user knows script is still running
        print("Done!")
        stat = subprocess.Popen(['cat' , 'stat.txt'])
        """
        code block to handle storing inputs as separate variables and comparing. if files are different, print
        difference and continue, if same, continue
        """

        time.sleep(2)  # change to 55 when finished. left shorted to test cycles of program
        os.system('clear')

    with open("cron.txt", "w") as cron_file:  # creates file and header for crontab aspect
        os.system('clear')
        cron_file.write("-----------------------------------------------------------------------------------\n")
        cron_file.flush()
        cron = subprocess.Popen(['crontab' , '-l'], stdout=cron_file , stderr = cron_file)
        print("Pulling new crontab data.")
        time.sleep(5)  # adding pause and "loading" screen so user knows script is still running
        print("Done!")
        cron = subprocess.Popen(['cat' , 'cron.txt'])
        """
        code block to handle storing inputs as separate variables and comparing. if files are different, print
        difference and continue, if same, continue
        """

        time.sleep(5)
        os.system('clear')

print("-----------------------------------------------------------------------------------")
