import yaml
from pprint import pprint
import hashlib


class Inventory:
    def __init__(self):
        self.schema = {"artists": {}}

    def create_schema(self, artist: str, album: str, tracks: list) -> None:
        self.schema["artists"][artist] = {
            "artist_id": self._id_generator(f"{artist}"),
            "albums": {
                album: {
                    "album_id": self._id_generator(f"{artist}/{album}"),
                    "tracks": tracks
                }
            }
        }
        pprint(self.schema)
        inventory = yaml.dump(self.schema, sort_keys=False)
        # TODO: change path to the init directory: $HOME/.tunehunt/inventory.yaml
        with open('inventory.yaml', 'w') as file:
            file.write(inventory)

    @classmethod
    def _id_generator(cls, s: str) -> str:
        uid = hashlib.sha1(str.encode(s)).hexdigest()
        return uid

