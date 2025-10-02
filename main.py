import argparse
import os

import librosa
import pretty_midi
import soundfile as sf
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

parser = argparse.ArgumentParser(prog="PyPMV")
parser.add_argument("-m", "--midi", required=True, help="Path to the MIDI file")
parser.add_argument("-c", "--clip", required=True, help="Path to the video clip file")
parser.add_argument(
    "-o",
    "--output",
    required=False,
    help="Path to the output video file",
    default="output.mp4",
)
args = parser.parse_args()
midiFile = pretty_midi.PrettyMIDI(args.midi)
notes = []
for instrument in midiFile.instruments:
    for note in instrument.notes:
        notes.append(note)
clip1 = VideoFileClip(args.clip)
noteClips = []
count = 0
for note in notes:
    print(note)
    count += 1
    clip = clip1.speedx(clip1.duration / (note.end - note.start))
    audio = clip1.audio
    audio.to_audiofile("temp.wav")
    y, sr = librosa.load("temp.wav")
    y = librosa.effects.time_stretch(y, rate=clip1.duration / (note.end - note.start))
    y = librosa.effects.pitch_shift(
        y, sr=sr, n_steps=(note.pitch - 60), bins_per_octave=12
    )
    sf.write("temp2.wav", y, sr)
    audio = AudioFileClip("temp2.wav")
    clip = clip.set_audio(audio)
    clip = clip.set_start(note.start)
    noteClips.append(clip)
os.remove("temp.wav")
os.remove("temp2.wav")
combined = CompositeVideoClip(noteClips)
combined.write_videofile(args.output)
