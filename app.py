from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)