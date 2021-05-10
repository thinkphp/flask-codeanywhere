from flask import Flask
from flask import render_template, render_template_string, request
from flask import redirect, url_for, request
from flask import request
from flask import jsonify
import socket

app = Flask(__name__)

@app.route('/')
def index():    

    out  = "<!DOCTYPE html><head><title>Rails</title></head><h1 style='font-size: 70px;'>Web Development - <mark>Flask</mark></h1>"

    out += "<div style='color: lightgreen;font-size: 40px'><a href='/home'>Home</a> | <a href='/about'>About</a> | <a href='/projects'>Projects</a> | <a href='/github'>GitHub</a> | <a href='/contact'>Contact</a> | <a href='/vue2'>vue2</a> | <a href='/myip'>MyIP</a> | <a href='/gitcommits'>GitHubCommits</a>  </div>"

    out += "<h3>from flask import Flask</h3>"

    out += "<h3>from flask import render_template</h3>"

    out += "<h3>app = Flask(__name__)</h3>"

    out += "<h3>@app.route('/')</h3>"

    out += "<h3>def index():</h3>"

    out += "<h3>return 'Web App with Python Flask!'</h3>"

    out += "<h3>app.run(host='0.0.0.0', port=81)</h3>"

    out += "<p>Created by <a href='http://thinkphp.github.io'>Adrian Statescu</a></p>"

    return out

@app.route('/contact')
def contact():
    name = 'Adrian'
    welcome = 'Contact'    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return render_template('contact.html', title = welcome, name = name, ip = ip_address, hostname = hostname) 

@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/projects')
def pro():
    return "<h1 style='font-size: 100px;background-color: yellow; color:black'>./projects</h1><a href='/projects/10/3'>projects/10/3</a>"

@app.route('/projects/<int:a>/<int:b>')
def projects(a,b):
    def euclid(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a    

    a = a
    b = b
    c = euclid(a, b)

    return render_template('projects.html', a = a, b = b, result = c) 

@app.route('/github')
def github():
    return render_template('github.html') 

@app.route("/myip", methods=["GET"])
def get_my_ip():
    ob = {"ip": request.remote_addr}
    return "<h1 style='background-color: yellow; color: mediumseagreen;font-family: verdana;font-size: 150px'>Your IP: "+ob['ip']+"</h1>"

@app.route("/vue2")
def vue():
    return render_template("vue.html", flash_message="False")

@app.route("/gitcommits")
def gitcommit():
    return render_template("gitcommits.html", flash_message="False")

    
