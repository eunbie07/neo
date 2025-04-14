import urllib.request

url = 'https://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg'

filename = 'p291_urllib.jpg'

urllib.request.urlretrieve(url, filename)

print('web image : ' + url)
print(filename +  ' saved')

print('-' * 50)