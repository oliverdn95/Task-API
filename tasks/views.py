from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import TaskSerializer

@api_view(["GET"])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# ChatGPT me sugeriu instalar o CORS após eu comentarr sobre o erro de requisição que eu recebis
@api_view(["POST"])
def create_task(request):
  serializer = TaskSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def task_detail(request, pk):
   try:
      task = Task.objects.get(pk=pk)
   except Task.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == "GET":
      serializer = TaskSerializer(task)
      return Response(serializer.data)
   
   elif request.method == "PUT":
      serializer = TaskSerializer(task, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   elif request.method == "DELETE":
      task.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
   
@api_view(["PUT"])
def task_done(request, pk):
   try:
      task = Task.objects.get(pk=pk)
      task.status = "done"
      task.save()

      serializer = TaskSerializer(task)
      return Response(serializer.data)
   except Task.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(["PUT"])
def updateOrder(request):
   order = 0
   todo_list = request.data.get("todoList", [])
   working_list = request.data.get("workingList", [])
   done_list = request.data.get("doneList", [])

   for task in todo_list:
      try:
         oldTask = Task.objects.get(id=task["id"])

         if oldTask.index != task["index"] or oldTask.status != task["status"]:
            task["status"] = "todo"
            task["index"] = order
            serializer = TaskSerializer(oldTask, data=task)
            if serializer.is_valid():
               serializer.save()
            else:
               print("tarefa não encontrada")
               continue
         order += 1
      except Task.DoesNotExist:
         continue

   order = 0
   for task in working_list:
      try:
         oldTask = Task.objects.get(id=task["id"])

         if oldTask.index != task["index"] or oldTask.status != task["status"]:
            task["status"] = "working"
            task["index"] = order
            serializer = TaskSerializer(oldTask, data=task)
            if serializer.is_valid():
               serializer.save()
            else:
               print("tarefa não encontrada")
               continue
         order += 1
      except Task.DoesNotExist:
         continue

   order = 0
   for task in done_list:
      try:
         oldTask = Task.objects.get(id=task["id"])

         if oldTask.index != task["index"] or oldTask.status != task["status"]:
            task["status"] = "done"
            task["index"] = order
            serializer = TaskSerializer(oldTask, data=task)
            if serializer.is_valid():
               serializer.save()
            else:
               print("tarefa não encontrada")
               continue
         order += 1
      except Task.DoesNotExist:
         continue

   return Response(status=status.HTTP_202_ACCEPTED)