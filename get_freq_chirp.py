import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
from scipy import signal

frame_rate = 48000.0
 
infile = "2a64ff.wav"
 
num_samples = 48000
 
wav_file = wave.open(infile, 'r')
 
data = wav_file.readframes(num_samples)
 
wav_file.close()

data = struct.unpack('{n}h'.format(n=num_samples), data)
 	
data = np.array(data)

data_fft = np.fft.fft(data)

frequencies = np.abs(data_fft)

print("The frequency is {} Hz".format(np.argmax(frequencies)))

plt.subplot(2,1,1)
 
plt.plot(data[:60000])
 
plt.title("Original audio wave")
plt.ylabel("Amplitude")
plt.xlabel("Time (sec)")

 
plt.subplot(2,1,2)

plt.plot(frequencies)
 
plt.title("Frequencies found")
 
plt.xlim(0,16000)
plt.subplots_adjust(hspace = 1)
plt.xlabel("Frequency (Hz)")
plt.show()

freqs, times, spectrogram = signal.spectrogram(data)

plt.figure(figsize=(5, 4))
plt.imshow(spectrogram, aspect='auto', cmap='hot_r', origin='lower')
plt.title('Spectrogram')
plt.ylabel('Frequency band')
plt.xlabel('Time window')
plt.tight_layout()


freqs, psd = signal.welch(data)

plt.figure(figsize=(5, 4))
plt.semilogx(freqs, psd)
plt.title('PSD: power spectral density')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.tight_layout()
