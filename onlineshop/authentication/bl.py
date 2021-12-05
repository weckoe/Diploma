def create_new_user(user_form):
    new_user = user_form.save(commit=False)
    new_user.set_password(user_form.cleaned_data['password1'])
    new_user.save()
    return new_user
