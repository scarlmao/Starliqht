import requests
import os
import time
import random
import base64
import re
from bs4 import BeautifulSoup
import urllib.parse
from collections import deque
import json
from pystyle import Colors, Colorate

os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class text():
    LINE = "---------------------------------------------------------------------------------------------\n"
    OPTIONS = "[1] Pinger                                     [7] Webhook Editor                    [13] Website Email Scraper\n[2] Email Osint                                [8] Grabify Flooder                   [14] Website Directory Sniffer\n[3] IP Searcher                                [9] Fake Report Bot                   [15] Username Osint\n\n[4] Tweaking                                   [10] Id To Token                       [16] Unshorten Url\n[5] Mail Bomber                                [11] Google Hacking\n[6] Generators                                 [12] Email Header Tracer"
    OPTIONS2 = "[1] Roblox\n[2] Amazon\n[3] Playstation\n\n[4] Credit Cards\n[5] Steam\n[6] Fortnite"
    SPACE = "                             "

def login():
   main()

def main():
 os.system('cls')
 os.system('title STARLIQHT - HOME')
 print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
 print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
 print(style.RED + text.LINE)
 print (style.BLUE + text.OPTIONS)
 choice = input(style.RED + "> ")
 if choice == "1":
    pinger()
 if choice == "2":
    emailsearch()
 if choice == "3":
    ipscan()
 if choice == "4":
    tweak()
 if choice == "5":
    emailer()
 if choice == "6":
    cards()
 if choice == "7":
    webhook()
 if choice == "8":
    grabify()
 if choice == "9":
    reporter()
 if choice == "10":
    discordidtotoken()
 if choice == "11":
    google()
 if choice == "12":
    emailheader()
 if choice == "13":
    websitescrape()
 if choice == "14":
    directorysniff()
 if choice == "15":
    username()
 if choice == "16":
    unshorten()

def pinger():
   print(style.BLUE + 'Enter The Ip You Want To Ping')
   INPUTIP = input(style.RED + '> ')
   os.system('ping -n 4 {}'.format(INPUTIP))
   print(style.BLUE + "Press Enter To Return To Menu")
   INPUTIP = input(style.RED + '> ')
   main()



def emailsearch():
 os.system('cls')
 print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
 print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
 print(style.RED + text.LINE)
 print(style.BLUE + "Type Mail To Search.")
 mail = input(style.RED + "> ")

 
 
 headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
 }
 response = requests.get(f'https://api.proxynova.com/comb?highlight=1&query={mail}', headers=headers)
 data = json.loads(response.text)
 lines = data["lines"]

 for line in lines[:3]:
    formatted_line = line.replace("</strong>", "").replace("<strong>", "")
    print(style.BLUE + formatted_line)
    
 time.sleep(5)
 main()

def ipscan():
   os.system('cls')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.BLUE + "Type Ip To Scan.")
   ip = input(style.RED + "> ")
   print('site: {ip} ext:log')
   print('site: {ip} inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth')
   print('site: {ip} ext:sql | ext:dbf | ext:mdb')
   print(f'https://www.whois.com/{ip}')
   print(f'https://iknowwhatyoudownload.com/en/peer/?ip={ip}')

