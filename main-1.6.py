# Version: 1.6
# Release date: 17.07.2022

version = 1.6

import os
import sys
import pyuac
import ctypes
import winreg
import logging
import requests
import colorama
import subprocess
import dns.resolver
import zipfile
from shutil import copyfile, rmtree, unpack_archive
from pythonping import ping
from win32api import GetLogicalDriveStrings
from logging import info, debug, error, basicConfig, DEBUG
from termcolor import colored
from os import system, path, chdir, getenv, getlogin, mkdir
from speedtest import Speedtest
from time import sleep
from tempfile import gettempdir

system("cls")
ctypes.windll.kernel32.SetConsoleTitleW(f"OT-Optimizer {version} - www.discord.gg/RMQcevDWng")

username = getlogin()
APPDATA = getenv('APPDATA')
yes = ["y", "Y", "yes", "Yes", "YES"]

basicConfig(
    level=DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style="{",
    filename=f"OTO-Log_{username}.log",
    filemode="a"
)


info("\n" + 140*"-" + "\n")
info("STOP, READ CAREFULLY!")
info("This file is for developers only, please do not change, modify or delete this file!")
info("Send this file when prompted.")
info("More information can be found here: www.discord.gg/t3gWbBdbNQ")
debug(f"Program with version {version} has been started.")

drive_letter = getenv('HOMEDRIVE')

links = ['https://cdn.discordapp.com/attachments/985667930962403360/988882811287113808/clean.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/988883043206975558/dns_er.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/988483339897929798/net_er.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/985670447515455548/LogParser.dll',
         'https://cdn.discordapp.com/attachments/985667930962403360/985670448010387567/Interop.MSUtil.dll',
         'https://cdn.discordapp.com/attachments/985667930962403360/985670447775498310/UnparkCPU.exe',
         'https://cdn.discordapp.com/attachments/985667930962403360/987026646555058227/test.reg',
         'https://cdn.discordapp.com/attachments/985667930962403360/987026646378872852/test2.reg',
         'https://cdn.discordapp.com/attachments/985667930962403360/997937119165161634/Turn_on_Game_Mode.reg',
         'https://cdn.discordapp.com/attachments/985667930962403360/997991749660192808/sdi.zip',
         'https://cdn.discordapp.com/attachments/985667930962403360/997997020277133322/sdi.bat']

unique_link = 'https://cdn.discordapp.com/attachments/985667930962403360/988904728404557854/dns_backup.bat'

if not pyuac.isUserAdmin():
    info("UAC access: FALSE")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    debug("Re-ran with admin!")
    exit()
else:
    info("UAC access: TRUE")

debug("Defining show_menu()...")
def show_menu():
    print(30*"-")
    print(f"OT-Optimizer v{version}")
    print(30*"-")

debug("Defining clear_last_line()...")
def clear_last_line():
    print("\033[A                             \033[A")

show_menu()
print("Downloading assets...\n")
chdir(gettempdir())
debug("Requesting download...")

download_error = False
counter = 0
for link in links:
    counter += 1
    try:
        debug(f"Downloading {link}...")
        r = requests.get(link, allow_redirects=True)
        open(link.split("/")[-1], 'wb').write(r.content)
        debug(f"Downloaded {link} to {gettempdir()}")
        if counter < 10:
            counter = str(counter)
            counter = "0" + counter
        print(f'({counter}/12) Downloaded {link.split("/")[-1]}')
        counter = int(counter)
    except Exception as error_:
        download_error = True
        error(f"ERROR 0x1: Critical issue occured while downloading file, {error_}")
        space = ""
        if counter < 10:
            space = ""
            counter = str(counter)
            counter = "0" + counter
        print(f'({str(counter)}/12){space}', colored(f'Error {link.split("/")[-1]}', 'red'))
        if isinstance(counter, str):
            counter.split("0")
        counter = int(counter)
try:
    debug(f"Downloading {unique_link}...")
    r = requests.get(unique_link, allow_redirects=True)
    open(unique_link.split("/")[-1], 'wb').write(r.content)
    debug(f"Downloaded {unique_link} to '{drive_letter}\\OTO-Backup\\dns_backup.bat'")
    counter += 1
    print(f'({str(counter)}/12) Downloaded {unique_link.split("/")[-1]}')
