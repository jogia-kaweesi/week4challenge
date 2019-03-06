import requests
from clint.textui import puts, colored, indent
from pyfiglet import Figlet
f = Figlet(font='slant')
class NewsApi:
    def __init__(self, name):
        self.name = name
    def source(self, source):
        url =  "https://newsapi.org/v2/top-headlines?sources="+ source +"&apiKey=3ce9580385ea4c42a97d1e59537c2f00"
        print(colored.red(f.renderText(source) + "\tTop 10 headlines"))
        response = requests.get(url)
        json_object = response.json()
        articles = json_object['articles']
        headline = 0
        while headline<10:
          z = str(articles[headline]['source'])
          a = str(articles[headline]['author'])
          b = str(articles[headline]['title'])
          c = str(articles[headline]['description'])
          pub = str(articles[headline]['publishedAt'])
          q = str(articles[headline]['url'])
         #print(z +colored.green("\n Source:")+ a + colored.red("\n Title: ")+ a +colored.black("\n Author: ")+ c + colored.green("\n Description: ") + c + colored.red("\nFor more infor, click the link below:\n Url: ")+ q + colored.green("\n Date of publition: ")+ pub)
          print(colored.yellow("Source:")+ z + colored.green("\n Title: ")+ b +colored.red("\n Author: ")
            + a + colored.blue("\n Description: ") + c + colored.green("\nFor more information, click the link below:\n Url: ")+ q + colored.red("\n Published At: ")
             + pub)

        print("\n")
        headline+=1    
    def home(self):
        print(colored.red(f.renderText("OUR FAVOURITE NEW!")))
        print("Hi "+ self.name +" WELCOME TO OUR FAVOURITE NEWS SITE")
        sources = ["mtv-news", "Cnn", "abc-news", "bbc-sport"]
        items=1
        for source in sources:
            print(str(items)+":" + source)
            items+=1
        source = input("Enter source number:")
        source_int = int(source)
        if source_int == 1:
            self.source("mtv-news")
        elif source_int == 2:
            self.source("cnn")
        elif source_int == 3:
            self.source("abc-news")
        elif source_int == 4:
            self.source("bbc-sport")
        else:
            print("invalid Input")
newsReader = NewsApi("NAKAWEESI")
print(newsReader.home())