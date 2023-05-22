from flask import Flask, render_template, url_for, request

app = Flask(__name__)

task = ""
date = ""

taskCards = []
completedCards = []

class TaskCard:
    def __init__(self, task, date):
        self.task = task
        self.date = date

    def completeTask(self, taskCards, completedCards):
        taskCards.remove(self)
        completedCards.append(self)


@app.route("/", methods=["GET", "POST"])
def trello():
    if request.method == "POST":
        if request.form.get("task") or request.form.get("date"):
            task = request.form.get("task")
            date = request.form.get("date")

            if task == "" or date == "":
                return render_template("trello.html", taskCards = taskCards)
            
            taskCard = TaskCard(task, date)
            taskCards.append(taskCard)
            print(len(taskCards))
            
            return render_template("trello.html", taskCards = taskCards)
        else: 
            for task in taskCards:
                if request.form.get(str(taskCards.index(task))) == "Complete":
                    task.completeTask(taskCards, completedCards)
                    return render_template("trello.html", taskCards = taskCards)
            
        
    return render_template("trello.html")

if __name__ == "__main__":
    app.run(debug=True)