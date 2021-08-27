from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')

    def clean(self):
        data = self.cleaned_data

        title = data.get('title')
        content = data.get('content')

        qs_title = Article.objects.filter(title__icontains=title)
        qs_content = Article.objects.filter(content__icontains=content)

        if qs_title.exists():
            self.add_error('title', f"{title} is already in use")

        if qs_content.exists():
            self.add_error('title', f"{content} is already in use")

        return data


class ArticleFormRaw(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')

    #     if title.lower().strip() == 'the office':
    #         raise forms.ValidationError('This title is taken.')
    #     return title

    # def clean_content(self):
    #     cleaned_data = self.cleaned_data
    #     content = cleaned_data.get('content')
    #     return content

    def clean(self):
        cleaned_data = self.cleaned_data
        print("cleaned_data", cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title.lower().strip() == 'the office':
            self.add_error('title', 'This title is taken.')

        if 'office' in content.lower().strip() or 'office' in title.lower().strip():
            self.add_error('content', "Office is can not be allowed")
            raise forms.ValidationError('Office is not allowed')
        return cleaned_data
