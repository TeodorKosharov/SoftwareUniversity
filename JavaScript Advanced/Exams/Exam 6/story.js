class Story {
    constructor(title, creator) {
        this.title = title;
        this.creator = creator;
        this._comments = [];
        this._likes = [];
        this.commentId = 1;
    }

    get likes() {
        if (this._likes.length === 0) return `${this.title} has 0 likes`;
        if (this._likes.length === 1) return `${this._likes[0]} likes this story!`;
        return `${this._likes[0]} and ${this._likes.length - 1} others like this story!`;
    }

    like(username) {
        if (this._likes.includes(username)) throw Error('You can\'t like the same story twice!');
        if (this.creator === username) throw Error('You can\'t like your own story!');
        this._likes.push(username);
        return `${username} liked ${this.title}!`;
    }

    dislike(username) {
        if (this._likes.includes(username)) {
            this._likes.splice(this._likes.indexOf(username), 1);
            return `${username} disliked ${this.title}`;
        }
        throw Error('You can\'t dislike this story!');
    }

    comment(username, content, id) {
        if (id === undefined || !this._comments.map(x => x.id).includes(id)) {
            this._comments.push({
                id: this.commentId, username, content, replies: []
            });
            this.commentId++;
            return `${username} commented on ${this.title}`;
        }

        const selectedComment = this._comments.filter(x => x.id === id)[0];
        selectedComment.replies.push({
            id: `${id}.${selectedComment.replies.length + 1}`, username, content
        });
        return 'You replied successfully';
    }

    toString(sortingType) {
        if (sortingType === 'asc') {
            this._comments.sort((a, b) => a.id - b.id);
            for (const comment of this._comments) {
                comment.replies.sort((a, b) => a.id - b.id);
            }
        } else if (sortingType === 'desc') {
            this._comments.sort((a, b) => b.id - a.id);
            for (const comment of this._comments) {
                comment.replies.sort((a, b) => b.id - a.id);
            }
        } else {
            this._comments.sort((a, b) => a.username.localeCompare(b.username));
            for (const comment of this._comments) {
                comment.replies.sort((a, b) => a.username.localeCompare(b.username));
            }
        }

        let result = `Title: ${this.title}\nCreator: ${this.creator}\nLikes: ${this._likes.length}\nComments:`;
        if (this._comments.length > 0) {
            for (const comment of this._comments) {
                result += `\n-- ${comment.id}. ${comment.username}: ${comment.content}`;
                if (comment.replies.length > 0) {
                    for (const reply of comment.replies) {
                        result += `\n--- ${reply.id}. ${reply.username}: ${reply.content}`;
                    }
                }
            }
        }
        return result;
    }

}
