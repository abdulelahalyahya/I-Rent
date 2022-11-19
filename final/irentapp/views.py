from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import items, ask



def add_items(request : HttpRequest):

    if request.method == "add":
        new_items = add_items(title=request.items["name"], content = request.items["content"], added_date=request.items["date"], is_added = request.POST["is_added"])
        new_items.save()


    return render(request, "irentpp/add_items.html")



def list_items(request: HttpRequest):

    if "search" in request.GET:
        items = items.objects.filter(title__contains=request.GET["search"])
    else:
        items = items.objects.all()

   
    return render(request, "irentapp/view_items.html", {"items" : items})



def items_details(request : HttpRequest, item_id : int):

    try:
        add = items.objects.get(id=items_id)
        question = question.objects.filter(items = items)
    except:
        return render(request , "irentpp/not_found.html")

    return render(request, "irentpp/items_detail.html", {"items" : items, "question" : questions})



def update_items HttpRequest: HttpRequest, post_id:int):

    try:
        items = items.objects.get(id=post_id)
    except:
        return render(request , "blogApp/not_found.html")

    if request.method == "POST":
        items.title = request.POST["title"]
        items.content = request.POST["content"]
        items.added_date = request.POST["added_date"]
        items.added = request.POST["is_added"]
        items.save()

        return redirect("blogApp:list_items")

    items.added_date = items.added_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "irentapp/update_items.html", {"items" : items})



def delete_items(request: HttpRequest, item_id:int):

    try:
        item = item.objects.get(id=item_id)
    except:
        return render(request ,"irentpp/not_found.html")

    items.delete()

    return redirect("irentapp:list_items")




def add_items(request: HttpRequest, items_id:int):
    item = item.objects.get(id=items_id)

    if request.method == "POST":
        new_comment = Comment(items=items, name = request.items["name"], content=request.items["content"])
        new_comment.save()

    
    return redirect("blogApp:items_detail", items.id)