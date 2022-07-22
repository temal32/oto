@echo off
cls
for /F "skip=3 tokens=1,2,3* delims= " %%G in ('netsh interface show interface') DO (
    IF "%%H"=="Disconnected" netsh interface set interface "%%J" enabled
    IF "%%H"=="Connected" netsh interface set interface "%%J" enabled
    echo %%J
    netsh interface ip set dns %%J static 1.1.1.1
)
exit