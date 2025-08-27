# PyPMV
PyPMV is a Python script for generating YTPMV audio and visuals, all in one!
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
