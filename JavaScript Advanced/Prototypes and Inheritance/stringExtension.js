(function solve() {
    String.prototype.ensureStart = function (str) {
        if (this.startsWith(str)) return this.toString();
        return str + this.toString();
    };

    String.prototype.ensureEnd = function (str) {
        if (this.endsWith(str)) return this.toString();
        return this.toString() + str;
    };

    String.prototype.isEmpty = function () {
        return this.length === 0;
    };

    String.prototype.truncate = function (n) {
        if (n < 4) {
            return '.'.repeat(n);
        } else if (this.toString().length <= n) return this.toString();

        else if (this.toString().length > n && this.includes(' ')) {
            const splitted = this.toString().split(' ');
            for (let lastIndex = splitted.length - 1; lastIndex >= 0; lastIndex--) {
                if ((splitted.slice(0, lastIndex).join(' ') + '...').length <= n) {
                    return splitted.slice(0, lastIndex).join(' ') + '...';
                }
            }
        } else if (!(this.toString().includes(' '))) {
            return this.toString().slice(0, n - 3) + '...';
        }
    }

    String.format = function (str, ...params) {
        let counter = 0;

        for (let parameter of params) {
            str = str.replace(`{${counter}}`, parameter);
            counter++;
        }
        return str;
    }
})()
