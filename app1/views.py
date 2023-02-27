from django.shortcuts import render, redirect
from .models import Item, Comment
from accounts.models import Profile
from .forms import ItemForm, CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

#ホームページ
def index(request):
    item = Item.objects.order_by("-posted_at")
    try:
        user = Profile.objects.get(user = request.user)
        context = {'items': item, 'user': user}
    except:
        context = {'items' : item}
    return render(request, 'app1/index.html', context)

#貸出可能一覧
@login_required
def lending(request):
    item = Item.objects.filter(Q(category = 0) | Q(category = 1)).order_by("-posted_at")
    try:
        user = Profile.objects.get(user = request.user)
        context = {'items': item, 'user': user}
    except:
        context = {'items' : item}
    return render(request, 'app1/lending.html', context)

#リクエスト一覧
@login_required
def req(request):
    item = Item.objects.filter(category = 2).order_by("-posted_at")
    try:
        user = Profile.objects.get(user = request.user)
        context = {'items': item, 'user': user}
    except:
        context = {'items' : item}
    return render(request, 'app1/request.html', context)

#詳細画面
@login_required
def detail(request, item_id):
    item = Item.objects.get(pk = item_id)
    comments = Comment.objects.filter(item = item).order_by("-cmt_posted_at")
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('detail', item_id = item.id)
    context = {'item' : item, 'comments' : comments, 'form' : form}
    return render(request, 'app1/detail.html', context)

#アイテム投稿
@login_required
def item_upload(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    try:
        user = Profile.objects.get(user = request.user)
        if form.is_valid():
            item = form.save()
            return redirect('detail', item_id = item.id)
        context = {'form' : form, 'user': user}
    except:
        context = {'form' : form}
    
    return render(request, 'app1/item_upload.html', context)

#削除
@login_required
def item_deleted(request):
    return 0





    

