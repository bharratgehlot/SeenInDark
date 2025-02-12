#Port Removed
# TEST Push

from flask import Flask, render_template
from datetime import datetime, timedelta
from models import db, Image
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///seenindark.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the app and create tables inside the app context

'''
with app.app_context():
    db.init_app(app)
    db.create_all()
   '''
    
db.init_app(app)

with app.app_context():
    db.create_all()


# Global variable to store the latest image
latest_image = None

def update_image():
    global latest_image
    with app.app_context():
        today = datetime.today().date()
        latest_image = Image.query.filter_by(date=today).first()

@app.route('/')
def index():
    if latest_image:
        next_update = datetime.combine(datetime.today().date() + timedelta(days=1), datetime.min.time())
        next_update_str = next_update.isoformat()
        return render_template('index.html', 
                               image_path=latest_image.image_path, 
                               description=latest_image.description, 
                               date=latest_image.date, 
                               next_update_date=next_update_str)
    return "No image found for today."

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_image, 'cron', hour=0, minute=0)  # Runs at midnight
    scheduler.start()
    update_image()  # Load initial image
    app.run()
    
   #debug=True, port=5000, host="0.0.0.0"     