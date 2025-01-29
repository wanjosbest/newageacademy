from django import forms

# Define the UserForm to handle user data
class userform(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email Address')
    age = forms.IntegerField(label='Age')

    # You can add custom validation if needed
    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        return age
