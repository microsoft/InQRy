from lxml import html
import requests

serial_number = '8729wr1'

# url = 'http://www.dell.com/support/home/us/en/4/product-support/servicetag/' + serial_number + '/warranty'

page = requests.get(
    'http://www.dell.com/support/home/us/en/4/product-support/servicetag/'
    + serial_number + '/warranty')

type(page)

tree = html.fromstring(page.content)

print(tree)
