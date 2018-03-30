def getSelectors():
    selectors = {
        'indianexpress.com':'.full-details p',
        'indiatoday.intoday.in':'.ad-blocker-ajax p',
        'gadgets.ndtv.com':'.content_text p',
        'www.moneycontrol.com':'#article-main p',
        'www.ndtv.com':'#ins_storybody',
        'profit.ndtv.com':'[itemprop="articleBody"]',
        'timesofindia.indiatimes.com':'.Normal',
        'economictimes.indiatimes.com':'.Normal',
        'www.cnn.com':'.l-container .zn-body__paragraph',
        'www.ibtimes.co.in':'#article_content p',
        'www.livemint.com':'.story-content',
        'www.firstpost.com':'.article-full-content p',
        'www.financialexpress.com':'.main-story-content p',
        'www.hindustantimes.com':'.story-details p',
        'www.business-standard.com':'#hpcontentbox > div.row-panel > div.main-cont-left.topB > div > div.story-content > span p',
        'www.dnaindia.com':'.body-text p',
        'www.thehindu.com':'body > div.container-main > header > section > div > div > div > div p',
        'www.deccanchronicle.com':'#storyBody p',
        'zeenews.india.com':'.field-item p',
        'sports.ndtv.com':'[itemprop="articleBody"] p',
        'www.newindianexpress.com':'.page p',
        'www.indiatvnews.com':'.madbodynew p',
	'www.news18.com' : '.paragraph',
	"www.oneindia.com" : "#container > section > div > div.leftpanel > article > div",
	"www.mid-day.com" : "article > div > div.articlebody"

    }

    return selectors
