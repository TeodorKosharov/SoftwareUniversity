from Lab.Hotel_Rooms.project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [x for x in self.rooms if x.number == room_number][0]
        room.take_room(people)

    def free_room(self, room_number):
        room = [x for x in self.rooms if x.number == room_number][0]
        room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {sum(x.guests for x in self.rooms)} total guests\n"
        result += f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}\n"
        result += f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}\n"
        return result
