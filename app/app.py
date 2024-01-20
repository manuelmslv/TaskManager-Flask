from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

tasks=[]
task_id_counter = 1 ##ID único para identificar cada tarea en la lista de tareas

#Redirecciona todas las peticiones al index
@app.route("/")
def reload_index ():
    return render_template("index.html")


@app.route("/index", methods=["GET", "POST"])
def index(): 
    """
    Función que crea y lista los objetivos.
    Si el método es POST, crea una nueva tarea y la agrega a la lista de tareas.
    Independientemente del método, renderiza la plantilla index.html con las tareas.
    """
    global task_id_counter
    if request.method == "POST":
        new_task = request.form.get("task")
        task = {"task_id":task_id_counter, "task_name": new_task}
        tasks.append(task)
        task_id_counter +=1
        return redirect(url_for("index"))  # Cambia esto a tu ruta de formulario
    
    return render_template("index.html", tasks=tasks)

@app.route("/delete_task", methods=["POST"])
def delete_task(): 
    """
    Función para eliminar tareas.
    Si el método es POST, recupera el ID de la tarea del formulario y busca esa tarea en la lista de tareas.
    Si encuentra la tarea, la elimina de la lista.
    Independientemente de si se eliminó una tarea o no, redirige al usuario a la página de inicio.
    """
    if request.method == "POST":
        task_id_to_delete = int(request.form.get("task_id"))
        for task in tasks:
            if task["task_id"] == task_id_to_delete:
                tasks.remove(task)
                break
        return redirect(url_for("index")) 
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)

