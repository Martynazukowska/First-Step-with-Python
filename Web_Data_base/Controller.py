import web 

url=('/','home',
    '/register', 'register')

render=web.template.render("Views/Template",base="MainLayout")
app=web.application(url,globals())

#klasy
class home:
    def GET(self):
        return render.home()

class register:
    def GET(self):
        return render.register()

if __name__=="__main__":
    app.run()