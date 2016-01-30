import web

render = web.template.render('templates/')

db = web.database(dbn='sqlite', db='test')

urls = (
    '/', 'index',
    '/add', 'add'
)

class index:
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)


class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
