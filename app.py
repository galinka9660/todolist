from task import Task

tasks = []
# erstellt eine neue Aufgabe und fuegt diese der Aufgabenliste hinzu
def create_task():
    description = "Aufgabentext"
    task = Task(description)
    tasks.append(task)

# loescht Element i auf der liste Tasks
def delete_task(index):
    tasks.pop(index)

# zeigt die Aufgaben auf der Konsole an
def show_tasks():
    cntr = 0
    for task in tasks:
        print(f"{cntr} {task.desc}")
        cntr += 1

show_tasks()
while True:
    user_input = input("Was moechten Sie machen? Aufgabe erstellen - n, Aufgabe loeschen - d: ")
    if user_input == "n":
        create_task()
        show_tasks()
        

    if user_input == "d" and len(tasks) > 0:
        run = True
        while run:
            index = int(input("Welche Aufgabenummer wollen Sie loeschen? "))
            if index >= 0 and len(tasks) > index: 
                delete_task(index)
                show_tasks()
                run = False
            else:
                print("Keine gueltige Eingabe.")
                show_tasks()
    