from os import *
import time
import subprocess
import datetime
system('color a')
print("------------------------------OS-GAR------------------------------")
#---------------------------
#show_inside
#show_path
#show_wifi
#run // $all, $here
#go_path
#new_folder
#rename
#delete file
#delete folder
#power //$shut_down, $restart,$sleep
#version
#refresh
#os_gar
#cmd
#commands
#date
#exit
#---------------------------

version = "OS-GAR 1.4.8"
location = getcwd()

def show_inside():
    x = 0
    for i in lst:
            x += 1
            txt = "{}. {}".format(x, i)
            print(' ', txt)

def show_path():
    filePath = getcwd()
    print(filePath)

def run():
    print("1) $all")
    print("2) $here\n")
    opn = input("Run file/folder name: ")
    print("Searching... ")

    if opn in lst:
        print("'{}' is found!".format(opn))
        startfile(opn)

    elif opn == "$all":
        print("Runing all files...")
        for all in lst:
            startfile(all)

    elif opn == "$here":
        hr = getcwd()
        startfile(hr)
        print('Done!')

    else:
        print("File is not found!")

def go_path():
    pth = input("Path: ")
    print('Moving...')
    chdir(pth)
    print('Done!')

def new_folder():
    nam = input("Folder name: ")
    if nam in lst:
        print("Already '{}' folder existing in that path!".format(nam))
    else:
        mkdir(nam)
        print("Done!")

def rnm():
    nm = input("Name file/folder: ")
    if nm in lst:
        print("'{}' is found!".format(nm))
        to_name = input("New name: ")
        rename(nm, to_name)
        print('Done!')
    else:
        print("'{}' is not found!".format(nm))

def delete_file():
    rmv = input("File name: ")
    print("Searching... ")
    if rmv in lst:
        qrmv = input("Are you sure, delete '{}' file?(Y/N)".format(rmv))
        if qrmv == 'y' or qrmv == 'Y':
            remove(rmv)
            print("Done!")
        else:
            print("File didn't deleted!")
    else:
        print("'{}' file is not found!".format(rmv))

def delete_folder():
    print('Important: Folder must is empty!')
    rf = input("Folder name: ")
    print("Searching... ")
    if rf in lst:
        qrf = input("Are you sure, delete '{}' folder?(Y/N)".format(rf))
        if qrf == 'y' or qrf == 'Y':
            rmdir(rf)
            print("Done!")
        else:
            print("Folder didn't deleted!")
    else:
        print("'{}' folder is not found!".format(rf))

def power():
    print("1) $log_off")
    print("2) $restart")
    print("3) $shutdown\n")

    opns = input("power: ")
    chdir('C:/Windows/System32')
    gt = getcwd()
    print('Moving this path: ', gt, '\n')

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

def commands():
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
    print('* run')
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
    print('* date')
    time.sleep(0.05)
    print('* cmd')
    time.sleep(0.05)
    print('* exit')
    time.sleep(0.05)
    print('-----------------------')

def show_wifi():
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

def os_gar():
    chdir(location)
    startfile('OS-GAR.py')

def refresh():
    chdir(location)
    startfile('OS-GAR.py')

def versionOSGAR():
    print(version)

def exit():
    print("Goodbye!")

def date():
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def shell():
    while True:
        chdir('C:/Windows/System32')
        print()
        shl = input("OS-GAR >> {}>".format(getcwd()))
        system(shl)
        if shl == 'exit':
            break
#-------------------------------------------

while True:

    lst = listdir()

    print()
    cmd = input("Command: ")
    print()

    if cmd == "show_inside":
        show_inside()

    if cmd == "show_path":
        show_path()

    if cmd == "run":
        run()

    if cmd == "go_path":
        go_path()

    if cmd == "new_folder":
        new_folder()

    if cmd == "rename":
        rnm()

    if cmd == "delete_file":
        delete_file()

    if cmd == "delete_folder":
        delete_folder()

    if cmd == "power":
        power()

    if cmd == "commands":
        commands()

    if cmd == 'show_wifi':
        show_wifi()

    if cmd == "os_gar":
        os_gar()

    if cmd == "refresh":
        refresh()
        break

    if cmd == "version":
        versionOSGAR()

    if cmd == "date":
        date()

    if cmd == "cmd":
        shell()

    if cmd == "exit":
        exit()
        break

