from win32api import GetLogicalDriveStrings
from decimal import Decimal
from logging import info, debug, error, basicConfig, DEBUG
from termcolor import colored
from os import system, path, chdir, getenv, startfile
from speedtest import Speedtest
from time import sleep
from subprocess import run
from ctypes import windll
from urllib.request import urlretrieve
from tempfile import gettempdir

# Variables
APPDATA = getenv('APPDATA')
MessageBox = windll.user32.MessageBoxW

links = ['https://cdn.discordapp.com/attachments/985667930962403360/985668051427008552/clean.bat'
         'https://cdn.discordapp.com/attachments/985667930962403360/985668066274861136/Doublehit_Connection.reg',
         'https://cdn.discordapp.com/attachments/985667930962403360/985670447515455548/LogParser.dll',
         'https://cdn.discordapp.com/attachments/985667930962403360/985670448010387567/Interop.MSUtil.dll',
         'https://cdn.discordapp.com/attachments/985667930962403360/985670447775498310/UnparkCPU.exe',
         'https://cdn.discordapp.com/attachments/985667930962403360/987026646555058227/test.reg',
         'https://cdn.discordapp.com/attachments/985667930962403360/987026646378872852/test2.reg']

#MessageBox(None, 'By using this program your accept our Terms of Service that can be found here: \nwww.temal.cf/OTO/TOS.html', 'OTOptimizer', 0)
system("cls")
system("title OT-Optimizer - www.discord.gg/zrzWHcea8w")
# creating basic configuration for "logging" module to log into txt files
basicConfig(
    level=DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style="{",
    filename="OT_log.log",
    filemode="w"
)

# Functions


def clear():  # function to clear console
    system("cls")


def show_menu():  # function to show a good menu in console
    print(30*"-")
    print("OT-Optimizer v1.0")
    print(30*"-")


def get_ping():  # function to get ping and network speed
    test = Speedtest()
    debug("Getting servers...")
    print("Getting server...")
    test.get_servers()
    debug("Getting best server...")
    best = test.get_best_server()

    debug(
        f"Found best server: {best['host']} located in {best['country']}")
    print(f"Found best server: {best['host']} located in {best['country']}")

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

    debug(
        f"Done with testing, results: {old_download, old_upload, old_ping}")

    system("cls")
    print(f"Download: {old_download} mbits")
    print(f"Upload: {old_upload} mbits")
    print(f"Ping: {old_ping} ms")
    debug("Done with getting network info. Terminate function.")


def settings_minecraft():
    debug("settings_minecraft function has been executed")
    fps = input("Would you like to apply the best in-game settings? (y/n)")
    debug("Input gotten, answer is: " + fps)
    if fps == "y":
        debug("Executing if-statement...")
        print('''Choose a value (1, 2)
Option 1 - High end computer (Good graphics with the highest FPS)
Option 2 - Low end computer (lowest graphics with the highest FPS)''')
        op_1 = input("Enter value: ")
        debug("Input gotten, answer is: " + op_1)
# HERE
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
            print("Enter a correct value")
            settings_minecraft()
    else:
        debug(f"User input was {fps}, skipping...")
        print("OK, skipping...")
        pass


def appearance():
    debug("appearance function has been executed...")
    op_2 = input(
        "Would you like to lower the appearance of windows to increase performance? (y/n)")
    debug("Input gotten, answer is: " + op_2)
    if op_2 == "y":
        system("REG ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects /v VisualFXSetting /t REG_DWORD /d 2 /f")
    else:
        debug(f"User input was {op_2}, skipping...")
        print("OK, skipping...")
        pass


def defrag():
    debug("defrag function has been executed...")
    defrag = input(
        "Would you like to defrag your drives to increase performance? (y/n)")
    debug("Input gotten, answer is: " + defrag)
    if defrag == "y":
        debug("Defraging drives...")
        drives = GetLogicalDriveStrings().split("\000")
        for drive in drives:
            if path.exists(drive):
                system(f'defrag.exe {drive}')
    else:
        debug(f"User input was {defrag}, skipping...")
        print("OK, skipping...")
        pass


info("STOP, READ CAREFULLY!")
info(
    "This file is for developers only, please do not change, modify or delete this file!")
info("Send this file when prompted.")
info(
    "More information can be found here: https://discord.gg/t3gWbBdbNQ")

debug("Program has been started.")
# Switch to the TEMP directory
chdir(gettempdir())
debug("Requesting download...")
try:
    for link in links:
        debug(f"Downloading {link}...")
        urlretrieve(link, link.split("/")[-1])
        debug(f"Downloaded {link} to {gettempdir()}")
        print(f"Downloaded {link} to {gettempdir()}")
except Exception as error_:
    system("cls")
    system("color 4")
    error(
        f"ERROR 0x1: Critical issue occured while downloading file, {error_}")
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

show_menu()
get_ping()
clear()
show_menu()
print(f"Your current ping is: " + colored(old_ping, "red"))

debug("Operating question 1, waiting for user input...")
question_1 = input(
    "Do you want to upgrade to the best windows power plan? (y/n)")
debug("Input gotten, answer is: " + question_1)
if question_1 == "y":
    debug("Executing cmd command to change power plan...")
    system("powercfg -setactive scheme_min")
    clear()
    show_menu()
    debug("Done, plan should be changed, no confirmation tho...")
    print("Successful!")
else:
    debug(f"User input was {question_1}, skipping...")
    print("OK, skipping...")
    pass

