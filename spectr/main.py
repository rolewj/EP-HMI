import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# note frequency
B_3    = 1975.50
A_DI_3 = 1864.60
A_3    = 1720.00
G_DI_3 = 1661.20
G_3    = 1568.00
F_DI_3 = 1480.00
F_3    = 1396.90
E_3    = 1318.50
D_DI_3 = 1244.50
D_3    = 1174.60
C_DI_3 = 1108.70
C_3    = 1046.50

B_2    = 987.75
A_DI_2 = 932.32
A_2    = 880.00
G_DI_2 = 830.60
G_2    = 784.00
F_DI_2 = 739.98
F_2    = 698.46
E_2    = 659.26
D_DI_2 = 622.26
D_2    = 587.32
C_DI_2 = 554.36
C_2    = 523.25

B_1    = 493.88
A_DI_1 = 466.16
A_1    = 440.00
G_DI_1 = 415.30
G_1    = 392.00
F_DI_1 = 369.99
F_1    = 349.23
E_1    = 329.63
D_DI_1 = 311.13
D_1    = 293.66
C_DI_1 = 277.18
C_1    = 261.63

B_M    = 246.96
A_DI_M = 233.08
A_M    = 220.00
G_DI_M = 207.00
G_M    = 196.00
F_DI_M = 185.00
F_M    = 174.62
E_M    = 164.81
D_DI_M = 155.56
D_M    = 147.83
C_DI_M = 138.59
C_M    = 130.82

B_B    = 123.48
A_DI_B = 116.54
A_B    = 110.00
G_DI_B = 103.80
G_B    = 98.00
F_DI_B = 92.50
F_B    = 87.31
E_B    = 82.41
D_DI_B = 77.78
D_B    = 73.91
C_DI_B = 69.30
C_B    = 65.41

amplitude = 0.1 # amplitude (within: +-1.0)
fs = 3000      # 3000 time samples per second

def nt(note_fs, time):
  timeSamples = np.arange(np.ceil(time * fs)) / fs
  return amplitude / note_fs * np.sin(2 * np.pi * note_fs * timeSamples)

# note duration
BT = 2
BT2 = BT / 2
BT4 = BT / 4
BT8 = BT / 8
BT16 = BT / 16
BT32 = BT / 32
BTX2 = BT * 2

# volume
A05 = 0.05
A1 = 0.1
A2 = 0.2
A5 = 0.5
A8 = 0.8

