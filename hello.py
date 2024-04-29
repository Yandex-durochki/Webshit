from flask import Flask, render_template, request, url_for, redirect

import source.add
from py.Users import compare_data_with, check_password
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


@application.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        data = check_password(username, password)
        if data == True:
            return redirect("https://www.youtube.com/watch?v=-452p_9ESbM&ab_channel=FANVIDOS-%D0%9C%D0%B8%D0%BB%D1%8B%D0%B5%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8")
        else:
            error = data[1]
            return render_template('login.html', logincss=source.add.logcss, pagecss=source.add.pagecss,
                                   jquery=source.add.jquery, pagejs=source.add.pagejs, mmpng=source.add.mmpng,
                                   error=error)

    return render_template('login.html', logincss=source.add.logcss, pagecss=source.add.pagecss,
                           jquery=source.add.jquery, pagejs=source.add.pagejs, mmpng=source.add.mmpng, error=error)


@application.route("/registration", methods=['GET', 'POST'])
def registration():
    error = None
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
            return redirect(url_for('login'))
        else:
            error = 'Пользователь с таким именем уже существует'
            return render_template('reg.html', reg=source.add.reg, pagecss=source.add.pagecss, jquery=source.add.jquery,
                           pagejs=source.add.pagejs, mmpng=source.add.mmpng, error=error)

    return render_template('reg.html', reg=source.add.reg, pagecss=source.add.pagecss, jquery=source.add.jquery,
                           pagejs=source.add.pagejs, mmpng=source.add.mmpng, error=error)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=20000, debug=True)
