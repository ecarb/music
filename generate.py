
from scipy.io import wavfile
import numpy as np

'''
would be nice to have a timbre-adding function
'''

# UTILS

from notes import note_to_frequency_Hz as note_to_freq
from convolve import convolve

def duration_to_num_samples (duration, sample_rate):
	return duration * sample_rate

def num_samples_to_duration (num_samples, sample_rate):
	return num_samples / sample_rate

# END UTILS

# SOUND GENERATION

def generate_sin (num_samples, sample_rate, frequency_Hz, amplitude=1.0, phase_shift=0):
	x = np.arange(num_samples).astype(np.float32)
	y = float(amplitude)*np.sin(2*np.pi*frequency_Hz*x/sample_rate + phase_shift)
	return y

def generate_simple_harmony (notes, num_samples, sample_rate, total_amplitude=1.0, phase_shift=0):
	waves = []
	for note in notes:
		waves.append(generate_sin(num_samples, sample_rate, note_to_freq[note], amplitude=float(total_amplitude)/(len(notes)), phase_shift=phase_shift))
	return sum(waves)

# END SOUND GENERATION





if __name__ == '__main__':
	c4 = generate_sin(48000, 48000, note_to_freq['C4'])
	c5 = generate_sin(48000, 48000, note_to_freq['C5'])
	d5 = generate_sin(48000, 48000, note_to_freq['D5'])
	g5 = generate_sin(48000, 48000, note_to_freq['G5'])
	y = np.concatenate((c4, c5, d5, g5, c4))
	wavfile.write('melody.wav', 48000, y)
	sr0, y0 = wavfile.read('rachel.wav')
	sr1, y1 = wavfile.read('../ir_3_L_7.wav')
	y = convolve(y0, sr0, y1, sr1)
	wavfile.write('rachel_reverb.wav', sr0, y)
