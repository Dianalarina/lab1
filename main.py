from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://iotvega.com/product')

productElements = driver.find_elements(By.CLASS_NAME, 'product-name')
priceElements = driver.find_elements(By.CLASS_NAME, 'price_item')

productNames = list(map(lambda element:element.text, productElements))
productPrices = list(map(lambda element:element.text, priceElements))

driver.quit()

df = pd.DataFrame([productNames, productPrices])
df.to_excel(excel_writer= "product.xlsx")




