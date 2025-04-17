import speech_recognition as sr
from pydub import AudioSegment
import os
from transformers import pipeline
import torch
from tqdm import tqdm

class AudioSummarizer:
    def __init__(self):
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        
        # Initialize summarization pipeline
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        
    def convert_audio_to_text(self, audio_path):
        """Convert audio file to text using speech recognition."""
        try:
            # Load audio file
            if audio_path.endswith('.mp3'):
                audio = AudioSegment.from_mp3(audio_path)
                # Convert to wav for speech recognition
                wav_path = audio_path.replace('.mp3', '.wav')
                audio.export(wav_path, format="wav")
                audio_path = wav_path
            
            # Initialize text variable
            full_text = ""
            
            # Load audio file
            with sr.AudioFile(audio_path) as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source)
                
                # Get audio duration
                audio_duration = source.DURATION
                
                # Process audio in chunks (30 seconds each)
                chunk_duration = 30
                num_chunks = int(audio_duration / chunk_duration) + 1
                
                print(f"Processing audio in {num_chunks} chunks...")
                
                # Process each chunk
                for i in tqdm(range(num_chunks)):
                    # Record audio chunk
                    audio_chunk = self.recognizer.record(source, duration=min(chunk_duration, audio_duration - i * chunk_duration))
                    
                    try:
                        # Convert speech to text
                        text = self.recognizer.recognize_google(audio_chunk)
                        full_text += text + " "
                    except sr.UnknownValueError:
                        print(f"Could not understand audio in chunk {i+1}")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
            
            # Clean up temporary wav file if it was created
            if audio_path.endswith('.wav') and os.path.exists(audio_path):
                os.remove(audio_path)
            
            return full_text.strip()
            
        except Exception as e:
            print(f"Error processing audio: {str(e)}")
            return None

    def generate_summary(self, text, max_length=130, min_length=30):
        """Generate a summary from the text."""
        try:
            # Split text into chunks if it's too long (BART has a max input length)
            max_chunk_length = 1024
            chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
            
            summaries = []
            for chunk in chunks:
                # Generate summary for each chunk
                summary = self.summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
                summaries.append(summary[0]['summary_text'])
            
            # Combine summaries
            final_summary = " ".join(summaries)
            return final_summary
            
        except Exception as e:
            print(f"Error generating summary: {str(e)}")
            return None

def main():
    summarizer = AudioSummarizer()
    
    print("Audio Summarizer")
    print("===============")
    print("This program converts audio to text and generates a summary.")
    
    while True:
        print("\nOptions:")
        print("1. Process audio file")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == '1':
            audio_path = input("\nEnter the path to your audio file (MP3 or WAV): ").strip()
            
            if not os.path.exists(audio_path):
                print("Error: File does not exist.")
                continue
            
            print("\nConverting audio to text...")
            text = summarizer.convert_audio_to_text(audio_path)
            
            if text:
                print("\nTranscribed Text:")
                print("-----------------")
                print(text)
                
                print("\nGenerating summary...")
                summary = summarizer.generate_summary(text)
                
                if summary:
                    print("\nSummary:")
                    print("--------")
                    print(summary)
                    
                    # Save summary to file
                    output_file = os.path.splitext(audio_path)[0] + "_summary.txt"
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(summary)
                    print(f"\nSummary saved to: {output_file}")
            
        elif choice == '2':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 