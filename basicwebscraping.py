import requests
from bs4 import BeautifulSoup
import time

def productCheck():
    URL = 'https://www.amazon.com.tr/MSI-A14VIG-067TR-Dizüstü-Bilgisayar-I9-14900HX/dp/B0CTKT55J1/ref=sr_1_7?dib=eyJ2IjoiMSJ9.oicGZXCDnYNcGZH0KGVX-VvLtIDwnU1Pvrkf7aae4b2VDXMdquj42PJ1khiC7Ja8PA8Qu3V7dYH8Sr5K-9QgL0hf4VNFUmTBvvBjOyZVl1wiSv_7naukrv7G2UYuFZUtcPXGV86Y5qlRzBsx_0fKBFdSPX7HjPZrirsANg4Bu45sxNY9nB6l_tyLSijldQZRcWnfp5MYXwY1y8nlv_BDBoRzFDRAvN_ymUP5feiYloRFdnwwJPQEFSHqjfsj-52Qo8urE8vKqW70tnJc8FlpHuIsiTOaIem4VU-32oWBJqk.kIWp5gEOo5KUUjjnK1ADKWFGCayitsAnLOPi2mXh444&dib_tag=se&qid=1710611618&refinements=p_89%3AMSI&s=computers&sr=1-7'
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"}
    page = requests.get(URL, headers = headers)
    content = BeautifulSoup(page.content,'html.parser')

    productName = content.find(id='productTitle').get_text().strip()

    price = content.find(class="a-price-whole").get_text().strip()
    priceConventer = price[1:8].replace('.','')

    if(priceConventer < 220000)
        print(f"{priceConventer} {productName} the price has dropped, hurry up.")
    else:
        print(f"{priceConventer} {productName} the price has not dropped.")

while(True):
    productCheck()
    time.sleep(60 * 60 * 24)