from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/')
def index():
    fin = open('config.json', 'r')
    data = json.loads(fin.read())
    fin.close()
    return render_template('all.html', name=data['name'], text0=data['text0'], text1=data['text1'],
                           endtext=data['endtext'], link=data['link'],
                           ls=data['details'], date=datetime.now().strftime("%Y.%m.%d"))


if __name__ == '__main__':
    app.run()
