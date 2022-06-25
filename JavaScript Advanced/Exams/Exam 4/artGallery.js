class ArtGallery {
    constructor(creator) {
        this.creator = creator;
        this.possibleArticles = {"picture": 200, "photo": 50, "item": 250};
        this.listOfArticles = [];
        this.guests = [];
    }

    addArticle(articleModel, articleName, quantity) {
        articleModel = articleModel.toLowerCase();
        if (this.possibleArticles[articleModel] === undefined) throw Error('This article model is not included in this gallery!');
        if (this.listOfArticles.map(x => x.articleName).includes(articleName)) {
            const selectedArticle = this.listOfArticles.filter(x => x.articleName === articleName)[0];
            if (selectedArticle.articleModel === articleModel) {
                selectedArticle.quantity += quantity;
            }
        } else {
            this.listOfArticles.push({
                articleModel, articleName, quantity
            });
        }
        return `Successfully added article ${articleName} with a new quantity- ${quantity}.`;
    }

    inviteGuest(guestName, personality) {
        if (this.guests.map(x => x.guestName).includes(guestName)) throw Error(`${guestName} has already been invited.`);
        let points;
        if (personality === 'Vip') points = 500; else if (personality === 'Middle') points = 250; else points = 50;
        this.guests.push({
            guestName, points, purchaseArticle: 0
        });
        return `You have successfully invited ${guestName}!`;

    }

    buyArticle(articleModel, articleName, guestName) {
        if (!(this.listOfArticles.map(x => x.articleName).includes(articleName))) throw Error('This article is not found.');
        const selectedArticle = this.listOfArticles.filter(x => x.articleName === articleName)[0];
        if (selectedArticle.articleModel !== articleModel) throw Error('This article is not found.');
        if (selectedArticle.quantity === 0) return `The ${articleName} is not available.`;
        if (!(this.guests.map(x => x.guestName).includes(guestName))) return 'This guest is not invited.';
        const selectedGuest = this.guests.filter(x => x.guestName === guestName)[0];
        const selectedArticleModel = selectedArticle.articleModel;
        const neededArticlePoints = this.possibleArticles[selectedArticleModel];
        if (neededArticlePoints > selectedGuest.points) return 'You need to more points to purchase the article.';
        selectedArticle.quantity--;
        selectedGuest.purchaseArticle++;
        selectedGuest.points -= neededArticlePoints;
        return `${guestName} successfully purchased the article worth ${neededArticlePoints} points.`;
    }

    showGalleryInfo(criteria) {
        if (criteria === 'article') {
            let result = 'Articles information:';
            this.listOfArticles.forEach(article => result += `\n${article.articleModel} - ${article.articleName} - ${article.quantity}`);
            return result;
        } else if (criteria === 'guest') {
            let result = 'Guests information:';
            this.guests.forEach(guest => result += `\n${guest.guestName} - ${guest.purchaseArticle}`);
            return result;
        }
    }

}
