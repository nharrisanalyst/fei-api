import os
import time

from types import SimpleNamespace
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from psycopg_pool import ConnectionPool

from Repositories.zipcode_repository import ZipCodeRepository
from Services.zipcodeservice import ZipcodeService
from Repositories.avg_repository import AverageRepo
from Services.avgservice import AverageService
from Repositories.suggestion_repository import SuggestionRepository
from Services.suggestionservice import SuggestionService

from Models.average import DataAvgData
from Models.email import EmailForm, EmailService, EmailBuilder

time.sleep(60)

user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
db = os.environ.get("POSTGRES_DB")
host = os.environ.get("POSTGRES_HOST")
port= os.environ.get("POSTGRES_PORT")
email_password = os.environ.get("EMAIL_PASSWORD")
email_name = os.environ.get("EMAIL_NAME")

pool = ConnectionPool(f"dbname={db} user={user} password={password} host={host} port={port}")
 
zipcode_r = ZipCodeRepository(pool)
zipcode_s = ZipcodeService(repo=zipcode_r)

avg_r = AverageRepo(pool)
avg_s =  AverageService(repo=avg_r)

sug_r = SuggestionRepository(pool)
sug_s = SuggestionService(repo=sug_r)


app = Flask(__name__)
CORS(app)

## email configs
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = email_name
app.config['MAIL_PASSWORD'] = email_password

mail = Mail(app)

@app.route('/')
def hello_world():
    return 'Hello World!', 200

@app.route('/zipcode', methods=['GET'])
def zipcod_root():
    if request.method == 'GET':
        return 'Use this endpoint to get info on zipcodes'

@app.route('/zipcode/<int:zipcode>', methods=['GET'])
def zipcode_lookup(zipcode):
    if request.method == 'GET':
        zipcode_data = zipcode_s.getZipCode(zipcode)
        return jsonify(zipcode_data), 200
    
@app.route('/data/avgdata', methods=['GET'])
def data_avg_get():
    if request.method == 'GET':
        avg_data:DataAvgData = avg_s.getDataAvg()
        return jsonify({"avg_data":avg_data}), 200

@app.route('/data/zipcode/<int:zipcode>', methods=['GET'])
def zipcode_data_lookup(zipcode):
    if request.method == 'GET':
        zipcode_data = zipcode_s.getZipCodeData(zipcode)   
        return jsonify({'data':zipcode_data}), 200

@app.route('/zipcode/all', methods=['GET'])
def zipcode_get_all():
    if request.method == 'GET':
        zipcode_all = zipcode_s.getAllZipCodes() 
        return jsonify({'data':zipcode_all}), 200
    
@app.route('/email', methods=['POST'])
def email_inqueries():
    if request.method == 'POST':
        builder = EmailBuilder(EmailForm=EmailForm, Message=Message)
        msg = builder.build(request.form)
        email = EmailService(emailTransport=mail)
        return email.send(msg)
    
@app.route('/searchhelp/cities', methods=['get'])
def citySearch():
    if request.method == 'GET':
        citySuggestion = request.args.get('search')
        city_suggestion_data = sug_s.getCitySuggestions(citySuggestion)
        return jsonify({'suggestions':city_suggestion_data}), 200
    
@app.route('/searchhelp/zipcodes', methods=['get'])
def zipcodeSearch():
    if request.method == 'GET':
        zipSuggestion = int(request.args.get('search'))
        zipcode_suggestion_data = sug_s.getZipCodeSuggestions(zipSuggestion)
        return jsonify({'suggestions':zipcode_suggestion_data}), 200
        
        
    
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
