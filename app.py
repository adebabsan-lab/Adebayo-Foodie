from flask import Flask, render_template

app = Flask(__name__)

recipes = [
    {"name":"Jollof Rice","image":"food6.jpg","description":"Classic Nigerian Party Jollof"},
    {"name":"Suya","image":"food2.jpg","description":"Northern Nigerian Grilled Beef"},
    {"name":"Asun","image":"food4.jpg","description":"Peppered Goat Meat"},
    {"name":"Dodo","image":"food8.jpg","description":"Fried Sweet Plantain"},
    {"name":"Street Food","image":"food1.jpg","description":"Popular Nigerian Street Food"},
    {"name":"Fish Rice","image":"food12.jpg","description":"Fresh Fish and Rice"}
]

@app.route("/")
def home():
    return render_template("index.html", recipes=recipes)

@app.route("/recipes")
def recipes_page():
    return render_template("recipes.html", recipes=recipes)

@app.route('/gallery')
def gallery():
    gallery_images = [
        'food1.jpg',
        'food2.jpg',
        'food3.jpg',
        'food4.jpg',
        'food5.jpg',
        'food6.jpg',
        'food7.jpg',
        'food8.jpg',
        'food9.jpg',
        'food10.jpg',
        'food11.jpg',
        'food12.jpg',
        'food13.jpg',
        'food14.jpg'
    ]

    return render_template(
        'gallery.html',
        images=gallery_images
    )
@app.route("/gallery")
def gallery():
    images = [f"food{i}.jpg" for i in range(1,15)]
    return render_template("gallery.html", images=images)

@app.route("/stories")
def stories():
    return render_template("stories.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
