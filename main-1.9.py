# Version: 1.9
# Release date: 23.07.2022 (dd/mm/yyyy)
version = 1.9

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
from shutil import copyfile, rmtree, unpack_archive, get_terminal_size
from pythonping import ping
from wmi import WMI
from win32api import GetLogicalDriveStrings
from logging import info, debug, error, basicConfig, DEBUG
from termcolor import colored
from os import system, path, chdir, getenv, getlogin, mkdir
from speedtest import Speedtest
from time import sleep
from tempfile import gettempdir
from platform import win32_ver
from getpass import getpass

username = getlogin()
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
debug("Changing size of terminal window...")
os.system("mode 120,46")
debug("Done changing size!")

def input_exit():
    getpass("Press enter to exit...")
    exit()

if os.name == "nt":
    debug("Operating system is nt.")
    win_ver = win32_ver()[0]
    if win_ver != "10":
        error(f"But OS is not windows 10 or 11: {win_ver}")
        print("Sorry, your windows version (7 or 8) is not supported.")
        print("This tool is supported for Windows 10 up to Windows 11.")
        input_exit()
    else:
        debug(f"Operating system is {win_ver}, supported.")
else:
    error(f"Operating system not supported, os: {os.name}")
    print("Sorry, your operating system is currently not supported.")
    print("This tool is supported for Windows 10 up to Windows 11.")
    input_exit()

system("cls")
ctypes.windll.kernel32.SetConsoleTitleW(f"OT-Optimizer {version} - www.discord.gg/RMQcevDWng - Temal#5222 - ItzOwo#1414")
APPDATA = getenv('APPDATA')
yes = ["y", "Y", "yes", "Yes", "YES"]
drive_letter = getenv('HOMEDRIVE')

links = ['https://cdn.discordapp.com/attachments/985667930962403360/988883043206975558/dns_er.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/1000114266789117992/oto_tcp.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/997937119165161634/Turn_on_Game_Mode.reg',
         'https://cdn.discordapp.com/attachments/985667930962403360/999740172444901397/sdi.zip',
         'https://cdn.discordapp.com/attachments/985667930962403360/997997020277133322/sdi.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/1000010946850324541/enable-AGPU_scheduling.reg']

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
    terminal_columns = get_terminal_size().columns
    fill_chara = colored(terminal_columns*"-", color="cyan")
    menu_line = colored(f"OT-Optimizer v{version}", color="blue", attrs=['underline', 'bold'])
    menu_contact = colored("Temal#5222 - ItzOwo#1414", color="blue")
    menu_dc = colored("www.discord.gg/RMQcevDWng", color="blue")
    menu_github = colored("www.github.com/temal32/oto", color="blue")
    menu_disclaimer = "By using this program, you agree that you are liable for any damage."
    print(fill_chara)
    print(menu_line)
    print(menu_contact)
    print(menu_dc)
    print(menu_github)
    print(menu_disclaimer)
    print(fill_chara)

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
        print(f'({counter}/07) Downloaded {link.split("/")[-1]}')
        counter = int(counter)
    except Exception as error_:
        download_error = True
        error(f"ERROR 0x1: Critical issue occured while downloading file, {error_}")
        space = ""
        if counter < 10:
            space = ""
            counter = str(counter)
            counter = "0" + counter
        print(f'({str(counter)}/07){space}', colored(f'Error {link.split("/")[-1]}', 'red'))
        if isinstance(counter, str):
            counter.split("0")
        counter = int(counter)
try:
    debug(f"Downloading {unique_link}...")
    r = requests.get(unique_link, allow_redirects=True)
    open(unique_link.split("/")[-1], 'wb').write(r.content)
    debug(f"Downloaded {unique_link} to '{drive_letter}\\OTO-Backup\\dns_backup.bat'")
    counter += 1
    if counter < 10:
        counter = str(counter)
        counter = "0" + counter
    print(f'({str(counter)}/07) Downloaded {unique_link.split("/")[-1]}')
except Exception as error____:
    counter += 1
    download_error = True
    error(f"ERROR 0x2: Critical issue occured while downloading file, {error____}")
    print(f'({str(counter)}/07)', colored(f'Error {unique_link.split("/")[-1]}', 'red'))
