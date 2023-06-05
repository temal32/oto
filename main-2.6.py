# Version: 2.6
# Release date: 05.06.2023 (dd/mm/yyyy)

version = 2.6

from wmi import WMI
from time import sleep
from requests import get
from ctypes import windll
from pytz import timezone
from subprocess import run
from hashlib import sha256
from pythonping import ping
from itertools import cycle
from getpass import getpass
from winshell import startup
from threading import Thread
from datetime import datetime
from pyuac import isUserAdmin
from termcolor import colored
from cursor import hide, show
from platform import win32_ver
from tempfile import gettempdir
from speedtest import Speedtest
from colorama import Fore, Style
from urllib.parse import urlparse
from dns.resolver import Resolver
from webbrowser import open as web_open
from sys import argv, executable, stdout
from messagebox import askyesno, showinfo
from win32api import GetLogicalDriveStrings
from powerplan import get_current_scheme_guid
from shutil import copyfile, rmtree, get_terminal_size
from discord_webhook import DiscordWebhook, DiscordEmbed
from logging import info, debug, error, basicConfig, DEBUG, shutdown
from winreg import HKEY_CURRENT_USER, OpenKey, KEY_ALL_ACCESS, EnumValue
from os import system, chdir, getenv, getlogin, mkdir, remove, name, listdir, path; from os.path import isfile, islink, isdir

restricted_ver = False
username = getlogin()
encry_username = sha256(username.encode()).hexdigest()[:10]
drive_letter = getenv('HOMEDRIVE')
basicConfig(
    level=DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style="{",
    filename=f"OTO-Logs_{encry_username}.log",
    filemode="a"
)
info("\n" + 140*"-" + "\n")
info("STOP, READ CAREFULLY!")
info('Auto-generated file by "OT-Optimizer", DO NOT EDIT')
info("This file is for developers only, please do not change, modify or delete this file!")
info("Send this file when prompted.")
info("More information can be found by joining our discord server: www.discord.gg/Vsm9dMA6TB")
debug(f"Program with version {version} has been started.")
system("mode 120,46")
debug("Defining functions...")


def input_exit():
    getpass("\nPress enter to exit...")
    exit()


def clear_last_line():
    print("\033[A                             \033[A")


def clear():
    system("cls")


def show_menu():
    terminal_columns = get_terminal_size().columns
    fill_chara_cyan = colored(terminal_columns*"-", color="cyan")
    menu_line = colored(f"OT-Optimizer v{version}", color="blue", attrs=['underline', 'bold'])
    menu_contact = colored(" - Temal#1000", color="cyan")
    menu_dc = colored("\nwww.discord.gg/Vsm9dMA6TB", color="blue")
    menu_github = colored("www.github.com/temal32/oto", color="blue")
    print(fill_chara_cyan)
    print(menu_line, end="" + menu_contact)
    print(menu_dc)
    print(menu_github)
    print(fill_chara_cyan)


loading_done = False


def animate(text):
    hide()
    for c in cycle(['', '.', '..', '...', '   ', '.', '..', '...']):
        if loading_done:
            break
        stdout.write(f'\r{text}' + c)
        stdout.flush()
        sleep(0.1)
    show()


def check_update():
    show_menu()
    debug("Checking for updates...")
    Thread(target=animate, args=["Checking for updates"]).start()
    debug("Thread started.")
    sleep(1)
    try:
        debug("Getting response...")
        response = get('https://raw.githubusercontent.com/temal32/oto/main/version.txt')
        data = response.text
        debug("Got response!")
        debug(f"float data = {float(data)} : float version = {float(version)}")
        global loading_done
        loading_done = True
        if float(data) > float(version):
            debug("Current version outdated!")
            print(colored("\nUpdate available!", "green"))
            print("Starting download of new version...")
            debug("Starting download of new version...")
            new_version = float(data)
            updated_link = f"https://github.com/temal32/oto/releases/download/OTO-{new_version}/OT-Optimizer_{new_version}.exe"
            try:
                r = get(updated_link, allow_redirects=True)
                open(f"OT-Optimizer_{new_version}.exe", 'wb').write(r.content)
                debug("New version downloaded!")
                print("Downloaded new version!")
                sleep(1)
                print("Executing updated version of OTO...")
                sleep(2)
                run(f"OT-Optimizer_{new_version}.exe")
            except Exception as request_error:
                error(f"Could not download update or run updated version, {request_error}")
                if agreed:
                    embed = DiscordEmbed(title='ERROR',
                                         description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{request_error}',
                                         color='ff0000')
                    webhook_error_reporting.add_embed(embed)
                    rsp = webhook_error_reporting.execute().status_code
                    debug(f"Error-Webhook sent with status code: {rsp}")
                print(colored("ERROR: An error occurred while updating OTO.", "red"))
                input_exit()
            sleep(2)
            loading_done = True
        else:
            loading_done = True
            print(colored("\nYou're already using the latest version of this software.", "green"))
            debug("Already using newest version!")
            sleep(3)
    except Exception as request_error:
        error(f"Could not check for new updates, {request_error}")
        print(colored("ERROR: Could not check for updates.", "red"))
        loading_done = True
        if agreed:
            embed = DiscordEmbed(title='ERROR',
                                 description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{request_error}',
                                 color='ff0000')
            webhook_error_reporting.add_embed(embed)
            rsp = webhook_error_reporting.execute().status_code
            debug(f"Error-Webhook sent with status code: {rsp}")
        input_exit()


def typewriter(text):
  for character in text:
    sleep(0.80)
    stdout.write(character)
    stdout.flush()


def delete(path):
    try:
        if isfile(path) or islink(path):
            remove(path)
            print(Fore.LIGHTRED_EX + "REMOVED" + Style.RESET_ALL + " - " + path + Style.RESET_ALL)
        elif isdir(path):
            rmtree(path)
            print(Fore.LIGHTRED_EX + "REMOVED" + Style.RESET_ALL + " - " + path + " and all it's content" + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + "MISSED " + Style.RESET_ALL + " - " + path + Style.RESET_ALL)
    except:
        pass


