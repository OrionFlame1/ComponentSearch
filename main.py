from bs4 import BeautifulSoup
import requests

term = input("Look for:") #global term, used and locally overwritten in every function

def Altex(): # request.get failure, policy matters suspected
    termcopy = term.replace(" ", "%2520")
    print(termcopy)
    termcopy = "https://altex.ro/cauta/?q=" + termcopy
    print(termcopy)
    page = requests.get(termcopy)
    print("request made")
    soup = BeautifulSoup(page.content, "html.parser")
    print("parsing")
    soup = soup.find("li", class_="Products-item")
    print("list item class found")
    titlu = soup.find("h2", class_="Product-nameHeading")
    print("title class found")
    pret = soup.find("div", class_="Price-current")
    print("price current class found")
    link = soup.find("a", class_="Product flex")
    print("product link found")
    print(f"Altex: {titlu.text} {link.get('href')}\n{pret}") # #

def eMag():
    termcopy = term.replace(" ", "%20")
    page = requests.get("https://www.emag.ro/search/" + termcopy + "?ref=effective_search")
    soup = BeautifulSoup(page.content, "html.parser")

    soup = soup.find("div", class_="card-v2")  # gtx 1050 -3
    titlu = soup.find("a", class_="card-v2-title")
    pret = soup.find("p", class_="product-new-price")
    pret = pret.text
    pret = pret[:len(pret) - 6] + "," + pret[-6:]
    link = soup.find("a", class_="card-v2-thumb")

    print(f"eMag: {titlu.text} {link.get('href')}\n{pret}")

def MediaGalaxy(): # request.get failure, policy matters suspected
    termcopy = term.replace(" ", "%2520")
    termcopy = "https://mediagalaxy.ro/cauta/?q=" + termcopy
    page = requests.get(termcopy)
    print(page.status_code)


eMag()

#Altex xx
#Flanco
#Media Galaxy
#eMag v
#pcGarage
