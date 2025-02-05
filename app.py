# The Flask App will Show a Fact or unseen image that users have never seen before. It should be thought provoking, shocking and entertaning. 

from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
  today = datetime.date.today()
  return render_template('index.html', date=today)

if __name__ == "__main__":
  app.run(debug=True, port = 5000)