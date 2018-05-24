import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

#opens the url
uClient = uReq(my_url)
page_html = uClient.read()
#closing connection
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#page_soup.h1 // to look at the h1 tag of the website
#page_soup.p // to find p tag

#img_links = page_soup.findAll("a", {"class":"item-img"})
#image = img_links.a["href"]
#for img_link in img_links:
#print (img_link.img['src'])

#grabs each product
containers = page_soup.findAll("div" , {"class" : "item-container"})

filename = "products"
#filename = "products.csv" use this when it is a new file

f = open(filename, "w")

headers = "brand , product _name, shipping\n"
f.write(headers)


for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class" : "item-title"})
	product_name = title_container[0].text

	shipping_container =  container.findAll("li" , {"class": "price-ship"})
	#strip() gets rid of open spaces
	shipping = shipping_container[0].text.strip()

	print("brand:" + brand)
	print("procut_name:" + product_name)
	print("shipping:" + shipping)

	f.write(brand + "," + product_name.replace(",","|")  + "," +  shipping + "\n")

f.close()