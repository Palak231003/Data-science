from bs4 import BeautifulSoup

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return content

def extract_Watches(soup):
    Watches = []

    Watch_elements = soup.find_all(name="div", class_="Watch")

    for Watch in Watch_elements:
        Name = Watch.find("h2").text
        Model = Watch.find("h2").text
        Price = Watch.find("p").text

        Watches.append({"Name": Name, "Model": Model, "Price": Price})

    return Watches

html_content = load_html("watch store.html")
soup = BeautifulSoup(html_content, "html.parser")
Watch =  extract_Watches(soup)

for Watch in Watch:
    print(f"Name:{Watch['Name']}")
    print (f"Model:{Watch['Model']}")
    print (f"Price:{Watch['Price']}")
    print("---------------------------------")