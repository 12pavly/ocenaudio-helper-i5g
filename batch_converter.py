import os
import sys
import argparse
from pydub import AudioSegment

def convert_to_mp3(input_file, output_file, bitrate):
    """Convert an audio file to MP3 format with a specified bitrate."""
    try:
        audio = AudioSegment.from_file(input_file)
        # Convert bitrate string like "192k" to just "192k" format pydub expects
        audio.export(output_file, format="mp3", bitrate=bitrate)
        print(f"Converted '{input_file}' to '{output_file}' at {bitrate} bitrate.")
    except Exception as e:
        print(f"Error converting '{input_file}': {e}")

def batch_convert(input_dir, output_dir, bitrate):
    """Batch convert all audio files in the input directory to MP3 format."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.wav', '.flac', '.ogg', '.m4a')):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.mp3")
            convert_to_mp3(input_file, output_file, bitrate)
        else:
            print(f"Skipped non-audio file: '{filename}'")

def main():
    """Main function to handle argument parsing and batch conversion."""
    parser = argparse.ArgumentParser(description="Batch convert audio files to MP3 format.")
    parser.add_argument("input_dir", help="Directory containing audio files to convert.")
    parser.add_argument("output_dir", help="Directory to save converted MP3 files.")
    parser.add_argument("--bitrate", default="192k", help="Bitrate for the converted MP3 files (default: 192k).")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.input_dir):
        print(f"Input directory '{args.input_dir}' does not exist.")
        sys.exit(1)

    batch_convert(args.input_dir, args.output_dir, args.bitrate)

if __name__ == "__main__":
    main()

# TODO: Add support for more input file types.
# TODO: Implement a user-friendly GUI for easier usage.
# TODO: Add logging instead of print statements for better traceability.
