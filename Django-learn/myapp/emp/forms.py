from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email ID", required=False)
    name = forms.CharField(label="Name", max_length=20, required=False)
    feedback = forms.CharField(label="Feedback", max_length=2000, required=False)

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

