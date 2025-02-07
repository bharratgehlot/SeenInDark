# The Flask App will Show a Fact or unseen image that users have never seen before. It should be thought provoking, shocking and entertaning. 
# Testing Workflow Agains 
from flask import Flask, render_template
from datetime import datetime , timedelta
from models import db, Image


app = Flask(__name__)


#Configure SQLite database

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///seenindark.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Create the table if dont exists

with app.app_context():
     db.init_app(app)
     db.create_all()
      

@app.route('/')
def index():
    # Get today's date
    today = datetime.today().date()

    # Fetch the image for today
    image = Image.query.filter_by(date=today).first()

    if image:
        # Calculate the next image update time (at midnight of the next day)
        next_update = datetime.combine(today + timedelta(days=1), datetime.min.time())

        return render_template('index.html', 
                               image_path=image.image_path, 
                               description=image.description, 
                               date=image.date, 
                               next_update_date=next_update)
    
    return "No image found for today."


if __name__ == "__main__":
    app.run()
    
#debug=True, port=5000, host="0.0.0.0"    