def defrag():
    debug("defrag function has been executed...")
    defrag = input("Would you like to defrag your drives to increase performance? (Only use this function when using HDD, not SSD!) (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + defrag)
    if defrag in yes:
        debug("Defraging drives...")
        print("Defraging... (this can take from several minutes up to a few hours)\n" + colored("Press Ctrl+C if you want to cancel the process!", "yellow"))
        sleep(3)
        try:
            drives = GetLogicalDriveStrings().split("\000")
            for drive in drives:
                if path.exists(drive):
                    system(f'defrag.exe {drive}')
        except KeyboardInterrupt as err__:
            debug("Defrag progress cancelled due to keyboard interrupt. (143)")
            print("Process cancelled!")
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

mc_hosts = ['213.32.7.212', '51.161.99.99', '216.238.107.135', '51.79.245.200', '207.246.121.152', '162.19.138.143', '51.79.163.166']
mc_hosts_names = ['MMC EU       ', 'MMC NA       ', 'MMC SA       ', 'MMC AS       ', 'Stratus      ', 'AcentraMC EU ', 'AcentraMC AS ']


def get_ping():
    global loading_done
    if speed_test_best is None:
        error("speed_test_best variable is undefined, fatal.")
        print(colored(f"Fatal error occurred, please try again later!\nError code: undefined_variable_219", "red"))
        if agreed:
            embed = DiscordEmbed(title='ERROR',
                                 description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\nundefined_variable_219',
                                 color='ff0000')
            webhook_error_reporting.add_embed(embed)
            rsp = webhook_error_reporting.execute().status_code
            debug(f"Error-Webhook sent with status code: {rsp}")
        input_exit()
    debug(f"Found best server: {speed_test_best['host']} located in {speed_test_best['country']}")
    debug("Writing server host to textfile...")
    try:
        with open(f"{drive_letter}\\OTO\\server_best.txt", 'w') as file:
            file.write(speed_test_best['host'])
            file.close()
    except Exception as write_err:
        error(f"Could not write server_best.txt file, error: {write_err}")
        if agreed:
            embed = DiscordEmbed(title='ERROR',
                                 description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{write_err}',
                                 color='ff0000')
            webhook_error_reporting.add_embed(embed)
            rsp = webhook_error_reporting.execute().status_code
            debug(f"Error-Webhook sent with status code: {rsp}")
        print(colored("ERROR: Couldn't join path or file.", "red"))
        input_exit()
    debug("Done with getting network info. Terminate function.")
    global speed_test_old_latency
    speed_test_old_latency = speed_test_best["latency"]
    print(f"\nCurrent ping: {speed_test_old_latency}, using server located in {speed_test_best['country']}.")
    ask_opt_ping = input("Do you optionally want to ping several Minecraft servers before starting optimization for better comparison? (y/n)\nEnter: ")
    if ask_opt_ping in yes:
        loading_done = False
        Thread(target=animate, args=["Pinging additional servers"]).start()
        def ping_host(host):
            try:
                ping_result = ping(target=host, count=10, timeout=2)
            except Exception as ping_exc:
                error(f"Could not get mc latency. Errorcode: {ping_exc}, filecontent: {host}")
                print("Could not get mc latency, try again!")
                if agreed:
                    embed = DiscordEmbed(title='ERROR',
                                         description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{ping_exc}',
                                         color='ff0000')
                    webhook_error_reporting.add_embed(embed)
                    rsp = webhook_error_reporting.execute().status_code
                    debug(f"Error-Webhook sent with status code: {rsp}")
                input_menu()
            return {'host': host, 'avg_latency': ping_result.rtt_avg_ms}


        try:
            dir = path.join(f"{drive_letter}\\OTO", "OTO-Pings")
            if not path.exists(dir):
                mkdir(dir)
        except Exception as exception_path:
            error(f"Couldn't join/make path, {exception_path}")
            print(colored("ERROR: Couldn't join path.", "red"))
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{exception_path}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
            input_menu()
        for host in mc_hosts:
            with open(f"{drive_letter}\\OTO\\OTO-Pings\\ping_{ping_host(host)['host']}.txt", 'w+') as file:
                file.write(str(ping_host(host)['avg_latency']))
        loading_done = True

    else:
        print("OK, skipping...")
        sleep(2)
    return speed_test_old_latency


def settings_minecraft():
    debug("settings_minecraft function has been executed")
    fps = input("Would you like to apply the best Minecraft in-game settings? (y/n)\nEnter: ")
    debug("Input gotten, answer is: " + fps)
    if fps in yes:
        debug("Executing if-statement...")
        print('''Choose a value (1, 2)
        Option 1 - High end computer (good graphics with the highest FPS)
        Option 2 - Low end computer (lowest graphics with the highest FPS)''')
        op_1 = input("Enter value: ")
        debug("Input gotten, answer is: " + op_1)
        options_file = f"{APPDATA}\\.minecraft\\optionsof.txt"
        if op_1 == "1":
            try:
                options = open(options_file, "w")
            except Exception as settings_mc_apply_err:
                error(f"ERROR 0x317: Critical issue occurred while applying new Minecraft settings, {settings_mc_apply_err}")
                if agreed:
                    embed = DiscordEmbed(title='ERROR',
                                         description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{settings_mc_apply_err}',
                                         color='ff0000')
                    webhook_error_reporting.add_embed(embed)
                    rsp = webhook_error_reporting.execute().status_code
                    debug(f"Error-Webhook sent with status code: {rsp}")
                print(colored(f"\nERROR 0x317: Critical issue occurred while applying Minecraft settings,\nplease check if Minecraft is installed in the correct path.", "red"))
                print("Please contact support and send log file when prompted.")
                print("Breakpoint reached, won't continue.")
                input_exit()
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
            try:
                options = open(options_file, "w")
            except Exception as settings_mc_apply_err:
                error(f"ERROR 0x317: Critical issue occurred while applying new Minecraft settings, {settings_mc_apply_err}")
                if agreed:
                    embed = DiscordEmbed(title='ERROR',
                                         description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{settings_mc_apply_err}',
                                         color='ff0000')
                    webhook_error_reporting.add_embed(embed)
                    rsp = webhook_error_reporting.execute().status_code
                    debug(f"Error-Webhook sent with status code: {rsp}")
                print(colored(f"\nERROR 0x317: Critical issue occurred while applying Minecraft settings,\nplease check if Minecraft is installed in the correct path.", "red"))
                print("Please contact support and send log file when prompted.")
                print("Breakpoint reached, won't continue.")
                input_exit()
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


def appearance():
    debug("appearance function has been executed...")
    op_2 = input("Would you like to lower the appearance of Windows to increase performance? (y/n)\nEnter: ")
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


def update_drivers():
    debug("update_drivers function has been executed...")
    update_drv = input("Would you like to update GPU drivers (Nvidia only!)? (y/n)\nEnter: ")
    if update_drv in yes:
        debug("Calling nvddl.exe with argument: -dl, -s")
        run(['nvddl.exe', '-dl', '-s'], cwd=gettempdir())
        print("Please manually continue driver installation.")
        sleep(5)
    else:
        debug(f"User input was {update_drv}, skipping...")
        print("OK, skipping...")
        pass


def disable_autostart():
    debug("disable_autostart function has been executed...")
    disable_ques = input("Would you like to disable autostart for certain programs? (y/n)\nEnter: ")
    if disable_ques in yes:
        try:
            r = OpenKey(HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_ALL_ACCESS)
        except Exception as open_key_error:
            error(f"Could not open path/key in registry, {open_key_error}")
            print(colored("ERROR: Could not open registry keys.", "red"))
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{500}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{open_key_error}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
            input_exit()
        try:
            count = 0
            while 1:
                name, value, type = EnumValue(r, count)
                del_reg = input(f"Would you like to disable autostart for following service? (y/n):\n{colored(eval(repr(name)), 'blue')}\nEnter: ")
                if del_reg in yes:
                    system(f'reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v "{eval(repr(name))}" /f')
                    debug(f"Disabled autostart for following service: {name}")
                count = count + 1
        except Exception as errr:
            debug(f"Warning 0x264: Fatal issue occurred while looping trough regedit keys, {errr}")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {disable_ques}, skipping...")
        print("OK, skipping...")
        pass


def clean_junk():
    debug("clean_junk function has been executed...")
    quest_clean_junk = input("Would you like to clean unnecessary junk files? (y/n)\nEnter: ")
    if quest_clean_junk in yes:
        debug("Start cleaning files...")
        all_files = listdir(gettempdir())
        for temp_file in all_files:
            try:
                delete(f"{gettempdir()}\\{temp_file}")
                debug(f"Deleted: {temp_file}")
            except Exception as del_error:
                error("HARMLESS: ", del_error)
                pass
        all_files2 = listdir(f"{drive_letter}\\Windows\\Temp")
        for temp_file2 in all_files2:
            try:
                delete(f"{drive_letter}\\Windows\\Temp\\{temp_file2}")
                debug(f"Deleted: {temp_file2}")
            except Exception as del_error2:
                error("HARMLESS: ", del_error2)
                pass
        path3 = f"{drive_letter}\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Recent"
        all_files3 = listdir(path3)
        for temp_file3 in all_files3:
            try:
                delete(f"{path3}\\{temp_file3}")
                debug(f"Deleted: {temp_file3}")
            except Exception as del_error3:
                error("HARMLESS: ", del_error3)
                pass
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {quest_clean_junk}, skipping...")
        print("OK, skipping...")
        pass


def disable_services():
    debug("disable_services function has been executed...")
    disable_ques = input("Would you like to disable certain Windows services? (you can safely disable all of them) (y/n)\nEnter: ")
    if disable_ques in yes:
        services = {
            "Windows Defender": "WdNisSvc",
            "Windows Mobile Hotspot Service": "icssvc",
            "Print Spooler": "Spooler",
            "Fax Service": "Fax",
            "Windows Security Center": "wscsvc",
            "Certificate Propagation Service": "CertPropSvc",
            "Windows Biometric Service": "WbioSrvc",
            "Broadcast DVR Server": "BcastDVRUserService",
            "Windows OneSyncSvc": "OneSyncSvc_65f79",
            "Windows Update Service": "wuauserv",
            "Downloaded Maps Manager": "MapsBroker"
        }
        for service in services:
            disable_ser = input(f"Would you like to disable following service? (y/n):\n{colored(service, 'blue')}\nEnter: ")
            if disable_ser in yes:
                run(["powershell", "Set-Service", "-Name", services[service], "-StartupType", "Disabled"], capture_output=True)
                debug(f"Disabled following service: {service}")
                print(f"Disabled {service}")
            else:
                print("OK, skipping...")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {disable_ques}, skipping...")
        print("OK, skipping...")
        pass


def disable_xbox_gamebar():
    debug("disable_xbox_gamebar function has been executed...")
    disable_ques = input("Would you like to disable Xbox Game Bar? (y/n)\nEnter: ")
    if disable_ques in yes:
        run(["powershell", "Get-AppxPackage", "Microsoft.XboxGamingOverlay", "|", "Remove-AppxPackage"])
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {disable_ques}, skipping...")
        print("OK, skipping...")
        pass


def uninstall_onedrive():
    debug("uninstall_onedrive function has been executed...")
    uninstall_od = input("Would you like to uninstall OneDrive to get better performance? (y/n)\nEnter: ")
    if uninstall_od in yes:
        system("%SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall")
        debug("Uninstalled OneDrive.")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {uninstall_od}, skipping...")
        print("OK, skipping...")
        pass


def enable_gamemode():
    debug("enable_gamemode function has been executed...")
    enable_ques = input("Would you like to enable Windows Game Mode? (y/n)\nEnter: ")
    if enable_ques in yes:
        chdir(gettempdir())
        system(r"%windir%\system32\reg.exe import Turn_on_Game_Mode.reg")
        debug("Enabled Windows Game Mode!")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {enable_ques}, skipping...")
        print("OK, skipping...")
        pass


def open_overclock():
    debug("open_overclock function has been executed...")
    enable_ques = input("Would you like to get redirected to a website to overclock your GPU? (y/n)\nEnter: ")
    if enable_ques in yes:
        chdir(gettempdir())
        web_open("https://www.msi.com/Landing/afterburner/graphics-cards")
        debug("Opened webbrowser!")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {enable_ques}, skipping...")
        print("OK, skipping...")
        pass


def enable_agpu_scheduling():
    debug("enable_agpu_scheduling function has been executed...")
    enable_ques = input("Would you like to enable hardware accelerated GPU scheduling? (y/n)\nEnter: ")
    if enable_ques in yes:
        chdir(gettempdir())
        system(r"%windir%\system32\reg.exe import enable-AGPU_scheduling.reg")
        debug("Enabled hardware accelerated GPU scheduling!")
        clear()
        show_menu()
        print("Done! Continuing...")
    else:
        debug(f"User input was {enable_ques}, skipping...")
        print("OK, skipping...")
        pass


def change_powerplan():
    debug("Executing cmd command to change power plan...")
    system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
    system("powercfg /setactive scheme_min")
    clear()
    show_menu()
    debug("Power plan has been changed.")
    print("Successful. We additionally added the ultimate power plan, you may want to switch manually.")


def flush_clean_net():
    system("ipconfig /renew")
    system("ipconfig /flushdns")
    debug("Ran file!")
    sleep(10)
    clear()
    show_menu()
    print("Done! Continuing...")


def change_dns():
    debug("Changing DNS...")
    run(f"{gettempdir()}\\dns_er.bat")
    clear()
    show_menu()
    print("Done! Continuing...")


def unpark_cpu():
    debug("Running reg command...")
    system(r'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" /v ValueMax /t REG_DWORD /d 0 /f')
    system(r'REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" /v ValueMin /t REG_DWORD /d 0 /f')
    debug("Ran!")
    clear()
    show_menu()
    print("Done! Continuing...")


def optimize_tcp():
    sleep(2)
    debug("Calling oto_tcp.bat file...")
    chdir(gettempdir())
    run(f"{gettempdir()}\\oto_tcp.bat")
    debug("Called!")
    sleep(3)
    clear()
    show_menu()
    print("Done! Continuing...")


def scan_sfc():
    run(["sfc", "/scannow"])
    debug("Done")
    clear()
    show_menu()
    print("Done! Continuing...")


def change_net_prop():
    global connection_type
    for x in WMI().Win32_NetworkAdapter():
        match x.NetConnectionID:
            case 'Ethernet':
                debug("WMI RETURNS ETHERNET!!!")
                ethernet_right = input("Is it right that you are actively using Ethernet? (y/n)\nEnter: ")
                if ethernet_right in yes:
                    debug(f"User input: Ethernet : {x.name}")
                    connection_type = "Ethernet"
                    break
                else:
                    wifi_right = input("Are you using Wi-Fi then? (y/n)\nEnter: ")
                    if wifi_right in yes:
                        debug(f"User input: Wi-Fi : {x.name}")
                        connection_type = "Wi-Fi"
                        break
                    else:
                        debug("Confused, using Ethernet...")
                        connection_type = "Ethernet"
            case 'Wi-Fi':
                debug("WMI RETURNS WI-FI!!!")
                debug(f"Skipping change_net_prop, user using Wi-Fi : {x.name}")
                connection_type = "Wi-Fi"
                break
    print("Please wait, this can take a while...")
    try:
        pw_template = 'powershell -Command "& {Set-NetAdapterAdvancedProperty -Name "' + connection_type + '" -RegistryKeyword '
        keywords_values = ['"*InterruptModeration" -RegistryValue 0}',
                           '"*IPChecksumOffloadIPv4" -RegistryValue 3}',
                           '"*JumboPacket" -RegistryValue 1514}',
                           '"*LsoV2IPv4" -RegistryValue 0}', '"*LsoV2IPv6" -RegistryValue 0}',
                           '"*NumRssQueues" -RegistryValue 4}',
                           '"*ReceiveBuffers" -RegistryValue 512}', '"*RSS" -RegistryValue 1}',
                           '" -RegistryKeyword "*TCPChecksumOffloadIPv4" -RegistryValue 3}',
                           '"*TCPChecksumOffloadIPv6" -RegistryValue 3}',
                           '" -RegistryKeyword "*TransmitBuffers" -RegistryValue 128}',
                           '" -RegistryKeyword "AdvancedEEE" -RegistryValue 0}',
                           '" -RegistryKeyword "EnableGreenEthernet" -RegistryValue 0}',
                           '" -RegistryKeyword "GigaLite" -RegistryValue 0}',
                           '" -RegistryKeyword "PowerSavingMode" -RegistryValue 0}']
        for command in keywords_values:
            cmd_net = run(pw_template + command, shell=True, capture_output=True).returncode
            if cmd_net != 0:
                error(f"Normal error: following network property is not supported: {command}")
            else:
                debug(f"Changed following network property: {command}")
    except Exception as error_:
        error(f"Couldn't change network adapter properties, {error_}")
        print("Couldn't change network adapter properties!")
        if agreed:
            embed = DiscordEmbed(title='ERROR',
                                 description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{error_}',
                                 color='ff0000')
            webhook_error_reporting.add_embed(embed)
            rsp = webhook_error_reporting.execute().status_code
            debug(f"Error-Webhook sent with status code: {rsp}")
        input_menu()
    print("Done!")
    sleep(3)
    clear()
    debug("Done")
    clear()
    show_menu()
    print("Done! Continuing...")


def create_backup():
    print(f"\n{colored('DISCLAIMER:', attrs=['underline'])}\nIf all successful, backup will include following data:\n - Restore point creation\n - Registry data\n - Certain Minecraft settings\n - DNS resolver\n - Powerplan scheme",
        "\n\n1. This backup does not include files or any other 3rd-party data."
        "\n2. Creating a backup will also create a Windows restore point but you need to restore from it manually.")
    print(colored("3. Creating a backup cannot guarantee the security of your files and your system.", color="red", attrs=["blink", "bold"]))
    sleep(10)
    backup_ques = input("\n\nYou are about to create a backup, would you like to continue? (y/n)\nEnter: ")
    if backup_ques in yes:
        print("Creating restore point...")
        debug("Creating restore point...")
        system(f'powershell.exe Enable-ComputerRestore -Drive "{drive_letter}"')
        debug("Enabled ComputerRestore!")
        system(r'wmic.exe /Namespace:\\root\default Path SystemRestore Call CreateRestorePoint "OT-Optimizer: Automatized restore point", 100, 7')
        debug("Actually created a restore point.")
        debug("Backing up!")
        debug("Creating folder...")
        try:
            dir = path.join(f"{drive_letter}\\OTO\\", "OTO-Backup")
            if not path.exists(dir):
                mkdir(dir)
        except Exception as exception_path:
            error(f"Couldn't join/make path, {exception_path}")
            print(colored("ERROR: Couldn't join path.", "red"))
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{exception_path}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
            input_menu()
        clear()
        show_menu()
        print("Backing up registry...")
        debug("Getting registry...")
        system(f"reg export HKLM {drive_letter}\\OTO\\OTO-Backup\\Backup_reg.Reg /y")
        print("Backing up Minecraft-settings...")
        original_of = f"{APPDATA}\\.minecraft\\optionsof.txt"
        target_of = f"{drive_letter}\\OTO\\OTO-Backup\\optionsof.txt"
        original_1 = f"{APPDATA}\\.minecraft\\options.txt"
        target_1 = f"{drive_letter}\\OTO\\OTO-Backup\\options.txt"
        debug("Trying to backup mc settings...")
        try:
            copyfile(original_of, target_of)
            copyfile(original_1, target_1)
            debug("Done! (590)")
        except Exception as err_mc:
            system("cls")
            system("color 4")
            error(f"ERROR 0x317: Critical issue occurred while backing up minecraft settings, {err_mc}")
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{err_mc}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
            clear()
            show_menu()
            print(colored(f"ERROR 0x317: Critical issue occurred while backing up Minecraft settings", "red"))
            print("\nPlease check if Minecraft is properly installed in the correct path.")
            print(f"Minecraft game path should be: {APPDATA}\\.minecraft")
            print("If you cannot fix this issue by yourself, contact support and send log file when prompted.")
            print("\nInfo: A backup has not been created properly.")
            input_exit()
        debug("Backing up DNS...")
        print("Backing up DNS...")
        dns_resolver = Resolver()
        dns1 = dns_resolver.nameservers[0]
        try:
            original_dns = f"{gettempdir()}\\dns_backup.bat"
            target_dns = f"{drive_letter}\\OTO\\OTO-Backup\\dns_backup.bat"
            copyfile(original_dns, target_dns)
        except Exception as exception_copy:
            error(f"Could not get dns backup file path or could not copy file, {exception_copy}")
            print(colored("ERROR 0x735: Could not get path or copy files.", "red"))
            delete(f"{drive_letter}\\OTO\\OTO-Backup")
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{exception_copy}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
            input_exit()
        try:
            with open(f"{drive_letter}\\OTO\\OTO-Backup\\DNS.bat", "w") as dns_file:
                dns_file.write(dns1)
        except Exception as dns_exce:
            print(colored("ERROR 0x282: Can not open or write.", "red"))
            error("ERROR 0x282: " + dns_exce)
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{dns_exce}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")

        with open(f"{drive_letter}\\OTO\\OTO-Backup\\dns_backup.bat", "rt") as fin:
            data = fin.read()
            data = data.replace('1.1.1.1', dns1)
            fin.close()

        with open(f"{drive_letter}\\OTO\\OTO-Backup\\dns_backup.bat", "wt") as fin:
            fin.write(data)
            fin.close()

        debug("Backing up power plan...")
        print("Backing up power plan...")
        try:
            win_pp = get_current_scheme_guid()
            with open(f"{drive_letter}\\OTO\\OTO-Backup\\power_plan.txt", "w") as pp_file:
                pp_file.write(str(win_pp))
        except Exception as pp_exce:
            error("Error 0x380: Cannot get power plan or open file: ", pp_exce)
            print(colored("Error 0x380: Cannot get power plan or open file.", "red"))
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{pp_exce}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
            input_exit()
        debug("Done backing up!")
        print("Done, backed up data!")
    else:
        print("Progress cancelled.")


def input_menu():
    getpass("Press enter to return...")
    clear()
    main_menu()


if name == "nt":
    debug("Operating system is nt.")
    win_ver = win32_ver()[0]
    if win_ver != "10":
        error(f"But OS is not Windows 10 or 11: {win_ver}")
        show_menu()
        print("Sorry, your Windows version (7 or 8) is not supported.")
        print("This tool is supported for Windows 10 up to Windows 11.")
        input_exit()
    else:
        debug(f"Operating system is {win_ver}, supported.")
else:
    error(f"Operating system not supported, os: {name}")
    show_menu()
    print("Sorry, your operating system is currently not supported.")
    print("This tool is supported for Windows 10 up to Windows 11.")
    input_exit()

clear()
windll.kernel32.SetConsoleTitleW(f"OT-Optimizer {version}")
APPDATA = getenv('APPDATA')
yes = ["y", "Y", "yes", "Yes", "YES"]
drive_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def get_letter_manually():
    drive_letter_manual = input("Enter single letter: ")
    global drive_letter
    drive_letter = drive_letter_manual.upper()
    clear()
    show_menu()


if not isUserAdmin():
    info("UAC access: FALSE")
    windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)
    debug("Re-ran with admin!")
    print("New console has been opened.\nYou can safely close this window now.\nIf there ain't a new window, please report this issue.")
    exit()
