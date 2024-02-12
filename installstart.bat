@echo off
echo Installing packages...
pip install -r requirements.txt
cls
echo Starting bot
cls
python main.py
echo Bot stopped. exiting
ping 3 > nul
