from app import app, db
from models import Image
from datetime import date, timedelta

def insert_sample_data():
     # Get Todays Date
    today = date.today()
  
  # List of descriptions for each image
    descriptions = [
        "Description for image 1. This is a detailed explanation of image 1.",
        "Description for image 2. This is a detailed explanation of image 2.",
        "Description for image 3. This is a detailed explanation of image 3.",
        "Description for image 4. This is a detailed explanation of image 4.",
        "Description for image 5. This is a detailed explanation of image 5.",
        "Description for image 6. This is a detailed explanation of image 6.",
        "Description for image 7. This is a detailed explanation of image 7.",
        "Description for image 8. This is a detailed explanation of image 8.",
        "Description for image 9. This is a detailed explanation of image 9.",
        "Description for image 10. This is a detailed explanation of image 10.",
        "Description for image 11. This is a detailed explanation of image 11.",
        "Description for image 12. This is a detailed explanation of image 12.",
        "Description for image 13. This is a detailed explanation of image 13.",
        "Description for image 14. This is a detailed explanation of image 14.",
        "Description for image 15. This is a detailed explanation of image 15.",
        "Description for image 16. This is a detailed explanation of image 16.",
        "Description for image 17. This is a detailed explanation of image 17.",
        "Description for image 18. This is a detailed explanation of image 18.",
        "Description for image 19. This is a detailed explanation of image 19.",
        "Description for image 20. This is a detailed explanation of image 20.",
        "Description for image 21. This is a detailed explanation of image 21.",
        "Description for image 22. This is a detailed explanation of image 22.",
        "Description for image 23. This is a detailed explanation of image 23.",
        "Description for image 24. This is a detailed explanation of image 24.",
        "Description for image 25. This is a detailed explanation of image 25.",
        "Description for image 26. This is a detailed explanation of image 26.",
        "Description for image 27. This is a detailed explanation of image 27.",
        "Description for image 28. This is a detailed explanation of image 28.",
        "Description for image 29. This is a detailed explanation of image 29.",
        "Description for image 30. This is a detailed explanation of image 30."
    ]
  
  # Loop to generate 30 Days of data
  
    for i in range(30):
    # Create a new image record for each day
      new_image = Image(
         date= today + timedelta(days=i), # Set the date for each image for 30 days
         image_path= f"sample{i+1}.jpg",
         description=descriptions[i],
         shown = False
      )
      db.session.add(new_image)
      
    db.session.commit()
    print("Sample data inserted successfully!")
    
if __name__ == "__main__":
  with app.app_context():
    insert_sample_data()    