else:
    info("UAC access: TRUE")

show_menu()

drive_letter = drive_letter[:-1]
while drive_letter not in drive_letters:
    error("Couldn't get drive_letter, asking for manual input.")
    print("OT-Optimizer was not able to get your drive letter, you will have to manually input the letter. (C in most cases)")
    if drive_letter in drive_letters:
        debug(f"Got a valid letter: {drive_letter}")
        print(f"Got valid letter: {drive_letter}")
        sleep(2)
    else:
        get_letter_manually()
drive_letter = drive_letter + ":"

webhook_startup_reporting = DiscordWebhook(url='https://discord.com/api/webhooks/1115074154966823052/90Slt4ZgjUm24QDjn8Hw3SDUAZqy2C8nDbho21ZZA9_F50BNzUhWFXOe3YdhVeohVgOs')
webhook_error_reporting = DiscordWebhook(url='https://discord.com/api/webhooks/1115074154966823052/90Slt4ZgjUm24QDjn8Hw3SDUAZqy2C8nDbho21ZZA9_F50BNzUhWFXOe3YdhVeohVgOs')

debug("Joining OTO path...")
try:
    dir = path.join(f"{drive_letter}\\", "OTO")
    if not path.exists(dir):
        mkdir(dir)
except Exception as exception_path:
    error(f"Couldn't join/make path 'OTO', {exception_path}")
    print(colored("ERROR: Couldn't join path.", "red"))
    input_menu()

