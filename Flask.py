from flask import Flask, render_template, url_for, request

app = Flask(__name__)

task = ""
date = ""

taskCards = []

class TaskCard:
    def __init__(self, task, date):
        self.task = task
        self.date = date

@app.route("/trello", methods=["GET", "POST"])
def trello():
    if request.method == "POST":
        task = request.form.get("task")
        date = request.form.get("date")
        
        taskCard = TaskCard(task, date)
        taskCards.append(taskCard)

        return render_template("trello.html", taskCards = taskCards)
        
    return render_template("trello.html")

if __name__ == "__main__":
    app.run(debug=True)