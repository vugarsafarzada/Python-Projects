from os import *
import time
import subprocess
import datetime

location = getcwd()
chdir('C:/Windows/System32')
system('color a')
system('mode 60')
print("---------------------------OS-GAR---------------------------")
#---------------------------
#show_inside
#show_path
#show_wifi
#run // $all, $here
#go_path
#go
#new_folder
#rename
#delete file
#delete folder
#power //$shut_down, $restart,$sleep
#version
#refresh
#os_gar
#cmd
#create_file
#select
#commands
#date
#exit
#---------------------------

version = "OS-GAR 1.6.4"
chdir(location)


def show_inside():
    x = 0
    for i in lst:
            x += 1
            txt = "{}. {}".format(x, i)
            print(' ', txt)

def show_path():
    filePath = getcwd()
    print(filePath)

def go_path():
    pth = input("Path: ")
    print('Moving...')
    try:
        chdir(pth)
        print('Done!')
    except:
        print("\n@ERROR!, That is wrong path!")

def select():
    nchos = 1
    print("1) $all")
    print("If you want stop selecting: '$stop'")

    while True:
        slc = input("{}.Select file: ".format(nchos))
        if slc in lst:
            selecteds.append(slc)
            nchos += 1
        elif slc == '$stop':
            print('-----------------------')
            print('Selected {} files:\n'.format(nchos-1))
            for z1 in selecteds:
                print(z1)
            break

        elif slc == '$all':
            for sc in lst:
                selecteds.append(sc)
                nchos += 1
            print('-----------------------')
            print('Selected {} files:\n'.format(nchos - 1))
            for z1 in selecteds:
                print(z1)
            break
        else:
            print('-----------------------')
            print("File is not find!")

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
    print("1) $all")
    print("2) $selected\n")
    try:
        rmv = input("File name: ")
        print("Searching... ")
        if rmv in lst:
            qrmv = input("Are you sure, delete '{}' file?(Y/N)".format(rmv))
            if qrmv == 'y' or qrmv == 'Y':
                remove(rmv)
                print("Done!")
            else:
                print("File didn't deleted!")
        elif rmv == '$all':
            print("Important! Must not be folder or directory in this path!")
            qrmv = input("Are you sure, delete all files?(Y/N)".format(rmv))
            if qrmv == 'y' or qrmv == 'Y':
                for i in lst:
                    remove(i)
                    print("'{}' deleting...".format(i))
        elif rmv == '$selected':
            try:
                for rm in selecteds:
                    print('{} deleting...'.format(rm))
                    remove(rm)
            except:
                print('@Error')
                print("There are folder!")
        else:
            print("'{}' file is not found!".format(rmv))
    except:
        print("There is folder or directory in this path")

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
    lct = getcwd()
    chdir('C:/Windows/System32')
    gt = getcwd()
    print('Moving this path: ', gt, '\n')

    print("1) $log_off")
    print("2) $restart")
    print("3) $shutdown\n")

    opns = input("power: ")

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

    chdir(lct)

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
    lct = getcwd()
    while True:
        chdir('C:/Windows/System32')
        print()
        shl = input("OS-GAR >> {}>".format(getcwd()))
        system(shl)
        if shl == 'exit':
            chdir(lct)
            break

def create():
        nam = input('File name: ')
        ext = input('File extension: ')
        dot = '.'
        if ext.startswith('.'):
            fle = nam + ext
        else:
            fle = nam + dot + ext

        print(fle, ' is creating...')

        if fle in lst:
            print('\n@ERROR!')
            print("'{}' already there is here".format(fle))
        else:
            try:
                system('type nul > {}'.format(fle))
                print("Done!")
            except:
                print('@ERROR')
                print("File is not created!")

def run():
    print("1) $all")
    print("2) $selected")
    print("3) $here\n")
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

    elif opn == "$selected":
        for r in selecteds:
            startfile(r)

    else:
        print("File is not found!")

def go():
    gopth = cmd[3:]
    lc = getcwd()
    golc = lc + "\\" + gopth
    if gopth in lst:
        try:
            chdir(golc)
            print('Moving...')
            print(getcwd())
        except:
            startfile(gopth)
    else:
        print("{} is not find!".format(gopth))

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
    print('* go/')
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
    print('* create_file')
    time.sleep(0.05)
    print('* select')
    time.sleep(0.05)
    print('* exit')
    time.sleep(0.05)
    print('-----------------------')

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

    if cmd == "create_file":
        create()

    if cmd == 'select':
        selecteds = []
        select()

    if cmd[:3] == 'go/':
        go()

    if cmd == "exit":
        exit()
        break