except Exception as error____:
    counter += 1
    download_error = True
    error(f"ERROR 0x2: Critical issue occured while downloading file, {error____}")
    print(f'({str(counter)}/12)', colored(f'Error {unique_link.split("/")[-1]}', 'red'))
if download_error == False:
    print(colored("\nProcess finished successfully, continue in 5 seconds...", "green"), end="")
    sleep(1), clear_last_line()
    print(colored("\nProcess finished successfully, continue in 4 seconds...", "green"), end="")
    sleep(1), clear_last_line()
    print(colored("\nProcess finished successfully, continue in 3 seconds...", "green"), end="")
    sleep(1), clear_last_line()
    print(colored("\nProcess finished successfully, continue in 2 seconds...", "green"), end="")
    sleep(1), clear_last_line()
    print(colored("\nProcess finished successfully, continue in 1 second...", "green"))
    sleep(1)
else:
    error("Error 0x44: One or more file*s failed to download.")
    print(colored("\nError 0x44: One or more file*s failed to download.", "red"))
    print("Press enter to exit...")
    input()
    exit()
system("cls")
debug("Defining speedtest function in speedtest class in a variable.")
test = Speedtest()

debug("Defining functions...")
debug("Defining clear()...")
def clear():
    system("cls")

debug("Defining delete()...")
info_msg = "INFO:"
def delete(path):
    try:
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
            print(colorama.Fore.LIGHTRED_EX + "REMOVED" + colorama.Style.RESET_ALL + " - " + path + colorama.Style.RESET_ALL)
        elif os.path.isdir(path):
            rmtree(path)
            print(colorama.Fore.LIGHTRED_EX + "REMOVED" + colorama.Style.RESET_ALL + " - " + path + " and all it's content" + colorama.Style.RESET_ALL)
        else:
            print(colorama.Fore.LIGHTRED_EX + "MISSED " + colorama.Style.RESET_ALL + " - " + path + colorama.Style.RESET_ALL)
    except Exception as err:
        print(colorama.Fore.LIGHTRED_EX + "ERROR  " + colorama.Style.RESET_ALL + " -", err)
debug("Getting servers...")
show_menu()
print("Getting server...")
server = test.get_servers()
debug("Getting best server...")
global best
best = test.get_best_server()
clear()

def get_ping():
    debug(f"Found best server: {best['host']} located in {best['country']}")
    print(f"Using server: {best['host']} located in {best['country']}")
    debug("Starting download test...")
    print("Performing download test...")
    download_result = test.download()
    debug("Starting upload test...")
    print("Performing upload test...")
    upload_result = test.upload()
    debug("Starting ping test...")
    print("Performing ping test...")
    ping_result = test.results.ping
    global old_download, old_upload, old_ping
    old_download = f'{download_result / 1024 / 1024:.2f}'
    old_upload = f'{upload_result / 1024 / 1024:.2f}'
    old_ping = f"{ping_result:.2f}"
    debug(f"Done with testing, results: {old_download, old_upload, old_ping}")
    system("cls")
    print(f"Download: {old_download} mbits")
    print(f"Upload: {old_upload} mbits")
    print(f"Ping: {old_ping} ms")
    debug("Done with getting network info. Terminate function.")
    return old_ping
