# 5000
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')



# 5000/ninjas

@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')





# 5000/dojos/new


@app.route('/dojo/new')
def dojos():
  return render_template('dojos.html')
if __name__ == '__main__':
    app.run(debug=True)
