@echo off
REM This batch file processes audio and video files using Python scripts.

:menu
cls
echo Please select an operation:
echo [1] Extract audio from video
echo [2] Split audio file
echo [3] Merge audio files
echo [4] Set audio to video
echo [5] Display help
echo [6] Exit
echo.

REM Use the CHOICE command to get user input.
choice /C 123456 /N /M "Enter your choice:"

REM Check the error level returned by CHOICE to determine the operation.
if errorlevel 6 goto end
if errorlevel 5 goto help
if errorlevel 4 goto setAudioToVideo
if errorlevel 3 goto merge
if errorlevel 2 goto split
if errorlevel 1 goto extract

:extract
REM Extract audio from a video file.
set /p filepath=Enter the path of the video file:
set "filepath=%filepath:\=/%"
python -c "from video_to_audio import extractAudioFromVideo; print(extractAudioFromVideo('%filepath%'))"
pause
goto menu

:split
REM Split an audio file into smaller parts.
set /p filepath=Enter the path of the audio file:
set "filepath=%filepath:\=/%"
set /p duration=Enter the duration for splitting (in seconds):
python -c "from audio_splitter import splitAudioFiles; print(splitAudioFiles('%filepath%', %duration))"
pause
goto menu

:merge
REM Merge multiple audio files into one.
set /p filepath=Enter the path where the audio files are located:
set "filepath=%filepath:\=/%"
python -c "from audio_files_merge import mergeAudioFiles; print(mergeAudioFiles('%filepath%'))"
pause
goto menu

:setAudioToVideo
REM Set audio to a video file.
set /p video_path=Enter the path of the video file:
set "video_path=%video_path:\=/%"
set /p audio_path=Enter the path of the audio file:
set "audio_path=%audio_path:\=/%"
python -c "from replace_video_audio import setAudioToVideo_ffmpeg; print(setAudioToVideo_ffmpeg('%video_path%', '%audio_path%'))"
pause
goto menu

:help
echo.
echo This batch file supports the following operations:
echo   [1] Extract - Extracts audio from a video file.
echo   [2] Split   - Splits an audio file into segments of a specified duration.
echo   [3] Merge   - Merges multiple audio files into one.
echo   [4] Set Audio - Sets a new audio to a video file.
echo   [5] Help    - Displays this help message.
echo   [6] Exit    - Exits the batch file.
echo.
pause
goto menu

:end
echo Exiting...