mus = np.concatenate((
# 1
  nt(D_2, BT8),    
  nt(A_2, BT8),    
  nt(G_2, BT8),   
# 2
  nt(A_2, BT4)       + nt(B_B, BT4) + nt(C_DI_M, BT4) + nt(F_M, BT4) + nt(G_B, BT4),     
  nt(D_2, BT8) + A8 * (nt(B_B, BT8) + nt(C_DI_M, BT8) + nt(F_M, BT8) + nt(G_B, BT8)),    
#   nt(A_2, BT8) + A5 * (nt(B_B, BT8) + nt(C_DI_M, BT8) + nt(F_M, BT8) + nt(G_B, BT8)),    
#   nt(G_2, BT8) + A2 * (nt(B_B, BT8) + nt(C_DI_M, BT8) + nt(F_M, BT8) + nt(G_B, BT8)),    
#   nt(A_2, BT4)       + nt(C_DI_M, BT4) + nt(E_M, BT4) + nt(F_M, BT4) + nt(A_DI_M, BT4),     
#   nt(D_2, BT8) + A8 * (nt(C_DI_M, BT8) + nt(E_M, BT8) + nt(F_M, BT8) + nt(A_DI_M, BT8)),    
#   nt(A_2, BT8) + A5 * (nt(C_DI_M, BT8) + nt(E_M, BT8) + nt(F_M, BT8) + nt(A_DI_M, BT8)),    
#   nt(G_2, BT8) + A2 * (nt(C_DI_M, BT8) + nt(E_M, BT8) + nt(F_M, BT8) + nt(A_DI_M, BT8)),   
# # 3
#   nt(C_1, BT4)       + nt(D_M, BT4) + nt(E_2, BT4) + nt(G_M, BT4),    
#   nt(F_2, BT4) + A5 * (nt(D_M, BT4) + nt(E_2, BT4) + nt(G_M, BT4)),    
#                        nt(C_M, BT4) + nt(G_2, BT4) + nt(C_1, BT4),    
#   nt(C_2, BT8) + A8 * (nt(C_M, BT8) + nt(G_2, BT8) + nt(C_1, BT8)),     
#   nt(D_2, BT8) + A5 * (nt(C_M, BT8) + nt(G_2, BT8) + nt(C_1, BT8)),    
#   nt(A_2, BT8) + A2 * (nt(C_M, BT8) + nt(G_2, BT8) + nt(C_1, BT8)),    
#   nt(G_2, BT8),   
# # 4
#   nt(A_2, BT4)       + nt(B_B, BT4) + nt(C_DI_M, BT4) + nt(F_M, BT4) + nt(G_B, BT4),    
#   nt(D_2, BT8) + A8 * (nt(B_B, BT8) + nt(C_DI_M, BT8) + nt(F_M, BT8) + nt(G_B, BT8)),    
#   nt(A_2, BT8) + A5 * (nt(B_B, BT8) + nt(C_DI_M, BT8) + nt(F_M, BT8) + nt(G_B, BT8)),    
#   nt(G_2, BT8) + A2 * (nt(B_B, BT8) + nt(C_DI_M, BT8) + nt(F_M, BT8) + nt(G_B, BT8)),    
#   nt(C_3, BT4)          + nt(C_DI_M, BT4) + nt(E_M, BT4) + nt(F_M, BT4) + nt(A_DI_M, BT4),    
#   nt(A_DI_2, BT4) + A5 * (nt(C_DI_M, BT4) + nt(E_M, BT4) + nt(F_M, BT4) + nt(A_DI_M, BT4)),  
# # 5
#   nt(A_2, BT8)       + nt(F_B, BT8) + nt(C_M, BT8) + nt(F_M, BT8),    
#   nt(E_3, BT8) + A8 * (nt(F_B, BT8) + nt(C_M, BT8) + nt(F_M, BT8)),    
#   nt(E_3, BT8) + A5 * (nt(F_B, BT8) + nt(C_M, BT8) + nt(F_M, BT8)),    
#   nt(F_3, BT8) + A2 * (nt(F_B, BT8) + nt(C_M, BT8) + nt(F_M, BT8)),    
#   nt(C_3, BT8)       + nt(C_1, BT8) + nt(F_1, BT8),    
#   nt(D_3, BT8) + A8 * (nt(C_1, BT8) + nt(F_1, BT8)),    
#   nt(C_3, BT8) + A5 * (nt(C_1, BT8) + nt(F_1, BT8)),    
#   nt(D_2, BT8) + A2 * (nt(C_1, BT8) + nt(F_1, BT8)),    
#   nt(A_2, BT8),    
#   nt(A_DI_2, BT8),
#   # 6
#   nt(A_2, BT4)       + nt(B_B, BT4) + nt(C_DI_M, BT4) + nt(F_M, BT4) + nt(G_B, BT4),    
#   nt(C_3, BT4) + A5 * (nt(B_B, BT4) + nt(C_DI_M, BT4) + nt(F_M, BT4) + nt(G_B, BT4)),    
#   nt(A_2, BT4)       + nt(C_DI_M, BT4) + nt(E_M, BT4) + nt(F_M, BT4) + nt(A_DI_M, BT4),    
#   nt(G_2, BT4) + A5 * (nt(C_DI_M, BT4) + nt(E_M, BT4) + nt(F_M, BT4) + nt(A_DI_M, BT4)),  
# # 7
#   nt(E_2, BT4) + nt(D_M, BT4) + nt(A_M, BT4) + nt(C_1, BT4),    
#   nt(F_2, BT4) + nt(C_M, BT4) + nt(F_M, BT4) + nt(A_M, BT4),    
#   nt(A_2, BT4) + nt(F_B, BT4) + nt(C_M, BT4),    
#   nt(D_2, BT8)       + nt(B_B, BT8) + nt(D_M, BT8) + nt(F_M, BT8) + nt(A_M, BT8),    
#   nt(A_2, BT8) + A5 * (nt(B_B, BT8) + nt(D_M, BT8) + nt(F_M, BT8) + nt(A_M, BT8)),    
#   nt(G_2, BT8),  
# # 8
#   nt(A_2, BT4)       + nt(A_DI_B, BT4) + nt(D_M, BT4) + nt(F_M, BT4) + nt(B_M, BT4),    
#   nt(D_2, BT8) + A8 * (nt(A_DI_B, BT8) + nt(D_M, BT8) + nt(F_M, BT8) + nt(B_M, BT8)),    
#   nt(A_2, BT8) + A5 * (nt(A_DI_B, BT8) + nt(D_M, BT8) + nt(F_M, BT8) + nt(B_M, BT8)),    
#   nt(G_2, BT8) + A2 * (nt(A_DI_B, BT8) + nt(D_M, BT8) + nt(F_M, BT8) + nt(B_M, BT8)),    
#   nt(F_2, BT4)          + nt(A_B, BT4) + nt(C_DI_M, BT4) + nt(E_M, BT4) + nt(A_M, BT4),    
#   nt(C_DI_2, BT4) + A5 * (nt(A_B, BT4) + nt(C_DI_M, BT4) + nt(E_M, BT4) + nt(A_M, BT4)),  
# # 9
#         nt(E_2, BT4) + nt(D_M, BT4) + nt(A_M, BT4) + nt(D_1, BT4),    
#   A8 * (nt(E_2, BT8) + nt(D_M, BT8) + nt(A_M, BT8) + nt(D_1, BT8)),
#   A5 * (nt(E_2, BT8) + nt(D_M, BT8) + nt(A_M, BT8) + nt(D_1, BT8)),
#   A2 * (nt(E_2, BT8) + nt(D_M, BT8) + nt(A_M, BT8) + nt(D_1, BT8)),
#   A1 * (nt(E_2, BT8) + nt(D_M, BT8) + nt(A_M, BT8) + nt(D_1, BT8)),
#   A05 * (nt(E_2, BT4) + nt(D_M, BT4) + nt(A_M, BT4) + nt(D_1, BT4))

), axis = 0)

mus = mus/mus.max()

n = 4500
f = [1, 2, 4, 8] 
A = [1, 3, 4, 2] 
t = np.linspace(0, 1, n, endpoint=True) 

# Fourier transform calculation
signalFFT = np.fft.fft(mus) 
signalFFTabs = 2*np.abs(signalFFT) / n

# Plotting
fig = plt.figure(figsize=(16, 5), dpi=100) 

# Graph: Signal in Time
plt.subplot(1, 2, 1) 
plt.title('Signal') 
plt.stem(t, mus, basefmt='C0') 
plt.xlim([0, t[len(t)-1]]) 
plt.xlabel('Time') 
plt. grid () 

# Graph: signal spectrum
plt.subplot(1, 2, 2) 
plt.title('Signal spectrum') 
plt.stem(signalFFTabs, basefmt='C0') 
plt.xlim([0, n//2-1]) 
plt.xlabel('Frequency') 
plt. grid () 
plt.tight_layout()
plt.show()
