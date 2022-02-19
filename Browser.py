import webbrowser

webbrowser.open('http://www.wikipedia.org')
r = webbrowser.get(url)
print(r.text)
print("Status code:")
print("\t *", r.status_code)

h = webbrowser.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
    'User-Agent': 'Iphone 8'
}
url2 = 'http://httpbin.org/headers'
rh = webbrowser.get(url2, headers=headers)
print(rh.text)
