import yaml
import uuid
from pathlib import Path


class Inventory:
    def __init__(self):
        # TODO: change inventory path to the init directory: `$HOME/.tunehunt/inventory.yaml`
        self.inventory_file: Path = Path('../testing/inventory.yaml')
        self.schema: dict = {"artists": {}}
        self.data: dict = self._load_data()

    def create_inventory(self, artist: str, album: str, tracks: list) -> None:
        self.schema["artists"][artist] = {
            "artist_id": self._generate_artist_id(artist_name=artist),
            "albums": {
                album: {
                    "album_id": self._generate_album_id(artist_name=artist,
                                                        album_name=album),
                    "tracks": tracks
                },
            }
        }
        with open(self.inventory_file, 'w') as file:
            yaml.safe_dump(self.schema, file, sort_keys=False)

    def _load_data(self):
        try:
            with open(self.inventory_file, 'r') as file:
                return yaml.safe_load(file) or {}
        except FileNotFoundError:
            return {}

    def _save_data(self):
        with open(self.inventory_file, 'w') as file:
            yaml.safe_dump(self.data, file, sort_keys=False)

    def update_inventory(self):
        pass

    def delete_from_inventory(self):
        pass

    @classmethod
    def _generate_artist_id(cls, artist_name) -> str:
        namespace = uuid.NAMESPACE_DNS
        return str(uuid.uuid5(namespace, artist_name))

    @classmethod
    def _generate_album_id(cls, artist_name, album_name) -> str:
        namespace = uuid.NAMESPACE_DNS
        fqd = f"{artist_name}.{album_name}"
        return str(uuid.uuid5(namespace, fqd))

