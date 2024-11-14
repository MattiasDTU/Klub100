from functions import *
import random
"""
This is the main script, its here where you essentially run the whole program.

Args:
    file_path (str): Path to the Excel file. (MUST BE AN EXCEL FILE)
    output_path (str): Path to save the output files.
"""
output_path = "Code/MusicTest/"
file_path = 'Data.xlsx' 
urls, start_time, end_time, custom_text = read_data(file_path)
Random = True #Randomize the order of the audio


if Random:
    indices = list(range(len(urls)))
    random.shuffle(indices)
    urls = [urls[i] for i in indices]
    start_time = [start_time[i] for i in indices]
    end_time = [end_time[i] for i in indices]
    custom_text = [custom_text[i] for i in indices]

for idx in range(len(urls)):
     #------------ Variables ------------#
    youtube_url = urls[idx] # URL of Youtube video
    start = start_time[idx] # start time in seconds
    end = end_time[idx]     # end time in seconds
    text = custom_text[idx] # custom text to be added to the audio
    #------------ Output files ------------#
    output_file = f"{output_path}audio_{idx}.mp3"
    tts_output_file = f"{output_path}tts_{idx}.mp3"
    combined_output_file = f"{output_path}combined_audio_{idx}.mp3"



    downloaded_file = download_audio(youtube_url, output_file)
    if downloaded_file:
        trim_audio(downloaded_file, output_file, start, end)
        if text:
            text_to_speech(text, tts_output_file)
            combine_audio_files([output_file, tts_output_file], combined_output_file)
        else:
            combine_audio_files(output_file, combined_output_file)
    else:
        print("Failed to download audio.")

combined_files = []
for idx in range(len(urls)):
    combined_files.append(f"{output_path}combined_audio_{idx}.mp3")
final_output_file = f"{output_path}final_audio.mp3"
combine_audio_files(combined_files, final_output_file)
