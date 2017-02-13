from lxml import html
import requests

serial_number = '8729wr1'

page = requests.get(
    'http://www.dell.com/support/home/us/en/4/product-support/servicetag/'
    + serial_number + '/warranty')

tree = html.fromstring(page.content)

print(tree)
