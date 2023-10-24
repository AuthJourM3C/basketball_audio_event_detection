import os

class Config:
    def __init__(self, nn='cnn', nfft=2048, hop=512, sr=44100, win_size = 44, win_hop = 22):
        
        self.nn = nn
        self.nfft = nfft
        self.hop = hop
        self.sr = sr
        self.win_size = win_size
        self.win_hop = win_hop