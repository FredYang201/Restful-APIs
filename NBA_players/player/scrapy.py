import requests
from lxml import etree
from faker import Faker

class Players(object):

    def __init__(self, url):
        self.url = url
        self.faker = Faker()

    def getHtml(self, url):
        faker = self.faker.user_agent()
        headers = {
            'user-agent': faker,
        }
        print(faker)
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        return response.text


    def getTeamLink(self, html):
        obj = etree.HTML(html)
        teamReg = '//*[@id="block-teamlistblock"]/team-list/div[2]/div/div/a'
        fields = {'teamName': 'text()', 'teamLink': '@href'}
        teams = obj.xpath(teamReg)
        result = [{item: each.xpath(fields[item])[0] for item in fields} for each in teams]
        # print(result)
        return result

    def getPlayerLink(self, html):
        obj = etree.HTML(html)
        playerReg = '//*[@id="block-league-content"]/team-detail/div/section[4]/section/section'
        players = obj.xpath(playerReg)
        infos = {
            'playerNumber': 'span[@class="nba-player-trending-item__number"]/text()',
            'playerLink': 'a/@href',
            'playPosition': 'a/div[2]/span[1]/text()',
        }
        information = [{item: each.xpath(infos[item])[0] for item in infos} for each in players]
        return information

    def getPlayerInfos(self, html):
        obj = etree.HTML(html)
        nameReg = '//*[@id="block-league-content"]/player-detail/section[1]/header/section[2]/section/p/text()'
        playerName = ' '.join([each.strip() for each in obj.xpath(nameReg)])

        heightReg = '//*[@id="player-tabs-Info"]/section/section[1]/section[1]/section[1]/p[3]/text()'
        playerHeight = obj.xpath(heightReg)[0].strip('/').strip() + 'm'

        weightReg = '//*[@id="player-tabs-Info"]/section/section[1]/section[1]/section[2]/p[3]/text()'
        playerWeight = obj.xpath(weightReg)[0].strip('/').strip() + 'kg'

        bornReg = '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li/span[1][contains(text(), "BORN")]/../span[2]/text()'
        playerBorn = obj.xpath(bornReg)[0].strip()

        ageReg = '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li/span[1][contains(text(), "AGE")]/../span[2]/text()'
        playerAge = obj.xpath(ageReg)[0].strip().split(' ')[0].strip()

        yearsReg = '//*[@id="player-tabs-Info"]/section/section[1]/section[2]/ul/li/span[1][contains(text(), "YEARS IN NBA")]/../span[2]/text()'
        playerYears = obj.xpath(yearsReg)[0].strip()

        print({'playerName':playerName, 'playerHeight':playerHeight, 'playerWeight':playerWeight,
                'playerBorn':playerBorn, 'playerAge':playerAge, 'playerYears':playerYears})

        return {'playerName':playerName, 'playerHeight':playerHeight, 'playerWeight':playerWeight,
                'playerBorn':playerBorn, 'playerAge':playerAge, 'playerYears':playerYears}

    def store(self, Model):
        response = self.getHtml(self.url)
        nextLink = self.getTeamLink(response)
        for i in nextLink:
            iUrl = 'https://www.nba.com' + i['teamLink']
            iHtml = self.getHtml(iUrl)
            iPlayers = self.getPlayerLink(iHtml)
            for j in iPlayers:
                jUrl = 'https://www.nba.com' + j['playerLink']
                jHtml = self.getHtml(jUrl)
                player = self.getPlayerInfos(jHtml)
                Model.objects.create(name=player['playerName'], number=j['playerNumber'],
                                     link=jUrl, position=j['playPosition'], height = player['playerHeight'],
                                     weight=player['playerWeight'], born=player['playerBorn'],
                                     age=player['playerAge'], years_in_nba=player['playerYears'],
                                    team=i['teamName'])
