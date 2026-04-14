def task():
    tasks=[]

    print("---welcome---")
    tasks_input=int(input("enter total no.of tasks"))
    for i in range(1 , tasks_input+1):
        task_name=input("enter task:")
        tasks.append(task_name)
    print(f"total tasks are:\n{tasks}") 

    while True:
        operations=int(input("enter 1-add , 2-del , 3-view , 4-replace/update 5- stop/exit :"))
        if operations==1:
            add_task=input("enter task: ")
            tasks.append(add_task)
            print("the task is added succesfully")
        elif operations==2:    
            del_task=input("enter task: ")
            if del_task in tasks :
                ind_task=tasks.index(del_task)
                tasks.pop(ind_task)
                print("task is deleted")
            else :
                print("task not found")
        elif operations==3 :
            print(f"tasks are {tasks}")
        elif operations==4:
            update_val=input("enter task to replace/update: ")
            if update_val in tasks :
                replaced_task=input("enter new task : ")
                ind_task=tasks.index(update_val)
                tasks[ind_task]=replaced_task
                print("the task is updated/replaced")
            else:
                print("no task found")    
        else:
            break        
        
task()