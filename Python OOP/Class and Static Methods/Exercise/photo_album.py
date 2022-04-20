from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for slot in self.photos:
            if len(slot) < 4:
                slot.append(label)
                return f"{label} photo added successfully on page {self.photos.index(slot) + 1} slot {len(slot)}"
        return "No more free slots"

    def display(self):
        result = ''
        total_photos = sum([len(x) for x in self.photos])

        for page in range(self.pages):
            result += 11 * '-' + '\n'

            for photo in range(1, 5):
                if total_photos == 0:
                    break
                if photo < 4:
                    result += '[] '
                else:
                    result += '[]'
                total_photos -= 1

            result += '\n'

        result += 11 * '-'

        return result.strip()


# Test code:

album = PhotoAlbum(1)
album.add_photo("baby")
album.add_photo("first grade")
album.add_photo("eight grade")
album.add_photo("party with friends")

print(album.display())
