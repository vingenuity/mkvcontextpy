::
:: InstallContextMenus.bat
:: 
:: Author: Vincent Kocks (engineering@vingenuity.net)
:: v1.1.0
::
:: Double-click batch script wrapper to install context menus.
::
@echo off



:: --------------------------------------------------------------
:: FILE PARAMETERS
:: --------------------------------------------------------------
set MANAGE_MENUS_SCRIPT=%~dp0python\manage_context_menus.py
set PACKAGE_REQUIREMENTS_FILE=%~dp0requirements.txt
set PROJECT_NAME=mkvcontextpy
set PYTHON=python



:: --------------------------------------------------------------
:: MAIN SCRIPT FLOW
:: --------------------------------------------------------------
echo Installing required Python packages for %PROJECT_NAME%...
%PYTHON% -m pip install -r %PACKAGE_REQUIREMENTS_FILE%
if ERRORLEVEL 1 goto :package_install_error
echo Installed Python packages successfully.

echo Installing %PROJECT_NAME% context menu...
%PYTHON% %MANAGE_MENUS_SCRIPT% install
if ERRORLEVEL 1 goto :menu_install_error
echo Installed %PROJECT_NAME% context menu successfully.
goto finish


:package_install_error
echo Python package installation failed!
pause
goto finish


:menu_install_error
echo %PROJECT_NAME% context menu installation failed!
pause
goto finish


:finish
if /I not "%1"=="-nopause" pause
