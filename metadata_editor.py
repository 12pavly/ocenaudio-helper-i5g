import mutagen
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, ID3NoHeaderError, TIT2, TALB, TPE1, TCON, TRCK, TDRC
import os

class MetadataEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.audio = self.load_audio_file()

    def load_audio_file(self):
        """Load the audio file and return its metadata."""
        try:
            audio = MP3(self.file_path, ID3=ID3)
            # Handle files without ID3 tags
            if audio.tags is None:
                audio.add_tags()
            return audio
        except ID3NoHeaderError:
            # Create new ID3 header for files without one
            audio = MP3(self.file_path)
            audio.add_tags()
            return audio
        except (FileNotFoundError, mutagen.MutagenError) as e:
            print(f"Error loading file {self.file_path}: {e}")
            return None

    def set_title(self, title):
        """Set the title metadata."""
        if self.audio is None:
            print("No audio loaded, cannot set title.")
            return
        self.audio.tags.add(TIT2(encoding=3, text=title))
        print(f"Title set to '{title}'")

    def set_artist(self, artist):
        """Set the artist metadata."""
        if self.audio is None:
            print("No audio loaded, cannot set artist.")
            return
        self.audio.tags.add(TPE1(encoding=3, text=artist))
        print(f"Artist set to '{artist}'")

    def set_album(self, album):
        """Set the album metadata."""
        if self.audio is None:
            print("No audio loaded, cannot set album.")
            return
        self.audio.tags.add(TALB(encoding=3, text=album))
        print(f"Album set to '{album}'")

    def set_genre(self, genre):
        """Set the genre metadata."""
        if self.audio is None:
            print("No audio loaded, cannot set genre.")
            return
        self.audio.tags.add(TCON(encoding=3, text=genre))
        print(f"Genre set to '{genre}'")

    def set_track_number(self, track_number):
        """Set the track number metadata."""
        if self.audio is None:
            print("No audio loaded, cannot set track number.")
            return
        self.audio.tags.add(TRCK(encoding=3, text=str(track_number)))
        print(f"Track number set to '{track_number}'")

    def set_year(self, year):
        """Set the year metadata."""
        if self.audio is None:
            print("No audio loaded, cannot set year.")
            return
        self.audio.tags.add(TDRC(encoding=3, text=str(year)))
        print(f"Year set to '{year}'")

    def save(self):
        """Save the changes to the audio file."""
        if self.audio is None:
            print("No audio loaded, cannot save changes.")
            return
        try:
            self.audio.save()
            print(f"Metadata for '{self.file_path}' saved successfully.")
        except Exception as e:
            print(f"Error saving metadata: {e}")

# TODO: Add functionality to read existing metadata
# TODO: Implement batch processing for multiple files
# TODO: Add command line interface for easier usage

# Example usage:
# editor = MetadataEditor("example.mp3")
# editor.set_title("My Song")
# editor.set_artist("My Artist")
# editor.save()
