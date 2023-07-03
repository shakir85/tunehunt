import yaml
import uuid


class Inventory:
    def __init__(self):
        self.schema = {"artists": {}}

    def create_inventory(self, artist: str, album: str, tracks: list) -> None:
        self.schema["artists"][artist] = {
            "artist_id": self._generate_artist_id(artist_name=artist),
            "albums": {
                album: {
                    "album_id": self._generate_album_id(artist_name=artist,
                                                        album_name=album),
                    "tracks": tracks
                }
            }
        }
        inventory = yaml.dump(self.schema, sort_keys=False)
        # TODO: change path to the init directory: $HOME/.tunehunt/inventory.yaml
        with open('inventory.yaml', 'w') as file:
            file.write(inventory)

    def read_inventory(self):
        pass

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

