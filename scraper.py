# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import datetime
#
# # Read in a page
html = scraperwiki.scrape("http://steamcommunity.com/id/mikeshenry/")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
content = root.cssselect("div#recentgame_quicklinks h2")

date = datetime.date.today()
#
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=date, data={"content": content, "date": date})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
