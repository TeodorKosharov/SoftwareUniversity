from Exercise.Spoopify.project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name in [x.name for x in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            if [x for x in self.albums if x.name == album_name][0].published:
                return "Album has been published. It cannot be removed."
        except IndexError:
            return f"Album {album_name} is not found."

        self.albums = [x for x in self.albums if x.name != album_name]
        return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}" + "\n"

        for album in self.albums:
            result += f"{album.details()}" + "\n"

        return result
