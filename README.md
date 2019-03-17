# SDR
Software Defined Radio (SDR) projects on the Hack RF One by Great Scott Gadgets

## Quadrature Phase Shift Keying
QPSK is a form of phase modulation technique, in which two information bits (combined as one symbol) are modulated at once, selecting one of the four possible carrier phase shift states (pi/4, 3pi/4, 5pi/4, 7pi/4 radians).
![QPSK equation](img/img4-qpsk-equation1.png)
Note that the the cosine and sine portions of the signal are out of phase from one another by 90 degrees or pi/2 radians, or quadrature. This signal can be presented as an in-phase and quadrature-phase, or I and Q. 
Sequence of events:

1. A splitter separates odd and even bits
2. Each bit is over-sampled at T_sym = 2 T_b
3. Even and odd bits are independently sent through rectangular pulse shaping filter . I(t) is multiplied by cos (2 pi f_c t) and Q(t) is multiplied by sin (2 pi f_c t).
4. I(t) and Q(t) and  are summed to create s(t).

In MatLab this is represented as follows:
```function [s,t,I,Q] = qpsk_mod(a,fc,OF)
%Modulate an incoming binary stream using conventional QPSK
%a - input binary data stream (0's and 1's) to modulate
%fc - carrier frequency in Hertz
%OF - oversampling factor (multiples of fc) - at least 4 is better
%s - QPSK modulated signal with carrier
%t - time base for the carrier modulated signal
%I - baseband I channel waveform (no carrier)
%Q - baseband Q channel waveform (no carrier)
L = 2*OF;%samples in each symbol (QPSK has 2 bits in each symbol)
ak = 2*a-1; %NRZ encoding 0-> -1, 1->+1
I = ak(1:2:end);Q = ak(2:2:end);%even and odd bit streams
I=repmat(I,1,L).'; Q=repmat(Q,1,L).';%even/odd streams at 1/2Tb baud
I = I(:).'; Q = Q(:).'; %serialize
fs = OF*fc; %sampling frequency
t=0:1/fs:(length(I)-1)/fs; %time base
iChannel = I.*cos(2*pi*fc*t);qChannel = -Q.*sin(2*pi*fc*t);
s = iChannel + qChannel; %QPSK modulated baseband signal
```
Within GRC, the PSK Modulator handles the processing above. 

### QPSK Transmitter (QT)
![QPSK transmitter](img/img1-qpsk_tx_uhd.png)

### QPSK Transmitter (WX)
![QPSK transmitter](img/img3-qpsk_wx.png)

## FM Receiver
![FM receiver](img/img2-fm_rx.png)
