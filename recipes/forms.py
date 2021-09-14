from django import forms
from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    # name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Recipe Name', }))
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    # directions = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Recipe
        fields = ('name', 'description', 'directions')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            attributes = {
                "placeholder": f"Recipe {str(field)}",
                "class": "form-control",
                # "hx-post": "",
                # "hx-trigger": "keyup changed delay:500ms",
                # "hx-target": "#recipe-container",
                # "hx-swap": "innerHTML",
            }
            self.fields[str(field)].widget.attrs.update(attributes)

        # self.fields['name'].label = ""
        # self.fields['name'].help_text = "This is help_text !!!!<a href='#'>Contact Us</a>"
        # self.fields['name'].widget.attrs.update(
        #     {"class": "form-control-2", 'placeholder': 'Recipe Name'})

        self.fields['description'].widget.attrs.update({"rows": 2})
        self.fields['directions'].widget.attrs.update({"rows": 4})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ('name', 'quantity', 'unit')
