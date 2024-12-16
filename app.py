from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas en memoria
tasks = []

# Ruta principal (GET y POST)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:  # Agregar nueva tarea
            tasks.append({"name": task, "done": False})
    return render_template("index.html", tasks=tasks)

# Ruta para marcar como completada
@app.route("/complete/<int:task_id>")
def complete(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id]["done"]
    return redirect(url_for("index"))

# Ruta para eliminar tarea
@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
