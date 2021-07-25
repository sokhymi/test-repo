@echo off
setlocal EnableDelayedExpansion
for %%a in (*.tif) do (
   set fileName=%%~a
   set datePart=!fileName:~20,7!
   if not exist "C:\directory\!datePart!" md "C:\directory\!datePart!"
   move "%%a" "C:\directory\!datePart!"
)

REM This batch file is used for organizing multiple files into folders based on their filenames. "set datePart" determines which characters are of
REM importance. Files whose names contain the same characters in the set datePart variable will be organized into a new folder named with the aforementioned characters.
REM Place this .bat file in the directory where the myriad of files are located.
REM Note that the "!fileName" parameter's first value is = first character position - 1, 
REM while the latter is length of the key characters + 1.

REM This script can be performed on any file. Change the ".tif" extension on line 3.