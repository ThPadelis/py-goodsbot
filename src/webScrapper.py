from datetime import datetime
import requests
from bs4 import BeautifulSoup


def scrapProduct():
    URL = "https://www.eshopspecials.gr/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    titleOutterWrapper = soup.find("div", class_="featured-section")
    titleInnerWrapper = titleOutterWrapper.find("div", class_="featured-price")
    titleWrapper = titleInnerWrapper.find("div", class_="wrapper")
    title = titleWrapper.find("h2").text.title()

    descriptionWrapper = soup.find("div", class_="text-wrapper")
    description = descriptionWrapper.find("p").text

    fromPriceWrapper = soup.find("div", class_="ab-prices-block previous")
    fromPriceText = fromPriceWrapper.find("span", class_="ab-span-price-value")
    fromPrice = float(fromPriceText.text.replace("€", "").strip())

    toPriceWrapper = soup.find("div", class_="ab-prices-block current")
    toPriceText = toPriceWrapper.find("span", class_="ab-span-price-value")
    toPrice = float(toPriceText.text.replace("€", "").strip())

    imgWrapper = soup.find("div", class_="featured-img")
    imgElement = imgWrapper.find("img", class_="img-responsive")
    imgSrc = imgElement.get("src")

    productWrapper = soup.find("div", class_="featured-img")
    productElement = productWrapper.find("a")
    productLink = productElement.get("href")

    discount = round(((1 - toPrice / fromPrice) * 100), 2)

    product = {
        "title": title,
        "description": description,
        "link": productLink,
        "image": imgSrc,
        "listingPrice": fromPrice,
        "sellingPrice": toPrice,
        "discount": discount,
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }

    return product