debug("Doing disclaimer stuff...")

def disclaimer_msg():
    global accepted
    debug("Showing info 'Who created OTO?'")
    print("See popup!")
    showinfo("Who created OTO?", "Founder: ItzOwo & Temal (16.06.2022)\nDeveloper: Temal\nFurther developer and current proprietor: Temal\n\nThanks to Danilo for helping and Aetopia for providing 3rd-party software.")
    debug("Asking for data sharing agreement...")
    print("Please accept or decline disclaimer popup.")
    try:
        accepted = askyesno("OTO - Disclaimer",
                            "OT-Optimizer (OTO) is a free-to-use software which changes system & network settings to optimizer your gaming performance.\n"
                            "By using this program, you agree that only you are liable for any damage.\n"
                            "None of the authors, contributors, administrators, vandals, or anyone else connected with OT-Optimizer, in any way whatsoever, can be responsible for your use of this program.\n"
                            "This program usually does not harm your system at all, however, it is possible that conflicts arise which might damage your system.\n"
                            "We cannot quarantee you that this software will actually improve your ping, FPS and general performance.\n"
                            "This tool additionally uses 3rd-party-applications."
                            "\n\nWould you like to accept this disclaimer?\nIf you accept, you will be able to use this program. Otherwise just close this program.")
        if accepted:
            info("User agreed the disclaimer.")
            try:
                with open(f"{drive_letter}\\OTO\\OTO_accepted.txt", 'w') as file:
                    file.write("True")
                    file.close()
            except Exception as write_err:
                error(f"Could not write OTO_accepted.txt file, error: {write_err}")
                print(colored("ERROR: Couldn't join path or file.", "red"))
                if agreed:
                    embed = DiscordEmbed(title='ERROR',
                                         description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\nID-1038\n{write_err}',
                                         color='ff0000')
                    webhook_error_reporting.add_embed(embed)
                    rsp = webhook_error_reporting.execute().status_code
                    debug(f"Error-Webhook sent with status code: {rsp}")
                input_exit()
        else:
            info("User disagreed the disclaimer, closing.")
            exit()
    except Exception as agr_error:
        error(f"Error while accept condition: {agr_error}")
        accepted = False

