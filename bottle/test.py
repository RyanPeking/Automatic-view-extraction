from bottle import Bottle, run
#
# app = Bottle()
#
# @app.route('/hello')
# def hello():
#     return "Hello World!"
#
# run(app, host='localhost', port=8080)

from bottle import static_file
from bottle import error

app = Bottle()
@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='D:\Github_project\Project_one\d3')
run(app, host='localhost', port=8080)

@error(404)
def error404(error):
    return 'Nothing here, sorry'