def tweak():
   os.system(r'''
            Reg.exe add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "SystemPages" /t REG_SZ /d "0" /f
            Reg.exe add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "PoolUsageMaximum" /t REG_SZ /d "00000060" /f
            Reg.exe add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\GameDVR" /v "AppCaptureEnabled" /t REG_SZ /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DisableExceptionChainValidation" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DpcWatchdogProfileOffset" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "DpcWatchdogPeriod" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "KernelSEHOPEnabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "SerializeTimerExpiration" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel" /v "InterruptSteeringDisabled" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync" /v "SyncPolicy" /t REG_DWORD /d "5" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\BrowserSettings" /v "Enabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Credentials" /v "Enabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Accessibility" /v "Enabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Windows" /v "Enabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "EnableTransparency" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v "HwSchMode" /t REG_DWORD /d "2" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\DirectX\UserGpuPreferences" /v "DirectXUserGlobalSettings" /t REG_SZ /d "VRROptimizeEnable=0;" /f
            Reg.exe add "HKCU\Control Panel\Accessibility\MouseKeys" /v "Flags" /t REG_SZ /d "0" /f
            Reg.exe add "HKCU\Control Panel\Accessibility\StickyKeys" /v "Flags" /t REG_SZ /d "0" /f
            Reg.exe add "HKCU\Control Panel\Accessibility\Keyboard Response" /v "Flags" /t REG_SZ /d "0" /f
            Reg.exe add "HKCU\Control Panel\Accessibility\ToggleKeys" /v "Flags" /t REG_SZ /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo" /v "Enabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\Control Panel\International\User Profile" /v "HttpAcceptLanguageOptOut" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "Start_TrackProgs" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SubscribedContent-338393Enabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SubscribedContent-353696Enabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Speech_OneCore\Settings\OnlineSpeechPrivacy" /v "HasAccepted" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Personalization\Settings" /v "AcceptedPrivacyPolicy" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\InputPersonalization" /v "RestrictImplicitInkCollection" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\InputPersonalization" /v "RestrictImplicitTextCollection" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore" /v "HarvestContacts" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack" /v "ShowedToastAtLevel" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy" /v "TailoredExperiencesWithDiagnosticDataEnabled" /t REG_DWORD /d "0" /f
            Reg.exe add "Powercfg" -h off
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Siuf\Rules" /v "NumberOfSIUFInPeriod" /t REG_DWORD /d "0" /f
            Reg.exe delete "HKCU\SOFTWARE\Microsoft\Siuf\Rules" /v "PeriodInNanoSeconds" /f
            Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "PublishUserActivities" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "UploadUserActivities" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userNotificationListener" /v "Value" /t REG_SZ /d "Deny" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location" /v "Value" /t REG_SZ /d "Deny" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics" /v "Value" /t REG_SZ /d "Deny" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userAccountInformation" /v "Value" /t REG_SZ /d "Deny" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v "GlobalUserDisabled" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v "BackgroundAppGlobalToggle" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\Control Panel\Desktop\WindowMetrics" /v "MinAnimate" /t REG_SZ /d "0" /f
            Reg.exe add "HKCU\Control Panel\Desktop\WindowMetrics" /v "MaxAnimate" /t REG_SZ /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ExtendedUIHoverTime" /t REG_DWORD /d "196608" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DontPrettyPath" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ListviewShadow" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "TaskbarAnimations" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\DWM" /v "EnableAeroPeek" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DWM" /v "DWMWA_TRANSITIONS_FORCEDISABLED" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DWM" /v "DisallowAnimations" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoLowDiskSpaceChecks" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "LinkResolveIgnoreLinkInfo" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoResolveSearch" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoResolveTrack" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoInternetOpenWith" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoInstrumentation" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "EnergyEstimationEnabled" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\Control Panel\Desktop" /v "FontSmoothing" /t REG_SZ /d "2" /f
            Reg.exe add "HKCU\Control Panel\Desktop" /v "FontSmoothingType" /t REG_DWORD /d "2" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MultitaskingView\AllUpView" /v "AllUpView" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MultitaskingView\AllUpView" /v "Remove TaskView" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "ConvertibleSlateMode" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d "38" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\usbxhci\Parameters" /v "ThreadPriority" /t REG_DWORD /d "31" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\USBHUB3\Parameters" /v "ThreadPriority" /t REG_DWORD /d "31" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\nvlddmkm\Parameters" /v "ThreadPriority" /t REG_DWORD /d "31" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\NDIS\Parameters" /v "ThreadPriority" /t REG_DWORD /d "31" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DisallowShaking" /t REG_DWORD /d "1" /f
            Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "EnableBalloonTips" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v "StartupDelayInMSec" /t REG_DWORD /d "0" /f
            Reg.exe add "HKCU\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\PushNotifications" /v "NoTileApplicationNotification" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowDeviceNameInTelemetry" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Affinity" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Background Only" /t REG_SZ /d "False" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Clock Rate" /t REG_DWORD /d "10000" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d "8" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Priority" /t REG_DWORD /d "6" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Scheduling Category" /t REG_SZ /d "High" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "SFIO Priority" /t REG_SZ /d "High" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "BackgroundPriority" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Latency Sensitive" /t REG_SZ /d "True" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v "CoalescingTimerInterval" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Attributes" /t REG_DWORD /d "2" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Affinity" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Background Only" /t REG_SZ /d "False" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Clock Rate" /t REG_DWORD /d "10000" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "GPU Priority" /t REG_DWORD /d "8" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Priority" /t REG_DWORD /d "6" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Scheduling Category" /t REG_SZ /d "High" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "SFIO Priority" /t REG_SZ /d "High" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "BackgroundPriority" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Latency Sensitive" /t REG_SZ /d "True" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "DisableTaggedEnergyLogging" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "TelemetryMaxApplication" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "TelemetryMaxTagPerApplication" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Processor" /v "Cstates" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Processor" /v "Capabilities" /t REG_DWORD /d "516198" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "HighPerformance" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "HighestPerformance" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "MinimumThrottlePercent" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "MaximumThrottlePercent" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "MaximumPerformancePercent" /t REG_DWORD /d "100" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "Class1InitialUnparkCount" /t REG_DWORD /d "100" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "InitialUnparkCount" /t REG_DWORD /d "100" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "MaximumPerformancePercent" /t REG_DWORD /d "100" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" /v "PowerThrottlingOff" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WcmSvc\GroupPolicy" /v "fDisablePowerManagement" /t REG_DWORD /d "1" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PDC\Activators\Default\VetoPolicy" /v "EA:EnergySaverEngaged" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PDC\Activators\28\VetoPolicy" /v "EA:PowerStateDischarging" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Misc" /v "DeviceIdlePolicy" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "PerfEnergyPreference" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "PerfEnergyPreference" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPMinCores" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPMaxCores" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPMinCores1" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPMaxCores1" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CpLatencyHintUnpark1" /t REG_DWORD /d "100" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPDistribution" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CpLatencyHintUnpark" /t REG_DWORD /d "100" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "MaxPerformance1" /t REG_DWORD /d "100" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "MaxPerformance" /t REG_DWORD /d "100" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPDistribution1" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPHEADROOM" /t REG_DWORD /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPCONCUR
            Reg.exe add "HKCU\Control Panel\PowerCfg\GlobalPowerPolicy" /v "Policies" /t REG_BINARY /d "01000000020000000100000000000000020000000000000000000000000000002c0100003232030304000000040000000000000000000000840300002c01000000000000840300000001646464640000" /f
            Reg.exe add "HKCU\Control Panel\PowerCfg\GlobalPowerPolicy" /v "Policies" /t REG_BINARY /d "01000000020000000100000000000000020000000000000000000000000000002c0100003232030304000000040000000000000000000000840300002c01000000000000840300000001646464640000" /f
            Reg.exe add "HKCU\Control Panel\Desktop" /v "AutoEndTasks" /t REG_SZ /d "1" /f
            Reg.exe add "HKCU\Control Panel\Desktop" /v "HungAppTimeout" /t REG_SZ /d "1000" /f
            Reg.exe add "HKCU\Control Panel\Desktop" /v "WaitToKillAppTimeout" /t REG_SZ /d "2000" /f
            Reg.exe add "HKCU\Control Panel\Desktop" /v "LowLevelHooksTimeout" /t REG_SZ /d "1000" /f  
            Reg.exe add "HKCU\Control Panel\Desktop" /v "MenuShowDelay" /t REG_SZ /d "0" /f
            Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control" /v "WaitToKillServiceTimeout" /t REG_SZ /d "2000" /f
            taskkill /f /im explorer.exe
            start explorer.exe
        ''')
   os.system('cls')
   print("Cleaning temporary files...")
   os.system('timeout 3 >nul')
   os.system(f'del /s /f /q {os.environ["SYSTEMDRIVE"]}\\windows\\temp\\*.*')
   os.system(f'rd /s /q {os.environ["SYSTEMDRIVE"]}\\windows\\temp')
   os.system('md c:\\windows\\temp')
   os.system(f'del /s /f /q {os.environ["SYSTEMDRIVE"]}\\WINDOWS\\Prefetch')
   os.system(f'del /s /f /q {os.environ["temp"]}\\*.*')
   os.system(f'rd /s /q {os.environ["temp"]}')
   os.system('cls')
   print("Successful deleted temporary files!")
   os.system('timeout 1 >nul')
   os.system('cls')
   os.system('timeout 3 >nul')
   print("Cleaning logs...")
   os.system('md %temp%')
   os.system(f'del /q /f /s {os.environ["SYSTEMDRIVE"]}\\Temp\\*.*')
   os.system(f'del /q /f /s {os.environ["WINDIR"]}\\Prefetch\\*.*')
   os.system(f'del /q /f /s {os.environ["SYSTEMDRIVE"]}\\*.log')
   os.system(f'del /q /f /s {os.environ["SYSTEMDRIVE"]}\\*.bak')
   os.system(f'del /q /f /s {os.environ["SYSTEMDRIVE"]}\\*.gid')
   os.system('cls')
   print("Successful cleaned logs!")
   os.system('timeout 2 >nul')
   print("Returning to menu...")
   os.system('timeout 3 >nul')
   main()

