# -*- coding: UTF-8 -*-
import web
import os, sys
import string
import bagwords.extract as ext

app_path = os.path.dirname(__file__)
sys.path.append(app_path)
if app_path:
    os.chdir(app_path)
else: # CherryPy
    app_path = os.getcwd()


EXAMPLE_TEXT = u'Esto es un ejemplo del funcionamiento de Grasp, coloca el cursor sobre las palabras marcadas para ver su definición. \n \nGrasp es un procesador de texto que identifica palabras extrañas o foráneas del Español y te provee con una definición de estas para que puedas descrifrar el significado de cualquier texto, por rebuscado que este sea.\n Grasp usa el Wikccionario como fuente de las definiciones.'

render = web.template.render('templates/')

db = web.database(dbn='sqlite', db='static/source.db')

urls = (
    '/', 'index',
    '/solve', 'solve',
    '/clear', 'clear',
    '/example', 'example'
)

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

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
        definitions = process(winput.text)
        return render.show(text,definitions)

class example :
    def GET(self) :
        text = web_format(EXAMPLE_TEXT)
        definitions = process(EXAMPLE_TEXT)
        return render.show(text,definitions)


def web_format(content) :
    lines = content.split('\n')
    result = []
    for i in lines :
        result.append(ext.process_line(i))
    return result

def def_format(definition) :
    formated = definition.replace(u'\n',u'<br>')
    formated = formated.replace('H2:','<b>')
    formated = formated.replace(':2H','</b>')
    return formated


def process(content) :
    text = web_format(content)
    definitions = {}
    for i in text :
        for j in i :
            word = j.lower()
            # s = "SELECT times from bag where word = '" + word + "'"
            # count = db.query(s)
            s = u'word = "{}"'.format(word)
            count = db.select('bag',what='times',where=s)
            # print "COUNT:",count
            count = count.list()
            if count :
                if count[0]['times'] < 3000 :
                    # s = "SELECT def from dic where word = '" + i + "'"
                    # fetch = db.query(s)
                    fetch = db.select('dic',what='def',where=s)
                    fetch = fetch.list()
                    if fetch :
                        # word_def = unicode(fetch[0]['def'],'utf-8')
                        word_def = fetch[0]['def']
                        definitions[j] = def_format(word_def)
                        # print "DEFS:", repr(definitions[j])
                    elif word != j :
                        s = u'word = "{}"'.format(j)
                        fetch = db.select('dic',what='def',where=s)
                        fetch = fetch.list()
                        if fetch :
                            word_def = fetch[0]['def']
                            # word_def = unicode(fetch[0]['def'],'utf-8')
                            definitions[j] = def_format(word_def)
                            # print "DEFS:", repr(definitions[j])
    return definitions

if __name__ == "__main__":
    # app = web.application(urls, globals())
    app.run()
