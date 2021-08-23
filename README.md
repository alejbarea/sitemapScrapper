# SitemapScrapper by punlover

By using this webscrapper implemented with BeautifulSoup in Python, you can obtain a huge database of prices and names of products of a website

## Setting Up 🚀

Follow this instructions carefully :)

### Requirements 📋

Install the libraries included in the requirements.txt file:

```
pip install -r requirements.txt
```

### Use 🔧

Firstly, you must add XML files obtained from the sitemap (sometimes you can find it in the robots.txt of a webpage) to a folder called Sitemaps
in the same directory as the script.

Then you can run it by:

```
python sitemapScrapper.py [-h] --name_class NAME_CLASS [NAME_CLASS ...] --price_class PRICE_CLASS [PRICE_CLASS ...]
                          [--overwrite] [--errorMode] [--delay DELAY] [--sep SEP]
```
* **NAME_CLASS:** The class tag of the name of the product (it can be a list)
* **PRICE_CLASS:** The class tag of the price of the product (it can be a list)
* **--overwrite:** Add this if you want to start from the beginning.
* **--errorMode:** This logs to a errors.txt file everything that goes wrong.
* **--delay:** The delay between requests (in order not to lag the requested server, DO NOT USE THIS TOOL TO LAG OR DDOS WEBPAGES)
* **--sep:** The separator between columns in data.csv (the output file)

Enjoy, we will keep updating our project and adding more features!




## Authors ✒️

* **Alejandro Barea Moreno - punlover** - *Trabajo Inicial* - [villanuevand](https://github.com/punlover)

## Licence 📄

This project is under the license: GNU GENERAL PUBLIC LICENSE - read more in [LICENSE.md](LICENSE.md)

## Thanks to 🎁

* My friend Adriano, who helped start this project - [Adriano Ruiz Barbero](https://github.com/aruiz-ba)
* My friend Abel, who gave me the idea ;)


