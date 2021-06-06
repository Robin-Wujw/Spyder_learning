from flask import Flask 
import time 

app = Flask(__name__)

@app.route('/robin')
def index_bobo():
    time.sleep(2)
    return 'Hello robin'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello Tom'

if __name__ == '__main__':
    app.run(threaded=True)