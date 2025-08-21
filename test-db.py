import os
import shutil

# Base directory where all speakers' folders are located
base_dir = r"C:\first data work\mna_clips"

# Loop over each speaker's folder
for speaker in os.listdir(base_dir):
    speaker_path = os.path.join(base_dir, speaker)
    refined_wave_path = os.path.join(speaker_path, "refined_wave")

    if not os.path.isdir(refined_wave_path):
        continue  # Skip if no refined_wave folder

    # Define new train-db and test-db paths
    train_db_path = os.path.join(speaker_path, "train-db")
    test_db_path = os.path.join(speaker_path, "test-db")

    # Rename refined_wave -> train-db
    if not os.path.exists(train_db_path):
        os.rename(refined_wave_path, train_db_path)

    # Make test-db if not exists
    os.makedirs(test_db_path, exist_ok=True)

    # List all clips and sort alphabetically
    clips = sorted([f for f in os.listdir(train_db_path) if f.lower().endswith((".wav", ".mp3"))])

    # Take first 10 clips
    clips_to_move = clips[:10]

    # Move 10 clips into test-db
    for clip in clips_to_move:
        src = os.path.join(train_db_path, clip)
        dst = os.path.join(test_db_path, clip)
        shutil.move(src, dst)

    print(f"Processed {speaker}: moved {len(clips_to_move)} clips to test-db.")


