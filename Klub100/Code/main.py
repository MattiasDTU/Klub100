from functions import *


file_path = 'Data.xlsx' 
urls, start_time, end_time, custom_text = read_data(file_path)

for idx in range(len(urls)):
     #------------ Variables ------------#
    youtube_url = urls[idx] # URL of Youtube video
    start = start_time[idx] # start time in seconds
    end = end_time[idx]     # end time in seconds
    text = custom_text[idx] # custom text to be added to the audio
    #------------ Output files ------------#
    output_file = f"Code/MusicTest/audio_{idx}.mp3"
    tts_output_file = f"Code/MusicTest/tts_{idx}.mp3"
    combined_output_file = f"Code/MusicTest/combined_audio_{idx}.mp3"



    downloaded_file = download_audio(youtube_url, output_file)
    if downloaded_file:
        trim_audio(downloaded_file, output_file, start, end)
        text_to_speech(text, tts_output_file)
        combine_audio_files([output_file, tts_output_file], combined_output_file)
    else:
        print("Failed to download audio.")

combined_files = []
for idx in range(len(urls)):
    combined_files.append(f"Code/MusicTest/combined_audio_{idx}.mp3")
final_output_file = "Code/MusicTest/final_audio.mp3"
combine_audio_files(combined_files, final_output_file)