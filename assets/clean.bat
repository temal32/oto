@echo off
netsh interface tcp set global autotuning=normal
ipconfig /renew
ipconfig /flushdns
