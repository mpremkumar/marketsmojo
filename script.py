from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException  

urls= [
'https://www.marketsmojo.com/Stocks?StockId=608125&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=363433&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=744293&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=878484&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=793847&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=166837&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=539868&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=422311&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=751831&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=687677&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=513245&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=639617&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=597145&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=463886&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=761462&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=383151&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=171892&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=213617&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=435326&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=179698&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=880342&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=313810&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=589145&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=107657&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=110452&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=129013&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=950027&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=347516&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=816180&Exchange=0',
'https://www.marketsmojo.com/Stocks?StockId=372338&Exchange=0'
]
f= open("share1.txt","a+")
browser=webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.marketsmojo.com/Stocks?StockId=565016&Exchange=0')
#browser.implicitly_wait(15)
#browser.find_element_by_css_selector('body > div > div > table.m_tbl.tbl_error > tbody > tr > td > table.table-upper > tbody > tr:nth-child(2) > td > a').click()
#browser.implicitly_wait(10)
#browser.find_element_by_css_selector('body > div > div > form > table.m_tbl > tbody > tr > td > table.table-upper > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(1) > input.btn').click()
browser.find_element_by_xpath("//*[@id='step-0']/a/i").click()
for url in urls:
	#browser=webdriver.Chrome()
	#browser.maximize_window()
	browser.get(url)
	#browser.switch_to_alert()
	#browser.find_element_by_xpath("//*[@id='step-0']/a/i").click()
	browser.execute_script("window.scrollTo(10,9300);")
	browser.implicitly_wait(2.5)
	try:
		browser.find_element_by_xpath("//div[contains(.,' No Shareholding data available ')]")
		f.write("No data available"+"\n")
		pass
	except:
		add=browser.find_element_by_css_selector('#btnShareholdingDashboardFullDetails')
		SearchButton = browser.find_element_by_css_selector('#btnShareholdingDashboardFullDetails')
		Hover = ActionChains(browser).move_to_element(add).move_to_element(SearchButton)
		Hover.click().perform()
		browser.implicitly_wait(1.5)
		browser.find_elements_by_css_selector('#allquarters > div > table')
		add1 = browser.find_element_by_css_selector('#AllQuarters')
		SearchButton1 = browser.find_element_by_css_selector('#AllQuarters')
		Hover1 = ActionChains(browser).move_to_element(add).move_to_element(SearchButton1)
		Hover1.click().perform()
		data = []
		for tr in browser.find_elements_by_css_selector('#allquarters > div > table'):
			ths = tr.find_elements_by_tag_name('th')
			tds = tr.find_elements_by_tag_name('td')
			if ths: 
				data.append([th.text for th in ths])
			if tds: 
				data.append([td.text for td in tds])
			f.write(str(data)+"\n")
			
	
browser.quit()
#allquarters > div > table
#shareholdingCompare > div.card-content > div.alert.alert-warning.mar-empty
#btnShareholdingDashboardFullDetails

	
