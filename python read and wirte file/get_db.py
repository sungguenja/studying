import requests
import re

write_f = open('db_mivies.json','w',encoding='utf-8')
data = '['
for i in range(1,101):
    res = requests.get().json()
    for ge in res['results']:
        data += '{' + '"model": "movies.movie", "pk": ' + str(ge['id']) + ', "fields": {"title": "' + ge['title'] + '", "popularity": ' + str(ge['popularity']) + ', "vote_count": ' + str(ge['vote_count']) + ', "video": '
        if ge['video'] == False:
            data += 'false'
        else:
            data += 'true'
        data += ', "poster_path": "' + ge['poster_path'] + '", "adult": '
        if ge['adult'] == False:
            data += 'false'
        else:
            data += 'true'
        data += ', "backdrop_path": "' + str(ge['backdrop_path']) + '", "original_language": "' + str(ge['original_language']) + '", "original_title": "' + str(ge['original_title']) + '", "vote_average": ' + str(ge['vote_average']) + ', "overview": "' + ge['overview'].replace('\n','\\n').replace('\t', '\\t').replace('"',' ') + '", "release_date": "' + str(ge['release_date']) + '", "genres": ' + str(ge['genre_ids']) + '} },'
data += ']'
write_f.write(data)