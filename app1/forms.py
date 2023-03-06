from django import forms
from .models import Item, Comment
 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('posted_at',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_name'].required = True
        self.fields['category'].required = True
        self.fields['description'].required = False
        self.fields['image'].required = False
    def validation_data(self):
        item_name = self.cleaned_data.get("item_name")
        category = self.cleaned_data.get("category")
        if not item_name:
            raise forms.ValidationError("アイテム名を入力してくだちい")
        if category != 0 or category != 1 or category != 2:
            raise forms.ValidationError("カテゴリを選択してくだちい")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('cmt_posted_at',)
        widgets = {
            'detail': forms.Textarea(attrs={'rows':1, 'cols':40}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['detail'].required = True



    