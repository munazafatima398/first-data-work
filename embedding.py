from pathlib import Path
from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import os

# Paths
mna_clips_dir = Path("C:/first data work/mna_clips")
embedding_dir = Path("C:/first data work/embeddings")
embedding_dir.mkdir(exist_ok=True)

# Load encoder
encoder = VoiceEncoder()

# Har MNA folder ke andar "train-db" check karo
for mna_folder in mna_clips_dir.iterdir():
    if mna_folder.is_dir():
        train_db = mna_folder / "train-db"
        if not train_db.exists():
            print(f"⚠️ Skipped (train-db not found): {mna_folder}")
            continue

        embeddings = []
        for wav_file in train_db.glob("*.wav"):
            try:
                wav = preprocess_wav(wav_file)
                emb = encoder.embed_utterance(wav)
                embeddings.append(emb)
            except Exception as e:
                print(f"❌ Error on {wav_file}: {e}")

        if embeddings:
            emb = np.mean(embeddings, axis=0)  # average embedding
            np.save(embedding_dir / f"{mna_folder.name}.npy", emb)
            print(f"✅ Saved embedding for {mna_folder.name}")






