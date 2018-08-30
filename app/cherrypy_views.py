import cherrypy
import jinja2

# jinja2 template renderer
ENV  = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, 'templates')))
def render_template(template, **context):
    global ENV
    template = ENV.get_template(template+'.html')
    return template.render(context)


class BSEParser(object):

    @cherrypy.expose
    def index(self):
        return 'Hello inhabitants of Earth \V/'

    @cherrypy.expose
    def get_data(self):
        return render_template('object', data=dict())

    @cherrypy.expose
    def find_scrip(self):
        return render_template('object', data=dict())


if __name__=='__main__':
    cherrypy.quickstart(BSEParser())
