from flask import Flask, render_template, request
from openAI import openAIHelper
from result import Result
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/getScript/<message>", methods=['GET'])
def getScript(message):
    if(message == None):
        return Result.fail('پیام خالی است').apiResult()
    
    openaiHelper = openAIHelper(message)
    result = openaiHelper.getScript()
    print(result)
    return Result.apiResult(result)

@app.route("/getData/<message>", methods=['GET'])
def getData(message):
    if(message == None):
        return Result.fail('پیام خالی است').apiResult()
    
    openaiHelper = openAIHelper(message)
    result = openaiHelper.getDataFormDB()
    print(result.__dict__)
    return Result.apiResult(result)