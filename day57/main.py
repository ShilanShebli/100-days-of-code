from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_list = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_list.append(post_obj)

@app.route('/')
def home():
    api = "https://api.npoint.io/c790b4d5cab58020d391"
    requested_posts = requests.get(api).json()
    return render_template("index.html", posts=requested_posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_list:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, index=requested_post.id)




if __name__ == "__main__":
    app.run(debug=True)
