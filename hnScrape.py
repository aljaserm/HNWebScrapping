import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink')
# votes = soup.select('.score')
subText = soup.select('.subtext')
links2 = soup2.select('.storylink')
# votes2 = soup2.select('.score')
subText2 = soup2.select('.subtext')

mega_links = links+links2
mega_subText = subText+subText2

def sort_story_by_vote(hnList):
    return sorted(hnList, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links,subText):
    hn = []
    for idx,item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subText[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points> 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_story_by_vote(hn)


hn = create_custom_hn(mega_links, mega_subText)
pprint.pprint(hn)

