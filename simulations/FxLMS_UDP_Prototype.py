# ZPRE-10 UDP - FxLMS Prototype
# Simulates a simplified Feedforward Least Mean Squares (FxLMS) algorithm
# used in waveform cancellation under the Unified Dampening Protocol (UDP)

import numpy as np
import matplotlib.pyplot as plt

# Sample input waveform (simulated noise)
np.random.seed(42)
input_wave = np.random.normal(0, 1, 500)

# Reference signal
reference_wave = np.convolve(input_wave, [0.6, -0.2], mode='same')

# Adaptive filter
def fx_lms(reference, desired, mu=0.01, filter_len=32):
    n = len(desired)
    w = np.zeros(filter_len)
    output = np.zeros(n)
    error = np.zeros(n)
    
    for i in range(filter_len, n):
        x = reference[i-filter_len:i]
        y = np.dot(w, x)
        output[i] = y
        error[i] = desired[i] - y
        w += mu * error[i] * x
    return output, error, w

filtered, err, weights = fx_lms(reference_wave, input_wave)

# Plot
plt.figure(figsize=(10,4))
plt.plot(input_wave, label='Input')
plt.plot(filtered, label='Filtered')
plt.legend()
plt.title("UDP – FxLMS Noise Cancellation")
plt.show()
