"""Original deterministic upbeat instrumental, 112 BPM, C major, 16 bars."""
import wave
from pathlib import Path
import numpy as np
sr=44100; beat=60/112; duration=16*4*beat+2
mix=np.zeros((int(duration*sr),2)); rng=np.random.default_rng(24)
def add(at,s,amp=.2,pan=0):
    i=int(at*sr); n=min(len(s),len(mix)-i)
    mix[i:i+n,0]+=s[:n]*amp*np.sqrt((1-pan)/2)
    mix[i:i+n,1]+=s[:n]*amp*np.sqrt((1+pan)/2)
def note(at,midi,length,amp=.2,pan=0,bass=False):
    t=np.arange(int(length*sr))/sr; f=440*2**((midi-69)/12)
    env=(1-np.exp(-t*180))*np.exp(-t*(5 if not bass else 3))*np.minimum(1,(length-t)*50)
    s=sum(np.sin(2*np.pi*f*k*t)*np.exp(-t*k*.8)/(k*k) for k in range(1,5))*env
    add(at,s,amp,pan)
chords=[(48,[60,64,67]),(43,[59,62,67]),(45,[60,64,69]),(41,[60,65,69])]
melodies=[[76,79,81,79,76,74,72,74],[74,76,79,76,74,71,67,71],[72,76,81,79,76,74,72,76],[77,76,74,72,69,72,74,72]]
for bar in range(16):
    root,chord=chords[bar%4]; start=bar*4*beat
    for b in range(4):
        at=start+b*beat
        note(at,root+(12 if b%2 else 0),beat*.8,.34,bass=True)
        for j,m in enumerate(chord):note(at+beat*.5+j*.009,m,.32,.12,(j-1)*.35)
        t=np.arange(int(.19*sr))/sr
        kick=np.sin(2*np.pi*(48*t+35*.035*(1-np.exp(-t/.035))))*np.exp(-t*24)
        add(at,kick,.29)
        if b%2:
            noise=rng.normal(0,1,len(t)); add(at,noise*np.exp(-t*38)*.4+np.sin(2*np.pi*180*t)*np.exp(-t*35)*.25,.15)
        for off in [0,.5]:
            t=np.arange(int(.065*sr))/sr; noise=rng.normal(0,1,len(t)); noise=np.concatenate(([0],np.diff(noise)))
            add(at+off*beat,noise*np.exp(-t*80),.026,.45)
    if bar>=2:
        for j,m in enumerate(melodies[bar%4]):
            if j==7 and bar%2:continue
            at=start+j*.5*beat+(0.025 if j%2 else 0)
            note(at,m,.46,.23,-.12); note(at+.16,m,.38,.045,.45)
note(64*beat,72,1.8,.2)
mix*=np.minimum(1,np.arange(len(mix))/sr/.25)[:,None]
mix*=np.minimum(1,(len(mix)-np.arange(len(mix)))/sr/1.3)[:,None]
mix=np.tanh(mix*1.2); mix*=.88/max(.88,np.max(np.abs(mix)))
out=Path(__file__).with_name('sunny-day.wav')
with wave.open(str(out),'wb') as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((mix*32767).astype('<i2').tobytes())
print(f'{out.name}: {duration:.1f}s; peak {np.max(np.abs(mix)):.3f}')