if download_error == False:
    print(colored("\nProcess finished successfully, continuing in 5 seconds...", "green"), end="")
    sleep(1), clear_last_line()
    print(colored("\nProcess finished successfully, continuing in 4 seconds...", "green"), end="")
    sleep(1), clear_last_line()
    print(colored("\nProcess finished successfully, continuing in 3 seconds...", "green"), end="")
    sleep(1), clear_last_line()
    print(colored("\nProcess finished successfully, continuing in 2 seconds...", "green"), end="")
    sleep(1), clear_last_line()
    print(colored("\nProcess finished successfully, continuing in 1 second...", "green"))
    sleep(1)
else:
    error("Error 0x44: One or more file*s failed to download.")
    print(colored("\nError 0x44: One or more file*s failed to download.", "red"))
    input_exit()
system("cls")
debug("Defining speedtest function in speedtest class in a variable.")
try:
    test = Speedtest()
except Exception as connect_err:
    error(f"Error occured while connecting to speedtest!, {connect_err}")
    show_menu()
    print(colored(f"Error occured while connecting to speedtest server, please try again later!\nError code: {connect_err}", "red"))
    input_exit()

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
print("Getting server... (this can take up to several minutes)")
server = test.get_servers()
debug("Getting best server...")
best = test.get_best_server()
clear()

