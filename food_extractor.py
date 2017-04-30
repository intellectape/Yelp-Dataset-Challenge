import requests
from bs4 import BeautifulSoup

file1 = open("food_items.txt", "w")

for i in range(1, 27):
    url = "http://www.oxfordreference.com/view/10.1093/acref/9780199640249.001.0001/acref-9780199640249?avail_01=unlocked&btog=chap&hide=true&page="+str(i)+"&pageSize=100&skipEditions=true&sort=titlesort&source=%2F10.1093%2Facref%2F9780199640249.001.0001%2Facref-9780199640249"

    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, sdch",
        'accept-language': "en-US,en;q=0.8",
        'cache-control': "no-cache",
        'postman-token': "bfcde8be-f61b-a527-42b1-10939d8f5043"
        }

    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    list = soup.find_all('h2', class_='itemTitle');

    for h2 in list:
        food_name = h2.find('a').contents[0].encode('utf-8')
        file1.write(food_name+"\n")

file1.close()
