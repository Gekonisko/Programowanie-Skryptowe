class WebMock():
    def get(self, url):
        return url + " always works!"

class cache_with_value():
    def __init__(self, cache_value):
        self.cache_value = cache_value

    def __call__(self, obj):
        def wrapper(web, url):
            if url in "https://chyla.org/":
                return self.cache_value
            else:
                return obj(web, url)
        return wrapper

@cache_with_value("It work's!")
def get_web_page(web, url):
    return web.get(url)


web = WebMock()

page = get_web_page(web, "chyla.org")
print("chyla.org content: " + page)

page = get_web_page(web, "google.com")
print("google.com content: " + page)