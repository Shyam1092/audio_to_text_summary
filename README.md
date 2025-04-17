# Audio Summarizer

A Python tool that converts audio files to text and generates concise summaries using speech recognition and natural language processing.

## Features

- Converts audio files (MP3 or WAV) to text using Google Speech Recognition
- Processes long audio files in chunks for better accuracy
- Generates summaries using the BART-large-CNN model
- Supports both MP3 and WAV audio formats
- Saves summaries to text files automatically
- Interactive command-line interface

## Requirements

- Python 3.10
- SpeechRecognition
- pydub
- transformers
- torch
- tqdm

## Installation

1. Clone this repository:
```bash
git clone <https://github.com/Shyam1092/audio_to_text_summary>
cd <audio_summarizer.py>
```

2. Install the required packages:
```bash
pip install SpeechRecognition pydub transformers torch tqdm
```

3. Install FFmpeg (required for audio processing):
- Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html)
- Linux: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`

## Usage

1. Run the script:
```bash
python audio_summarizer.py
```

2. Choose from the available options:
   - Option 1: Process audio file
   - Option 2: Exit

3. When processing an audio file:
   - Enter the path to your audio file (MP3 or WAV)
   - Wait for the conversion and summarization process
   - View the transcribed text and summary in the console
   - Find the saved summary in a text file with "_summary" suffix

## How It Works

1. **Audio to Text Conversion**:
   - Converts MP3 files to WAV format if necessary
   - Processes audio in 30-second chunks
   - Uses Google Speech Recognition API for transcription
   - Handles ambient noise adjustment

2. **Text Summarization**:
   - Splits long texts into manageable chunks
   - Uses BART-large-CNN model for summarization
   - Combines summaries from multiple chunks
   - Generates concise summaries with configurable length

## Output

The program generates two types of output:
1. Console output showing:
   - Transcribed text
   - Generated summary
2. A text file containing the summary (saved as `[original_filename]_summary.txt`)

## Error Handling

The program includes error handling for:
- File not found errors
- Audio processing errors
- Speech recognition errors
- Summarization errors

## Links
- GitHub: [GitHub Repository](<https://github.com/Shyam1092>)
- LinkedIn: [LinkedIn Profile](<https://www.linkedin.com/in/shyam-padhiyar-90a955189?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app>)

Thanks for using the Audio Summarizer!
