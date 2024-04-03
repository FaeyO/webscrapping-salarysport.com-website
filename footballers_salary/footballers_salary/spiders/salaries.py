import scrapy


class SalariesSpider(scrapy.Spider):
    name = "salaries"
    allowed_domains = ["salarysport.com"]
    #start_urls = ["https://salarysport.com/football/premier-league/manchester-united-f.c."]

    def start_requests(self):
        team_names = ['chelsea-f.c.' , 'manchester-united-f.c.']
        for team_name in team_names:
            url = f"https://salarysport.com/football/premier-league/{team_name}"
            yield scrapy.Request(url, callback=self.parse, meta={'team_name': team_name})


    
    def parse(self, response):
        #team_name = response.meta['team_name']
        players = response.xpath('(//tbody)[1]/tr')
        for player in players:
            
            footballer_names = player.xpath('.//td/a[@class="Table__StyledLink-sc-373fc0-2 giJwcy" ]/text()').get()
            if footballer_names is None:
                footballer_names = player.xpath('.//td[1]/text()').get()
            weekly_wage = player.xpath('.//td[2]/text()').get()
            monthly_wage = player.xpath('.//td[3]/text()').get()
            footballer_age = player.xpath('.//td[4]/text()').get()
            position = player.xpath('.//td[5]/text()').get()
            country = player.xpath('.//td[6]/text()').get()

            yield {
                #'team':team_name,
                'name':footballer_names,
                'week_wage':weekly_wage,
                'monthly_wage':monthly_wage,
                'footballer_age':footballer_age,
                'position':position,
                'country':country
            }
