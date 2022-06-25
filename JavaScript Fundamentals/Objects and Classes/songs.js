function solve(arr) {

    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    let numberOfSongs = Number(arr.shift());
    let type = arr[arr.length - 1];
    let songs = [];

    for (let index = 0; index < arr.length - 1; index++) {
        let tokens = arr[index].split('_');
        songs.push(new Song(tokens[0], tokens[1], tokens[2]));
    }

    for (let song of songs) {
        if (type == 'all') console.log(song.name);
        else {
            if (type == song.typeList) console.log(song.name);
        }
    }
}
