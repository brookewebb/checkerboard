from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
@app.route('/<int:numH>/<int:numV>')
@app.route('/<int:numH>/<int:numV>/<color1>/<color2>')
def numColors(numH = 6, numV = 6, color1 = 'pink', color2 = 'brown'):

    return render_template('checkerboard.html', numH = numH, numV = numV, color1 = color1, color2 = color2)
    

if __name__=="__main__":
    app.run(debug=True)