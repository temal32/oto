# Version: 1.0
# Release date: 16.06.2022

import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
#MessageBox(None, 'By using this program your accept our Terms of Service that can be found here: \nwww.temal.cf/OTO/TOS.html', 'OTOptimizer', 0)
import subprocess
import time
import speedtest
import os
import os.path
from termcolor import colored
os.system("cls")
os.system("title OT-Optimizer - www.discord.gg/zrzWHcea8w")
import logging
import requests
from decimal import Decimal
import win32api
# creating basic configuration for "logging" module to log into txt files
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style="{",
    filename="OT_log.log",
    filemode="w"
)

logging.info("STOP, READ CAREFULLY!")
logging.info("This file is for developers only, please do not change, modify or delete this file!")
logging.info("Send this file when prompted.")
logging.info("More information can be found here: https://discord.gg/t3gWbBdbNQ")

logging.debug("Program has been started.")
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
    except Exception as error_:
        os.system("cls")
        os.system("color 4")
        logging.error(f"ERROR 0x1: Critical issue occured while downloading file, {error_}")
        print(30 * "-")
        print("OT-Optimizer v1.0")
        print(30 * "-")
        print(colored(f"\nERROR 0x1: Critical issue occured.", "red"))
        print("Please contact support and send log file when prompted.")
        print("More information here: www.discord.gg/uve9t7raAt")
        print("Breakpoint reached, won't continue.")
        input()
        if input():
            exit(1)
        else:
            exit(1)
username = os.getlogin()
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
    print("OT-Optimizer v1.0")
    print(30*"-")
logging.debug("Defining get_ping()...")
def get_ping(): # function to get ping and network speed
    logging.debug("Getting servers...")
    print("Getting server...")
    test.get_servers()
    logging.debug("Getting best server...")
    best = test.get_best_server()
    logging.debug(f"Found best server: {best['host']} located in {best['country']}")
    print(f"Found best server: {best['host']} located in {best['country']}")
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
        options_file = f"C:\\Users\\{username}\\AppData\\Roaming\\.minecraft\\optionsof.txt"
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
        drives = win32api.GetLogicalDriveStrings()
        if "A:" in drives:
            print("CLEANING A:\...")
            logging.debug("Letter A...")
            os.system("defrag A:")
        if "B:" in drives:
            print("CLEANING B:\...")
            logging.debug("Letter B...")
            os.system("defrag B:")
        if "C:" in drives:
            print("CLEANING C:\...")
            logging.debug("Letter C...")
            os.system("defrag C:")
        if "D:" in drives:
            print("CLEANING D:\...")
            logging.debug("Letter D...")
            os.system("defrag D:")
        if "E:" in drives:
            print("CLEANING E:\...")
            logging.debug("Letter E...")
            os.system("defrag E:")
        if "F:" in drives:
            print("CLEANING F:\...")
            logging.debug("Letter F...")
            os.system("defrag F:")
        if "G:" in drives:
            print("CLEANING G:\...")
            logging.debug("Letter G...")
            os.system("defrag G:")
        if "H:" in drives:
            print("CLEANING H:\...")
            logging.debug("Letter H...")
            os.system("defrag H:")
        if "I:" in drives:
            print("CLEANING I:\...")
            logging.debug("Letter I...")
            os.system("defrag I:")
        if "J:" in drives:
            print("CLEANING J:\...")
            logging.debug("Letter J...")
            os.system("defrag J:")
        if "K:" in drives:
            print("CLEANING K:\...")
            logging.debug("Letter K...")
            os.system("defrag K:")
        if "L:" in drives:
            print("CLEANING L:\...")
            logging.debug("Letter L...")
            os.system("defrag L:")
        if "M:" in drives:
            print("CLEANING M:\...")
            logging.debug("Letter M...")
            os.system("defrag M:")
        if "N:" in drives:
            print("CLEANING N:\...")
            logging.debug("Letter N...")
            os.system("defrag N:")
        if "O:" in drives:
            print("CLEANING O:\...")
            logging.debug("Letter O...")
            os.system("defrag O:")
        if "P:" in drives:
            print("CLEANING P:\...")
            logging.debug("Letter P...")
            os.system("defrag P:")
        if "Q:" in drives:
            print("CLEANING Q:\...")
            logging.debug("Letter Q...")
            os.system("defrag Q:")
        if "R:" in drives:
            print("CLEANING R:\...")
            logging.debug("Letter R...")
            os.system("defrag R:")
        if "S:" in drives:
            print("CLEANING S:\...")
            logging.debug("Letter S...")
            os.system("defrag S:")
        if "T:" in drives:
            print("CLEANING T:\...")
            logging.debug("Letter T...")
            os.system("defrag T:")
        if "U:" in drives:
            print("CLEANING U:\...")
            logging.debug("Letter U...")
            os.system("defrag U:")
        if "V:" in drives:
            print("CLEANING V:\...")
            logging.debug("Letter V...")
            os.system("defrag V:")
        if "W:" in drives:
            print("CLEANING W:\...")
            logging.debug("Letter W...")
            os.system("defrag W:")
        if "X:" in drives:
            print("CLEANING X:\...")
            logging.debug("Letter X...")
            os.system("defrag X:")
        if "Y:" in drives:
            print("CLEANING Y:\...")
            logging.debug("Letter Y...")
            os.system("defrag Y:")
        if "Z:" in drives:
            print("CLEANING Z:\...")
            logging.debug("Letter Z...")
            os.system("defrag Z:")
    else:
        logging.debug(f"User input was {defrag}, skipping...")
        print("OK, skipping...")
        pass

