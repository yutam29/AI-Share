from django.shortcuts import render, redirect
from .models import Item, Comment, Lending
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
    user = Profile.objects.get(user = request.user)
    item = Item.objects.filter(category = 2).order_by("-posted_at")
    try:
        user = Profile.objects.get(user = request.user)
        context = {'items': item, 'user': user}
    except:
        context = {'items' : item, 'user': user}
    return render(request, 'app1/request.html', context)

#詳細画面
@login_required
def detail(request, item_id):
    user = Profile.objects.get(user = request.user)
    item = Item.objects.get(pk = item_id)
    comments = Comment.objects.filter(item = item).order_by("-cmt_posted_at")
    form = CommentForm(request.POST or None)
    lendings = Lending.objects.filter(item = item).order_by("-posted_at")
    if form.is_valid():
        form.save()
        return redirect('detail', item_id = item.id)
    context = {'user' : user,
                'item' : item, 
               'comments' : comments, 
               'form' : form, 
               'lendings' : lendings,
               }
    return render(request, 'app1/detail.html', context)

#アイテム投稿
@login_required
def item_upload(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    try:
        user = Profile.objects.get(user = request.user)
        message = ""
        if request.method == 'POST':
            if form.is_valid():
                item = form.save()
                return redirect('detail', item_id = item.id)
            else:
                category = form.cleaned_data.get("category")
                if not category:
                    message = "形式を選択してくだちい"
        context = {'form' : form, 'user': user, 'message' : message}
    except:
        context = {'form' : form}
    
    return render(request, 'app1/item_upload.html', context)

@login_required
#貸出受付
def deliver_register(request, item_id):
    item = Item.objects.get(pk=item_id)
    user = Profile.objects.get(user = request.user)
    try:
        lending = Lending.objects.filter(item = item).get(lender = user)
    except:
        lending = Lending(
            lender = user,
            item = item
        )
        lending.save()
    return redirect('detail', item_id = item_id)


#貸出状態変更
@login_required
def change_state(request, list_id):
    lending = Lending.objects.get(pk=list_id)
    lending.state += 1
    lending.save()
    return redirect('detail', item_id = lending.item.id)

#削除
@login_required
def item_deleted(request):
    return 0





    

