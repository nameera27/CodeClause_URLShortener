import pyshorteners

shortner = pyshorteners.Shortener()
url = input('Enter the url : ')

tiny = shortner.tinyurl.short(url)

print(f'Short url is : {tiny}')