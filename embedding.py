import os
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav

# Initialize Resemblyzer encoder
encoder = VoiceEncoder()

# Base folder
base_folder = r"C:\first data work"

# Data folders
data_folders = ["train-db", "test-db"]

# Embeddings folder
embeddings_folder = os.path.join(base_folder, "embeddings")
os.makedirs(embeddings_folder, exist_ok=True)

# Loop through each data folder
for folder in data_folders:
    folder_path = os.path.join(base_folder, folder)
    save_base = os.path.join(embeddings_folder, folder)
    os.makedirs(save_base, exist_ok=True)

    # Loop through each Mna folder
    for mna_name in os.listdir(folder_path):
        mna_path = os.path.join(folder_path, mna_name)
        if os.path.isdir(mna_path):
            save_folder = os.path.join(save_base, mna_name)
            os.makedirs(save_folder, exist_ok=True)

            for file_name in os.listdir(mna_path):
                if file_name.lower().endswith(".wav"):
                    file_path = os.path.join(mna_path, file_name)
                    try:
                        # Preprocess wav and generate embedding
                        wav = preprocess_wav(file_path)
                        embedding = encoder.embed_utterance(wav)

                        # Save embedding as .npy
                        embedding_file = os.path.splitext(file_name)[0] + ".npy"
                        embedding_path = os.path.join(save_folder, embedding_file)
                        np.save(embedding_path, embedding)
                        print(f"Saved embedding: {embedding_path}")
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")

