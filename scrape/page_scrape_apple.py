from lxml import html
import requests

serial_number = 'F5KQH0P9F9VN'
serial_end = serial_number[8:12]
print(serial_end)

page = requests.get(
    'http://support-sp.apple.com/sp/product/?cc='
    + serial_number)

tree = html.fromstring(page.content)

print(tree)
