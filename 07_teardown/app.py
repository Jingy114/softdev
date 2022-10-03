'''
Jing Feng, Anna Fang, Prattay Dey
SoftDev
04_choose
2022-09-22
'''
from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
- You can't run this script in Thonny, you have to run it via terminal to open a webpage
QCC:
- What is Flask?
- WHy are we importing Flask from flask
- What is the significance of the front-slash?

0. 
1. With a double front-slash, we can make comments in Java.
2. It will print to a webpage on a browser
3. It will print the return statement
4. It will appear on the webpage because we ran it to confirm
5. We saw run() when doing processing in APCS
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
