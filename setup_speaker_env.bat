@echo off
REM ------------------------------
REM Setup Resemblyzer Environment on Windows
REM ------------------------------

echo Activating speaker_env...
call conda activate speaker_env

echo.
echo Step 1: Installing PyTorch (CPU only)...
conda install pytorch torchaudio cpuonly -c pytorch -y

echo.
echo Step 2: Creating embedding folder...
mkdir "C:\first data work\embedding"

echo.
echo Step 3: Installing Resemblyzer and dependencies...
REM Using conda-forge for Windows compatibility
conda install -c conda-forge resemblyzer -y

echo.
echo Step 4: Verifying installation...
python -c "from resemblyzer import VoiceEncoder, preprocess_wav; print('Resemblyzer is working!')"

echo.
echo ✅ Setup complete! Your speaker_env is ready.
pause
