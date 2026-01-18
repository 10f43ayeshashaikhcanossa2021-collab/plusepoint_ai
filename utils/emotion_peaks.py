import librosa
import numpy as np

def get_emotional_timestamps(audio_path, top_n=5):
    y, sr = librosa.load(audio_path)
    energy = librosa.feature.rms(y=y)[0]
    times = librosa.frames_to_time(range(len(energy)), sr=sr)

    peaks = np.argsort(energy)[-top_n:]
    return sorted(times[p] for p in peaks)
