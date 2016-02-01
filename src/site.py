import web
import string
import bagwords.extract as ext




render = web.template.render('web/templates/')

db = web.database(dbn='sqlite', db='source.db')

# DEF_TEMPLATE =  string.Template(u'<span class="hover">$word<span class="appear">$def</span></span>')

urls = (
    '/', 'index',
    '/solve', 'solve',
    '/clear', 'clear'


)

class index():
    def GET(self):
        return render.index('')


class clear:
    def GET(self):
        raise web.seeother('/')



class solve :
    def POST(self) :
        winput = web.input()
        text = web_format(winput.text)
        definitions = {}
        for i in text :
            for j in i :
                word = j.lower()
                # s = "SELECT times from bag where word = '" + word + "'"
                # count = db.query(s)
                s = 'word = "{}"'.format(word)
                count = db.select('bag',what='times',where=s)
                if count :
                    if count[0] < 1500 :
                        # s = "SELECT def from dic where word = '" + i + "'"
                        # fetch = db.query(s)
                        fetch = db.select('dic',what='def',where=s)
                        if fetch :
                            word_def = unicode(fetch[0],'utf-8')
                            defintions[i]=word_def
                        else :
                            s = 'word = "{}"'.format(j)
                            fetch = db.select('dic',what='def',where=s)
                            if fetch :
                                word_def = unicode(fetch[0],'utf-8')
                                defintions[i]=word_def

        return render.show(text,definitions)

        # raise web.seeoter('/show')


def web_format(content) :
    lines = content.split('\n')
    result = []
    for i in lines :
        result.append(ext.process_line(i))
    return result


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
