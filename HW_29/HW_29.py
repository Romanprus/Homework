import re

string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
pairs = re.findall(r"(\w+)=(\w+)", string)
result = {key: value for key, value in pairs}
print(result)

camel_case = ["FirstItem", "FriendsList", "MyTuple"]
snake_case = [re.sub(r"(?<=[a-z])([A-Z])", r"_\1", x).lower() for x in camel_case]
print(snake_case)

with open('text', 'r') as file:
    text = file.read()

text = re.sub(r'(\w)\.(?!\s)', r'\1,', text)
text = re.sub(r'(\w),(?!\s)', r'\1 ', text)
sentences = re.split(r'[.!?]+', text)

for sentence in sentences:
    if sentence.strip():
        print(sentence.strip() + '.')

with open("index.html", "r") as file:
    html_text = file.read()

link_pattern = re.compile(r'<div id="(\w+)">\s*<a href="([^"]+)">\s*(\w+)\s*</a>\s*</div>')
links = re.findall(link_pattern, html_text)

print(links)

with open("index.html", "r") as file:
    html_text = file.read()

link_pattern = re.compile(r'<div id="(\w+)">\s*<a href="([^"]+)">\s*(\w+)\s*</a>\s*</div>')
links = re.findall(link_pattern, html_text)

result = []
for link in links:
    id, url, text = link
    domain = url.replace("www.", "").split(".")[0].replace("http://", "")
    result.append((id, domain + ".com", text))

print(result)