from django import forms
class feedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'Form-control',
                'placeholder':'your Name'

            }

        )
    )
    rating = forms.IntegerField(
        label="Enter your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'Form-control',
                'placeholder': 'your Rating'

            }

        )
    )
    feedback= forms.CharField(
        label="Enter your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'Form-control',
                'placeholder': 'your Feedback'

            }

        )
    )