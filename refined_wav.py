import subprocess
from pathlib import Path

def convert_mp3_to_wav(mp3_path, output_dir):
    output_path = output_dir / (mp3_path.stem + ".wav")
    subprocess.run([
        "ffmpeg", "-y", "-i", str(mp3_path),
        "-ar", "16000", "-ac", "1",
        str(output_path)
    ], check=True)
    return output_path

input_dir = Path("mna_clips")   # root folder jisme subfolders hain
output_dir = Path("refined_wave")
output_dir.mkdir(exist_ok=True)

# subfolders ke andar sab mp3 files search karega
for mp3_file in input_dir.rglob("*.mp3"):
    print(f"Converting: {mp3_file}")
    wav_file = convert_mp3_to_wav(mp3_file, output_dir)
    print(f"Saved: {wav_file}")

import os
import shutil
from pathlib import Path

# Base folders
mna_clips = Path("mna_clips")       # jahan mna ke folders hain
refined_wave = Path("refined_wave") # abhi jahan sab wav mix ho gaye hain

# refined_wave ke andar sab wav files loop karo
for wav_file in refined_wave.glob("*.wav"):
    # file ka naam se mna ka folder extract karo (split by "_part")
    mna_name = wav_file.stem.split("_part")[0]

    # destination folder banao -> mna_clips/<mna_name>/refined_wave/
    dest_folder = mna_clips / mna_name / "refined_wave"
    dest_folder.mkdir(parents=True, exist_ok=True)

    # file move karo
    shutil.move(str(wav_file), dest_folder / wav_file.name)

print("✅ Sab files apne-apne mna folders me chali gayi hain!")