def get_ping():
    debug(f"Found best server: {best['host']} located in {best['country']}")
    print(f"Using server: {best['host']} located in {best['country']}")
    debug("Writing server host to textfile...")
    try:
        with open(f"{drive_letter}\\server_best.txt", 'w') as file:
            file.write(best['host'])
            file.close()
    except Exception as write_err:
        error(f"Could not write server_best.txt file, error: {write_err}")
    debug("Starting download test...")
    print("Performing download test...")
    try:
        download_result = test.download()
    except Exception as download_err:
        error(f"Error occured while downloading!, {download_err}")
        print(colored("Error occured while downloading!", "red"))
    debug("Starting upload test...")
    print("Performing upload test...")
    try:
        upload_result = test.upload()
    except Exception as upload_err:
        error(f"Error occured while uploading!, {upload_err}")
        print(colored("Error occured while uploading!", "red"))
    debug("Starting ping test...")
    print("Performing ping test...")
    try:
        ping_result = test.results.ping
    except Exception as ping_res_err:
        error(f"Error occured while getting ping result!, {ping_res_err}")
        print(colored("Error occured while getting ping result!", "red"))
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
            options.write("ofFogType:3"
                          "\nofFogStart:0.8"
                          "\nofMipmapType:0"
                          "\nofOcclusionFancy:false"
                          "\nofSmoothFps:false"
                          "\nofSmoothWorld:false"
                          "\nofAoLevel:1.0"
                          "\nofClouds:3"
                          "\nofCloudsHeight:0.0"
                          "\nofTrees:4"
                          "\nofDroppedItems:0"
                          "\nofRain:0"
                          "\nofAnimatedWater:0"
                          "\nofAnimatedLava:0"
                          "\nofAnimatedFire:true"
                          "\nofAnimatedPortal:false"
                          "\nofAnimatedRedstone:true"
                          "\nofAnimatedExplosion:true"
                          "\nofAnimatedFlame:true"
                          "\nofAnimatedSmoke:true"
                          "\nofVoidParticles:true"
                          "\nofWaterParticles:true"
                          "\nofPortalParticles:true"
                          "\nofPotionParticles:true"
                          "\nofFireworkParticles:true"
                          "\nofDrippingWaterLava:false"
                          "\nofAnimatedTerrain:true"
                          "\nofAnimatedTextures:true"
                          "\nofRainSplash:false"
                          "\nofLagometer:false"
                          "\nofAutoSaveTicks:4000"
                          "\nofBetterGrass:3"
                          "\nofConnectedTextures:2"
                          "\nofWeather:true"
                          "\nofSky:false"
                          "\nofStars:true"
                          "\nofSunMoon:false"
                          "\nofVignette:1"
                          "\nofChunkUpdates:1"
                          "\nofChunkUpdatesDynamic:false"
                          "\nofTime:0"
                          "\nofClearWater:false"
                          "\nofAaLevel:0"
                          "\nofAfLevel:1"
                          "\nofProfiler:false"
                          "\nofBetterSnow:false"
                          "\nofSwampColors:true"
                          "\nofRandomEntities:false"
                          "\nofSmoothBiomes:true"
                          "\nofCustomFonts:true"
                          "\nofCustomColors:true"
                          "\nofCustomItems:true"
                          "\nofCustomSky:true"
                          "\nofShowCapes:true"
                          "\nofNaturalTextures:false"
                          "\nofEmissiveTextures:true"
                          "\nofLazyChunkLoading:true"
                          "\nofRenderRegions:false"
                          "\nofSmartAnimations:true"
                          "\nofDynamicFov:false"
                          "\nofAlternateBlocks:true"
                          "\nofDynamicLights:3"
                          "\nofScreenshotSize:1"
                          "\nofCustomEntityModels:true"
                          "\nofCustomGuis:true"
                          "\nofShowGlErrors:true"
                          "\nofFullscreenMode:Default"
                          "\nofFastMath:true"
                          "\nofFastRender:false"
                          "\nofTranslucentBlocks:1"
                          "\nkey_of.key.zoom:46")
            options.close()
            clear()
            show_menu()
            print("Done! Continuing...")
        elif op_1 == "2":
            options = open(options_file, "w")
            options.write("ofFogType:3"
                          "\nofFogStart:0.8"
                          "\nofMipmapType:0"
                          "\nofOcclusionFancy:false"
                          "\nofSmoothFps:false"
                          "\nofSmoothWorld:false"
                          "\nofAoLevel:0.0"
                          "\nofClouds:3"
                          "\nofCloudsHeight:0.0"
                          "\nofTrees:1"
                          "\nofDroppedItems:0"
                          "\nofRain:0"
                          "\nofAnimatedWater:2"
                          "\nofAnimatedLava:2"
                          "\nofAnimatedFire:false"
                          "\nofAnimatedPortal:false"
                          "\nofAnimatedRedstone:false"
                          "\nofAnimatedExplosion:false"
                          "\nofAnimatedFlame:false"
                          "\nofAnimatedSmoke:false"
                          "\nofVoidParticles:false"
                          "\nofWaterParticles:false"
                          "\nofPortalParticles:false"
                          "\nofPotionParticles:false"
                          "\nofFireworkParticles:true"
                          "\nofDrippingWaterLava:false"
                          "\nofAnimatedTerrain:false"
                          "\nofAnimatedTextures:false"
                          "\nofRainSplash:false"
                          "\nofLagometer:false"
                          "\nofShowFps:false"
                          "\nofAutoSaveTicks:4000"
                          "\nofBetterGrass:3"
                          "\nofConnectedTextures:3"
                          "\nofWeather:true"
                          "\nofSky:false"
                          "\nofStars:true"
                          "\nofSunMoon:false"
                          "\nofVignette:1"
                          "\nofChunkUpdates:1"
                          "\nofChunkUpdatesDynamic:false"
                          "\nofTime:0"
                          "\nofClearWater:false"
                          "\nofAaLevel:0"
                          "\nofAfLevel:1"
                          "\nofProfiler:false"
                          "\nofBetterSnow:false"
                          "\nofSwampColors:true"
                          "\nofRandomEntities:false"
                          "\nofSmoothBiomes:true"
                          "\nofCustomFonts:true"
                          "\nofCustomColors:true"
                          "\nofCustomItems:true"
                          "\nofCustomSky:true"
                          "\nofShowCapes:true"
                          "\nofNaturalTextures:false"
                          "\nofEmissiveTextures:false"
                          "\nofLazyChunkLoading:true"
                          "\nofRenderRegions:false"
                          "\nofSmartAnimations:true"
                          "\nofDynamicFov:false"
                          "\nofAlternateBlocks:false"
                          "\nofDynamicLights:3"
                          "\nofScreenshotSize:1"
                          "\nofCustomEntityModels:true"
                          "\nofCustomGuis:true"
                          "\nofShowGlErrors:true"
                          "\nofFullscreenMode:Default"
                          "\nofFastMath:true"
                          "\nofFastRender:true"
                          "\nofTranslucentBlocks:1"
                          "\nkey_of.key.zoom:46")
            options.close()
            clear()
            show_menu()
            print("Done! Continuing...")
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
        clear()
        show_menu()
        print("Done! Continuing...")
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
        clear()
        show_menu()
        print("Done! Continuing...")
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
        clear()
        show_menu()
        print("Done! Continuing...")
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
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {enable_ques}, skipping...")
        print("OK, skipping...")
        pass

