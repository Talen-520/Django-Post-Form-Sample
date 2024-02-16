from django.shortcuts import render

from myapp.forms import  CommentForm
from .models import UserComments
from django.http import JsonResponse

# Create your views here.
def form_view(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST) #form data user entered 
        if form.is_valid():
            cd = form.cleaned_data #result of clean data function on the form object, helps data normalization
            uc = UserComments( #send data to uc and assign it to user model class
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment']
            )
            # prevent same user leave mutiple comments 
            # if UserComments.objects.filter(first_name=uc.first_name, last_name=uc.last_name, comment=uc.comment).exists():
            #    return JsonResponse({'message': 'You have already left this comment.'})
            # else:
            uc.save() #update model data

            return JsonResponse({
                'message':'success'
            })
    return render(request,'blog.html',{'form':form})

