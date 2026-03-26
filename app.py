from flask import Flask, render_template
import random
import os

app = Flask(__name__)

PORTRAIT_IMAGE_PATH = "/static/portrait.jpg"  # Place your attached image here
GALLERY_IMAGES = [
    "/static/gallery1.jpg",
    "/static/gallery2.jpg",
    "/static/gallery3.jpg",
    "/static/gallery4.jpeg",
    "/static/gallery5.jpeg"
]

ABOUT_BIO = [
    "a man of faith, a builder, and a lifelong student of growth. My journey isn't about perfection; it's about showing up every single day with intention and heart.",
    "At my core, I am a giver. I genuinely believe that my purpose on this earth is to serve others and make lives better — it's what God would have me do. Whether it's lifting someone up through encouragement, showing up for my community, or collaborating as a teammate, I pour into people because that's where real fulfillment lives.",
    "We rise by lifting others. Through teamwork, collaboration, and building each other up, we don't just grow individually — we grow together. That's the mission. From the weight room to the tech world, from community softball games to corporate boardrooms — service is the thread that ties it all together."
]

@app.route('/')
def home():
    return render_template('card.html',
                           portrait_url=PORTRAIT_IMAGE_PATH,
                           about_bio=ABOUT_BIO,
                           gallery_ids=GALLERY_IMAGES)

@app.route('/gallery')
def gallery():
    return render_template('card.html',
                           portrait_url=PORTRAIT_IMAGE_PATH,
                           about_bio=ABOUT_BIO,
                           gallery_ids=GALLERY_IMAGES)

@app.route('/merch')
def merch():
    return render_template('card.html',
                           portrait_url=PORTRAIT_IMAGE_PATH,
                           about_bio=ABOUT_BIO,
                           gallery_ids=GALLERY_IMAGES)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
    