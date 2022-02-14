from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def board():
    
    return render_template('checkerboard.html', numH = 6, numV = 6, color1 = 'Black', color2 = 'Red')

@app.route('/<int:numH>/<int:numV>')
def nums(numH, numV):

    return render_template('checkerboard.html', numH = numH, numV = numV, color1 = 'Black', color2 = 'Red')

@app.route('/<int:numH>/<int:numV>/<color1>/<color2>')
def numColors(numH, numV, color1, color2):

    return render_template('checkerboard.html', numH = numH, numV = numV, color1 = color1, color2 = color2)
    

if __name__=="__main__":
    app.run(debug=True)