# -*- coding:utf-8 -*-
__author__ = 'liuxiaotong'
from flask import Flask, request, make_response, redirect, render_template

from service.user import UserService

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    return 'hello, world!'


@app.route('/', methods=['GET'])
def welcome():
    token = request.cookies.get('token')
    if token:
        user = UserService.get_user_info(token)
    else:
        user = {}
    return render_template('welcome.html', user=user)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserService.register(username, password)
        resp = make_response(redirect('/', '302'))
        resp.set_cookie('token', user['token'])
        return resp
    elif request.method == 'GET':
        return render_template('register.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