def emailer():
    print(style.MAGENTA + "Type Mail To Spam.")
    mail = input(style.RED + "> ")
    data = {
    'meta_web_form_id': '1363572662',
    'meta_split_id': '',
    'listname': 'leosanswers',
    'redirect': 'https://newsletter.askleo.com/please-confirm-your-subscription/',
    'meta_adtracking': 'Home Page',
    'meta_message': '1',
    'meta_required': 'email',
    'meta_tooltip': '',
    'name': '',
    'email': f'{mail}',
    'submit.x': '127',
    'submit.y': '34',
}

    response = requests.post('https://www.aweber.com/scripts/addlead.pl', data=data)

def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

def cards():
   os.system('cls')
   os.system('title STARLIQHT - GIFT CARDS')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.BLUE + text.OPTIONS2)
   print(style.RED + '[00] Return To Menu')
   choice = input(style.RED + "> ")
   
   if choice == "1":
    os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
    print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
    print(style.RED + text.LINE)
    print(style.BLUE + "How Many Cards To Generator")
    nn = input(style.RED + "> ")
    n = int(nn)
    for x in range(n):
        print("")
        print(style.BLUE + g(3)+"-"+g(3)+"-"+g(4))
        cards()
        
   if choice == "2":
    os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
    print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
    print(style.RED + text.LINE)
    print(style.BLUE + "How Many Cards To Generator")
    nn = input(style.RED + "> ")
    n = int(nn)
    for x in range(n):
        print("")
        print(style.BLUE + g(4)+"-"+g(6)+"-"+g(4))
        cards()
        
   if choice == "3":
    os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
    print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
    print(style.RED + text.LINE)
    print(style.BLUE + "How Many Cards To Generator")
    nn = input(style.RED + "> ")
    n = int(nn)
    for x in range(n):
        print("")
        print(style.BLUE + g(4)+"-"+g(4)+"-"+g(4))
        cards()

   if choice == "4":
    os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
    print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
    print(style.RED + text.LINE)
    print(style.BLUE + "How Many Cards To Generator")
    nn = input(style.RED + "> ")
    n = int(nn)
    for x in range(n):
        data = {
    'Type': 'visa',
    'X-Requested-With': 'XMLHttpRequest',
}
        response = requests.post('https://randommer.io/Card', data=data)
        print(style.BLUE + response.text)
        cards()

   if choice == "5":
    os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
    print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
    print(style.RED + text.LINE)
    print(style.BLUE + "How Many Cards To Generator")
    nn = input(style.RED + "> ")
    n = int(nn)
    for x in range(n):
        print("")
        print(style.BLUE + g(4)+"-"+g(6)+"-"+g(5))
        cards()

   if choice == "6":
    os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
    print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
    print(style.RED + text.LINE)
    print(style.BLUE + "How Many Cards To Generator")
    nn = input(style.RED + "> ")
    n = int(nn)
    for x in range(n):
        print("")
        print(style.BLUE + g(5)+"-"+g(4)+"-"+g(4))
        cards()
   
   if choice == "00":
      main()
       
