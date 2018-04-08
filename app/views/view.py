#!/usr/bin/python  
# -*-coding:utf-8-*-
from app import app
from flask import jsonify, request
from ..models.user import create_user, query_user


@app.route('/')
def index():
    return jsonify({"msg": "看电影了"})


@app.route("/post/", methods=['POST'])
def post():
    if request.method == 'POST' and request.values.get("name") and request.values.get("password"):
        name = request.values.get('name')
        password = request.values.get('password')
        return jsonify({"msg": {"name": name, "password": password}})
    else:
        return jsonify({"msg": "None"})

    # request.form.get("key", type=str, default=None) 获取表单数据
    # request.args.get("key") 获取get请求参数，
    # request.values.get("key") 获取所有参数
    # 推荐使用request.values.get()

# 注册接口
@app.route('/user/register/', methods=['POST'])
def customer_register():
    if request.method == 'POST' and request.values.get("name") and request.values.get("password"):
        name = request.values.get("name")
        password = request.values.get("password")
        if request.values.get("phone"):
            phone = request.values.get("phone")
        else:
            phone = ""
        if request.values.get("nickname"):
            nickname = request.values.get("nickname")
        else:
            nickname = ""
        uid = create_user(name, password, phone, nickname)
        if uid == 0:
            return jsonify({"msg": 400})
        return jsonify({"msg": "注册成功"})


@app.route('/login/', methods=['POST'])
def login():
    if request.method == 'POST' and request.values.get("name") and request.values.get("password"):
        name = request.values.get("name")
        if request.values.get("password") == query_user(name).password:
            return jsonify({"msg": "登录成功"})
        else:
            return jsonify({"msg": "请输入正确的密码"})
    else:
        return jsonify({"msg": "请输入正确的用户名和密码"})




