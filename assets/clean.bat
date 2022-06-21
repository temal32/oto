@echo off
netsh interface tcp set global autotuning=restricted
ipconfig /renew
ipconfig /flushdns
