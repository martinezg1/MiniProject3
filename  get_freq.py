import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

frame_rate = 48000.0
 
infile = "chirp_16khz_mono_2.wav"
 
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
 
plt.plot(data[:500])
 
plt.title("Original audio wave")

 
plt.subplot(2,1,2)

plt.plot(frequencies)
 
plt.title("Frequencies found")
 
plt.xlim(0,5000)
 
plt.show()