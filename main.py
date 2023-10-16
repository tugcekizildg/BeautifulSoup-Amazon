import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.tr/PUMA-Platform-Ayakkabı-Black-Strong-Gray-PUMA/dp/B0B37LM9JT/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.20309ab4-f986-4bd1-851e-2253ffa51552&pd_rd_r=cb2383d1-4fcf-4a75-9627-b6269c3fe0b9&pd_rd_w=juB5R&pd_rd_wg=Rnm1q&pf_rd_p=20309ab4-f986-4bd1-851e-2253ffa51552&pf_rd_r=XT0KW3Q5STAA3MJK1NKE&qid=1697461266&refinements=p_n_deal_type%3A26902947031&s=apparel&sr=1-1'

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

page = requests.get(url,headers= headers)

soup = BeautifulSoup(page.content,"lxml")

title = soup.find(id = "productTitle").get_text()
price = soup.find(id="corePrice_desktop").get_text()

print(title)
print(price)











