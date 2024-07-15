def task():
    tasks = []
    print("-----Welcome To The Task Management App-----")
    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(total_task):
        task_name = input(f"Enter task {i + 1}: ")
        tasks.append(task_name)
    
    print(f"Today's tasks are: {tasks}")

    while True:
        print("\nOptions:")
        print("1 = Add")
        print("2 = Update")
        print("3 = Delete")
        print("4 = View")
        print("5 = Exit")
        
        operation = int(input("Choose an option: "))
        
        if operation == 1:
            add = input("Enter your new task: ")
            tasks.append(add)
            print(f"Task '{add}' has been added successfully.")
        
        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' has been updated to '{up}'.")
            else:
                print(f"Task '{updated_val}' not found.")
        
        elif operation == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print(f"Task '{del_val}' not found.")
        
        elif operation == 4:
            print(f"Total tasks: {tasks}")
        
        elif operation == 5:
            print("Closing the program...")
            break
        
        else:
            print("Invalid input. Please try again.")

# Call the function to run the task management app
task()