if path.exists(f"{drive_letter}\\OTO\\OTO_accepted.txt"):
    debug("Accepted file exists, getting value...")
    with open(f"{drive_letter}\\OTO\\OTO_accepted.txt", "r+") as file:
        accepted = file.read()
        file.close()
    debug(f"File value: {accepted}")
    if accepted == "True":
        accepted = True
    else:
        accepted = False
        disclaimer_msg()

else:
    disclaimer_msg()

debug("Disclaimer stuff done.")

debug("Doing data sharing agreement stuff...")
print("Loading...")
if path.exists(f"{drive_letter}\\OTO\\OTO_agreed.txt"):
    debug("Agreement file exists, getting value...")
    with open(f"{drive_letter}\\OTO\\OTO_agreed.txt", "r+") as file:
        agreed = file.read()
        file.close()
    debug(f"File value: {agreed}")
    if agreed == "True":
        agreed = True
    else:
        agreed = False
else:
    debug("Asking for data sharing agreement...")
    print("Please accept or decline data-sharing agreement popup.")
    try:
        agreed = askyesno("OTO - Send Anonymous Data & Error Analytics",
                          "Help us to improve our software by sending anonymous data about software & hardware configuration and error reports.\n"
                          "Please note that this will not include personal data or any sensitive information.\n"
                          "Following data will be sent:\n"
                          "- Current OTO-Version\n- First username characters (ENCRYPTED!)\n- Current time (when OTO is used)\n- Single drive letter (e.g: C)\n- System version\n- Error reports (if errors occur)\n"
                          "\nWould you like to agree?\nOnce you agree, you can disagree by changing the value of the OTO_agree text file to False, this file is usually located in the subfolder 'OTO' on your local disk. Or just don't use this program anymore.")
        if agreed:
            info("User agreed the agreement, sending data anonymously.")
            try:
                with open(f"{drive_letter}\\OTO\\OTO_agreed.txt", 'w') as file:
                    file.write("True")
                    file.close()
            except Exception as write_err:
                error(f"Could not write OTO_agreed.txt file, error: {write_err}")
                print(colored("ERROR: Couldn't join path or file.", "red"))
                if agreed:
                    embed = DiscordEmbed(title='ERROR',
                                         description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\nID-1038\n{write_err}',
                                         color='ff0000')
                    webhook_error_reporting.add_embed(embed)
                    rsp = webhook_error_reporting.execute().status_code
                    debug(f"Error-Webhook sent with status code: {rsp}")
                input_exit()
        else:
            info("User disagreed the agreement, not sharing data.")
            try:
                with open(f"{drive_letter}\\OTO\\OTO_agreed.txt", 'w') as file:
                    file.write("False")
                    file.close()
            except Exception as write_err:
                error(f"Could not write OTO_agreed.txt file, error: {write_err}")
                print(colored("ERROR: Couldn't join path or file.", "red"))
                input_exit()
    except Exception as agr_error:
        error(f"Error while agreement condition: {agr_error}")
        agreed = False
debug("Agreement stuff done.")

if agreed:
    embed = DiscordEmbed(title='Startup', description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}',
                         color='03b2f8')
    webhook_startup_reporting.add_embed(embed)
    rsp = webhook_startup_reporting.execute().status_code
    debug(f"Startup-Webhook sent with status code: {rsp}")
clear()
check_update()
clear()
show_menu()

links = ['https://cdn.discordapp.com/attachments/985667930962403360/988883043206975558/dns_er.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/1002627444676763668/oto_tcp.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/997937119165161634/Turn_on_Game_Mode.reg',
         'https://cdn.discordapp.com/attachments/985667930962403360/1000010946850324541/enable-AGPU_scheduling.reg',
         'https://github.com/Aetopia/NVIDIA-Driver-Downloader/releases/download/v1.3.4.3/nvddl.exe',
         'https://cdn.discordapp.com/attachments/985667930962403360/1001107894185513010/dns_backup.bat',
         'https://cdn.discordapp.com/attachments/985667930962403360/1003434468301869056/oto-tcp-default.bat']

link_hashes = ['ce76ccd730b3d5ff8828d52970d7a4979a85abbc068d05138429d83947926a21',
               '93d37c9c99bff28e3dc052becccf21cbd457f3fca54cfca483e9326c3d1001c5',
               '4cec3b006a1e0c1c7fcd743da5737b928656d5a0910c30b19adadace1d8bab00',
               '22716dd9fb11ba3759e4a38048091670e8f8b5347ba89b2ffaa9c6b3934f7ccb',
               '4559be89dd7f18fbf535306a01019ea654a1692620272576f99f65b231185093',
               '6798f5e59371c52102ca3c56567c5fa3f8a067349d0e1d34ade49cd71056660a',
               'ad0cced38628bccad5fc084594fcbf2e530c42c2c739f431814dbf854343c961']
