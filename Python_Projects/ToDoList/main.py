class ToDo:
    '''
    Task: Create a to do list -
    1) Add a task
    2) Remove a task
    3) Update a task
    4) Display the task list
    5) Clear the task list
    
    Still thinking of more tasks ...
    '''
    def __init__(self):
        self.tasklist = ['a', 'b', 'c']
    
    def add_task(self, userTask):
        self.tasklist.append(userTask)
        self.display_tasklist()

    def update_task(self, taskIndex, userTask):
        self.tasklist[taskIndex-1] = userTask
        self.display_tasklist()
    
    def remove_task(self, taskIndex):
        self.tasklist.pop(taskIndex-1)
        self.display_tasklist()
    
    def clear_tasklist(self):
        print('PLease confirm your decision to clear the To-DO list.')
        print('Enter Yes or No : ')
        decision = input()
        if decision == 'No':
            self.display_tasklist()    
        elif decision == 'Yes':
            self.tasklist = []
            self.display_tasklist()
        else:
            print('Please enter an accepted option')
            self.clear_tasklist()

    def display_tasklist(self):
        if not self.tasklist:
            print('TO-DO List')
            print("Please enter some tasks to create the To-Do list")
        print('TO-DO List')
        for i in range(len(self.tasklist)):
            print(f'Task {i+1}: {self.tasklist[i]}')

if __name__ == "__main__":
    task1 = ToDo()
    task1.display_tasklist()
    task1.add_task('d')
    task1.remove_task(2)
    task1.add_task('fgh')
    task1.update_task(3, 'this is the best')
    task1.clear_tasklist()