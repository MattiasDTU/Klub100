"""
This is the part of the script that only includes the functions that are used in the main script.
"""

from pytubefix import YouTube
import os
from pydub import AudioSegment
from gtts import gTTS
import pandas as pd


def read_data(file_path : str) -> list[str]:
    """
    This function read the data in the Excel file and returns the URLS, start time
    end time and custom text.

    Args:
        file_path (str): Path to the Excel file. (MUST BE AN EXCEL FILE)
    """
    data = pd.read_excel(file_path, header=0)
    urls = []
    start_time = []
    end_time = []
    custom_text = []

    for i in range(len(data)):
        urls.append(data.iloc[i]["Youtube URL"])
        start_time.append(data.iloc[i]["Start Time"])
        end_time.append(data.iloc[i]["End Time"])
        custom_text.append(data.iloc[i]["Custom Text"])
    return urls, start_time, end_time, custom_text



def download_audio(youtube_url: str, output_file: str) -> str:
    """
    Downloads the audio from a YouTube video and saves it to the specified output file.

    Args:
        youtube_url (str): The URL of the YouTube video.
        output_file (str): The path to save the downloaded audio file.

    Returns:
        str: Path to the downloaded audio file.
    """
    try:
        output_path = os.path.dirname(output_file) or "."           # Creating output path
        os.makedirs(output_path, exist_ok=True)                     # Ensuring output path exists

        yt = YouTube(youtube_url)                                   # Creating YouTube object
        audio_stream = yt.streams.filter(only_audio=True).first()   # Filter for audio only
        
        downloaded_file = audio_stream.download(output_path)
        return downloaded_file
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def trim_audio(input_file: str, output_file: str, start_time: int, end_time: int) -> None:
    """
    Trims the audio file to the specified start and end times and saves the trimmed version.
    Deleates original file, leaving only the trimmed audio file.

    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the trimmed audio file.
        start_time (int): Start time in seconds.
        end_time (int): End time in seconds.
    """
    try:
        start_time *= 1000  # Convert to milliseconds
        end_time *= 1000    # Convert to milliseconds
        audio = AudioSegment.from_file(input_file)
        #-- Ensure start and end times are within the audio file length --#
        if end_time > len(audio):
            end_time = len(audio)
        if start_time > end_time:
            start_time = end_time - 100000
        
        trimmed_audio = audio[start_time:end_time]
        trimmed_audio.export(output_file, format="mp3")
        os.remove(input_file)
    except Exception as e:
        print(f"An error occurred while trimming the audio: {e}")



def text_to_speech(text: str, output_file: str) -> None:
    tts = gTTS(text, lang='en')
    tts.save(output_file)
    print(f"Audio saved as {output_file}")


def combine_audio_files(audio_files: list, output_file: str) -> None:
    """
    Combines multiple audio files into one.

    Args:
        audio_files (list): List of file paths to audio files.
        output_file (str): Path to save the combined audio file.
    """
    try:
        combined = AudioSegment.empty()
        
        for file in audio_files:
            try:
                audio = AudioSegment.from_file(file)
                combined += audio  # Append the audio file to the combined segment
                os.remove(file)    # Remove the original audio file
            except Exception as e:
                print(f"File doesn't exist: {e}")
        combined.export(output_file, format="mp3")
        
        print(f"Combined audio saved to: {output_file}")
    except Exception as e:
        print(f"An error occurred while combining audio files: {e}")