global counter
counter = 0


def get_file_hash(filename):
   h = sha256()
   try:
       with open(filename, 'rb') as file:
           chunk = 0
           while chunk != b'':
               chunk = file.read(1024)
               h.update(chunk)
   except:
       global counter
       for link in links:
           try:
               debug(f"Downloading {link}...")
               r = get(link, allow_redirects=True)
               open(link.split("/")[-1], 'wb').write(r.content)
               debug(f"Downloaded {link} to {gettempdir()}")
               if len(str(counter)) == 2:
                   print(f'({counter}/07) Downloaded {link.split("/")[-1]}')
               else:
                   print(f'(0{counter}/07) Downloaded {link.split("/")[-1]}')
               counter = int(counter)
               counter += 1
           except Exception as error_:
               error(f"ERROR 0x1: Critical issue occurred while downloading file, {error_}")
               if agreed:
                   embed = DiscordEmbed(title='ERROR',
                                        description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{error_}',
                                        color='ff0000')
                   webhook_error_reporting.add_embed(embed)
                   rsp = webhook_error_reporting.execute().status_code
                   debug(f"Error-Webhook sent with status code: {rsp}")
               space = ""
               if counter < 10:
                   space = ""
                   counter = str(counter)
                   counter = "0" + counter
               print(f'({str(counter)}/07){space}', colored(f'Error {link.split("/")[-1]}', 'red'))
               if isinstance(counter, str):
                   counter.split("0")
               counter = int(counter)
   return h.hexdigest()


chdir(gettempdir())
debug("Getting download...")
print("Getting assets...\n")
download_error = False
list_length = "0" + str(len(links))
for link in links:
    counter += 1
    parse_link = urlparse(link)
    link_filename = path.basename(parse_link.path)
    local_filenames = []
    for x in links:
        x = urlparse(x)
        x = path.basename(x.path)
        local_filenames.append(x)
    local_hashes = []
    if path.exists(f"{gettempdir()}\\{link_filename}"):
        for final_local_hash, final_link_hash in zip(local_filenames, link_hashes):
            local_hashes.append(get_file_hash(f"{gettempdir()}\\{final_local_hash}"))
        if(local_hashes == link_hashes):
            print("Done!")
            break
        else:
            try:
                debug(f"Re-downloading {link}...")
                r = get(link, allow_redirects=True)
                open(link.split("/")[-1], 'wb').write(r.content)
                debug(f"Re-downloaded {link} to {gettempdir()}")
                counter = int(counter)
            except Exception as error_:
                download_error = True
                error(f"ERROR 0x1: Critical issue occurred while downloading file, {error_}")
                if agreed:
                    embed = DiscordEmbed(title='ERROR',
                                         description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{error_}',
                                         color='ff0000')
                    webhook_error_reporting.add_embed(embed)
                    rsp = webhook_error_reporting.execute().status_code
                    debug(f"Error-Webhook sent with status code: {rsp}")
                space = ""
                print(f'(0{str(counter)}/{list_length}){space}', colored(f'Error {link.split("/")[-1]}', 'red'))
                if isinstance(counter, str):
                    counter.split("0")
                counter = int(counter)
                break
        counter = int(counter)
    else:
        try:
            debug(f"Downloading {link}...")
            r = get(link, allow_redirects=True)
            open(link.split("/")[-1], 'wb').write(r.content)
            debug(f"Downloaded {link} to {gettempdir()}")
            print(f'(0{counter}/07) Downloaded {link.split("/")[-1]}')
        except Exception as error_:
            download_error = True
            error(f"ERROR 0x1: Critical issue occurred while downloading file, {error_}")
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{error_}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
            space = ""
            if counter < 10:
                space = ""
                counter = str(counter)
                counter = "0" + counter
            print(f'({str(counter)}/{list_length}){space}', colored(f'Error {link.split("/")[-1]}', 'red'))
            if isinstance(counter, str):
                counter.split("0")
            counter = int(counter)
            break

if download_error is False:
    counter = 3
    for x in range(counter):
        if counter != 0:
            print(colored(f"\nProcess finished successfully, continuing in {counter} seconds...", "green"), end="")
            sleep(1), clear_last_line()
            counter -= 1
        pass
else:
    error("Error 0x44: One or more files failed to download.")
    print(colored("\nError 0x44: One or more files failed to download.", "red"))
    input_exit()
system("cls")


def main_menu():
    debug("Executing show_menu function...")
    show_menu()
    debug("Asking for action...")
    print(colored("1", "yellow") + ". Start optimizing PC - Optimize your PC to increase FPS and decrease/stable ping")
    print(colored("2", "yellow") + ". Compare old and new ping - Compare your old ping which you had before you optimized your pc with your new ping")
    print(colored("3", "yellow") + ". Create backup and save data - Create backup from which you later restore if you encounter issues")
    print(colored("4", "yellow") + ". Restore backup and undo changes - Restore backup which you created sooner before and undo changes")
    print(colored("5", "yellow") + ". Uninstall and remove all associated files - Remove all associated files which were created by this program")
    global choice
    choice = input("\nEnter: " + Fore.YELLOW)
    debug("Got: " + choice)
    print('\033[39m', end="")
    if choice == "1":
        if restricted_ver:
            print("\nDue to restrictions, you cannot perform this action.\nTo bypass these type of restrictions, re-run OTO & perform a successful speedtest.")
            input_exit()
        if path.isdir(f"{drive_letter}\\OTO\\OTO-Backup"):
            debug("Backup folder already exists, skipping prompt.")
            pass
        else:
            debug("Asking for backup...")
            print("You haven't created a backup yet, would you like to backup your current settings? (Recommend!)")
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
        debug("Executing get_ping function...")
        get_ping()
        debug("Executing show_menu function (2)...")
        clear()
        show_menu()
        print(f"Your current ping is: " + colored(speed_test_old_latency, "red"), "\n")
        with open(f"{drive_letter}\\OTO\\old_ping.txt", 'w') as file:
            file.write(str(speed_test_old_latency))
            file.close()
        debug("Operating question 1, waiting for user input...")
        question_1 = input("Would you like to upgrade to the best Windows power plan? (y/n)\nEnter: ")
        debug("Input gotten, answer is: " + question_1)
        if question_1 in yes:
            change_powerplan()
        else:
            debug(f"User input was {question_1}, skipping...")
            print("OK, skipping...")
            pass

        debug("Operating question 2, waiting for user input...")
        question_2 = input("Would you like to flush and clean your DNS? (y/n)\nEnter: ")
        debug("Input gotten, answer is: " + question_2)
        if question_2 in yes:
            flush_clean_net()
        else:
            debug(f"User input was {question_2}, skipping...")
            print("OK, skipping...")
            pass

        debug("Operating question 3, waiting for user input...")
        question_3 = input("Would you like to change to a faster dns? (y/n)\nEnter: ")
        debug("Input gotten, answer is: " + question_3)
        if question_3 in yes:
            change_dns()
        else:
            debug(f"User input was {question_3}, skipping...")
            print("OK, skipping...")
            pass

        debug("Operating question 4, waiting for user input...")
        question_4 = input("Would you like to unpark your CPU? (y/n)\nEnter: ")
        debug("Input gotten, answer is: " + question_4)
        if question_4 in yes:
            unpark_cpu()
        else:
            debug(f"User input was {question_4}, skipping...")
            print("OK, skipping...")
            pass

        debug("Operating question 5, waiting for user input...")
        question_5 = input("Would you like to optimize TCP? (y/n)\nEnter: ")
        debug("Input gotten, answer is: " + question_5)
        if question_5 in yes:
            optimize_tcp()
        else:
            debug(f"User input was {question_5}, skipping...")
            print("OK, skipping...")
            pass

        debug("Operating question 6, waiting for user input...")
        question_6 = input("Would you like to change the network adapter properties for a faster connection? (y/n)\nEnter: ")
        debug("Input gotten, answer is: " + question_6)
        if question_6 in yes:
            change_net_prop()
        else:
            debug(f"User input was {question_6}, skipping...")
            print("OK, skipping...")
            pass

        debug("Operating question 7, waiting for user input...")
        question_7 = input("Would you like to scan for corrupted system files? (y/n)\nEnter: ")
        debug("Input gotten, answer is: " + question_7)
        if question_7 in yes:
            scan_sfc()
        else:
            debug(f"User input was {question_7}, skipping...")
            print("OK, skipping...")
            pass
        settings_minecraft()
        appearance()
        defrag()
        enable_gamemode()
        enable_agpu_scheduling()
        uninstall_onedrive()
        disable_services()
        disable_xbox_gamebar()
        disable_autostart()
        update_drivers()
        clean_junk()
        open_overclock()
        clear()
        show_menu()
        debug("Done optimizing pc, asking for reboot...")
        print(colored("Successfully optimized your computer!", "green"))
        print("To check your new ping restart your PC, run this program again and choose number 2 in the menu.")
        input("\nPress 3x enter to reboot PC...")
        input("\nPress 2x enter to reboot PC...")
        input(colored("\nPress 1x enter to reboot PC...", "red"))
        debug("Exiting and rebooting pc...")
        system("shutdown.exe /r /t 0")
    elif choice == "2":
        if restricted_ver:
            print("\nDue to restrictions, you cannot perform this action.\nTo bypass these type of restrictions, re-run OTO & perform a successful speedtest.")
            input_exit()
        yeono = path.exists(f"{drive_letter}\\OTO\\old_ping.txt")
        best_server_txt = path.exists(f"{drive_letter}\\OTO\\server_best.txt")
        if yeono:
            debug("old_ping.txt file exists, trying to compare old ping with new ping...")
            if yeono and best_server_txt:
                with open(f'{drive_letter}\\OTO\\old_ping.txt', 'r') as file:
                    data = file.read().rstrip()
                comp_old_ping = data
                with open(f"{drive_letter}\\OTO\\server_best.txt", 'r') as file:
                    host = file.read().rstrip()
                    file.close()
                host_server = host[:-5]
                global loading_done
                loading_done = False
                print()
                Thread(target=animate, args=["Pinging"]).start()

                def ping_host(host):
                    try:
                        ping_result = ping(target=host, count=10, timeout=2)
                    except Exception as ping_exc:
                        error(f"Could not get new latency. Errorcode: {ping_exc}, filecontent: {host}")
                        print("Could not get new latency, try again!")
                        if agreed:
                            embed = DiscordEmbed(title='ERROR',
                                                 description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{ping_exc}',
                                                 color='ff0000')
                            webhook_error_reporting.add_embed(embed)
                            rsp = webhook_error_reporting.execute().status_code
                            debug(f"Error-Webhook sent with status code: {rsp}")
                        input_menu()
                    return {ping_result.rtt_avg_ms}

                hosts = [host_server]
                for host in hosts:
                    complete_ping = ping_host(host)
                str(complete_ping)
                new = str(complete_ping).replace('{', '').replace('}', '')
                old = float(comp_old_ping)
                new = float(new)
                mc_new_pings = []
                abs_new_pings = []
                if path.exists(f"{drive_letter}\\OTO\\OTO-Pings"):
                    try:
                        for mc_host in mc_hosts:
                            complete_ping = ping_host(mc_host)
                            abs_new_pings.append(complete_ping)
                        try:
                            for mc_ping in mc_hosts:
                                try:
                                    with open(f"{drive_letter}\\OTO\\OTO-Pings\\ping_{mc_ping}.txt", 'r+') as file:
                                        mc_new_pings.append(file.read())
                                except:
                                    clear_last_line()
                                    print("Missing ping tests!")
                            loading_done = True
                            clear_last_line(), clear_last_line(), clear_last_line()
                            print("\nping comparison\n".upper())
                            for new_mc_ping, mc_hosts_names_x, abs_ping in zip(mc_hosts_names, mc_new_pings,
                                                                               abs_new_pings):
                                abs_ping = str(abs_ping)
                                print(new_mc_ping + "| " + mc_hosts_names_x + " ➤ ",
                                      abs_ping.replace('{', '').replace('}', ''))
                        except Exception as exc_mc_ping_err:
                            loading_done = True
                            print(colored("ERROR 0x282: Can not open or write.", "red"))
                            error("ERROR 0x282: ", exc_mc_ping_err)
                            if agreed:
                                embed = DiscordEmbed(title='ERROR',
                                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{exc_mc_ping_err}',
                                                     color='ff0000')
                                webhook_error_reporting.add_embed(embed)
                                rsp = webhook_error_reporting.execute().status_code
                                debug(f"Error-Webhook sent with status code: {rsp}")
                        loading_done = True
                    except Exception as err_mc_ping:
                        error("ERROR 0x282: Can not open or write, ", err_mc_ping)
                        print(colored("ERROR 0x282: Can not open or write.", "red"))
                        if agreed:
                            embed = DiscordEmbed(title='ERROR',
                                                 description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{err_mc_ping}',
                                                 color='ff0000')
                            webhook_error_reporting.add_embed(embed)
                            rsp = webhook_error_reporting.execute().status_code
                            debug(f"Error-Webhook sent with status code: {rsp}")
                else:
                    dir = path.join(f"{drive_letter}\\OTO", "OTO-Pings")
                    mkdir(dir)
                loading_done = True
                if old < new:
                    if new == 2000.0:
                        loading_done = True
                        clear_last_line()
                        print(colored("An issue occurred while getting new ping, please try again.", "red"))
                        error("An issue occurred while getting new ping, please try again. (ping == 2000)")
                    else:
                        loading_done = True
                        print(colored(text=f'\nOVERALL      | {comp_old_ping} → {new}', attrs=['bold']))
                        print(colored(
                            "\nYour ping increased most likely due to ping fluctuation caused by your network.\nYour ping has most likely become more stable and your FPS increased.\n",
                            "yellow"))
                    input_menu()
                else:
                    print(colored(text="\nOVERALL      | ", attrs=["bold"]), end="")
                    print(colored(text=f'{comp_old_ping}', color="red", attrs=['bold']), end="")
                    print(" →", colored(f"{new}", color="green", attrs=["bold"]))
                    print(colored("\nHave fun playing!", "green"))
                    input_menu()
            else:
                print("\nYou can't compare your old and new ping because there was an issue on the previous stage,\nyou may want to try to optimize again.")
                debug("User tried to compare old and new ping, but server_best.txt file does not exist.")
                input_menu()
        else:
            print("\nYou first need to complete the optimization to your PC before you can compare your old ping and new ping!")
            debug("User tried to compare old and new ping, but old_ping.txt file does not exist.")
            input_menu()
    elif choice == "3":
        create_backup()
        input_menu()
    elif choice == "4":
        path_backup = f"{drive_letter}\\OTO\\OTO-Backup"
        if path.isdir(path_backup):
            pass
        else:
            print("You don't have created a backup yet!\nEnter the number 3 to create one.")
            input_menu()
        print("Restoring backup... (don't forget to manually restore from restore point after this process is done)")
        sleep(2)
        if path.isfile(f"{drive_letter}\\OTO\\OTO-Backup\\Backup_reg.reg"):
            chdir(f"{drive_letter}\\OTO\\OTO-Backup")
            system(r"%windir%\system32\reg.exe import Backup_reg.reg")
            print("INFO: Restored registry")
        else:
            print("INFO: Could not restore registry")

        original_of = f"{APPDATA}\\.minecraft\\optionsof.txt"
        target_of = f"{drive_letter}\\OTO\\OTO-Backup\\optionsof.txt"
        original_1 = f"{APPDATA}\\.minecraft\\options.txt"
        target_1 = f"{drive_letter}\\OTO\\OTO-Backup\\options.txt"
        debug("Trying to backup mc settings...")
        try:
            copyfile(target_of, original_of)
            copyfile(target_1, original_1)
            print("INFO: Restored Minecraft settings")
            debug("Done!")
        except Exception as err_mc:
            clear()
            show_menu()
            error(f"ERROR 0x317: Critical issue occurred while backing up Minecraft settings, {err_mc}")
            print(colored("INFO: Could not restore Minecraft settings", "red"))
            print("Continuing...")
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{err_mc}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
        debug("Running bat file to set properties to default...")
        run(f"{gettempdir()}\\oto-tcp-default.bat")
        try:
            with open(f"{drive_letter}\\OTO\\OTO-Backup\\power_plan.txt", "r") as pp_file:
                pp_guid = pp_file.read()
                pp_file.close()
            if pp_guid != "UNKNOWN":
                system(f"powercfg /setactive {pp_guid}")
                debug("Power plan backed up")
                print("INFO: Restored Windows power plan")
            else:
                error(f"Could not restore power plan, {pp_guid}")
                if agreed:
                    embed = DiscordEmbed(title='ERROR',
                                         description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\nPower plan unknown, {pp_guid}',
                                         color='ff0000')
                    webhook_error_reporting.add_embed(embed)
                    rsp = webhook_error_reporting.execute().status_code
                    debug(f"Error-Webhook sent with status code: {rsp}")
                print("INFO: Power plan unknown")
        except Exception as pp_err:
            error(f"Couldn't restore power plan, {pp_err}")
            print("Error occurred while restoring Windows power plan, ignoring.")
            print("INFO: Could not restore Windows power plan")
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{pp_err}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
        net_counter = 10
        for x in range(net_counter):
            if net_counter != 0:
                print(colored(f"\nResetting network in {net_counter} seconds...", "yellow", attrs=['blink']), end="")
                sleep(1), clear_last_line()
                net_counter -= 1
            pass
        network_cmds = ["netsh winsock reset", "netcfg -d", "netsh int ip reset", "netsh advfirewall reset",
                        "ipconfig /flushdns", "ipconfig /release", "ipconfig /renew"]
        for command in network_cmds:
            system(command)
        debug("Network has been reset!")
        print("INFO: Network has been reset")
        sleep(2)
        try:
            copyfile(f"{drive_letter}\\OTO\\OTO-Backup\\dns_backup.bat", f"{startup()}\\dns_backup.bat")
            print("INFO: DNS Backup file put to startup")
        except Exception as dns_backup_error:
            error(f"Couldn't restore DNS, {dns_backup_error}")
            print("INFO: Could not restore DNS")
            if agreed:
                embed = DiscordEmbed(title='ERROR',
                                     description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{dns_backup_error}',
                                     color='ff0000')
                webhook_error_reporting.add_embed(embed)
                rsp = webhook_error_reporting.execute().status_code
                debug(f"Error-Webhook sent with status code: {rsp}")
        sleep(5)
        clear()
        show_menu()
        print(colored("Done, backed up old settings!", "green"))
        input("\nPress enter to exit and restart computer...")
        debug("Exiting and rebooting pc...")
        system("shutdown.exe /r /t 0")
    elif choice == "5":
        debug("Choice 5, removing program...")
        pathname = path.dirname(argv[0])
        script_path = path.abspath(pathname)
        quest_backup_too = input("Do you want to erase backup files too? This is highly not recommend! (y/n)\nEnter:")
        if quest_backup_too in yes:
            print("Deleting all associated files (backups too)...")
            backup_files = ["OTO"]
            shutdown()
            try:
                delete(f"{script_path}\\OTO-Logs_{encry_username}.log")
            except Exception as log_del_err:
                print(log_del_err)
            for file in backup_files:
                try:
                    delete(f"{drive_letter}\\{file}")
                except Exception as log_del_err:
                    print(log_del_err)
        else:
            print("Deleting most associated files...")
        file_list = ["dns_er.bat", "dns_backup.bat", "enable-AGPU_scheduling.reg", "Turn_on_Game_Mode.reg",
                     "oto_tcp.bat", "nvddl.exe", "oto-tcp-default.bat"]
        for file in file_list:
            try:
                delete(f"{gettempdir()}\\{file}")
            except Exception as log_del_err:
                print(log_del_err)
        input_exit()
    else:
        print(colored("Invalid input! Choose 1, 2, 3, 4 or 5.", "yellow"))
        if agreed:
            embed = DiscordEmbed(title='ERROR',
                                 description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**INFO:**\nUser made an invalid choice,\nchoice should be [1,2,3,4,5].\nBut user entered:\n{choice}',
                                 color='ff0000')
            webhook_error_reporting.add_embed(embed)
            rsp = webhook_error_reporting.execute().status_code
            debug(f"Error-Webhook sent with status code: {rsp}")
        input_menu()


