task_list = []

while True:
    task = input("Entrez la tâche à effectuer : ")
    if task == "q":
        break
    task_list.append(task)




def show_task_list():
    print("To Do List")
    for task in task_list:
        print("- " + task)