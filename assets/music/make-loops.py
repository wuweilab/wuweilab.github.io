"""Create 75-second music-only editions; preserve source metadata and originals."""
import sys, subprocess
from pathlib import Path
import numpy as np
sys.path.insert(0,'D:/Codex/outputs/audio-runtime')
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe(); root=Path(__file__).parent; sr=44100
# End before the appended speech/tone segment. Short crossfades join music excerpts.
clips=[('study-lofi.mp3',.2,37),('study-ambient.mp3',.5,30),('study-jazz.mp3',.7,22),('study-rain.mp3',.4,58),('sunny-day.wav',4*60/112,64*60/112)]
for name,start,end in clips:
    src=root/name
    raw=subprocess.check_output([ff,'-v','error','-i',str(src),'-f','f32le','-ac','2','-ar',str(sr),'-'])
    a=np.frombuffer(raw,dtype='<f4').reshape(-1,2)[int(start*sr):int(end*sr)].copy()
    n=int(.15*sr); ramp=np.linspace(0,1,n)[:,None]; out=a.copy()
    while len(out)<75*sr:
        out[-n:]=out[-n:]*(1-ramp)+a[:n]*ramp
        out=np.concatenate((out,a[n:]))
    out=out[:75*sr]; edge=int(.03*sr)
    out[:edge]*=np.linspace(0,1,edge)[:,None];out[-edge:]*=np.linspace(1,0,edge)[:,None]
    out*=min(1,.94/float(np.max(np.abs(out))))
    dest=src.with_name(src.stem+'-loop.mp3')
    subprocess.run([ff,'-v','error','-y','-f','f32le','-ar',str(sr),'-ac','2','-i','pipe:0','-i',str(src),'-map','0:a','-map_metadata','1','-c:a','libmp3lame','-b:a','192k',str(dest)],input=out.astype('<f4').tobytes(),check=True)
    print(dest.name,'75.00 seconds, peak',round(float(np.max(np.abs(out))),3))
