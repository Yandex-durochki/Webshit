from flask import Flask, render_template, request

import source.add
from py.Users import compare_data_with
from py.registr import registrat

application = Flask(__name__)


@application.route("/")
def index():
    return render_template('index.html', maincss=source.add.main, pagecss=source.add.pagecss, jquery=source.add.jquery,
                           pagejs=source.add.pagejs, mmpng=source.add.mmpng, vid=source.add.vid)


@application.route("/main")
def main():
    return render_template('main.html', maincss=source.add.main, pagecss=source.add.pagecss, jquery=source.add.jquery,
                           pagejs=source.add.pagejs, mmpng=source.add.mmpng, vid=source.add.vid)


@application.route("/login", )
def login():
    return render_template('login.html', logincss=source.add.logcss, pagecss=source.add.pagecss,
                           jquery=source.add.jquery, pagejs=source.add.pagejs, mmpng=source.add.mmpng)


@application.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        address = request.form['address']
        tguse = request.form['tguse']
        sex = request.form['sex']
        age = request.form['age']
        data = compare_data_with(username)
        if not data:
            registrat(username, password, name, address, tguse, sex, age)
            return "Зареганы"
            return ''
        else:
            return "Такой пользватель уже есть!"

    return render_template('reg.html', reg=source.add.reg, pagecss=source.add.pagecss, jquery=source.add.jquery,
                           pagejs=source.add.pagejs, mmpng=source.add.mmpng)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=20000, debug=True)
