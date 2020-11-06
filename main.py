import requests as req
from bs4 import BeautifulSoup as bs

class Engine:
	"""
	Description:
	1 - Getting all summaries of which stock had entered.
	2 - Returning all values of the ticker if exists.
	"""

	def __init__(self, ticker):
		self.ticker = ticker
		self.url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=" + str(self.ticker)
		self.stock = {}

	def run(self):
		try:
			page = req.get(self.url)
			soup = bs(page.content, "html.parser")

			results = soup.find(id = "ozetFinansalGostergeler1")
			isim = soup.find(class_ = "share-title").text

			self.title = results.find_all("th") # Getting all titles financial ratios
			self.ratio = results.find_all("td") # Getting all ratios of ticker
		
		except:
			print(f"No stock found named {self.ticker}")

			return 0

		return 1

	def out(self):
		if self.run() == 1:

			for title, ratio in zip(self.title, self.ratio):
				self.stock[title.text] = ratio.text

			return self.stock # Returns dictionary

		else:
			return

	def prettify(self, dict):
		for title, ratio in dict.items():
			print(title,":", ratio)


if __name__ == "__main__":
	q = input("Which stock do you want to get?: ")
	print("Getting informations..")
	x = Engine(q)

	output = x.out()
	x.prettify(output)
	