logging.debug("Executing show_menu function...")
show_menu()
logging.debug("Executing get_ping function...")
get_ping()
logging.debug("Executing clear function...")
clear()
logging.debug("Executing show_menu function...")
show_menu()
print(f"Your current ping is: " + colored(old_ping, "red"))

logging.debug("Operating question 1, waiting for user input...")
question_1 = input("Do you want to upgrade to the best windows power plan? (y/n)")
logging.debug("Input gotten, answer is: " + question_1)
if question_1 == "y":
    logging.debug("Executing cmd command to change power plan...")
    os.system("powercfg -setactive scheme_min")
    clear()
    show_menu()
    logging.debug("Done, plan should be changed, no confirmation tho...")
    print("Successful!")
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
    #os.system("start C:\\Windows\\clean.bat")
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
    logging.debug("Changing DNS...")
    os.system('netsh interface ip set dns "Ethernet" static 1.0.0.1')
    os.system('netsh interface ip set dns "Ethernet0" static 1.0.0.1')
    os.system('netsh interface ip set dns "Ethernet1" static 1.0.0.1')
    os.system('netsh interface ip set dns "Wi-Fi" static 1.0.0.1')
    logging.debug("Done, changed DNS... not confirmed tho!")
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
    download("https://cdn.discordapp.com/attachments/985667930962403360/985670447515455548/LogParser.dll", "C:\\Windows\\LogParser.dll")
    logging.debug("Downloading Interop.MSUtil.dll...")
    download("https://cdn.discordapp.com/attachments/985667930962403360/985670448010387567/Interop.MSUtil.dll", "C:\\Windows\\Interop.MSUtil.dll")
    logging.debug("Downloading UnparkCPU.exe...")
    download("https://cdn.discordapp.com/attachments/985667930962403360/985670447775498310/UnparkCPU.exe", "C:\\Windows\\UnparkCPU.exe")
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
    download("https://cdn.discordapp.com/attachments/985667930962403360/987026646555058227/test.reg", "C:\\Windows\\test.reg")
    logging.debug("Downloading test2.reg...")
    download("https://cdn.discordapp.com/attachments/985667930962403360/987026646378872852/test2.reg","C:\\Windows\\test2.reg")
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
    logging.debug("Calling powershell commands...")
    logging.debug("Disabling Flow Control...")
    subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Flow Control' -DisplayValue 'Disabled'")
    logging.debug("Disabling Power Saving Mode...")
    subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Power Saving Mode' -DisplayValue 'Disabled'")
    logging.debug("Disabling Gigabit Lite")
    subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Gigabit Lite' -DisplayValue 'Disabled'")
    logging.debug("Disabling Green Ethernet...")
    subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Green Ethernet' -DisplayValue 'Disabled'")
    logging.debug("Disabling Energy-Efficient Ethernet...")
    subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Energy-Efficient Ethernet' -DisplayValue 'Disabled'")
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
logging.debug("Getting new ping...")
print("Getting new ping...")
new = speedtest.Speedtest()
logging.debug("Getting servers...")
print("Getting server...")
new.get_servers()
logging.debug("Getting best server...")
best = new.get_best_server()
logging.debug(f"Found best server: {best['host']} located in {best['country']}")
print(f"Found best server: {best['host']} located in {best['country']}")
logging.debug("Starting download test...")
print("Performing download test...")
download_result = new.download()
logging.debug("Starting upload test...")
print("Performing upload test...")
upload_result = new.upload()
logging.debug("Starting ping test...")
print("Performing ping test...")
ping_result = new.results.ping
global new_download, new_upload, new_ping
new_download = f'{download_result / 1024 / 1024:.2f}'
new_upload = f'{upload_result / 1024 / 1024:.2f}'
new_ping = f"{ping_result:.2f}"
clear()
show_menu()
old_ping = Decimal(old_ping)
new_ping = Decimal(new_ping)
difference = old_ping - new_ping
str(old_ping)
str(new_ping)
logging.debug("Old ping: " + str(old_ping) + ", new ping: " + str(new_ping))
print("OLD PING: " + str(old_ping))
print("NEW PING: " + str(new_ping))
#print(difference)
diff_str = str(difference)
if diff_str.startswith("-"):
    diff_str1 = diff_str.lstrip("-")
    print("Ping did not decrease this time, ping increased by " + diff_str1 + ".")
else:
    diff_str = diff_str.lstrip("-")
    print(colored("Ping decreased by " + diff_str, "green"))

logging.debug("Waiting for input...")
input("\nPress enter to reboot...")
logging.debug("Exiting and rebooting pc...")
os.system("shutdown -t 0 -r -f")
