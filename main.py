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
			self.page = req.get(self.url)
			self.soup = bs(self.page.content, "html.parser")

			self.results = self.soup.find(id = "ozetFinansalGostergeler1")
			self.isim = self.soup.find(class_ = "share-title").text

			self.title = self.results.find_all("th") # Getting all titles financial ratios
			self.ratio = self.results.find_all("td") # Getting all ratios of ticker
		
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

if __name__ == "__main__":
	q = input("Which stock do you want to get?: ")
	x = Engine(q)

	output = x.out()
	
	print(output) 
	

