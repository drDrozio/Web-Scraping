from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

#Grabbing the URL string
my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#Opening up the connection using urlopen,requesting and downloading url html
uClient=uReq(my_url)
raw_html=uClient.read() #Reads whole HTML
uClient.close()

#Parsing the HTML
page_soup=Soup(raw_html,"html.parser")
# page_soup.h1 #return h1 tags
# page_soup.p #return p tags
# page_soup.body.span

# #Grabs each product with given details
containers=page_soup.find_all("div",{"class":"item-container"}) 
# contain=container.findAll("div") #Getting all div in the container
# c=contain[1] #Travelling to a particular div in the list of div
# c.div.a.img["title"] #Brand of the item

filename="GPUs.csv"
f=open(filename,"w")
headers="Brand,Product,Shipping\n"
f.write(headers)

for container in containers:
	contain=container.find_all("div") 
	c=contain[1] 
	brand=c.div.a.img["title"]

	title_container=container.find_all("a",{"class":"item-title"}) 
	product=title_container[0].text

	price_container=container.find_all("li",{"class":"price-ship"})
	price=price_container[0].text.strip()

	print("Brand : "+brand)
	print("Product : "+product)
	print("Shipping_price : "+price)
	print()

	f.write(brand+","+product.replace(",","|")+","+price+"\n")