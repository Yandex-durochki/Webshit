from flask import Flask, render_template
from api.api_load import api_server
import requests
import source.add

application = Flask(__name__)


@application.route("/")
def index():
    return render_template('index.html', maincss=source.add.main, pagecss=source.add.pagecss, jquery=source.add.jquery, pagejs=source.add.pagejs, mmpng=source.add.mmpng, vid=source.add.vid)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=20000)
