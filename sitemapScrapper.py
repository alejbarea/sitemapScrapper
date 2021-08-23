import os
from bs4 import BeautifulSoup
import argparse
import lxml
import sys
from urllib.request import urlopen, Request
import time

class CumException(Exception):
    def __str__(self):
        return "There has been an error at the parsing process, don't play around."
def main(price_class,name_class,option,delay,sep,errorMode):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    try:
        lista_xmls = os.listdir("Sitemaps/")
    except:
        print("You have to add your XML files to a folder called 'Sitemaps' in the current directory :)")
        sys.exit()



    if option:
        with open("data.csv","w") as data:
            data.write("Link{}Name{}Price".format(sep,sep))
        i = 0
        j = 0
        k = 0
        l = 0
    elif option == False:
        if "register.txt" in os.listdir():
            with open("register.txt","r") as reg:
                i = int(reg.readline())
                j = int(reg.readline())
                k = int(reg.readline())
                l = int(reg.readline())
    else:
        raise CumException


    for xml in lista_xmls[(k + l):]:

        with open("Sitemaps/" + xml,"r",encoding="utf-8") as my_xml:
            try:
                my_xml_text = my_xml.read()
            except:
                l = l + 1

                continue
        soup = BeautifulSoup(my_xml_text, "lxml")

        elem = soup.find_all("loc")[i + j]

        print("Welcome to Sitemap Scrapper by punlover, Sit back and relax ;)")

        while elem:
            time.sleep(delay)
            elem = elem.find_next("loc")
            if elem:
                link = elem.text
                try:
                    req = Request(url=link, headers=headers)
                    html_text = urlopen(req).read()
                except:
                    j = j + 1
                    with open("register.txt","w") as reg:
                        reg.write(str(i)+"\n")
                        reg.write(str(j)+"\n")
                        reg.write(str(k)+"\n")
                        reg.write(str(l)+"\n")
                    print("Valid Downloads: {}".format(str(i)))
                    print("Not Valid Downloads: {}".format(str(j)))
                    if errorMode:
                        with open("errors.txt","a") as errors:
                            errors.write("\n"+link+"cannot access webpage")
                    continue

                elem_soup = BeautifulSoup(html_text,"html.parser")
                price = []
                name = []

                for m in price_class:
                    prices_found = elem_soup.find_all(class_=m)
                    for p in prices_found:
                        price.append(p)
                for m in name_class:
                    names_found = elem_soup.find_all(class_=m)
                    for n in names_found:
                        name.append(n)


                if (not price) or (not name):
                    j = j + 1
                    with open("register.txt","w") as reg:
                        reg.write(str(i)+"\n")
                        reg.write(str(j)+"\n")
                        reg.write(str(k)+"\n")
                        reg.write(str(l)+"\n")
                    print("Valid Downloads: {}".format(str(i)))
                    print("Not Valid Downloads: {}".format(str(j)))
                    if errorMode:
                        with open("errors.txt","a") as errors:
                            errors.write("\n"+link+" cannot find tag")
                    continue

                price = price[0].text
                name = name[0].text


                with open("data.csv","a",encoding="utf-8") as data:
                    data.write("\n{}{}{}{}{}".format(link,sep,name,sep,price))
                with open("register.txt","w") as reg:
                    reg.write(str(i)+"\n")
                    reg.write(str(j)+"\n")
                    reg.write(str(k)+"\n")
                    reg.write(str(l)+"\n")
                print("Valid Downloads: {}".format(str(i)))
                print("Not Valid Downloads: {}".format(str(j)))
                i = i + 1



        i = 0
        j = 0
        k = k + 1
        print("Valid XML: {}".format(str(k)))
        print("Invalid XML: {}".format(str(l)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sitemap Scrapper by punlover")
    parser.add_argument("--name_class",required=True,dest="name_class",nargs="+")
    parser.add_argument("--price_class",required=True,dest="price_class",nargs="+")
    parser.add_argument("--overwrite",dest="option",default=False,action="store_true",help="Start from the beggining")
    parser.add_argument("--errorMode",dest="errorMode",action="store_true",default=False,help="Logs the errors in a file called errors.txt")
    parser.add_argument("--delay",dest="delay",default=0.06,help="Delay of the different requests",type=float)
    parser.add_argument("--sep",dest="sep",default=";",help="Separator for your csv")
    args = parser.parse_args()
    print(type(args.name_class))
    main(args.price_class,args.name_class,args.option,args.delay,args.sep,args.errorMode)
