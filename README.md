# PyPMV
PyPMV is a Python script for generating YTPMV audio and visuals, all in one! 
# PyPMV-RosaFix
This fork aims to fix the librosa bug found in recent version of PyPMV, which makes the program unusable. 
This is due to librosa having a different way of doing the time_stretch() function in newer versions, meaning running the old time_stretch() logic would break the script.
# Requirements
- Python
# Usage
- Download this repository.
- Run ```pip install -r requirements.txt``` to install the requirements.
- Run ```python main.py -h``` for help.
```
usage: PyPMV [-h] -m MIDI -c CLIP [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -m MIDI, --midi MIDI  Path to the MIDI file
  -c CLIP, --clip CLIP  Path to the video clip file
  -o OUTPUT, --output OUTPUT
                        Path to the output video file
```
# Usage Examples
- ```python main.py -m "MIDIs\Test.mid" -c "Clips\Mr Beast.mp4" -o TestOutput.mp4```
- ```python main.p -m "MIDIs\Twinkle Twinkle Little Star.mid" -c "Clips\Mr Beast.mp4"```
# YouTube Video
[<img src="https://img.youtube.com/vi/KvH-a5EOg7A/maxresdefault.jpg" width="500px" alt="PyPMV - a Python script for generating YTPMV audio and visuals">](https://youtu.be/KvH-a5EOg7A)
