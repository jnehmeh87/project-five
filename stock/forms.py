from django import forms
from .widgets import CustomClearableImageInput, CustomClearableVideoInput
from .models import Item, Category


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableImageInput)
    video = forms.FileField(
        label='Video', required=False, widget=CustomClearableVideoInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
