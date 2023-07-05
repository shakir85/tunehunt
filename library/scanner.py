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


def fetch_audio_files(directory: Path):
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

            data = {
                'data': {
                    artist_dir.name: {
                        album_dir.name: tracks
                    }
                }
            }
            yield data


def assemble_crate():
    pass


from jinja2 import Template
with open('../template.jinja') as file:
    template = Template(file.read())

for i in fetch_audio_files(pathlib.Path('../testing')):
    output = template.render(i)
    print(output)
