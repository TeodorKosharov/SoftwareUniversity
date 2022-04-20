from Exercise.Spoopify.project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.name in [x.name for x in self.songs]:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in [x.name for x in self.songs]:
            return "Song is not in the album."
        elif self.published:
            return "Cannot remove songs. Album is published."
        else:
            self.songs = [x for x in self.songs if x.name != song_name]
            return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}" + "\n"
        for song in self.songs:
            result += "== " + song.get_info() + "\n"

        return result
