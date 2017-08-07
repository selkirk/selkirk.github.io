from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def route_home():
    return render_template('home.html')
    
@app.route("/selfkirk")
def route_selfkirk():
    return render_template('selfkirk.html')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  app.run('0.0.0.0', debug=True, port=port)