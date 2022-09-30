#importing all the requirements
from flask import Flask,request,render_template
import re

#object creation
app=Flask(__name__)

#Route and logic
@app.route('/', methods=['GET','POST'])
def index_fn():
    if request.method=='POST':
        c=0
        p = request.form["in_1"]
        s = request.form['in_2']
        pattern=re.compile(p)
        matches =[(ele.start(), ele.end()) for ele in re.finditer(pattern,s)]
        c=int(len(matches))
        return render_template('index.html', string=s, regex=p, match=matches, result=c)
    return render_template('index.html')

#run the app
if __name__=='__main__':
    app.run(debug=True)