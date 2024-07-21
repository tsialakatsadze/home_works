from flask import Flask, render_template, request, redirect, url_for

from models import db, Post

USER = 'postgres'
PASSWORD = 'spliyvi'
HOST = "localhost"
PORT = 5432
DATABASE = 'it_step_database'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/", methods=["GET"])
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/new", methods=["POST", "GET"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        answer = request.form["answer"]
        new_post = Post(title=title, content=content, answer=answer)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("new_post.html")


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.answer = request.form['answer']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_post.html', post=post)


@app.route("/delete/<int:post_id>", methods=["POST", "GET"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)