#############################################################################################
debug("Operating question 2, waiting for user input...")
question_2 = input("Would you like to flush and clean your DNS? (y/n)")
debug("Input gotten, answer is: " + question_2)
if question_2 == "y":
    debug("Calling clean.bat file...")
    #system("start clean.bat")
    startfile("clean.bat")
    debug("Ran file!")
    sleep(10)
    clear()
    show_menu()
    print("Done! Continuing...")
else:
    debug(f"User input was {question_2}, skipping...")
    print("OK, skipping...")
    pass

#############################################################################################
debug("Operating question 3, waiting for user input...")
question_3 = input(
    "Would you like to improve the TCP connection by applying a registry edit? (y/n)")
debug("Input gotten, answer is: " + question_3)
if question_3 == "y":
    print("In the next few seconds 4 windows will pop up please do following:")
    print("1. Confirm again by pressing 'Yes'")
    print("2. Finally press 'OK'")
    debug("Calling regedit file...")
    startfile("Doublehit_Connection.reg")
    debug("Called!")
    sleep(5)
    clear()
    show_menu()
    print("Done! Continuing...")
else:
    debug(f"User input was {question_3}, skipping...")
    print("OK, skipping...")
    pass

#############################################################################################
debug("Operating question 4, waiting for user input...")
question_4 = input("Do you want to change to a faster dns? (y/n)")
debug("Input gotten, answer is: " + question_4)
if question_4 == "y":
    debug("Changing DNS...")
    args = ['"Ethernet" static 1.0.0.1', '"Ethernet0" static 1.0.0.1',
            '"Ethernet1" static 1.0.0.1', '"Wi-Fi" static 1.0.0.1']
    for arg in args:
        system(f'netsh interface ip set dns {arg}')
    debug("Done, changed DNS... not confirmed tho!")
    clear()
    show_menu()
    print("Done! Continuing...")
else:
    debug(f"User input was {question_4}, skipping...")
    print("OK, skipping...")
    pass

########################################################################################
debug("Operating question 5, waiting for user input...")
question_5 = input("Do you want to execute cpu unparker? (y/n)")
debug("Input gotten, answer is: " + question_5)
if question_5 == "y":
    print("1. Press the Check Status button in the new window")
    print("2. After checking, press unpark all and exit the program")
    startfile("UnparkCPU.exe")
    sleep(5)
    debug("Ran!")
    clear()
    show_menu()
    print("Done! Continuing...")
else:
    debug(f"User input was {question_5}, skipping...")
    print("OK, skipping...")
    pass

################################################################################################

debug("Operating question 6, waiting for user input...")
question_6 = input("Do you want to optimize TCP? (y/n)")
debug("Input gotten, answer is: " + question_6)
if question_6 == "y":
    print("Please confirm both pop up's:")
    print("1. Confirm by pressing 'Yes'")
    print("2. Press 'OK'")
    print("3. Confirm again")
    print("4. Finally press 'OK'")
    debug("Calling test.reg file...")
    startfile("test.reg")
    debug("Calling test2.reg file...")
    startfile("test2.reg")
    debug("Called!")
    sleep(5)
    clear()
    show_menu()
    print("Done! Continuing...")
else:
    debug(f"User input was {question_6}, skipping...")
    print("OK, skipping...")
    pass

#########################################################################################################


debug("Operating question 7, waiting for user input...")
question_7 = input(
    "Would you like to change the Network Adapter Properties for a faster connection? (y/n)")
debug("Input gotten, answer is: " + question_6)
if question_7 == "y":
    debug_and_args = [{'debug': "Disabling Flow Control...", 'arg': "'Flow Control' -DisplayValue 'Disabled'"},
                      {'debug': "Disabling Power Saving Mode...",
                          'arg': "'Power Saving Mode' -DisplayValue 'Disabled'"},
                      {'debug': "Disabling Gigabit Lite...",
                       'arg': "'Gigabit Lite' -DisplayValue 'Disabled'"},
                      {'debug': "Disabling Green Ethernet...",
                       'arg': "'Green Ethernet' -DisplayValue 'Disabled'"},
                      {'debug': "Disabling Energy-Efficient Ethernet...", 'arg': "'Energy-Efficient Ethernet' -DisplayValue 'Disabled'"}]
    debug("Calling powershell commands...")
    for x in debug_and_args:
        debug(x['debug'])
        run(
            f"powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName {x['arg']}")
    debug("Done")
    clear()
    show_menu()
else:
    debug(f"User input was {question_7}, skipping...")
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
debug("Getting new ping...")
print("Getting new ping...")
new = Speedtest()

debug("Getting servers...")
print("Getting server...")
new.get_servers()

debug("Getting best server...")
best = new.get_best_server()

debug(
    f"Found best server: {best['host']} located in {best['country']}")
print(f"Found best server: {best['host']} located in {best['country']}")

debug("Starting download test...")
print("Performing download test...")
download_result = new.download()

debug("Starting upload test...")
print("Performing upload test...")
upload_result = new.upload()

debug("Starting ping test...")
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
debug("Old ping: " + str(old_ping) + ", new ping: " + str(new_ping))
print("OLD PING: " + str(old_ping))
print("NEW PING: " + str(new_ping))

# print(difference)
diff_str = str(difference)
if diff_str.startswith("-"):
    diff_str1 = diff_str.lstrip("-")
    print("Ping did not decrease this time, ping increased by " + diff_str1 + ".")
else:
    diff_str = diff_str.lstrip("-")
    print(colored("Ping decreased by " + diff_str, "green"))

debug("Waiting for input...")
input("\nPress enter to reboot...")
debug("Exiting and rebooting pc...")
system("shutdown.exe /r /t 0")