def webhook():
    print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
    print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
    print(style.RED + text.LINE)
    print(style.BLUE + "[1] Spam Webhook          [2] Delete Webhook          [3] Coming Soon.\n                [00] Return To Menu")
    ans = input(style.RED + "> ")
    if ans == "1":
       os.system('cls')
       print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
       print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
       print(style.RED + text.LINE)
       print(style.BLUE + "Enter The Webhook You Want To Spam")
       hook = input(style.RED + "> ")
       os.system('cls')
       print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
       print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
       print(style.RED + text.LINE)
       print(style.BLUE + "What Message Would You Like To Spam?")
       msg = input(style.RED + "> ")
       os.system('cls')
       print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
       print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
       print(style.RED + text.LINE)
       print(style.BLUE + "How Many Messages Would You Like To Spam?")
       amtmsg = input(style.RED + "> ")

       for i in range (amtmsg):
        response = requests.post(hook, json={"content": msg})

       webhook()

    if ans == "2":
       os.system('cls')
       print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
       print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
       print(style.RED + text.LINE)
       print(style.BLUE + "Enter The Webhook You Want To Delete")
       hook = input(style.RED + "> ")
       response = requests.delete(hook)
       webhook()
    if ans == "00":
       main()

def grabify():
       os.system('cls')
       print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
       print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
       print(style.RED + text.LINE)
       print(style.BLUE + "Enter The Link You Want To Flood (It Will Does Not Use Proxies So It Will Show Your Ip If You Use Grabify)")
       link = input(style.RED + "> ")
       os.system('cls')
       print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
       print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
       print(style.RED + text.LINE)
       print(style.BLUE + "How Many Times Would You Like To Flood The Link")
       linkamt = input(style.RED + "> ")
       for i in range(linkamt):
          response = requests.get(link)

       main()
   
