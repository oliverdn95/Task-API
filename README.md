# 📝Task API📝

Need to install [To Do App](https://github.com/oliverdn95/To-Do-App) to work.

This project was generated using [Django](https://www.djangoproject.com/download/) version 5.1.5.

Done by [Danilo Araújo de Oliveira](https://www.linkedin.com/in/oliverdn95/)

## Content

- [What is needed to run this APP?](#running-this-app-)
- [Used Techs](#techs)
- [Features](#features)
  1. [Route 'get-tasks'](#route-get-tasks)
  2. [Route 'create_task'](#route-create_task)
  3. [Route 'task_detail'](#route-task_detail)
  4. [Route 'task_done'](#route-task_done)
  5. [Route 'updateOrder'](#route-updateorder)
- [How to Test/Edit](#development-server)
- [Special Thanks](#special-thankss)


## Running this APP 👨‍💻
First you need to download my [To Do App](https://github.com/oliverdn95/To-Do-App).

Make sure you have [Python Installing Packaging](https://packaging.python.org/en/latest/tutorials/installing-packages/) installed.

Open terminal in the Api root folder, run:
```bash
pip install -r requirements.txt
```

After installing all packages, you can test the App:
```bash
py manage.py runserverr
```

remember that you at this point need to "ng serve" on APP too.

## Techs
Django v5.1.5 .

Django Cors Headers v4.6.0 .

Django Rest Framework v3.15.2 .

SqlParse v0.5.3 .

ASGIRef v3.8.1 .

TzData v2025.1 .


## Features
This is a Task api, you can test some endpoints. 🗂️

`http://localhost:8000/tasks/` 

it will show all endpoints you can access.

### Route 'get-tasks'
`http://localhost:8000/tasks/tasks/`

This route will return all tasks in the DB. 🎫
 

### Route 'create_task'
`http://localhost:8000/tasks/create/`

None of the fields are required to create/edit a Task. An created task will look like this.

```
taskObj = {
    id: number,
    name: string,
    status: string,
    priority: string,
    complexity: string,
    summary: string,
    index: number,
} 
```

Name field expect you a max of 100 char.
Status field expect to be either `todo`, `working` or `done`.
Priority and Complexity field expect to be either `low`, `medium` or `high`.
Summary field expect you a max of 500 char.
Index field is a num that is updated by the order of Tasks on [To Do App](https://github.com/oliverdn95/To-Do-App). 🎫

### Route 'task_detail'
`http://localhost:8000/tasks/tasks/<int:pk>`

When access this route it expect you to use an `integer` as parameter, it allows you to use the Methods: `GET`, `PUT`, `DELETE`.

On Method `GET`:
- it will return the task with this specific `id`.

On Method `PUT`:
- it will edit and return the task with this specific `id`.
- for this route a requisition is required.

On Method `DELETE`:
- it will delete a specific task bearer of this `id`.🎫

### Route 'task_done'
`http://localhost:8000/tasks/done/<int:pk>`

This route will change the field `Status` to `done`, then return the task back. 🎫

### Route 'updateOrder'
`http://localhost:8000/tasks/update/`

This route expect to receive an object like this:

```
TaskList = {
    todoList: [];
    workingList: [];
    doneList: [];
}
```
You can send objects inside of each list, it will update the index and the status for each list. 🎫

## Special Thanks
Special Thanks to this two channels on yt who helped me understand/learn Angular. ❤️

[Learning Partner](https://www.youtube.com/@LearningPartnerDigital)

[FED Learning](https://www.youtube.com/@FEDLearning)