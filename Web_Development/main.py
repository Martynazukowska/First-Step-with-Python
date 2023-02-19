import web 


#czyli jesli w url bedzie np. http://0.0.0.0:8080/martyna to martyna index
url=('/(.*)','index')

app=web.application(url,globals())

class index:
    def GET(self, name):
        return "<h1> Hej </h1>"+name

if __name__=="__main__":
    app.run()