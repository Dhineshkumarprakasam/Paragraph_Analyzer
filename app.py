from flask import Flask,render_template,request
import joblib
import pandas as pd

app = Flask(__name__)
#functions to find the counts
def countNoOfWords(content):
    return len(content.split())

def countNoOfLetters(content):
    value=0
    for i in content:
        if(i.isalpha()):
            value+=1
    return value

def countNoOfVowels(content):
    value=0
    for i in content:
        if i.isalpha() and i.lower() in ['a','e','i','o','u']:
            value+=1
    return value

def countNoOfCons(content):
    value=0
    for i in content:
        if i.isalpha() and i.lower() not in ['a','e','i','o','u']:
            value+=1
    return value
    
def countNoOfSplChar(content):
    value=0
    for i in content:
        if i.isalpha()==False and i.isspace()==False:
            value+=1
    return value

def countNoOfSpaces(content):
    value=0
    for i in content:
        if i.isspace():
            value+=1
    return value

def countNoOfNumbers(content):
    value=0
    for i in content:
        if i.isdigit():
            value+=1
    return value

def predictEmotion(content):
    model=joblib.load('para info\\static\\models\\emotion_detector.pkl')
    v=joblib.load('para info\\static\\models\\emotion_vectorizer.pkl')
    encoder=joblib.load('para info\\static\\models\\emotion_encoder.pkl')
    converted=v.transform([content])
    ans=model.predict(converted)
    return encoder.inverse_transform(ans)[0]

def findMostRepeated(content):
    arr=content.split()
    df=pd.DataFrame(arr)
    unique=df[0].unique()
    maximum_val=""
    maximum_cnt=0
    for i in unique:
        count=content.count(i)
        if(count>maximum_cnt):
            maximum_cnt=count
            maximum_val=i
    return maximum_val

def findLeastRepeated(content):
    arr=content.split()
    df=pd.DataFrame(arr)
    unique=df[0].unique()
    mini_val=unique[0]
    mini_cnt=len(unique[0])
    for i in unique:
        count=content.count(i)
        if(count<mini_cnt):
            mini_cnt=count
            mini_val=i
    return mini_val

def findAvgLength(content):
    value=0
    arr=content.split()
    for i in arr:
        value+=len(i)
    return round(value/len(arr),2)

def findUniqueWords(content):
    arr=content.split()
    df=pd.DataFrame(arr)
    unique=df[0].unique()
    return len(unique)

def findUppercase(content):
    value=0
    for i in content:
        if i.isalpha() and i.isupper():
            value+=1
    return value

def findLowercase(content):
    value=0
    for i in content:
        if i.isalpha() and i.islower():
            value+=1
    return value



@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/',methods=['POST','GET'])
def find():
    if request.method=="POST":
        content=request.form.get('content')

        noOfWords=countNoOfWords(content)
        noOfLetters=countNoOfLetters(content)
        noOfVowels=countNoOfVowels(content)
        noOfCons=countNoOfCons(content)
        noOfSplChar=countNoOfSplChar(content)
        noOfSpaces=countNoOfSpaces(content)
        noOfNumbers=countNoOfNumbers(content)

        mostRepeated=findMostRepeated(content)
        leastRepeated=findLeastRepeated(content)
        avgLength=findAvgLength(content)
        totalChar=len(content)
        uniqueWords=findUniqueWords(content)
        uppercase=findUppercase(content)
        lowercase=findLowercase(content)

        emotion = predictEmotion(content)


        
        dic1 = {
                'Words':noOfWords,
                'Letters':noOfLetters,
                'Vowels':noOfVowels,
                'Consonants':noOfCons,
                'Symbols':noOfSplChar,
                'Spaces':noOfSpaces,
                'Numbers':noOfNumbers
                }
        
        dic2 =  {
                    'Most Repeated':mostRepeated,
                    'Least Repeated':leastRepeated,
                    'Avg Length':avgLength,
                    'Total char':totalChar,
                    'Unique Words':uniqueWords,
                    'Upper Case' :uppercase,
                    'Lower Case':lowercase
                }
        
    return render_template('/index.html',dic1=dic1,dic2=dic2,emotion=emotion)

if __name__=="__main__":
    app.run(debug=True)
