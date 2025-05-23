@echo off
cd /d "%~dp0"
"C:\Users\neurophet1\AppData\Local\Programs\Python\Python313\python.exe" "%~dp0auto_git_push_jini.py" > "%~dp0scheduler_log.txt" 2>&1
pause 