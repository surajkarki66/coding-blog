from django.views.generic import TemplateView


class HomePageView(TemplateView):

    template_name = 'users/home.html'

    def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'users/index.html', context)
    else:
        firstname = 'Suraj'
        lastname = 'Karki'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'users/index.html', context)



