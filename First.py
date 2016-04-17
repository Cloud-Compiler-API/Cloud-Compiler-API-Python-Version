from bs4 import BeautifulSoup
import mechanize
import urlparse
import requests
import math
import random


class Scrape:
    url = "https://ideone.com/"  # static by default
    json = ""

    def getjson(self):
        s = requests.Session()
        r = s.get(self.url)
        soup = BeautifulSoup(r.content)
        p1 = soup.find(attrs={"name": "p1"})
        val = p1['value']
        print str(val)
        print int(math.floor(random.random() * math.pow(10, 10)))
        d = {"p1": str(val),
             "p2": 0,
             "p3": 0,
             "p4": 0,
             "clone_link": "/",
             "file": """
                    <?php
                    echo "hi sexy dude hello bro!!!!";
                    ?>
            """,
             "syntax": 1,
             "timelimit": 0,
             "input": "",
             "_lang": 29,
             "public": 1,
             "run": 1,
             "Submit": "",
             "note": "",
             }

        boundary = "------" + str(int(math.floor(random.random() * math.pow(10, 17))))
        encodedData = ''
        for key, value in d.items():
            encodedData += "--" + boundary + "\nContent-Disposition: form-data; name=\"" + str(key) + "\"\n\n" + str(
                value) + "\n"

        encodedData += boundary + "--"
        # print encodedData

        h = {'content-type': 'multipart/form-data; boundary=' + boundary}
        r = s.post("https://ideone.com/ideone/Index/submit/", data=encodedData, headers=h,
                   allow_redirects=True)  # collect other cookies
        soup = BeautifulSoup(r.content)  # reassiging value to variable thats it
        p1 = soup.find(attrs={"id": "solution_link"})
        val = p1['value']
        r = s.post("https://ideone.com/ideone/Index/view/id/" + str(val) + "/ajax/1/lp/1")
        self.json = r.content
        if str(self.json).__contains__("Running"):
            r = s.post("https://ideone.com/ideone/Index/view/id/" + str(val) + "/ajax/1/lp/1")
        self.json = r.content

    def parseJson(self):
        print self.json


if __name__ == '__main__':
    sc = Scrape()
    sc.getjson()
    sc.parseJson()
