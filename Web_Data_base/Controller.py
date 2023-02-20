import web 

url=('/','home')

app=web.application(url,globals())

#klasy
class home:
    def GET(self):
        return "home"

if __name__=="__main__":
    app.run()