# Mini Project 3 - Digital Signal Processing (DSP) using Python

# Introduction

Mini project 3 was about the study of DSP by analyzing in with the programming language Python. Basic topics of DSP were analyzed such as the frequency domain of a signal using Discrete Fourier Transform (DFT). A tutorial was followed in order to understand the basics of DSP analysis with python. Libaries that were used included numpy, matplotlib, wave ,and struct. Using these libraries, we can analyze signals.

# Included in the repository
- Script that outputs a graph of sine wave signal and frequency domain
- Script that creates an audio file, which was a sine wave with a amplitude and frequency that can be altered in the script.
- Audio file (test.wav)
- Tutorial followed: https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/

# Visualization using matplotlib

Using matplotlib is a very simple visualization tool to analyze signals. Similar to another programing language MATLAB, matplotlib allows you to create plots to visualize your signal or the frequency domain. For this example, an audio file was created, which was a sine wave with amplitude of 16000 and a frequency of 1kHz. The file is labeled as test.wav in the repository. In the following script, we open the test.wav file and analyze the signal in the time domain. Next, the discrete fourier transform was applied to extract the frequencies, so the frequency domain can be plotted. Using matplotlib, the time domain of the signal and frequency domain was plotted. 

Script:

![alt text](https://github.com/martinezg1/MiniProject3/blob/master/Script%20matplotlib.PNG)

Output:


![alt text](https://github.com/martinezg1/MiniProject3/blob/master/script_matplotlib_output.PNG)

Example code taken from https://scipy-lectures.org/intro/scipy/auto_examples/plot_spectrogram.html

# Visualization of a Chirp signal

For our semester project, we were working with the Chirp api. This api allows a audio signal of varying frequencies to be transmitted and received by other devices that contain the api. Analysis is similar to the previous example, but the audio file is a chirp file which is labeled as 16 kHz maximum frequency. Applying the same script as the last one, the entire signal was plotted. Next, the frequency domain was plotted.
Script: 
![alt text](https://github.com/martinezg1/MiniProject3/blob/master/Chirp_sig_script.PNG)

Output:
![alt text](https://github.com/martinezg1/MiniProject3/blob/master/chirp_output_1.PNG)

In addition to analyzing the frequency domain, an additional library can be used to analyze the signal's power spectral densitiy (power of the signal) and the spectrograph (frequency bands at various times). The library in use was scipy.

Script:

![alt text](https://github.com/martinezg1/MiniProject3/blob/master/2nd_chirp_script.PNG)

Output: 

![alt text](https://github.com/martinezg1/MiniProject3/blob/master/chirp_output_2.PNG)


Conclusion:

Python is a powerful tool. Not only is python useful for developing software, it has many applications in engineering fields. As demonstrated in this report, python is capable of digital signal processing. Due to python being a high level programing language, the learning curve for programing DSP scripts and applications is much lower compared other programing language. However, there are some other programs that can also handle DSP analysis like MATLAB. If a beginner wants to study DSP, python is a better choice due to it being free and has a plethora of resources to get started since MATLAB requires a licence to use. 

