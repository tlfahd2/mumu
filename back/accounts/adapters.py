# from allauth.account.adapter import DefaultAccountAdapter

# class CustomAccountAdapter(DefaultAccountAdapter):
    
#     def save_user(self, request, user, form, commit=False):
#         user = super().save_user(request, user, form, commit)
#         data = form.cleaned_data
#         user.name = data.get('name')
#         user.year = data.get('year')
#         user.month = data.get('month')
#         user.day = data.get('day')
#         user.gender = data.get('gender')
#         # if name:
#         #     user.name = name
#         # if year:
#         #     user.year = year
#         # if month:
#         #     user.month = month
#         # if day:
#         #     user.day = day
#         # if gender:
#         #     user.gender = gender
#         user.save()
#         return user