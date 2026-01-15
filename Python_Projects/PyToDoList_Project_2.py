import os

def get_task_id():
    try:
        with open(os.path.join(os.getcwd(),"todo_list.txt"),'r') as f:
            content = f.readlines()
            id = int(content[-1][0]) + 1
        return id
    except:
        id = 1
        return id

def add_new_todo_task(task_name):
    with open(os.path.join(os.getcwd(),'todo_list.txt'),'a+') as f:
        ## Todo List Format : task_id, task_name, task_completion
        id = get_task_id()
        todo_task = str(id)+","+str(task_name)+",False\n"
        f.write(todo_task)
    
    print(f"\nNew TODO Task - {id} : {task_name} has been added Successfully!")

def remove_from_todo_task(task_id):
    removed_list = []
    file_name = 'todo_list.txt'
    with open(os.path.join(os.getcwd(),file_name),'r') as f:
        todo_content = f.readlines()
        for task in todo_content:
            if task_id!=int(task.split(',')[0]):
                removed_list.append(task)
        with open(os.path.join(os.getcwd(),file_name),'w+') as f_write:
            f_write.writelines(removed_list)
    if len(removed_list)<len(todo_content):
        print(f"\nTODO Task - {task_id} has been removed Successfully!")
    else:
        print(f"\nInValid TODO Task ID: {task_id}")

def complete_todo_task(task_id):
    with open(os.path.join(os.getcwd(),'todo_list.txt'),'r') as f:
        new_task_list = []
        f_content = f.readlines()
        for task in f_content:
            if int(task.split(',')[0]) == task_id:
                updated_content = str(task_id)+","+task.split(',')[1]+",True\n"
                new_task_list.append(updated_content)
            else:
                new_task_list.append(task)
        with open(os.path.join(os.getcwd(),'todo_list.txt'),'w+') as f_write:
            f_write.writelines(new_task_list)
    print(f"\nTODO Task - {task_id} has been marked as Completed Successfully!")

def get_all_active_todo_tasks():
    with open(os.path.join(os.getcwd(),'todo_list.txt'),'r') as f:
        f_content = f.readlines()
    print(f"\nList of Active TODO Tasks: \n")
    print('task_id,task_name,task_completion')
    for task in f_content:
        task_completion = task.split(',')[-1].lower().removesuffix('\n')
        if task_completion == 'false':
            print(task.removesuffix('\n'))

print("============================Welcome to PyTODOList==================================")
print("=============Press 1: To Add the New Task in TODO List=============================")
print("=============Press 2: To Remove the Existing Task from TODO List===================")
print("=============Press 3: To Complete the Existing TODO List Task =====================")
print("=============Press 4: To Get All the Active Tasks from TODO List ==================")

user_option = int(input())
if user_option == 1:
    get_all_active_todo_tasks()
    task_name = input("\nEnter the Task to be added in the TODO List: ")
    add_new_todo_task(task_name)
    get_all_active_todo_tasks()
elif user_option == 2:
    get_all_active_todo_tasks()
    task_id = int(input("\nEnter the Task to be removed from the TODO List: "))
    remove_from_todo_task(task_id)
    get_all_active_todo_tasks()
elif user_option == 3:
    get_all_active_todo_tasks()
    task_id = int(input("\nEnter the Task to be marked as Completed in TODO List: "))
    complete_todo_task(task_id)
    get_all_active_todo_tasks()
elif user_option == 4:
    get_all_active_todo_tasks()