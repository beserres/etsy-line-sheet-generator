import requests
from jinja2 import Template

r = requests.get('https://openapi.etsy.com/v2/shops/8060333/listings/active?api_key=')
json_results = r.json()
listings = json_results["results"]

f = open("item_list.csv.j2")
template = Template(f.read())
rendered_template = template.render(listings=listings)

f = open("item_list.csv", "w")
f.write(rendered_template)
f.close()
