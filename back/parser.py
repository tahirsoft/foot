from bs4 import BeautifulSoup


countries = {}

with open('test.html') as file:
    parsed_html = BeautifulSoup(file, 'html.parser')

links = parsed_html.find_all("td", class_="_flag")
country_points = parsed_html.find_all("td", class_="_points")

for link, points_tag in zip(links, country_points):
    flag, country = link.img.attrs["src"], link.img.attrs["alt"]
    points = points_tag.contents[0]
    countries[country] = {"flag": flag, "points": points}

with open('data.txt', 'w') as f:
    f.write(str(countries))
