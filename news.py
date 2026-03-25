from cat import tool
import feedparser


def print_news(category):
    category_url = "https://www.rainews.it/rss/" + category.replace(" ", "")
    d = feedparser.parse(category_url)
    news_list = []
    for i in range(3):
        news = d["entries"][i]
        news_list.append({
            "Category": category,
            "Title": news["title"],
            "Summary": news["summary"],
            "Link": news["links"][0]["href"],
            "Published": news["published"]
        })
    return news_list


@tool(examples=[
    "politica, economia",
    "politica, economia, sport",
    "economia, sport, cronaca",
    "sport, cronaca, salute",
    "cronaca, salute, arte e spettacolo",
    "salute, arte e spettacolo, societa",
    "arte e spettacolo, societa, esteri",
    "societa, esteri, economia",
    "esteri, economia, inchieste",
    "economia, inchieste, spettacolo",
    "inchieste, spettacolo, politica"
])
def latest_news(topics, cat):
    """
    Fetches the latest news based on specified topics and category.

    This function retrieves news by comparing user-specified topics with predefined categories. If all provided topics
    match the categories, it returns news for  those topics. Otherwise, it defaults to fetching news for all available
    categories.
    """
    categories = [
            "politica",
            "economia e finanza",
            "scienza e tecnologia",
            "viaggi e turismo",
            "sport",
            "cronaca",
            "stili di vita e tempo libero",
            "salute",
            "arti e spettacolo",
            "societa",
            "esteri",
            "economia",
            "inchieste",
            "spettacolo",
        ]
    news=[]

    topics = topics.split(",")

    if all(topic in categories for topic in topics):
        for topic in topics:
            news.append(print_news(topic))
    else:
        for category in categories:
            news.append(print_news(category))

    return news