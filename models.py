class TodoList:
    def __init__(self, task_list):
        self.todo_list = task_list
        self.count = len(task_list)

    @property
    def undone_list(self):
        return list(filter(lambda item: not item['done'], self.todo_list))

    @property
    def done_list(self):
        return list(filter(lambda item: item['done'], self.todo_list))


todo_list = [
    {"id": 0, "info": "Racing car sprays burning fuel into crowd.", "done": True},
    {"id": 1, "info": "Japanese princess to wed commoner.", "done": False},
    {"id": 2, "info": "Australian walks 100km after outback crash.", "done": False},
    {"id": 3, "info": "Man charged over missing wedding girl.", "done": True},
    {"id": 4, "info": "Los Angeles battles huge wildfires.", "done": False}
]

todo = TodoList(todo_list)
