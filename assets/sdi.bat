::***********************************************************************************
::
:: Keep SDI.exe updated with the latest drivers and version of SDI_Rnnn.exe
::
:: NOTE: Put this batch file in the SDI_UPDATE directory with the SDI_Rnnn.exe file
::***********************************************************************************
::
::SET SDIPath to location of batch file which should be with SDI_Rnnn.exe
@echo off
SET SDIPath=%~dp0
PUSHD %SDIPath%
::Get the newest SDI_Rnnn.exe file
FOR /F "delims=|" %%I IN ('DIR "SDI_R*.exe" /B /O:D') DO SET NewestSDI=%%I
:: Run SDI update
CALL %NewestSDI% /autoupdate /autoclose
::Make sure we still have most current executable in case one was just downloaded
FOR /F "delims=|" %%I IN ('DIR "SDI_R*.exe" /B /O:D') DO SET NewestSDI=%%I
::Copy current version to SDI.exe
COPY %NewestSDI% SDI.exe /Y
POPD