from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import BorrowRecord

class BorrowRecordForm(forms.ModelForm):
    content_type = forms.ModelChoiceField(queryset=ContentType.objects.all())
    object_id = forms.IntegerField()
    item = forms.ModelChoiceField(queryset=ContentType.objects.none())
    class Meta:
        model = BorrowRecord
        fields = ['borrower', 'borrow_date', 'return_date']
        widgets = {
            'borrow_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'return_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(BorrowRecordForm, self).__init__(*args, **kwargs)
        # set input formats for datetime-local
        self.fields['borrow_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['return_date'].input_formats = ('%Y-%m-%dT%H:%M',)

    def clean_return_date(self):
        return_date = self.cleaned_data.get('return_date')
        borrow_date = self.cleaned_data.get('borrow_date')
        if return_date and borrow_date and return_date < borrow_date:
            raise forms.ValidationError("Return date cannot be before borrow date.")
        return return_date