reports = 0

def reporter():
   global reports
   os.system('cls')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.BLUE + "Enter The Username Of The Person Who You Would Like To Report")
   user = input(style.RED + "> ")
   os.system('cls')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.BLUE + "How Many Times Would You Like To Report Them?")
   amount = input(style.RED + "> ")
   for i in range(amount):
      reports += 1
      print(style.RED + f"[SYSTEM] Report Added {reports}/{amount}")
     
def discordidtotoken():
   os.system('cls')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.BLUE + "Enter The User Id You Want To Convert")
   userid = input(style.RED + "> ")
   converter = base64.b64encode(userid.encode("utf-8"))
   token = str(converter, "utf-8")
   os.system('cls')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.BLUE + "Hit Enter To Return To Menu")
   print(style.BLUE + f"TOKEN : {token}")
   continyou = input(style.RED + "> ")
   main()

def google():
   os.system('cls')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.BLUE + "site: intitle: username intitle: password filetype: pdf") 
   print(style.BLUE + "site: intitle: username intitle: password filetype: doc") 
   print(style.BLUE + "inurl:users.json + 'username'")
   print(style.BLUE + "inurl:'trello.com' and intext:'username' and intext:'password'")
   print(style.BLUE + "indexof:site")
   print(style.BLUE + "inurl: 'webcamxp5'")
   print(style.BLUE + "'battlefield' 'email' site:pastebin.com")
   print(style.BLUE + "Index of / +password.txt")
   print(style.BLUE + "site: .com intitle: microsoft filetype: pdf")
   print(style.RED + "Hit Enter To Return To Menu | Wherever Theres A Single Quote Put Double Quotes - ' = ''")
   continyou = input(style.RED + "> ")

