from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from chat.forms import *

@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)

def index(request):
    return render(request, "index.html")
   

def index1(request):
    return render(request, '404-2.html',)
def index2(request):
    return render(request, '404.html',)
def index3(request):
    return render(request, 'about-company.html',)
def index4(request):
    return render(request, 'about.html',)
def index5(request):
    return render(request, 'blog-detail.html',)
def index6(request):
    return render(request, 'blog-grid-left-sidebar.html',)
def index7(request):
    return render(request, 'blog-grid-right-sidebar.html',)
def index8(request):
    return render(request, 'blog-grid-wo-sidebar.html',)
def index9(request):
    return render(request, 'blog-list-left-sidebar.html',)
def index10(request):
    return render(request, 'blog-list-right-sidebar.html',)
def index11(request):
    return render(request, 'blog-list-wo-sidebar.html',)
def index12(request):
    return render(request, 'blog-masonry.html',)
def index13(request):
    return render(request, 'career-detail.html',)
def index14(request):
    return render(request, 'careers.html',)
def index15(request):
    return render(request, 'chosen-sprite.html',)
def index16(request):
    return render(request, 'chosen-sprite@2x.html',)
def index17(request):
    return render(request, 'contact-branches.html',)
def index18(request):
    return render(request, 'contact.html',)
def index19(request):
    return render(request, 'create-fav-page.html',)
def index20(request):
    return render(request, 'edit-account-setting.html',)
def index21(request):
    return render(request, 'edit-interest.html',)
def index22(request):
    return render(request, 'edit-password.html',)
def index23(request):
    if request.method == 'POST':
        form = UserInfoFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data added successfully')
        else:
            return HttpResponse(form.errors)
    else:
        form = UserInfoFrom()
    return render(request, 'edit-profile-basic.html', {'form': form})
def index24(request):
    return render(request, 'edit-work-eductation.html',)
def index25(request):
    return render(request, 'faq.html',)
def index26(request):
    return render(request, 'fav-page.html',)
def index27(request):
    return render(request, 'forum-create-topic.html',)
def index28(request):
    return render(request, 'forum-open-topic.html',)
def index29(request):
    return render(request, 'forum.html',)
def index30(request):
    return render(request, 'forums-category.html',)
def index31(request):
    return render(request, 'friends-list.html',)
def index32(request):
    return render(request, 'groups.html',)
def index33(request):
    return render(request, 'images.html',)
def index34(request):
    return render(request, 'inbox.html',)
def index35(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
    else:
        form = PostForm()
    return render(request, 'index-2.html', {'form': form})

def index36(request):
    return render(request, 'insight.html',)
def index37(request):
    return render(request, 'insights.html',)
def index38(request):
    return render(request, 'knowledge-base.html',)
def index39(request):
    if request.method == 'POST':
        form = CustomerDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
        else:
            return render(request,'index.html')
    else:
        form = CustomerDetailForm()
    return render(request, 'landing.html', {'form': form})

    return render(request, 'landing.html',)
def index40(request):
    return render(request, 'location.html',)
def index41(request):
    return render(request, 'login.html',)
def index42(request):
    return render(request, 'logout.html',)

def index44(request):
    return render(request, 'newsfeed.html',)
def index45(request):
    return render(request, 'notifications.html',)
def index46(request):
    return render(request, 'owl.video.play.html',)
def index47(request):
    return render(request, 'page-likers.html',)
def index48(request):
    return render(request, 'page.html',)
def index49(request):
    return render(request, 'people-nearby.html',)
def index50(request):
    return render(request, 'portfolio-2colm.html',)
def index51(request):
    return render(request, 'portfolio-3colm.html',)
def index52(request):
    return render(request, 'portfolio-4colm.html',)
def index53(request):
    return render(request, 'portfolio-detail.html',)
def index54(request):
    return render(request, 'shop-cart.html',)
def index55(request):
    return render(request, 'shop-checkout.html',)
def index56(request):
    return render(request, 'shop-masonry.html',)
def index57(request):
    return render(request, 'shop.html',)
def index58(request):
    return render(request, 'sitemap.html',)
def index59(request):
    return render(request, 'support-and-help-detail.html',)
def index60(request):
    return render(request, 'support-and-help-search-result.html',)
def index61(request):
    return render(request, 'support-and-help.html',)
def index62(request):
    return render(request, 'terms.html',)
def index63(request):
    return render(request, 'time-line.html',)
def index64(request):
    return render(request, 'timeline-friends.html',)
def index65(request):
    return render(request, 'timeline-groups.html',)
def index66(request):
    return render(request, 'timeline-pages.html',)
def index67(request):
    return render(request, 'timeline-photos.html',)
def index68(request):
    return render(request, 'timeline-videos.html',)
def index69(request):
    return render(request, 'videos.html',)
def index70(request):
    return render(request, 'widgets.html',)
def index71(request):
    return render(request, 'index-company.html',)
def index72(request):
    
    return render(request, 'index2.html',)
def index73(request):
    return render(request, 'shop-single.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate user against the customer_details model
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # User authentication successful, log in the user
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                # User authentication failed, display error message
                return render(request, 'landing.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'landing.html', {'form': form})
