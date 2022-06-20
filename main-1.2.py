# Version: 1.2
# Release date: 20.06.2022

import ctypes
import subprocess
import dns.resolver
import time
import speedtest
from pythonping import ping
import os
import shutil
import os.path
from termcolor import colored
import logging
import requests
import win32api
import sys

os.system("cls")
os.system("title OT-Optimizer - www.discord.gg/zrzWHcea8w")
username = os.getlogin()

# creating basic configuration for "logging" module to log into txt files
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style="{",
    filename=f"OTO-Log_{username}.log",
    filemode="a"
)
logging.info("\n" + 140*"-" + "\n")
logging.info("STOP, READ CAREFULLY!")
logging.info("This file is for developers only, please do not change, modify or delete this file!")
logging.info("Send this file when prompted.")
logging.info("More information can be found here: www.discord.gg/t3gWbBdbNQ")

logging.debug("Program has been started.")
logging.debug("Checking if windows is on C:...")

letter = os.getenv('WINDIR')
if "C" in letter:
    pass
else:
    print("Sorry, you do not fulfill the requirements. Please change your disk drive letter on which is windows installed to: C")
    input()
    exit()
logging.debug("Defining speedtest function in speedtest class in a variable.")
test = speedtest.Speedtest()

logging.debug("Defining functions...")
logging.debug("Defining download()...")
def download(url, path): # download file from web
    logging.debug("Requesting download...")
    try:
        url = url
        r = requests.get(url, allow_redirects=True)
        open(path, 'wb').write(r.content)
        logging.debug("successing...")
    except Exception as error_:
        logging.debug("Unexpected error...")
        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        if is_admin():
            os.system("cls")
            os.system("color 4")
            logging.error(f"ERROR 0x46: Critical issue occured while downloading file, {error_}")
            print(30 * "-")
            print("OT-Optimizer v1.2")
            print(30 * "-")
            print(colored(f"\nERROR 0x46: Critical issue occured.", "red"))
            print("Please contact support and send log file when prompted.")
            print("More information here: www.discord.gg/uve9t7raAt")
            print("Breakpoint reached, won't continue.")
            input()
            if input():
                exit(1)
            else:
                exit(1)
        else:
            # Re-run the program with admin rights
            logging.debug("It's because there are no admin privileges given!")
            logging.debug("Requesting privileges...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            logging.debug("Breakpoint before leaving for new app with privileges.")
            sys.exit(1)

logging.debug("Downloading clean.bat...")
download("https://cdn.discordapp.com/attachments/985667930962403360/985668051427008552/clean.bat", "C:\\Windows\\clean.bat")
logging.debug("Downloading Doublehit_Connection.reg...")
download("https://cdn.discordapp.com/attachments/985667930962403360/985668066274861136/Doublehit_Connection.reg", "C:\\Windows\\Doublehit_Connection.reg")
logging.debug("Defining clear()...")
def clear(): # function to clear console
    os.system("cls")
logging.debug("Defining show_menu()...")
def show_menu(): # function to show a good menu in console
    print(30*"-")
    print("OT-Optimizer v1.2")
    print(30*"-")
logging.debug("Defining get_ping()...")
###########################################################################
logging.debug("Getting servers...")
show_menu()
print("Getting server...")
server = test.get_servers()
logging.debug("Getting best server...")
global best
best = test.get_best_server()
clear()

def get_ping(): # function to get ping and network speed
    logging.debug(f"Found best server: {best['host']} located in {best['country']}")
    print(f"Using server: {best['host']} located in {best['country']}")
    logging.debug("Starting download test...")
    print("Performing download test...")
    download_result = test.download()
    logging.debug("Starting upload test...")
    print("Performing upload test...")
    upload_result = test.upload()
    logging.debug("Starting ping test...")
    print("Performing ping test...")
    ping_result = test.results.ping
    global old_download, old_upload, old_ping
    old_download = f'{download_result / 1024 / 1024:.2f}'
    old_upload = f'{upload_result / 1024 / 1024:.2f}'
    old_ping = f"{ping_result:.2f}"
    logging.debug(f"Done with testing, results: {old_download, old_upload, old_ping}")
    os.system("cls")
    print(f"Download: {old_download} mbits")
    print(f"Upload: {old_upload} mbits")
    print(f"Ping: {old_ping} ms")
    logging.debug("Done with getting network info. Terminate function.")
    return old_ping
logging.debug("Defining settings_minecraft()...")
def settings_minecraft():
    logging.debug("settings_minecraft function has been executed")
    fps = input("Would you like to apply the best in-game settings? (y/n)")
    logging.debug("Input gotten, answer is: " + fps)
    if fps == "y":
        logging.debug("Executing if-statement...")
        print("Choose a value (1, 2)")
        print("Option 1 - High end computer (Good graphics with the highest FPS)")
        print("Option 2 - Low end computer (lowest graphics with the highest FPS)")
        op_1 = input("Enter value: ")
        logging.debug("Input gotten, answer is: " + op_1)
############################################################################################################################################# HERE
        options_file = f"{os.getenv('APPDATA')}\\.minecraft\\optionsof.txt"
        if op_1 == "1":
            options = open(options_file, "w")
            options.write("ofFogType:3\nofFogStart:0.8\nofMipmapType:0\nofOcclusionFancy:false\nofSmoothFps:false\nofSmoothWorld:false\nofAoLevel:1.0\nofClouds:3\nofCloudsHeight:0.0\nofTrees:4\nofDroppedItems:0\nofRain:0\nofAnimatedWater:0\nofAnimatedLava:0\nofAnimatedFire:true\nofAnimatedPortal:false\nofAnimatedRedstone:true\nofAnimatedExplosion:true\nofAnimatedFlame:true\nofAnimatedSmoke:true\nofVoidParticles:true\nofWaterParticles:true\nofPortalParticles:true\nofPotionParticles:true\nofFireworkParticles:true\nofDrippingWaterLava:false\nofAnimatedTerrain:true\nofAnimatedTextures:true\nofRainSplash:false\nofLagometer:false\nofAutoSaveTicks:4000\nofBetterGrass:3\nofConnectedTextures:2\nofWeather:true\nofSky:false\nofStars:true\nofSunMoon:false\nofVignette:1\nofChunkUpdates:1\nofChunkUpdatesDynamic:false\nofTime:0\nofClearWater:false\nofAaLevel:0\nofAfLevel:1\nofProfiler:false\nofBetterSnow:false\nofSwampColors:true\nofRandomEntities:false\nofSmoothBiomes:true\nofCustomFonts:true\nofCustomColors:true\nofCustomItems:true\nofCustomSky:true\nofShowCapes:true\nofNaturalTextures:false\nofEmissiveTextures:true\nofLazyChunkLoading:true\nofRenderRegions:false\nofSmartAnimations:true\nofDynamicFov:false\nofAlternateBlocks:true\nofDynamicLights:3\nofScreenshotSize:1\nofCustomEntityModels:true\nofCustomGuis:true\nofShowGlErrors:true\nofFullscreenMode:Default\nofFastMath:true\nofFastRender:false\nofTranslucentBlocks:1\nkey_of.key.zoom:46")
            options.close()
        elif op_1 == "2":
            options = open(options_file, "w")
            options.write("ofFogType:3\nofFogStart:0.8\nofMipmapType:0\nofOcclusionFancy:false\nofSmoothFps:false\nofSmoothWorld:false\nofAoLevel:0.0\nofClouds:3\nofCloudsHeight:0.0\nofTrees:1\nofDroppedItems:0\nofRain:0\nofAnimatedWater:2\nofAnimatedLava:2\nofAnimatedFire:false\nofAnimatedPortal:false\nofAnimatedRedstone:false\nofAnimatedExplosion:false\nofAnimatedFlame:false\nofAnimatedSmoke:false\nofVoidParticles:false\nofWaterParticles:false\nofPortalParticles:false\nofPotionParticles:false\nofFireworkParticles:true\nofDrippingWaterLava:false\nofAnimatedTerrain:false\nofAnimatedTextures:false\nofRainSplash:false\nofLagometer:false\nofShowFps:false\nofAutoSaveTicks:4000\nofBetterGrass:3\nofConnectedTextures:3\nofWeather:true\nofSky:false\nofStars:true\nofSunMoon:false\nofVignette:1\nofChunkUpdates:1\nofChunkUpdatesDynamic:false\nofTime:0\nofClearWater:false\nofAaLevel:0\nofAfLevel:1\nofProfiler:false\nofBetterSnow:false\nofSwampColors:true\nofRandomEntities:false\nofSmoothBiomes:true\nofCustomFonts:true\nofCustomColors:true\nofCustomItems:true\nofCustomSky:true\nofShowCapes:true\nofNaturalTextures:false\nofEmissiveTextures:false\nofLazyChunkLoading:true\nofRenderRegions:false\nofSmartAnimations:true\nofDynamicFov:false\nofAlternateBlocks:false\nofDynamicLights:3\nofScreenshotSize:1\nofCustomEntityModels:true\nofCustomGuis:true\nofShowGlErrors:true\nofFullscreenMode:Default\nofFastMath:true\nofFastRender:true\nofTranslucentBlocks:1\nkey_of.key.zoom:46")
            options.close()
        else:
            print("Enter a correct value")
            settings_minecraft()
    else:
        logging.debug(f"User input was {fps}, skipping...")
        print("OK, skipping...")
        pass
logging.debug("Defining appearance()...")
def appearance():
    logging.debug("appearance function has been executed...")
    op_2 = input("Would you like to lower the appearance of windows to increase performance? (y/n)")
    logging.debug("Input gotten, answer is: " + op_2)
    if op_2 == "y":
        reg_cmd = "REG ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects /v VisualFXSetting /t REG_DWORD /d 2 /f"
        logging.debug("Running reg_cmd...")
        os.system(reg_cmd)
    else:
        logging.debug(f"User input was {op_2}, skipping...")
        print("OK, skipping...")
        pass
logging.debug("Defining defrag()...")
def defrag():
    logging.debug("defrag function has been executed...")
    defrag = input("Would you like to defrag your drives to increase performance? (y/n)")
    logging.debug("Input gotten, answer is: " + defrag)
    if defrag == "y":
        logging.debug("Defraging drives...")
        print("Defraging... (this can take from several seconds up to a few hours)\n" + colored("Press Ctrl+C if you want to cancel the proccess!", "yellow"))
        time.sleep(3)
        try:
            drives = win32api.GetLogicalDriveStrings().split("\000")
            for drive in drives:
                if os.path.exists(drive):
                    os.system(f'defrag.exe {drive}')
        except KeyboardInterrupt as err__:
            print("Proccess cancelled!")
            time.sleep(2)
            print("Continuing...")
            time.sleep(1)
            pass
    else:
        logging.debug(f"User input was {defrag}, skipping...")
        print("OK, skipping...")
        pass

logging.debug("Executing show_menu function...")
show_menu()
logging.debug("Asking for action...")
print("None of the authors, contributors, administrators, vandals, or anyone else connected with OT-Optimizer,\nin any way whatsoever, can be responsible for your use of this program. USE AT YOUR OWN RISK!")
print("This tool additionally uses 3rd-party-applications, credits to: Verzide, CoderBag")
print("\n1. Start optimizing PC\n2. Compare old and new ping\n3. Restore backup and undo changes")
choice = input("\nEnter: ")
logging.debug("Got: " + choice)
if choice == "1":
    if os.path.isdir("C:\\OTO-Backup"):
        pass
    else:
        logging.debug("Asking for backup...")
        print("Do you want to backup your current settings? (Recommend!)")
        backup_reg = input("(y/n): ")
        if backup_reg == "y":
            print("Creating restore point...")
            logging.debug("Creating restore point...")
            os.system('powershell.exe Enable-ComputerRestore -Drive "C:"')
            os.system(r'wmic.exe /Namespace:\\root\default Path SystemRestore Call CreateRestorePoint "OT-Optimizer: Automatized restore point", 100, 7')
            logging.debug("Backing up!")
            logging.debug("Creating folder...")
            dir = os.path.join("C:\\", "OTO-Backup")
            if not os.path.exists(dir):
                os.mkdir(dir)
            clear()
            show_menu()
            print("Backing up registry...")
            logging.debug("Getting registry...")
            os.system("reg export HKLM C:\\OTO-Backup\\Backup_reg.Reg /y")
            print("Backing up minecraft-settings...")

            original_of = f"{os.getenv('APPDATA')}\\.minecraft\\optionsof.txt"
            target_of = "C:\\OTO-Backup\\optionsof.txt"
            original_1 = f"{os.getenv('APPDATA')}\\.minecraft\\options.txt"
            target_1 = "C:\\OTO-Backup\\options.txt"
            original_lc = f"{os.getenv('APPDATA')}\\.minecraft\\optionsLC.txt"
            target_lc = "C:\\OTO-Backup\\optionsLC.txt"
            logging.debug("Trying to backup mc settings...")
            try:
                shutil.copyfile(original_of, target_of)
                shutil.copyfile(original_1, target_1)
                shutil.copyfile(original_lc, target_lc)
                logging.debug("Done!")
            except Exception as err_mc:
                os.system("cls")
                os.system("color 4")
                logging.error(f"ERROR 0x317: Critical issue occured while backing up minecraft settings, {err_mc}")
                clear()
                print(30 * "-")
                print("OT-Optimizer v1.2")
                print(30 * "-")
                print(colored(f"\nERROR 0x317: Critical issue occured.", "red"))
                print("Please contact support and send log file when prompted.")
                print("More information here: www.discord.gg/uve9t7raAt")
                print("Breakpoint reached, won't continue.")
                input()
                if input():
                    exit(1)
                else:
                    exit(1)
            logging.debug("Backing up DNS...")
            print("Backing up DNS...")
            dns_resolver = dns.resolver.Resolver()
            dns = dns_resolver.nameservers[0]
            try:
                with open("C:\\OTO-Backup\\DNS.bat", "w") as dns_file:
                    dns_file.write(dns)
            except Exception as dns_exce:
                print(dns_exce)
            download("https://cdn.discordapp.com/attachments/985667930962403360/988501434318344252/dns_er.bat", "C:\\OTO-Backup\\dns_backup.bat")


            fin = open("C:\\OTO-Backup\\dns_backup.bat", "rt")
            # read file contents to string
            data = fin.read()
            # replace all occurrences of the required string
            data = data.replace('1.1.1.1', dns)
            # close the input file
            fin.close()
            # open the input file in write mode
            fin = open("C:\\OTO-Backup\\dns_backup.bat", "wt")
            # overrite the input file with the resulting data
            fin.write(data)
            # close the file
            fin.close()


            logging.debug("Backing up power plan...")
            print("Backing up power plan...")
            try:
                output = subprocess.check_output(["powercfg", "-getactivescheme"])
            except Exception as err___:
                print("Fatal Error 0x357")
                logging.debug("Error occured fatal error 0x357", err___)

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
                logging.debug("Could not get current power plan!")
                gotten = False
            if gotten == False:
                pass
            else:
                try:
                    with open("C:\\OTO-Backup\\power_plan.txt", "w") as pp_file:
                        pp_file.write(win_pp)
                except Exception as pp_exce:
                    logging.debug("Fatal Error 0x380: ", pp_exce)
                    print("Fatal error occured 0x380")
            with open("C:\\server_best.txt", 'w') as file:
                file.write(best['host'])
                file.close()
            logging.debug("Done backing up!")
            print("Successfully backed up!")
            time.sleep(0.5)
            print("Continuing...")
            time.sleep(2)
        else:
            pass
    clear()
    show_menu()
    logging.debug("Executing get_ping function...")
    get_ping()
    logging.debug("Executing clear function...")
    clear()
    logging.debug("Executing show_menu function...")
    show_menu()
    print(f"Your current ping is: " + colored(old_ping, "red"))
    with open("C:\\old_ping.txt", 'w') as file:
        file.write(old_ping)
        file.close()
    logging.debug("Operating question 1, waiting for user input...")
    question_1 = input("Do you want to upgrade to the best windows power plan? (y/n)")
    logging.debug("Input gotten, answer is: " + question_1)
    if question_1 == "y":
        logging.debug("Executing cmd command to change power plan...")
        os.system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
        os.system("powercfg /setactive scheme_min")
        clear()
        show_menu()
        logging.debug("Power plan has been changed.")
        print("Successful, we additionally added ultimate power plan, you may want to switch manually.")
    else:
        logging.debug(f"User input was {question_1}, skipping...")
        print("OK, skipping...")
        pass

    #############################################################################################
    logging.debug("Operating question 2, waiting for user input...")
    question_2 = input("Would you like to flush and clean your DNS? (y/n)")
    logging.debug("Input gotten, answer is: " + question_2)
    if question_2 == "y":
        logging.debug("Calling clean.bat file...")
        # os.system("start C:\\Windows\\clean.bat")
        subprocess.call("C:\\Windows\\clean.bat")
        logging.debug("Ran file!")
        time.sleep(10)
        os.system("del C:\\Windows\\clean.bat")
        logging.debug("Deleted tmp bat file...")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        logging.debug(f"User input was {question_2}, skipping...")
        print("OK, skipping...")
        pass

    #############################################################################################
    logging.debug("Operating question 3, waiting for user input...")
    question_3 = input("Would you like to improve the TCP connection by applying a registry edit? (y/n)")
    logging.debug("Input gotten, answer is: " + question_3)
    if question_3 == "y":
        print("In the next few seconds 4 windows will pop up please do following:")
        print("1. Confirm again by pressing 'Yes'")
        print("2. Finally press 'OK'")
        logging.debug("Calling regedit file...")
        os.system("start C:\\Windows\\Doublehit_Connection.reg")
        logging.debug("Called!")
        time.sleep(5)
        os.system("del C:\\Windows\\Doublehit_Connection.reg")
        logging.debug("Deleted tmp reg file...")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        logging.debug(f"User input was {question_3}, skipping...")
        print("OK, skipping...")
        pass

    #############################################################################################
    logging.debug("Operating question 4, waiting for user input...")
    question_4 = input("Do you want to change to a faster dns? (y/n)")
    logging.debug("Input gotten, answer is: " + question_4)
    if question_4 == "y":
        logging.debug("Downloading dns_er.bat...")
        download("https://cdn.discordapp.com/attachments/985667930962403360/988069526530830356/dns_er.bat", "C:\\Windows\\dns_er.bat")
        logging.debug("Changing DNS...")
        subprocess.call("C:\\Windows\\dns_er.bat")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        logging.debug(f"User input was {question_4}, skipping...")
        print("OK, skipping...")
        pass

    ########################################################################################
    logging.debug("Operating question 5, waiting for user input...")
    question_5 = input("Do you want to execute cpu unparker? (y/n)")
    logging.debug("Input gotten, answer is: " + question_5)
    if question_5 == "y":
        logging.debug("Downloading LogParser.dll...")
        download("https://cdn.discordapp.com/attachments/985667930962403360/985670447515455548/LogParser.dll",
                 "C:\\Windows\\LogParser.dll")
        logging.debug("Downloading Interop.MSUtil.dll...")
        download("https://cdn.discordapp.com/attachments/985667930962403360/985670448010387567/Interop.MSUtil.dll",
                 "C:\\Windows\\Interop.MSUtil.dll")
        logging.debug("Downloading UnparkCPU.exe...")
        download("https://cdn.discordapp.com/attachments/985667930962403360/985670447775498310/UnparkCPU.exe",
                 "C:\\Windows\\UnparkCPU.exe")
        logging.debug("Done downloading unparker files!")
        logging.debug("Executing UnparkCPU.exe...")
        print("1. Press the Check Status button in the new window")
        print("2. After checking, press unpark all and exit the program")
        os.system("start C:\\Windows\\UnparkCPU.exe")
        time.sleep(5)
        logging.debug("Ran!")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        logging.debug(f"User input was {question_5}, skipping...")
        print("OK, skipping...")
        pass

    ################################################################################################

    logging.debug("Operating question 6, waiting for user input...")
    question_6 = input("Do you want to optimize TCP? (y/n)")
    logging.debug("Input gotten, answer is: " + question_6)
    if question_6 == "y":
        logging.debug("Downloading test.reg...")
        download("https://cdn.discordapp.com/attachments/985667930962403360/987026646555058227/test.reg",
                 "C:\\Windows\\test.reg")
        logging.debug("Downloading test2.reg...")
        download("https://cdn.discordapp.com/attachments/985667930962403360/987026646378872852/test2.reg",
                 "C:\\Windows\\test2.reg")
        print("Please confirm both pop up's:")
        print("1. Confirm by pressing 'Yes'")
        print("2. Press 'OK'")
        print("3. Confirm again")
        print("4. Finally press 'OK'")
        logging.debug("Calling test.reg file...")
        os.system("start C:\\Windows\\test.reg")
        logging.debug("Calling test2.reg file...")
        os.system("start C:\\Windows\\test2.reg")
        logging.debug("Called!")
        time.sleep(5)
        os.system("del C:\\Windows\\test.reg")
        os.system("del C:\\Windows\\test2.reg")
        logging.debug("Deleted tmp reg file...")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        logging.debug(f"User input was {question_6}, skipping...")
        print("OK, skipping...")
        pass

    #########################################################################################################

    logging.debug("Operating question 7, waiting for user input...")
    question_7 = input("Would you like to change the Network Adapter Properties for a faster connection? (y/n)")
    logging.debug("Input gotten, answer is: " + question_6)
    if question_7 == "y":
        download("https://cdn.discordapp.com/attachments/985667930962403360/988483339897929798/net_er.bat", "C:\\Windows\\net_er.bat")
        subprocess.call("C:\\Windows\\net_er.bat")
        print("Done!")
        time.sleep(3)
        clear()
        logging.debug("Done")
        clear()
        show_menu()
    else:
        logging.debug(f"User input was {question_7}, skipping...")
        print("OK, skipping...")
        pass
    #########################################################################################################
    settings_minecraft()
    appearance()
    defrag()
    ################################################################################################
    ################################################################################################
    clear()
    show_menu()
    print(colored("Successfully optimized your computer!", "green"))
    print("To check your new ping restart your PC, run this program again and choose numer 2 in the menu")
    input("\nPress 3x enter to reboot PC...")
    input("\nPress 2x enter to reboot PC...")
    input(colored("\nPress one more time enter to reboot PC...", "red"))
    logging.debug("Exiting and rebooting pc...")
    os.system("shutdown -t 0 -r -f")
elif choice == "2":
    path = "C:\\old_ping.txt"
    yeono = os.path.exists(path)
    if yeono == True:
        with open('C:\\old_ping.txt', 'r') as file:
            data = file.read().rstrip()
        comp_old_ping = data
        with open("C:\\server_best.txt", 'r') as file:
            host = file.read().rstrip()
            file.close()
        host_server = host[:-5]
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
        #print(type(comp_old_ping))
        #print((type(new)))

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
    input()
elif choice == "3":
    path = "C:\\OTO-Backup"
    if os.path.isdir(path):
        pass
    else:
        print("You don't have created a backup yet!\nStart optimizing your pc to create one.")
        input("\nPress enter to exit...")
        exit()
    print("Backing up...")
    time.sleep(2)
    if os.path.isfile("C:\\OTO-Backup\\Backup_reg.Reg"):
        os.system("start C:\\OTO-Backup\\Backup_reg.Reg")


    original_of = f"{os.getenv('APPDATA')}\\.minecraft\\optionsof.txt"
    target_of = "C:\\OTO-Backup\\optionsof.txt"
    original_1 = f"{os.getenv('APPDATA')}\\.minecraft\\options.txt"
    target_1 = "C:\\OTO-Backup\\options.txt"
    original_lc = f"{os.getenv('APPDATA')}\\.minecraft\\optionsLC.txt"
    target_lc = "C:\\OTO-Backup\\optionsLC.txt"
    logging.debug("Trying to backup mc settings...")
    try:
        shutil.copyfile(target_of, original_of)
        shutil.copyfile(target_1, original_1)
        shutil.copyfile(target_lc, original_lc)
        logging.debug("Done!")
    except Exception as err_mc:
        os.system("cls")
        os.system("color 4")
        logging.error(f"ERROR 1x317: Critical issue occured while backing up minecraft settings, {err_mc}")
        print("ERROR 1x317: Critical issue occured while backing up minecraft settings")
        input()
    with open("C:\\OTO-Backup\\power_plan.txt", "r") as pp_file:
        pp_guid = pp_file.read()
        pp_file.close()
    os.system(f"powercfg /setactive {pp_guid}")
    os.system("start C:\\OTO-Backup\\dns_backup.bat")
    clear()
    show_menu()
    print(colored("Done, backed up old settings!", "green"))
else:
    print("No valid input...")
    input("\nPress enter to exit...")