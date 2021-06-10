from django import forms

from .models import Post, Topic, Category


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': '¿Qué tienes en mente?'}
        ),
        max_length=4000,
        help_text='La longitud máxima del texto es 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'category', 'message']
        labels = {
            'subject': 'Titulo Hilo',
            'category': 'Categoria',
            'message': 'Mensaje',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
        labels = {
            'message': 'Mensaje',
        }


class CategoryForm(forms.ModelForm):
    category = forms.CharField(max_length=70)

    class Meta:
        model = Category
        fields = ['category', ]
        labels = {
            'category': 'Categoria',
        }