debug("Defining settings_minecraft()...")
def settings_minecraft():
    debug("settings_minecraft function has been executed")
    fps = input("Would you like to apply the best in-game settings? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + fps)
    if fps in yes:
        debug("Executing if-statement...")
        print('''Choose a value (1, 2)
        Option 1 - High end computer (Good graphics with the highest FPS)
        Option 2 - Low end computer (lowest graphics with the highest FPS)''')
        op_1 = input("Enter value: ")
        debug("Input gotten, answer is: " + op_1)
        options_file = f"{APPDATA}\\.minecraft\\optionsof.txt"
        if op_1 == "1":
            options = open(options_file, "w")
            options.write("ofFogType:3\nofFogStart:0.8\nofMipmapType:0\nofOcclusionFancy:false\nofSmoothFps:false\nofSmoothWorld:false\nofAoLevel:1.0\nofClouds:3\nofCloudsHeight:0.0\nofTrees:4\nofDroppedItems:0\nofRain:0\nofAnimatedWater:0\nofAnimatedLava:0\nofAnimatedFire:true\nofAnimatedPortal:false\nofAnimatedRedstone:true\nofAnimatedExplosion:true\nofAnimatedFlame:true\nofAnimatedSmoke:true\nofVoidParticles:true\nofWaterParticles:true\nofPortalParticles:true\nofPotionParticles:true\nofFireworkParticles:true\nofDrippingWaterLava:false\nofAnimatedTerrain:true\nofAnimatedTextures:true\nofRainSplash:false\nofLagometer:false\nofAutoSaveTicks:4000\nofBetterGrass:3\nofConnectedTextures:2\nofWeather:true\nofSky:false\nofStars:true\nofSunMoon:false\nofVignette:1\nofChunkUpdates:1\nofChunkUpdatesDynamic:false\nofTime:0\nofClearWater:false\nofAaLevel:0\nofAfLevel:1\nofProfiler:false\nofBetterSnow:false\nofSwampColors:true\nofRandomEntities:false\nofSmoothBiomes:true\nofCustomFonts:true\nofCustomColors:true\nofCustomItems:true\nofCustomSky:true\nofShowCapes:true\nofNaturalTextures:false\nofEmissiveTextures:true\nofLazyChunkLoading:true\nofRenderRegions:false\nofSmartAnimations:true\nofDynamicFov:false\nofAlternateBlocks:true\nofDynamicLights:3\nofScreenshotSize:1\nofCustomEntityModels:true\nofCustomGuis:true\nofShowGlErrors:true\nofFullscreenMode:Default\nofFastMath:true\nofFastRender:false\nofTranslucentBlocks:1\nkey_of.key.zoom:46")
            options.close()
        elif op_1 == "2":
            options = open(options_file, "w")
            options.write("ofFogType:3\nofFogStart:0.8\nofMipmapType:0\nofOcclusionFancy:false\nofSmoothFps:false\nofSmoothWorld:false\nofAoLevel:0.0\nofClouds:3\nofCloudsHeight:0.0\nofTrees:1\nofDroppedItems:0\nofRain:0\nofAnimatedWater:2\nofAnimatedLava:2\nofAnimatedFire:false\nofAnimatedPortal:false\nofAnimatedRedstone:false\nofAnimatedExplosion:false\nofAnimatedFlame:false\nofAnimatedSmoke:false\nofVoidParticles:false\nofWaterParticles:false\nofPortalParticles:false\nofPotionParticles:false\nofFireworkParticles:true\nofDrippingWaterLava:false\nofAnimatedTerrain:false\nofAnimatedTextures:false\nofRainSplash:false\nofLagometer:false\nofShowFps:false\nofAutoSaveTicks:4000\nofBetterGrass:3\nofConnectedTextures:3\nofWeather:true\nofSky:false\nofStars:true\nofSunMoon:false\nofVignette:1\nofChunkUpdates:1\nofChunkUpdatesDynamic:false\nofTime:0\nofClearWater:false\nofAaLevel:0\nofAfLevel:1\nofProfiler:false\nofBetterSnow:false\nofSwampColors:true\nofRandomEntities:false\nofSmoothBiomes:true\nofCustomFonts:true\nofCustomColors:true\nofCustomItems:true\nofCustomSky:true\nofShowCapes:true\nofNaturalTextures:false\nofEmissiveTextures:false\nofLazyChunkLoading:true\nofRenderRegions:false\nofSmartAnimations:true\nofDynamicFov:false\nofAlternateBlocks:false\nofDynamicLights:3\nofScreenshotSize:1\nofCustomEntityModels:true\nofCustomGuis:true\nofShowGlErrors:true\nofFullscreenMode:Default\nofFastMath:true\nofFastRender:true\nofTranslucentBlocks:1\nkey_of.key.zoom:46")
            options.close()
        else:
            print("Invalid value gotten")
            debug("Invalid value gotten at option choose!")
            settings_minecraft()
    else:
        debug(f"User input was {fps}, skipping...")
        print("OK, skipping...")
        pass
debug("Defining appearance()...")
def appearance():
    debug("appearance function has been executed...")
    op_2 = input("Would you like to lower the appearance of windows to increase performance? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + op_2)
    if op_2 in yes:
        reg_cmd = "REG ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects /v VisualFXSetting /t REG_DWORD /d 2 /f"
        debug("Running reg_cmd...")
        system(reg_cmd)
    else:
        debug(f"User input was {op_2}, skipping...")
        print("OK, skipping...")
        pass
debug("Defining defrag()...")
def defrag():
    debug("defrag function has been executed...")
    defrag = input("Would you like to defrag your drives to increase performance? (Only use this function when using HDD, not SSD!) (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + defrag)
    if defrag in yes:
        debug("Defraging drives...")
        print("Defraging... (this can take from several seconds up to a few hours)\n" + colored("Press Ctrl+C if you want to cancel the proccess!", "yellow"))
        sleep(3)
        try:
            drives = GetLogicalDriveStrings().split("\000")
            for drive in drives:
                if path.exists(drive):
                    system(f'defrag.exe {drive}')
        except KeyboardInterrupt as err__:
            print("Proccess cancelled!")
            sleep(2)
            print("Continuing...")
            sleep(1)
            pass
    else:
        debug(f"User input was {defrag}, skipping...")
        print("OK, skipping...")
        pass

def update_drivers():
    debug("update_drivers function has been executed...")
    update_drv = input("Do you want to update drivers? (y/n)\nEnter: ")
    if update_drv in yes:
        print(colored("Are you sure you want to update drivers?\nThis can take up to several hours, we recommend running this over night.", "blue"))
        confirmation_update = input("Still want to update drivers now? (y/n)\nEnter: ")
        if confirmation_update in yes:
            unpack_archive(f"{gettempdir()}\\sdi.zip", gettempdir())
            subprocess.call(gettempdir()+"\\sdi.bat")
    else:
        debug(f"User input was {update_drv}, skipping...")
        print("OK, skipping...")
        pass

def disable_autostart():
    debug("disable_autostart function has been executed...")
    disable_ques = input("Do you want to disable autostart for certain programs? (y/n)\nEnter: ")
    if disable_ques in yes:
        r = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        try:
            count = 0
            while 1:
                name, value, type = winreg.EnumValue(r, count)
                del_reg = input(f"Do you want to disable autostart for following service? (y/n):\n{colored(eval(repr(name)), 'blue')}\nEnter: ")
                if del_reg in yes:
                    system(f'reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v "{eval(repr(name))}" /f')
                    debug(f"Disabled autostart for following service: {name}")
                count = count + 1
        except WindowsError as errr:
            debug(f"Warning 0x264: Fatal issue occured while looping trough regedit keys, {errr}")
    else:
        debug(f"User input was {disable_ques}, skipping...")
        print("OK, skipping...")
        pass

def enable_gamemode():
    debug("enable_gamemode function has been executed...")
    enable_ques = input("Do you want to enable windows game mode? (y/n)\nEnter: ")
    if enable_ques in yes:
        os.chdir(gettempdir())
        system(r"%windir%\system32\reg.exe import Turn_on_Game_Mode.reg")
        debug("Enabled windows game mode!")
    else:
        debug(f"User input was {enable_ques}, skipping...")
        print("OK, skipping...")
        pass

def create_backup():
    print("Please note that not all settings can be backed up!")
    sleep(2)
    print("Creating restore point...")
    debug("Creating restore point...")
    system(f'powershell.exe Enable-ComputerRestore -Drive "{drive_letter}"')
    debug("Enabled ComputerRestore!")
    system(r'wmic.exe /Namespace:\\root\default Path SystemRestore Call CreateRestorePoint "OT-Optimizer: Automatized restore point", 100, 7')
    debug("Actually created a restore point.")
    debug("Backing up!")
    debug("Creating folder...")
    dir = path.join(f"{drive_letter}\\", "OTO-Backup")
    if not path.exists(dir):
        mkdir(dir)
    clear()
    show_menu()
    print("Backing up registry...")
    debug("Getting registry...")
    system(f"reg export HKLM {drive_letter}\\OTO-Backup\\Backup_reg.Reg /y")
    print("Backing up minecraft-settings...")
    original_of = f"{APPDATA}\\.minecraft\\optionsof.txt"
    target_of = f"{drive_letter}\\OTO-Backup\\optionsof.txt"
    original_1 = f"{APPDATA}\\.minecraft\\options.txt"
    target_1 = f"{drive_letter}\\OTO-Backup\\options.txt"
    debug("Trying to backup mc settings...")
    try:
        copyfile(original_of, target_of)
        copyfile(original_1, target_1)
        debug("Done!")
    except Exception as err_mc:
        system("cls")
        system("color 4")
        error(f"ERROR 0x317: Critical issue occured while backing up minecraft settings, {err_mc}")
        clear()
        show_menu()
        print(colored(f"\nERROR 0x317: Critical issue occured.", "red"))
        print("Please contact support and send log file when prompted.")
        print("More information here: www.discord.gg/uve9t7raAt")
        print("Breakpoint reached, won't continue.")
        input()
        if input():
            exit(1)
        else:
            exit(1)
    debug("Backing up DNS...")
    print("Backing up DNS...")
    dns_resolver = dns.resolver.Resolver()
    dns1 = dns_resolver.nameservers[0]
    original_dns = f"{gettempdir()}\\dns_backup.bat"
    target_dns = f"{drive_letter}\\OTO-Backup\\dns_backup.bat"
    copyfile(original_dns, target_dns)
    try:
        with open(f"{drive_letter}\\OTO-Backup\\DNS.bat", "w") as dns_file:
            dns_file.write(dns1)
    except Exception as dns_exce:
        print(colored("Error 0x28", "red"))
        error("Error: " + dns_exce)

    with open(f"{drive_letter}\\OTO-Backup\\dns_backup.bat", "rt") as fin:
        data = fin.read()
        data = data.replace('1.1.1.1', dns1)
        fin.close()

    with open(f"{drive_letter}\\OTO-Backup\\dns_backup.bat", "wt") as fin:
        fin.write(data)
        fin.close()

    debug("Backing up power plan...")
    print("Backing up power plan...")
    try:
        output = subprocess.check_output(["powercfg", "-getactivescheme"])
    except Exception as err___:
        print("Fatal Error 0x357")
        error("Error occured fatal error 0x357", err___)

    if b"381b4222-f694-41f0-9685-ff5bb260df2e" in output:
        win_pp = "381b4222-f694-41f0-9685-ff5bb260df2e"
        gotten = True
    elif b"8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c" in output:
        win_pp = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
        gotten = True
    elif b"a1841308-3541-4fab-bc81-f71556f20b4a" in output:
        win_pp = "a1841308-3541-4fab-bc81-f71556f20b4a"
        gotten = True
    elif b"e9a42b02-d5df-448d-aa00-03f14749eb61" in output:
        win_pp = "e9a42b02-d5df-448d-aa00-03f14749eb61"
        gotten = True
    else:
        error("Could not get current power plan!")
        gotten = False
    if gotten == False:
        pass
    else:
        try:
            with open(f"{drive_letter}\\OTO-Backup\\power_plan.txt", "w") as pp_file:
                pp_file.write(win_pp)
        except Exception as pp_exce:
            error("Fatal Error 0x380: ", pp_exce)
            print("Fatal error occured 0x380")
    with open(f"{drive_letter}\\server_best.txt", 'w') as file:
        file.write(best['host'])
        file.close()

debug("Executing show_menu function...")
show_menu()
debug("Asking for action...")
print("None of the authors, contributors, administrators, vandals, or anyone else connected with OT-Optimizer,\nin any way whatsoever, can be responsible for your use of this program. USE AT YOUR OWN RISK!")
print("This tool additionally uses 3rd-party-applications.")
print("\n1. Start optimizing PC\n2. Compare old and new ping\n3. Restore backup and undo changes\n4. Uninstall and remove all associated files ")
choice = input("\nEnter: ")
debug("Got: " + choice)
if choice == "1":
    if path.isdir(f"{drive_letter}\\OTO-Backup"):
        pass
    else:
        debug("Asking for backup...")
        print("Do you want to backup your current settings? (Recommend!)")
        backup_reg = input("Enter (y/n): ")
        if backup_reg in yes:
            create_backup()
            debug("Done backing up!")
            print("Successfully backed up!")
            sleep(0.5)
            print("Continuing...")
            sleep(2)
        else:
            print("Are you sure you don't want to create a backup? (y/n)")
            sure_no_backup = input("Enter: ")
            if sure_no_backup in yes:
                pass
            else:
                create_backup()
    clear()
    show_menu()
    debug("Executing get_ping function...")
    get_ping()
    debug("Executing clear function...")
    clear()
    debug("Executing show_menu function...")
    show_menu()
    print(f"Your current ping is: " + colored(old_ping, "red"))
    with open(f"{drive_letter}\\old_ping.txt", 'w') as file:
        file.write(old_ping)
        file.close()
    debug("Operating question 1, waiting for user input...")
    question_1 = input("Do you want to upgrade to the best windows power plan? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_1)
    if question_1 in yes:
        debug("Executing cmd command to change power plan...")
        system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
        system("powercfg /setactive scheme_min")
        clear()
        show_menu()
        debug("Power plan has been changed.")
        print("Successful, we additionally added ultimate power plan, you may want to switch manually.")
    else:
        debug(f"User input was {question_1}, skipping...")
        print("OK, skipping...")
        pass


    debug("Operating question 2, waiting for user input...")
    question_2 = input("Would you like to flush and clean your DNS? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_2)
    if question_2 in yes:
        debug("Calling clean.bat file...")
        subprocess.run(f"{gettempdir()}\\clean.bat")
        debug("Ran file!")
        sleep(10)
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_2}, skipping...")
        print("OK, skipping...")
        pass


    debug("Operating question 3, waiting for user input...")
    question_3 = input("Would you like to improve the TCP connection? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_3)
    if question_3 in yes:
        debug("Calling regedit file...")
        os.chdir(gettempdir())
        system(r"%windir%\system32\reg.exe import Doublehit_Connection.reg")
        debug("Called!")
        sleep(3)
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_3}, skipping...")
        print("OK, skipping...")
        pass


    debug("Operating question 4, waiting for user input...")
    question_4 = input("Do you want to change to a faster dns? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_4)
    if question_4 in yes:
        debug("Changing DNS...")
        subprocess.run(f"{gettempdir()}\\dns_er.bat")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_4}, skipping...")
        print("OK, skipping...")
        pass


    debug("Operating question 5, waiting for user input...")
    question_5 = input("Do you want to execute cpu unparker? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_5)
    if question_5 in yes:
        debug("Executing UnparkCPU.exe...")
        print("1. Press the Check Status button in the new window")
        print("2. After checking, press unpark all and exit the program")
        system(f"start {gettempdir()}\\UnparkCPU.exe")
        sleep(5)
        debug("Ran!")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_5}, skipping...")
        print("OK, skipping...")
        pass



    debug("Operating question 6, waiting for user input...")
    question_6 = input("Do you want to optimize TCP? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_6)
    if question_6 in yes:
        debug("Calling test.reg file...")
        os.chdir(gettempdir())
        system(r"%windir%\system32\reg.exe import test.reg")
        debug("Calling test2.reg file...")
        os.chdir(gettempdir())
        system(r"%windir%\system32\reg.exe import test.reg")
        debug("Called!")
        sleep(3)
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_6}, skipping...")
        print("OK, skipping...")
        pass



    debug("Operating question 7, waiting for user input...")
    question_7 = input("Would you like to change the Network Adapter Properties for a faster connection? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_6)
    if question_7 in yes:
        subprocess.run(f"{gettempdir()}\\net_er.bat")
        print("Done!")
        sleep(3)
        clear()
        debug("Done")
        clear()
        show_menu()
    else:
        debug(f"User input was {question_7}, skipping...")
        print("OK, skipping...")
        pass

    settings_minecraft()
    appearance()
    defrag()
    enable_gamemode()
    disable_autostart()
    update_drivers()
    clear()
    show_menu()
    print(colored("Successfully optimized your computer!", "green"))
    print("To check your new ping restart your PC, run this program again and choose numer 2 in the menu.")
    input("\nPress 3x enter to reboot PC...")
    input("\nPress 2x enter to reboot PC...")
    input(colored("\nPress 1x enter to reboot PC...", "red"))
    debug("Exiting and rebooting pc...")
    system("shutdown.exe /r /t 0")
elif choice == "2":
    path_old_ping = f"{drive_letter}\\old_ping.txt"
    yeono = path.exists(path_old_ping)
    if yeono == True:
        with open(f'{drive_letter}\\old_ping.txt', 'r') as file:
            data = file.read().rstrip()
        comp_old_ping = data
        with open(f"{drive_letter}\\server_best.txt", 'r') as file:
            host = file.read().rstrip()
            file.close()
        host_server = host[:-5]
        print("Pinging...")
        def ping_host(host):
            ping_result = ping(target=host, count=10, timeout=2)

            return {
                ping_result.rtt_avg_ms
            }


        hosts = [host_server]
        for host in hosts:
            complete_ping = ping_host(host)
        str(complete_ping)
        new = str(complete_ping).replace('{','').replace('}','')

        old = float(comp_old_ping)
        new = float(new)

        if old < new:
            print("\nOld ping: ", comp_old_ping)
            print("New ping: ", new)
            print("Your Ping is still optimized though!")
            input("\nPress enter to exit...")
        else:
            print("\nOld ping: ", colored(comp_old_ping, "red"))
            print("New ping: ", colored(new, "green"))
            print("Have fun playing!")
            input("\nPress enter to exit...")
    else:
        print("You first need to optimize your PC!")
        input("\nPress enter to exit...")
        exit()
elif choice == "3":
    path_backup = f"{drive_letter}\\OTO-Backup"
    if path.isdir(path_backup):
        pass
    else:
        print("You don't have created a backup yet!\nStart optimizing your pc to create one.")
        input("\nPress enter to exit...")
        exit()
    print("Backing up...")
    sleep(2)
    if path.isfile(f"{drive_letter}\\OTO-Backup\\Backup_reg.reg"):
        os.chdir(f"{drive_letter}\\OTO-Backup")
        system(r"%windir%\system32\reg.exe import Backup_reg.reg")


    original_of = f"{APPDATA}\\.minecraft\\optionsof.txt"
    target_of = f"{drive_letter}\\OTO-Backup\\optionsof.txt"
    original_1 = f"{APPDATA}\\.minecraft\\options.txt"
    target_1 = f"{drive_letter}\\OTO-Backup\\options.txt"
    debug("Trying to backup mc settings...")
    try:
        copyfile(target_of, original_of)
        copyfile(target_1, original_1)
        debug("Done!")
    except Exception as err_mc:
        system("cls")
        system("color 4")
        error(f"ERROR 1x317: Critical issue occured while backing up minecraft settings, {err_mc}")
        print("ERROR 1x317: Critical issue occured while backing up minecraft settings")
        input()
    with open(f"{drive_letter}\\OTO-Backup\\power_plan.txt", "r") as pp_file:
        pp_guid = pp_file.read()
        pp_file.close()
    system(f"powercfg /setactive {pp_guid}")
    debug("Power plan backed up")
    system("netsh winsock reset")
    system("netcfg -d")
    system("netsh int ip reset")
    system("netsh advfirewall reset")
    system("ipconfig /flushdns")
    system("ipconfig /release")
    system("ipconfig /renew")
    debug("Network reseted!")
    system(f"start {drive_letter}\\OTO-Backup\\dns_backup.bat")
    clear()
    show_menu()
    print(colored("Done, backed up old settings!", "green"))
    input("\nPress enter to exit and restart computer...")
    debug("Exiting and rebooting pc...")
    system("shutdown.exe /r /t 0")
elif choice == "4":
    print("Deleting all associated files (backups too)...")
    debug("Choice 4, removing program...")
    pathname = os.path.dirname(sys.argv[0])
    script_path = os.path.abspath(pathname)
    logging.shutdown()
    delete(f"{script_path}\\OTO-Log_{username}.log")
    delete(f"{drive_letter}\\server_best.txt")
    delete(f"{drive_letter}\\old_ping.txt")
    delete(f"{drive_letter}\\OTO-Backup")
    delete(f"{gettempdir()}\\clean.bat")
    delete(f"{gettempdir()}\\dns_er.bat")
    delete(f"{gettempdir()}\\dns_backup.bat")
    delete(f"{gettempdir()}\\net_er.bat")
    delete(f"{gettempdir()}\\LogParser.dll")
    delete(f"{gettempdir()}\\Interop.MSUtil.dll")
    delete(f"{gettempdir()}\\UnparkCPU.exe")
    delete(f"{gettempdir()}\\test.reg")
    delete(f"{gettempdir()}\\test2.reg")
    delete(f"{gettempdir()}\\Turn_on_Game_Mode.reg")
    delete(f"{gettempdir()}\\sdi.bat")
    delete(f"{gettempdir()}\\sdi.cfg")
    delete(f"{gettempdir()}\\drivers")
    delete(f"{gettempdir()}\\indexes")
    delete(f"{gettempdir()}\\logs")
    delete(f"{gettempdir()}\\tools")
    delete(f"{gettempdir()}\\SDI.exe")
    delete(f"{gettempdir()}\\sdi.zip")
    delete(f"{gettempdir()}\\SDI_auto.bat")
    delete(f"{gettempdir()}\\SDI_R526.exe")
    delete(f"{gettempdir()}\\SDI_x64_R526.exe")
    input("\nPress enter to exit...")
else:
    print("No valid input!")
    input("\nPress enter to exit...")