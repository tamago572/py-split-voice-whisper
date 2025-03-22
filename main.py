import os
import sys
import whisper
import time
import pydub
import pandas as pd

# Usage: python main.py <path_to_audio_file> <path_to_output_folder>

AUDIO_FILE_PATH = sys.argv[1]
OUTPUT_FOLDER_PATH = sys.argv[2]
MODEL = sys.argv[3] # "tiny", "base", "small", "medium", "large"


def check_args(audio_file_path, output_folder_path, model):
    print(f"Checking file and folder...")

    # Check if the file exists
    if not os.path.isfile(audio_file_path):
        print(f"File {audio_file_path} does not exist.")
        sys.exit(1)

    # check wav file
    if os.path.splitext(audio_file_path)[1] != ".wav":
        print(f"File {audio_file_path} is not a wav file.")
        sys.exit(1)

    # check folder exists
    if not os.path.isdir(output_folder_path):
        print(f"Folder {output_folder_path} does not exist.")
        sys.exit(1)

    # check model
    if model not in ["tiny", "base", "small", "medium", "large"]:
        print(f"Model {model} is not valid.")
        sys.exit(1)
    print("Completed checking file and folder.")



def transcribe(model_str, audio_file_path, output_folder_path):
    print("Processing...")

    
    model = whisper.load_model(model_str)

    start_time = time.time()

    try:
        result = model.transcribe(audio_file_path)
        print("Transcription completed.")
        print(f"Transcription time: {time.time() - start_time} seconds")
        print(result["text"])

        segments = result["segments"]

        for segment in segments:
            start = segment["start"] * 1000 # convert to milliseconds
            end = segment["end"] * 1000
            text = segment["text"]

            segment_audio = pydub.AudioSegment.from_wav(audio_file_path)[start:end]
            output_path = os.path.join(output_folder_path, f"{start}_{end}_{text}.wav")
            segment_audio.export(output_path, format="wav")
            print(f"Exported segment: {output_path}")

        print("Exported all segments.")
        pd.DataFrame(segments).to_csv(os.path.join(output_folder_path, "segments.csv"), index=False)
        print("Exported segments to CSV.")

    except Exception as e:
        print("An error occurred.")
        print(e)
        sys.exit(1)


check_args(AUDIO_FILE_PATH, OUTPUT_FOLDER_PATH, MODEL)
transcribe(MODEL, AUDIO_FILE_PATH, OUTPUT_FOLDER_PATH)
