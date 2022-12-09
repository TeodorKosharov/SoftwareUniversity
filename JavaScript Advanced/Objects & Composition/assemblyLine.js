function createAssemblyLine() {
    return {
        hasClima(obj) {
            obj.temp = 21;
            obj.tempSettings = 21;
            obj.adjustTemp = () => {
                if (obj.temp < obj.tempSettings) obj.temp++;
                else if (obj.temp > obj.tempSettings) obj.temp--;
            }
        },

        hasAudio(obj) {
            obj.currentTrack = {
                name: null,
                artist: null
            }
            obj.nowPlaying = () => {
                this.currentTrack.name !== null && this.currentTrack.artist !== null ? console.log(`Now playing '${this.currentTrack.name}' by ${this.currentTrack.artist}`) : '';
            }
        },

        hasParktronic(obj) {
            obj.checkDistance = (distance) => {
                if (distance < 0.1) console.log("Beep! Beep! Beep!");
                else if (distance >= 0.1 && distance < 0.25) console.log("Beep! Beep!");
                else if (distance >= 0.25 && distance < 0.5) console.log("Beep!");
                else console.log('');
            }
        }
    }
}

const assemblyLine = createAssemblyLine();
const myCar = {
    make: 'Toyota',
    model: 'Avensis'
};

assemblyLine.hasClima(myCar);
console.log(myCar.temp);
myCar.tempSettings = 18;
myCar.adjustTemp();
console.log(myCar.temp);
