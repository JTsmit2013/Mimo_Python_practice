todo_list = []

while True:
  if len(todo_list) == 0:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  
  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")
  
  # User next step
  choice = input("What do you want to do (1, 2, or 3): ")
  if choice == "1":
    new_task = input("What task do you want to add?: ")
    todo_list.append(new_task)
    print(f"{new_task} added to the todo list")
  elif choice == '2':
    if len(todo_list) == 0:
      print("Your ToDo list is empty")
    todo_list.pop()
  elif choice == "3":
    print("Quitting")
    break
  else:
    print('not a valid request')
