from bs4 import BeautifulSoup as bs


def file_splitter(html):
    split_articles = []
    with open(html, 'r') as htmlfile:
        soup = bs(htmlfile, 'lxml')
        articles = soup.find_all('article')
        for tag in articles:
            split_articles.append(tag.decode_contents())
    return split_articles


def main():
    html_file = 'dummy.html'
    split = file_splitter(html_file)

    for num, item in enumerate(split):
        with open(f"reddit_savedpost_{num:03d}.html", 'w') as splitfile:
            splitfile.write(item)


if __name__ == "__main__":
    main()
