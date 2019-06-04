from woocommerce import API
import json
import requests

class nlbase:
    def __init__(self, pub, priv, shopurl):
        self.pub = pub
        self.priv = priv
        self.url = shopurl

    def connect(self):
        self.wcapi = API(
            url=self.url,
            consumer_key=self.pub,
            consumer_secret=self.priv,
            wp_api=True,
            version="wc/v3"
        )
        return [True, {}, None]

    def inputnl(self):
        headers = {
            'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE1NTk2NDA0NjgsImV4cCI6MTU1OTY0NDA2OCwicm9sZXMiOlsiUk9MRV9BUEkiXSwidXNlcm5hbWUiOiJhcGkifQ.Zv7v_nDWiHeK-bLHkT3p0GGQ03BaMj5pt-nFWaZZyjkRfQQKjdqNyKXjlZ-GsufPTy9I6LDilP5bGOI_ggKL8AmK5RymEDXp8BAm7Q96mj1fINkj8upu4nx60Zwd3CqCjvZIAC7unV4IsQLA4Q2_Gj2WaFnaeyF8WVxQ91FyAzmOSPD7LmHjUiDkluXNMglukpgYXb0XCOLiEiXLmUZuBqB9s3B4pGeBTFmzHWlXXVvUNIXnJZPua_2LxoeRimPDezTZgyxFn9LMfyjjG__6phgP3xJYAMDkFyf3exovM8D0oj94ZxlRY-zeixcwGf4xVVw69iqTaQtwidE5TS2vc0SYIE1INFn0eNUFk_hLkxYogACFtF3fg3jBqk5j1E7u70L8GQzRuBYpcKnut5nzQTvBDzllp9bKd4L-I0Wu1h9efZWsTz0y6rQITecAEA2nUYAT5UXVkyrWDhrf5E3Yw5uzLMqF-6aEIeDdu4pid4N1yQphjcKCiMqHoGzqldb0wJQUMKbzBszTZ1js7VMFh9HjhYSyifCA3bGzyiy1GKpIRr3gf21UITCH96aZxOVMrSZUGIpWPr9w9dqpSpi69OI-OmlhkYOoVgCSibzh6-Tbq3xz3pQz4TmJMIJTYXh-IuQEjH8r7ZfcYDq3YZ729f9-ZIU1xSLLe8diiyMrQro"
        }
        d = requests.get("http://api2.nleurope.com/api/v1/product", headers=headers).text
        datas = json.loads(d)
        for d in datas:
            try:
                proddata = {
                "image": str(d[0]["productImage"]),
                "title": str(d[0]["technicalSheet"]["FR"]["title"]),
                "flavor": str(d[0]["technicalSheet"]["FR"]["flavor"]),
                "price": str(d[0]["technicalSheet"]["031"]["pk7ht"]),
                "prep": str(d[0]["technicalSheet"]["031"]["preparation"]),
                "ing": str(d[0]["technicalSheet"]["031"]["ingredientList"])
                }
                data = {
                    "name": proddata["title"],
                    "type": "simple",
                    "regular_price": proddata["price"],
                    "description": proddata["flavor"] + proddata["prep"] +  proddata["ing"],
                    "short_description": proddata["flavor"],
                    "status": "private",
                    "categories": [],
                    "images": [
                        {
                            "src": proddata["image"]
                        }
                    ]
                }
                try:
                    self.wcapi.post("products", data)
                except:
                    return [False, "Wrong Crendential for '" + str(self.url) + "'", 401]
            except:
                print("error")
        return [True, {}, 200]