def enable_agpu_scheduling():
    debug("enable_agpu_scheduling function has been executed...")
    enable_ques = input("Do you want to enable hardware accelerated GPU scheduling? (y/n)\nEnter: ")
    if enable_ques in yes:
        os.chdir(gettempdir())
        system(r"%windir%\system32\reg.exe import enable-AGPU_scheduling.reg")
        debug("Enabled hardware accelerated GPU scheduling!")
        clear()
        show_menu()
        print("Done! Continuing...")
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

debug("Executing show_menu function...")
show_menu()
debug("Asking for action...")
print(colored("None of the authors, contributors, administrators, vandals, or anyone else connected with OT-Optimizer,\nin any way whatsoever, can be responsible for your use of this program.", "magenta"))
print(colored("This tool additionally uses 3rd-party-applications.\n", "magenta"))
print(colored("1", "yellow") + ". Start optimizing PC - Optimize your PC to increase FPS and decrease/stable ping")
print(colored("2", "yellow") + ". Compare old and new ping - Compare your old ping which you had before you optimized your pc with your new ping")
print(colored("3", "yellow") + ". Restore backup and undo changes - Restore backup which you created sooner before and undo changes")
print(colored("4", "yellow") + ". Uninstall and remove all associated files - Remove all associated files which were downloaded by this program")
choice = input("\nEnter number: " + colorama.Fore.YELLOW)
print('\033[39m', end="")
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
        print("Successful. We additionally added the ultimate power plan, you may want to switch manually.")
    else:
        debug(f"User input was {question_1}, skipping...")
        print("OK, skipping...")
        pass


    debug("Operating question 2, waiting for user input...")
    question_2 = input("Would you like to flush and clean your DNS? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_2)
    if question_2 in yes:
        system("ipconfig /renew")
        system("ipconfig /flushdns")
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
    question_3 = input("Do you want to change to a faster dns? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_3)
    if question_3 in yes:
        debug("Changing DNS...")
        subprocess.run(f"{gettempdir()}\\dns_er.bat")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_3}, skipping...")
        print("OK, skipping...")
        pass


    debug("Operating question 4, waiting for user input...")
    question_4 = input("Do you want to unpark your cpu? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_4)
    if question_4 in yes:
        debug("Running reg command...")
        system(r'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" /v ValueMax /t REG_DWORD /d 0 /f')
        system(r'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" /v ValueMin /t REG_DWORD /d 0 /f')
        debug("Ran!")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_4}, skipping...")
        print("OK, skipping...")
        pass



    debug("Operating question 5, waiting for user input...")
    question_5 = input("Do you want to optimize TCP? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_5)
    if question_5 in yes:
        print("Thanks to Danilo#0001 for providing tcp optimization commands!")
        sleep(2)
        debug("Calling oto_tcp.bat file...")
        os.chdir(gettempdir())
        subprocess.run(f"{gettempdir()}\\oto_tcp.bat")
        debug("Called!")
        sleep(3)
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_5}, skipping...")
        print("OK, skipping...")
        pass



    debug("Operating question 6, waiting for user input...")
    question_6 = input("Would you like to change the network adapter properties for a faster connection? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + question_6)
    if question_6 in yes:
        has_ethernet, has_wifi = False, False
        for x in WMI().Win32_NetworkAdapter():
            match x.NetConnectionID:
                case 'Wi-Fi':
                    debug(f"User using Wi-Fi, {x.name}")
                    connection_type = "Wi-Fi"
                case 'Ethernet':
                    debug(f"User using Ethernet, {x.name}")
                    connection_type = "Ethernet"
        print("Please wait, this can take a while...")
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*EEE" -RegistryValue 0}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*FlowControl" -RegistryValue 0}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*InterruptModeration" -RegistryValue 0}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*IPChecksumOffloadIPv4" -RegistryValue 3}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*JumboPacket" -RegistryValue 1514}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*LsoV2IPv4" -RegistryValue 0}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*LsoV2IPv6" -RegistryValue 0}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*NumRssQueues" -RegistryValue 4}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*ReceiveBuffers" -RegistryValue 512}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*RSS" -RegistryValue 1}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*TCPChecksumOffloadIPv4" -RegistryValue 3}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*TCPChecksumOffloadIPv6" -RegistryValue 3}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "*TransmitBuffers" -RegistryValue 128}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "AdvancedEEE" -RegistryValue 0}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "EnableGreenEthernet" -RegistryValue 0}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "GigaLite" -RegistryValue 0}')
        system('powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword "PowerSavingMode" -RegistryValue 0}')
        print("Done!")
        sleep(3)
        clear()
        debug("Done")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {question_6}, skipping...")
        print("OK, skipping...")
        pass

    settings_minecraft()
    appearance()
    defrag()
    enable_gamemode()
    enable_agpu_scheduling()
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
    yeono = path.exists(f"{drive_letter}\\old_ping.txt")
    best_server_txt = path.exists(f"{drive_letter}\\server_best.txt")
    if yeono == True and best_server_txt == True:
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
            if new == 2000.0:
                error("An issue occured while getting new ping.")
                print("An issue occured while getting new ping, please try again.")
            else:
                print("\nOld ping: ", comp_old_ping)
                print("New ping: ", new)
                print("Your Ping and FPS are still optimized though!")
            input_exit()
        else:
            print("\nOld ping: ", colored(comp_old_ping, "red"))
            print("New ping: ", colored(new, "green"))
            print("Have fun playing!")
            input_exit()
    else:
        print("You first need to complete the optimization to your PC before you can compare your old ping and new ping!")
        input_exit()
