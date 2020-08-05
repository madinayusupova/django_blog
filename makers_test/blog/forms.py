from django import forms

from .models import Category, Post


#
# class AddPostForm(forms.Form):
#     title =forms.CharField(max_length=255, required=True, strip=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
#     text = forms.CharField(required=True, widget=forms.Textarea)
#     image = forms.ImageField()

class AddPostForm(forms.ModelForm):






    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image', 'user')
        extra_kwargs = {'title':{'required':False}}










class UpdatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        post = kwargs.pop('instance')
        super(UpdatePostForm, self).__init__(*args, **kwargs)
        self.fields['title'].initial = post.title
        self.fields['category'].initial = post.category




    title = forms.CharField(max_length=255, required=False)
    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image')

