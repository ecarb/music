
import numpy as np

def convolve (signal, signal_sample_rate, kernel, kernel_sample_rate):
    assert signal_sample_rate == kernel_sample_rate

    if signal.shape[0] > kernel.shape[0]:
        padding = np.zeros(signal.shape[0] - kernel.shape[0])
        new_kernel = np.concatenate((kernel, padding))
        new_signal = signal
    else:
        padding = np.zeros(kernel.shape[0] - signal.shape[0])
        new_signal = np.concatenate((signal, padding))
        new_kernel = kernel

    reverb = np.real(np.fft.ifft( np.fft.fft(new_signal)*np.fft.fft(new_kernel) ))
    return reverb / max(reverb)