elif choice == "3":
    path_backup = f"{drive_letter}\\OTO-Backup"
    if path.isdir(path_backup):
        pass
    else:
        print("You don't have created a backup yet!\nStart optimizing your pc to create one.")
        input_exit()
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
    try:
        with open(f"{drive_letter}\\OTO-Backup\\power_plan.txt", "r") as pp_file:
            pp_guid = pp_file.read()
            pp_file.close()
        system(f"powercfg /setactive {pp_guid}")
        debug("Power plan backed up")
    except Exception as pp_err:
        error(f"Could'nt restore power plan, {pp_err}")
        print("Error occured while restoring windows power plan, ignoring.")
    network_cmds = ["netsh winsock reset", "netcfg -d", "netsh int ip reset", "netsh advfirewall reset", "ipconfig /flushdns", "ipconfig /release", "ipconfig /renew"]
    for command in network_cmds:
        system(command)
    debug("Network reseted!")
    system(f"start {drive_letter}\\OTO-Backup\\dns_backup.bat")
    clear()
    show_menu()
    print(colored("Done, backed up old settings!", "green"))
    input("\nPress enter to exit and restart computer...")
    debug("Exiting and rebooting pc...")
    system("shutdown.exe /r /t 0")
elif choice == "4":
    debug("Choice 4, removing program...")
    pathname = os.path.dirname(sys.argv[0])
    script_path = os.path.abspath(pathname)
    logging.shutdown()
    quest_backup_too = input("Do you want to erase backup files too? This is highly not recommend! (y/n)\nEnter:")
    if quest_backup_too in yes:
        print("Deleting all associated files (backups too)...")
        backup_files = ["server_best.txt", "old_ping.txt", "OTO-Backup"]
        delete(f"{script_path}\\OTO-Log_{username}.log")
        for file in backup_files:
            delete(f"{drive_letter}\\{file}")
    else:
        print("Deleting most associated files...")
    file_list = ["dns_er.bat", "dns_backup.bat", "enable-AGPU_scheduling.reg", "Turn_on_Game_Mode.reg", "oto_tcp.bat", "sdi.bat", "sdi.cfg", "drivers", "indexes", "logs", "tools", "SDI.exe", "sdi.zip", "SDI_auto.bat", "SDI_R526.exe", "SDI_x64_R526.exe"]
    for file in file_list:
        delete(f"{gettempdir()}\\{file}")
    input_exit()
else:
    print("No valid input!")
    input_exit()