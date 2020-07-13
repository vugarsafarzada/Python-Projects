from os import *
import time
import subprocess

print("---------------OS-GAR---------------")
#---------------------------
#show_inside
#show_path
#show_wifi
#run // $all, $here
#go_path
#calculator
#new_folder
#rename
#delete file
#delete folder
#power //$shut_down, $restart,$sleep
#version
#refresh
#os_gar
#commands
#exit
#---------------------------

version = "OS-GAR 0.3.5"

while True:
    print()
    lst = listdir()
    cmd = input("Command: ")
    if cmd == "show_inside":
        print()
        x = 0
        for i in lst:
            x += 1
            txt = "{}. {}".format(x, i)
            print(txt)
    if cmd == "show_path":
        filePath = getcwd()
        print("")
        print(filePath)

    if cmd == "run":
        opn = input("Run file/folder: ")
        print("Searching... ")
        time.sleep(1.8)

        if opn in lst:
            print("'{}' is found!".format(opn))
            time.sleep(0.5)
            startfile(opn)

        elif opn == "$all":
            print("Runing all files...")
            for all in lst:
                time.sleep(0.5)
                startfile(all)
        elif opn == "$here":
            hr = getcwd()
            startfile(hr)
            time.sleep(0.5)
            print('Done!')


        else:
            print("File is not found!")

    if cmd == "go_path":
        pth = input("Path: ")
        print('Moving...')
        time.sleep(0.5)
        chdir(pth)
        print('Done!')

    if cmd == "new_folder":
        nam = input("Folder name: ")
        if nam in lst:
            print("Already '{}' folder existing in that path!".format(nam))
        else:
            mkdir(nam)
            print("Done!")

    if cmd == "rename":
        nm = input("Name file/folder: ")
        if nm in lst:
            print("'{}' is found!".format(nm))
            tonm = input("New name: ")
            rename(nm,tonm)
            print('Done!')
        else:
            print("'{}' is not found!".format(nm))

    if cmd == "delete_file":
        rmv = input("File name: ")
        print("Searching... ")
        time.sleep(0.8)
        if rmv in lst:
            qrmv = input("Are you sure, delete '{}' file?(Y/N)".format(rmv))
            if qrmv == 'y' or qrmv == 'Y':
                remove(rmv)
                print("Done!")
            else:
                print("File didn't deleted!")
        else:
            print("'{}' file is not found!".format(rmv))

    if cmd == "delete_folder":
        print('Important: Folder must is empty!')
        rf = input("Folder name: ")
        print("Searching... ")
        time.sleep(0.8)
        if rf in lst:
            qrf = input("Are you sure, delete '{}' folder?(Y/N)".format(rf))
            if qrf == 'y' or qrf == 'Y':
                rmdir(rf)
                print("Done!")
            else:
                print("Folder didn't deleted!")
        else:
            print("'{}' folder is not found!".format(rf))


    if cmd == "power":
        print("\n1) $log_off")
        print("2) $restar")
        print("3) $shutdown\n")

        opns = input("power: ")
        chdir('C:/Windows/System32')
        gt = getcwd()
        print('Moving this path: ',gt,'\n')

        if opns == "$log_off":
            print("Power going to sleep!")
            slp = input("Are you sure?(Y/N):")
            if slp == "Y" or slp == "y":
                system("shutdown /l")
                print('Please wait...')

        elif opns == "$shutdown":
            print("Power going to shut down!")
            slp = input("Are you sure?(Y/N):")
            if slp == "Y" or slp == "y":
                system("shutdown /s")
                print('Please wait...')


        elif opns == "$restart":
            print("Power going to restart!")
            slp = input("Are you sure?(Y/N):")
            if slp == "Y" or slp == "y":
                system("shutdown /r")
                print('Please wait...')

    if cmd == "commands":
        print('\nAll commands of {}:'.format(version))
        print('-----------------------')
        print('* show_inside')
        time.sleep(0.05)
        print('* show_path')
        time.sleep(0.05)
        print('* show_wifi')
        time.sleep(0.05)
        print('* go_path')
        time.sleep(0.05)
        print('* run / $all, $here')
        time.sleep(0.05)
        print('* new_folder')
        time.sleep(0.05)
        print('* rename')
        time.sleep(0.05)
        print('* refresh')
        time.sleep(0.05)
        print('* os_gar')
        time.sleep(0.05)
        print('* delete_file')
        time.sleep(0.05)
        print('* delete_folder')
        time.sleep(0.05)
        print('* version')
        time.sleep(0.05)
        print('* power')
        time.sleep(0.05)
        print('* commands')
        time.sleep(0.05)
        print('* exit')
        time.sleep(0.05)
        print('-----------------------')

    if cmd == 'show_wifi':

        results = subprocess.check_output(["netsh", "wlan", "show", "network"])
        results = results.decode("ascii")

        results = results.replace("\r", "")
        ls = results.split("\n")
        ls = ls[4:]
        ssids = []
        x = 0
        while x < len(ls):
            if x % 5 == 0:
                ssids.append(ls[x])
            x += 1
        for i in ssids:
            print(i)
        input("Press ENTER for exit!")

    if cmd == "os_gar":
        startfile('OS-GAR.py')

    if cmd == "refresh":
        startfile('OS-GAR.py')
        break

    if cmd == "version":
        print(version)

    if cmd == "exit":
        ques = input("Are you sure?(Y/N): ")
        if ques == 'Y' or ques == 'y':
            print("Goodbye!")
            break
