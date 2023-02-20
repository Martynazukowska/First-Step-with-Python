import web 


#czyli jesli w url bedzie np. http://0.0.0.0:8080/martyna/22 to index.name=martyna index.age=22
url=('/(.*)/(.*)','index')

render=web.template.render("zrodla/")

app=web.application(url,globals())

class index:
    def GET(self, name,age):
        return render.main(name,age)

if __name__=="__main__":
    app.run()