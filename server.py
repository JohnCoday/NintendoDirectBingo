from flask import Flask, render_template
import math
import random
app = Flask(__name__)                     

@app.route('/')
def play():
    bingoList = []
    i = 0
    while i < 25: 
        a = random.randrange(34)
        if a not in bingoList:
            bingoList.append(a)
            i += 1
    return render_template("index.html", l = bingoList, z = 0)

if __name__=="__main__":
    app.run(debug=True) 