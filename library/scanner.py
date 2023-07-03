import os
import pathlib
import magic
import ffmpeg
from pathlib import Path
from inventory import crud
obj = crud.Inventory()


def is_audio_file(file_path: Path) -> bool:
    try:
        probe = ffmpeg.probe(file_path)
        audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']
        return len(audio_streams) > 0
    except ffmpeg.Error as e:
        mime_type = magic.from_file(file_path, mime=True)
        return mime_type.startswith('audio/')


def assemble_audio_files(directory: Path):
    directory_path = Path(directory)

    # Iterate over the artist directories
    for artist_dir in directory_path.iterdir():
        if not artist_dir.is_dir():
            continue

        # Iterate over the album directories within the artist directory
        for album_dir in artist_dir.iterdir():
            if not album_dir.is_dir():
                continue

            tracks = []

            # Iterate over the track files within the album directory
            for track_file in album_dir.iterdir():
                if not track_file.is_file():
                    continue
                if is_audio_file(track_file):
                    tracks.append(track_file.name)

            yield artist_dir.name, album_dir.name, tracks


music_library = {}
for artist, album, tracks in assemble_audio_files(pathlib.Path('../testing')):
    obj.create_inventory(artist, album, tracks)
    # artist_data = music_library.setdefault(artist, {})
    # artist_data[album] = tracks


