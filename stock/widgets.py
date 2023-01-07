from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableImageInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'items/custom_widget_templates/custom_clearable_image_input.html')


class CustomClearableVideoInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Video')
    input_text = _('')
    template_name = (
        'items/custom_widget_templates/custom_clearable_video_input.html')