def emailheader():
   os.system('cls')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.GREEN + "You Must Have Your Email Header In header.txt Hit Enter To Continue")
   continyou = input(style.RED + "> ")
   def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'fail':
        return "Unknown"
    else:
        return f"{data['city']}, {data['regionName']}, {data['country']}"

   def extract_header_info(header):
    ip_pattern = r"(?i)received: from.*\[([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\]"
    subject_pattern = r"(?i)subject:(.*)"
    
    ip_match = re.search(ip_pattern, header)
    subject_match = re.search(subject_pattern, header)
    
    ip = ip_match.group(1) if ip_match else "Unknown"
    subject = subject_match.group(1).strip() if subject_match else "Unknown"
    
    return ip, subject

# Read email header from a text file
   with open('header.txt', 'r') as file:
    header = file.read()

   ip, subject = extract_header_info(header)
   ip_info = get_ip_info(ip)

   print(style.RED + "Source IP:", ip)
   print(style.RED + "IP Location:", ip_info)
   print(style.RED + "Email Subject:", subject)

def websitescrape():
    os.system('cls')
    print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
    print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
    print(style.RED + text.LINE)
    print(style.GREEN + "Gets Emails From The Site")
    user_url = str(input(style.BLUE + '(+] Enter Target URL To Scan: '))

    urls = deque([user_url])
    scraped_uris = set()
    emails = set()
    count = 0
    try:
        while urls:
            count += 1
            if count == 51:
                break
            url = urls.popleft()
            scraped_uris.add(url)

            parts = urllib.parse.urlsplit(url)
            site_url = '{0.scheme}://{0.netloc}'.format(parts)
            path = url[site_url.rfind('/') + 1:] if '/' in parts.path else url

            print('[-] Processing URL #%d: %s' % (count, url))
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            emails.update(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', response.text, re.I))
            
            soup = BeautifulSoup(response.text, features="lxml")
            
            for a_tag in soup.find_all('a'):
                new_url = a_tag.get('href')
                if new_url and not new_url.startswith('http'):
                    new_url = urllib.parse.urljoin(site_url, new_url)
                urls.append(new_url)
                
    except KeyboardInterrupt:
        print('\n[!] Program interrupted by user.')

    print('\n[+] Scan completed. Emails found:')
    for email in emails:
        print(email)
        main()

def directorysniff():
   word_list = ['development','images','imgs','img','developer','template','design','Mobile','Bootstrap','from','time','Cross','Config','config','server','Search','objects','data','database','db','root']
   os.system('cls')
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.GREEN + "Sniffs A Sites Directories")
   url = str(input(style.BLUE + 'Enter Target URL To Sniff > '))
   response = requests.get(url)
   if response.status_code == 200:
      for word in word_list:
         directory_url = url + '/' + word
         response2 = requests.get(directory_url)
         if response2.status_code == 200:
                print(f"Directory Found: {directory_url}")
         else:
                print(f"")
         time.sleep(2)
         main()

