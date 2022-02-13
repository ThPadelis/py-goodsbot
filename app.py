from src.pushNotification import sendNotification
from src.database import insertProduct
from src.webScrapper import scrapProduct


def main():
    product = scrapProduct()
    insertProduct(product)
    title = product["title"]
    text = product["description"] + "\n\n" + product["link"]
    sendNotification(title, text)


if __name__ == "__main__":
    main()
