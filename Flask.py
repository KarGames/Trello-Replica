from flask import Flask, render_template, url_for, request

app = Flask(__name__)

task = ""
date = ""

taskCards = []

@app.route("/trello", methods=["GET", "POST"])
def trello():
    if request.method == "POST":
        task = request.form.get("task")
        date = request.form.get("date")
        
        return render_template("trello.html", task = task, date = date)
        
        
    return render_template("trello.html")
    


class taskCard:
    def __init__(self, task, date):
        self.task = task
        self.date = date

print(task)
print(date)

if __name__ == "__main__":
    app.run(debug=True)