def username():
   os.system('cls')
   sites = [
    'https://youtube.com/@',
    'https://about.me/',
    'https://www.9gag.com/',
    'https://www.7cups.com/@',
    'https://airlinepilot.life/',
    'https://allmylinks.com/@',
    'https://xboxgamertag.com/search/',
    'https://en.wikipedia.org/wiki/',
    'https://vimeo.com/',
    'https://account.venmo.com/u/',
    'https://tenor.com/users/',
    'https://open.spotify.com/user/',
    'https://speedrun.com/user/',
    'https://soundcloud.com/',
    'https://www.snapchat.com/add/',
    'https://replit.com/@',
    'https://www.reddit.com/user/',
    'https://www.roblox.com/user.aspx?username=',
    'https://www.polygon.com/users/',
    'https://play.google.com/store/apps/developer?id=',
    'https://www.patreon.com/',
    'https://www.nitrotype.com/racer/',
    'https://api.nightbot.tv/1/channels/t/',
    'https://linktr.ee/',
    'https://lichess.org/@/',
    'https://www.chess.com/member/',
    'https://www.gumroad.com/',
    'https://www.github.com/',
    'https://fortnitetracker.com/profile/all/',
    'https://www.fiverr.com/',
    'https://www.etsy.com/shop/',
    'https://www.duolingo.com/profile/',
    'https://codepen.io/',
    'https://developer.apple.com/forums/profile/',
    'https://discussions.apple.com/profile/',
    'https://archive.org/details/@',
    'https://www.twitch.tv/',
    'https://tiktok.com/@',
    'https://www.behance.net/',
    'https://www.ebay.com/usr/',
    'https://Amazon.com/profile/',
    'https://www.instagram.com/',
    'https://cash.app/$',
    'https://www.rottentomatoes.com/critics/',
    'https://www.linkedin.com/in/',
    'https://www.kickstarter.com/profile/',
    'https://pastebin.com/u/',
    'https://patreon.com/',
    'https://steamcommunity.com/id/',
    'https://www.cnn.com/profiles/',
    'https://apex.tracker.gg/apex/profile/origin/',  # cloudflare prot
    'https://cod.tracker.gg/warzone/profile/atvi/',
    'https://r6.tracker.network/profile/pc/',
    'https://rocketleague.tracker.network/rocket-league/profile/epic/',
    'https://halotracker.com/halo-infinite/profile/xbl/',
    'https://tracker.gg/pubg/profile/steam/',
    'https://www.buzzfeed.com/',

]       
   errormsgs = ['not working', 'Sorry, nobody on Reddit goes by that name.',"Sorry. Unless you’ve got a time machine, that content is unavailable.",'find this account','Sorry, this user was not found.',"Sorry, this page isn't available.","This page doesn’t exist","the specified profile could not be found."]
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.GREEN + "Username Lookup")
   username = str(input(style.BLUE + 'Enter Target Username > '))
   for site in sites:
      lookup = site + username
      r = requests.get(lookup)
      #print(str(r.status_code) + lookup)
      error_found = False
      if any(message in r.text.lower() for message in errormsgs):
            error_found = True
            #break
      if not error_found:
         if r.status_code == 200:
          print(style.GREEN + "[+] " + lookup)
          time.sleep(0.1)
   Returntomenu = input(style.RED + "Hit Enter To Return > ")
   main()

def unshorten():
   print(Colorate.Horizontal(Colors.yellow_to_red, """███████╗████████╗ █████╗ ██████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║██╔═══██╗██║  ██║╚══██╔══╝
███████╗   ██║   ███████║██████╔╝██║     ██║██║   ██║███████║   ██║   
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║▄▄ ██║██╔══██║   ██║   
███████║   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   
                                                                      """"",1))
   print(style.YELLOW + "bc1qmrmym2568njv84xrauc3n5y6fewajxjf2jvsfq")
   print(style.RED + text.LINE)
   print(style.GREEN + "Link Unshortener")
   url = str(input(style.BLUE + 'Enter Target Link > '))
   os.system(f"curl --head --location '{url}' | findstr Location")

main()