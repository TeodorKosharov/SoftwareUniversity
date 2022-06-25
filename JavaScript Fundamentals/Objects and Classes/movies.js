function solve(arr) {
    let movies = [];

    class Movie {
        constructor(name, director, date) {
            this.name = name;
            this.director = director;
            this.date = date;
        }
    }

    for (let element of arr) {
        let tokens = element.split(' ');
        if (tokens[0] == 'addMovie') movies.push(new Movie(tokens.slice(1).join(' ')));
        else if (tokens.includes('directedBy') && movies.map(x => x.name).includes(tokens.slice(0, tokens.indexOf('directedBy')).join(' '))) {
            for (let index = 0; index < movies.length; index++) {
                if (movies[index].name == tokens.slice(0, tokens.indexOf('directedBy')).join(' ')) {
                    movies[index].director = tokens[2];
                    break;
                }
            }
        } else if (tokens.includes('onDate') && movies.map(x => x.name).includes(tokens.slice(0, tokens.indexOf('onDate')).join(' '))) {
            for (let index = 0; index < movies.length; index++) {
                if (movies[index].name == tokens.slice(0, tokens.indexOf('onDate')).join(' ')) {
                    movies[index].date = tokens[2];
                    break;
                }
            }
        }1
    }

    for (let movie of movies) {
        if (movie.name != undefined && movie.director != undefined && movie.date != undefined) console.log(JSON.stringify(movie));
    }
}