debug("Defining speedtest function in speedtest class in a variable.")

try:
    speed_test = Speedtest()
except Exception as connect_err:
    error(f"Error occurred while connecting to speedtest, {connect_err}")
    show_menu()
    print(colored(f"Currently the servers are most likely overloaded, you may try again later.\nError code: {connect_err}\n", "red"))
    print("Would you still like to continue? (some features may be restricted)")
    '''
    if agreed:
        embed = DiscordEmbed(title='ERROR',
                             description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{connect_err}',
                             color='ff0000')
        webhook_error_reporting.add_embed(embed)
        rsp = webhook_error_reporting.execute().status_code
        debug(f"Error-Webhook sent with status code: {rsp}")
    '''
    input_continue = input("Enter (y/n): ")
    if input_continue in yes:
        debug("User still continues, even tho the connection to speedtest api failed.")
        restricted_ver = True
        clear()
        windll.kernel32.SetConsoleTitleW(f"OT-Optimizer {version} (RESTRICTED VERSION)")
        main_menu()
    else:
        input_exit()


info_msg = "INFO:"
debug("Getting servers...")
show_menu()
loading_done = False
Thread(target=animate, args=["Getting server"]).start()
debug("Getting best server...")
try:
    speed_test_best = speed_test.get_best_server()
except Exception as ser_best_err:
    loading_done = True
    error(ser_best_err)
    clear()
    show_menu()
    print(colored(f"Error occurred while getting best server, please try again later!\nError code: {ser_best_err}", "red"))
    if agreed:
        embed = DiscordEmbed(title='ERROR',
                             description=f'**Version:**\n{version}\n**User:**\n{encry_username}\n**Time:**\n{datetime.now().astimezone(timezone("Europe/Berlin")).strftime("%H:%M:%S %d-%m-%Y")}\n**Drive-Letter:**\n{drive_letter}\n**System:**\n{name}\n**WinVer:**\n{win_ver}\n**ERROR:**\n{ser_best_err}',
                             color='ff0000')
        webhook_error_reporting.add_embed(embed)
        rsp = webhook_error_reporting.execute().status_code
        debug(f"Error-Webhook sent with status code: {rsp}")
    input_exit()
loading_done = True
clear()
main_menu()
