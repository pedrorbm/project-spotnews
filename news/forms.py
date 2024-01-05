from django import forms
from .models import Category, News, User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields["name"].label = "Nome"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        self.fields["author"].label = "Autoria"
        self.fields["created_at"].label = "Criado em"
        self.fields["image"].label = "URL da Imagem"

        self.fields["title"].widget = forms.TextInput()
        self.fields["content"].widget = forms.Textarea()
        self.fields["author"].widget = forms.Select(
            choices=[(user.id, user.name) for user in User.objects.all()],
        )
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )
        self.fields["image"].widget = forms.FileInput()

        self.fields["categories"] = forms.ModelMultipleChoiceField(
            label="categories",
            queryset=Category.objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )
