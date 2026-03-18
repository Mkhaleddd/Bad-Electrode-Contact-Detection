import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
folder_path = r"C:\Users\maria\Downloads\Task 1"
files = [f for f in os.listdir(folder_path) if f.endswith('.dat')]

def compute_metrics(signal):
    variance = np.var(signal)
    peak_to_peak = np.max(signal) - np.min(signal)
    noise_metric = np.std(np.diff(signal))
    return variance, peak_to_peak, noise_metric

def detect(signal):
    variance, p2p, noise = compute_metrics(signal)
    if variance < 1e-6 or noise < 1e-6 or p2p < 1e-6:
        return "Flatline (Bad Contact)"
    elif noise > 20 or variance > 500 or (p2p > 50 and p2p < 150):
        return "High Noise (Bad Contact)"
    elif p2p > 150:
        return "Movement Artifact"
    else:
        return "Normal EEG"

file_name = files[0]  
file_path = os.path.join(folder_path, file_name)
with open(file_path, 'rb') as f:
    data = pickle.load(f, encoding='latin1')

eeg_data = data['data'][:, :32, 384:]
signal = eeg_data[0, 0, :1000]  
normal = signal
flatline = np.zeros_like(signal)
high_noise = normal + np.random.normal(0,50,len(normal))
movement = normal.copy()
movement[100:150] += 200
signals = {
    "Normal EEG": normal,
    "Flatline": flatline,
    "High Noise": high_noise,
    "Movement Artifact": movement
}

fig, axes = plt.subplots(4, 1, figsize=(12, 8), sharex=True)
for i, (name, sig) in enumerate(signals.items()):
    axes[i].plot(sig)
    axes[i].set_title(f"{file_name} Trial 1: {name} -> {detect(sig)}")
    axes[i].set_ylabel("Amplitude")
axes[-1].set_xlabel("Sample")
plt.tight_layout()
plt.show()

for sample_idx in range(2): 
    file_name = files[sample_idx]
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'rb') as f:
        data = pickle.load(f, encoding='latin1')
    eeg_data = data['data'][:, :32, 384:]  
    print(f"\nDetection results for {file_name}:")
    
    num_trials = 10 
    for trial_idx in range(num_trials):
        results = []
        for ch in range(3):  
            signal = eeg_data[trial_idx, ch, :1000]  
            results.append(detect(signal))
        print(f"Trial {trial_idx+1}: {results}")