import os
from pydub import AudioSegment

# Input folder (jaha apki split files hain)
input_folder = "mna_clips"
# Output folder (converted files yaha save hongi)
output_folder = "refined_wav"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".m4a"):
        filepath = os.path.join(input_folder, file)
        
        # Load audio file
        audio = AudioSegment.from_file(filepath)
        
        # Refine: mono channel, 16kHz sample rate, 16-bit
        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_sample_width(2)
        
        # Export as WAV
        new_filename = os.path.splitext(file)[0] + ".wav"
        audio.export(os.path.join(output_folder, new_filename), format="wav")

print("✅ All files converted & refined to WAV format!")


    
