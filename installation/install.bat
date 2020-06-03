@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------  

cd "%~dp0" 
setlocal
setlocal enabledelayedexpansion

reg query "HKEY_LOCAL_MACHINE\SOFTWARE\QGIS 3.12" /v "InstallPath
if %ERRORLEVEL%==0 (goto :qgis312) ELSE (goto :qgis310)


:qgis310
echo "QGIS 3.10"
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\QGIS 3.10" /v "InstallPath
if %ERRORLEVEL%==0 (

for /f "usebackq tokens=3*" %%a in (`reg query "HKEY_LOCAL_MACHINE\SOFTWARE\QGIS 3.10" /v "InstallPath"`) do (
  set _acrobat_path=%%a %%b\OSGeo4W.bat
  echo !_acrobat_path!

  )

) ELSE (goto :unsupp)


call "!_acrobat_path!" start cmd.exe /c  "_acrobat_path && py3_env && pip install Fiona-1.8.13-cp37-cp37m-win_amd64.whl pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz pyproj-2.5.0-cp37-cp37m-win_amd64.whl"
echo "Successfuly"
endlocal
goto :end



:qgis312
echo "QGIS 3.12 initiation"


for /f "usebackq tokens=3*" %%a in (`reg query "HKEY_LOCAL_MACHINE\SOFTWARE\QGIS 3.12" /v "InstallPath"`) do (
  set _acrobat_path=%%a %%b\OSGeo4W.bat
  set py3_patn=%%a %%b\OSGeo4W.bat
  echo !_acrobat_path!

 
  )



call "!_acrobat_path!" start cmd.exe /c  "_acrobat_path && py3_env && pip install Fiona-1.8.13-cp37-cp37m-win_amd64.whl pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz pyproj-2.5.0-cp37-cp37m-win_amd64.whl"


echo "Successfuly"
endlocal
goto :end


:unsupp
echo "QGIS 3.10 and 3.12 was not found"
endlocal
goto :end

:end
echo "End script"
exit /b 0
