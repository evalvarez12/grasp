import web

render = web.template.render('templates/')

# db = web.database(dbn='sqlite', db='test')

urls = (
    '/', 'index',
    '/show', 'show',
    '/clear','clear'
)

class index():
    def GET(self):
        return render.index('')


class show:
    def POST(self):
        i = web.input()
        lines = i.text.split('\n')
        # if 'as' in text :
        #     # text = text.replace('as','<span class="hover">as<span class="appear"> <h1>My popup</h1>Hitherto and whenceforth.</span></span>')
        # print "ESTO ES T: ", repr(text)
        return render.show(lines)

class clear:
    def GET(self):
        raise web.seeother('/')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
