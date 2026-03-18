# Bad Electrode Contact Detection (EEG)

## Overview
This project aims to design an algorithm to detect bad electrode contact in EEG signals. Poor electrode contact can result in unreliable recordings such as flatlines, excessive noise, or movement artifacts.

The algorithm analyzes EEG signals using defined metrics and classifies signal quality automatically.

---

## Objectives
- Define quantitative metrics to assess EEG signal quality
- Simulate different EEG conditions
- Detect abnormal electrode behavior automatically

---

## Methodology

### 1. Metrics Used

1. Signal Variance
- Measures how much the signal changes over time
- Low variance indicates flatline
- High variance indicates noise or artifacts

2. Signal Amplitude Range
- Difference between maximum and minimum values
- Helps detect spikes or lack of signal

3. Signal-to-Noise Indicator (SNR-like)
- Compares useful signal level to noise
- Low value indicates noisy or poor signal quality

---

### 2. Simulated EEG Conditions

a) Normal EEG
- Smooth oscillatory signal with small noise
- Represents proper electrode contact

b) Flatline
- Nearly constant signal
- Represents disconnected electrode

c) High Noise
- Random signal with large fluctuations
- Represents interference

d) Movement Artifact
- Sudden spikes and irregular patterns
- Caused by motion or loose electrodes

---

## Algorithm Logic

1. Compute metrics:
   - Variance
   - Amplitude range
   - Noise indicator

2. Apply thresholds:
   - If variance is very low → Flatline
   - If variance is very high → Noise
   - If sudden spikes exist → Movement Artifact
   - Otherwise → Normal EEG

---

## Code
The implementation is written in Python using:
- numpy for signal processing
- matplotlib for visualization

Steps:
1. Generate simulated signals
2. Compute metrics
3. Classify signal
4. Plot results

---



## Results
The algorithm can successfully distinguish between:
- Normal EEG signals
- Flatline signals (low variance)
- Noisy signals (high variance)
- Movement artifacts (sudden spikes)

---

### 1. Why did you choose these metrics?
- Variance captures signal activity
- Amplitude range detects extremes or missing signal
- SNR-like metric identifies noise dominance

These are simple, fast, and effective for signal quality analysis.

---

### 2. Why did you choose these threshold values?
- Thresholds were chosen based on simulated data
- Tuned to clearly separate normal and abnormal cases
- Can be adjusted for real EEG datasets

---

### 3. How versatile/generalizable is the algorithm?
- Works on different EEG signals and sampling rates
- Can be extended to multi-channel EEG systems

Limitations:
- Thresholds may need tuning for real data
- Complex noise may reduce accuracy



## Future Work
- Apply to real EEG datasets
- Add signal filtering techniques
- Improve robustness for clinical use
