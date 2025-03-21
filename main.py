import os
import sys
import whisper
import time
import pydub
import pandas as pd

# Usage: python main.py <path_to_audio_file> <path_to_output_folder>

AUDIO_FILE_PATH = sys.argv[1]
OUTPUT_FOLDER_PATH = sys.argv[2]
MODEL = "large" # "tiny", "base", "small", "medium", "large"

print(f"Checking file and folder...")

# Check if the file exists
if not os.path.isfile(AUDIO_FILE_PATH):
    print(f"File {AUDIO_FILE_PATH} does not exist.")
    sys.exit(1)

# check wav file
if os.path.splitext(AUDIO_FILE_PATH)[1] != ".wav":
    print(f"File {AUDIO_FILE_PATH} is not a wav file.")
    sys.exit(1)

# check folder exists
if not os.path.isdir(OUTPUT_FOLDER_PATH):
    print(f"Folder {OUTPUT_FOLDER_PATH} does not exist.")
    sys.exit(1)

print("Completed checking file and folder.")
print("Processing...")

model = whisper.load_model(MODEL)

start_time = time.time()

try:
    result = model.transcribe(AUDIO_FILE_PATH)
    print("Transcription completed.")
    print(f"Transcription time: {time.time() - start_time} seconds")
    print(result["text"])

    segments = result["segments"]

    for segment in segments:
        start = segment["start"] * 1000 # convert to milliseconds
        end = segment["end"] * 1000
        text = segment["text"]

        segment_audio = pydub.AudioSegment.from_wav(AUDIO_FILE_PATH)[start:end]
        output_path = os.path.join(OUTPUT_FOLDER_PATH, f"{start}_{end}_{text}.wav")
        segment_audio.export(output_path, format="wav")
        print(f"Exported segment: {output_path}")

    print("Exported all segments.")
    pd.DataFrame(segments).to_csv(os.path.join(OUTPUT_FOLDER_PATH, "segments.csv"), index=False)
    print("Exported segments to CSV.")

except Exception as e:
    print("An error occurred.")
    print(e)
    sys.exit(1)

