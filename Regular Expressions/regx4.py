import re
def main():
    url = input("youtube url:")
    shorturl(url)
def shorturl(url):
    if match:= re.search("^https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)$",url):
        return print(f"https://youtu.be/{match.group(1)}")
    else:
        return print(f"Invalid Url")
main()