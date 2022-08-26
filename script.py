import json
from random import randint # randint(start, end) **inclusive**

watched = json.load(open('helpers/watched.txt', 'r'))
titles = json.load(open('helpers/titles.txt', 'r'))
seasons = [22, 22, 23, 23, 22, 22, 22]

watch_index = int(watched['false'][randint(0, len(watched['false']) - 1)])

watched['false'].remove(watch_index)
watched['true'].append(watch_index)
json.dump(watched, open('helpers/watched.txt', 'w'))

season = 1
while(watch_index > 0): 
    seasons[0] -= 1
    if not seasons[0]: # if season number == 0
        seasons.pop(0)
        season += 1
    watch_index -= 1

episode = seasons[0]

title = titles[str(episode)]
s_e_string = "Season: {}".format(season) + ", Episode: {}".format(episode)

with open('helpers/this_time_through.txt', 'a') as f: 
    f.write(s_e_string + ": " + '\n')
    f.write(title + '\n')

print(s_e_string)
print(title)