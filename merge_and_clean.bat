@echo off

rem Specify the file paths for dicMerger.py
set "input_file1=C:\pathToDictionaryToMerge1\input1.dic"
set "input_file2=C:\pathToDictionaryToMerge2\input2.dic"
set "merged_output=C:\\pathToDictionaryOutput\output.dic"

rem Create a log file to capture the output of all scripts
set "log_file=%~dp0log_output.txt"
if exist "%log_file%" del "%log_file%"

rem Run dicMerger.py
echo Running dicMerger.py... >> "%log_file%"
python dicMerger.py "%input_file1%" "%input_file2%" "%merged_output%" >> "%log_file%" 2>&1
if %errorlevel% neq 0 (
    echo Error running dicMerger.py >> "%log_file%"
    exit /b %errorlevel%
)

rem Run dicDuplicateRemover.py
echo Running dicDuplicateRemover.py... >> "%log_file%"
python dicDuplicateRemover.py "%merged_output%" >> "%log_file%" 2>&1
if %errorlevel% neq 0 (
    echo Error running dicDuplicateRemover.py >> "%log_file%"
    exit /b %errorlevel%
)

rem Run dicInvalidRemover.py
echo Running dicInvalidRemover.py... >> "%log_file%"
python dicInvalidRemover.py "%merged_output%" >> "%log_file%" 2>&1
if %errorlevel% neq 0 (
    echo Error running dicInvalidRemover.py >> "%log_file%"
    exit /b %errorlevel%
)

rem Run dicValidator.py
echo Running dicValidator.py... >> "%log_file%"
python dicValidator.py "%merged_output%" >> "%log_file%" 2>&1
if %errorlevel% neq 0 (
    echo Error running dicValidator.py >> "%log_file%"
    exit /b %errorlevel%
)

echo All scripts executed successfully. >> "%log_file%"
pause
