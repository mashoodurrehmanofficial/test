from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import * 
# Create your views here.
def index(request):  
    data = DjangoAjaxPosts.objects.all()
    return fetchpost(request,'Home')
    # return render(request, 'ajax-django-posts/django-ajax.html', {'posts':data})

def fetchpost(request,url): 
    data = DjangoAjaxPosts.objects.all()
    page_info = data.get(url=url)
    previous_item = data.filter(id=page_info.id-1).first()
    next_item = data.filter(id=page_info.id+1).first()
    pages = DjangoAjaxPosts.objects.all().exclude(url=url).exclude(url='Home')
    related_articles = random.sample(list(pages), len(pages)) 
    length1 = int((70*len(pages))/100) 
    if len(pages)<=10:length1=len(pages) 

    context = {
        'posts':data,
        'previous': previous_item,
        'next':next_item,
        'page_title':page_info.short_name,
        'article_heading': page_info.heading,
        'app_name': 'Django + Ajax', 
        'related_articles':related_articles[:length1],
        'bottom_articles':related_articles[length1:]
    }
    return render(request, f'ajax-django-posts/{url}/{url}.html', context)

def getcities(request, country):
    cities = {
        'China':['Beijing','Shanghai','Wuhan'],
        'England': ['London','Manchester','Oxford'],
        'Germany':['Berlin','Frankhart','Munich'],
    }  
    return JsonResponse({'cities':cities[country]})

def verifyemail(request, email):
    all_emails = ['asad@gmail.com','mashood@gmail.com', 'saad@gmail.com',] 
    if email.lower() in all_emails:
        availability = 'Email alredy exists'
    else:
        availability = ''
    return JsonResponse({'availability':availability})
import random

def loadmore(request): 
    numbers = [random.randint(1,100000000000000) for _ in range(10)]
    return JsonResponse({'numbers':numbers})


def getdata(request, country_name):     
    country_data = {
        
        'China':{
            'country_name': country_name,
            'intro': 'China is located in Asia',
            'capital': 'Beijing',
            'flag': 'https://www.countryflags.io/cn/flat/64.png' 
        },
        'England':{
            'country_name': country_name,
            'intro': 'England is not located in Europe',
            'capital': 'London',
            'flag': 'https://www.countryflags.io/gb/flat/64.png' 
        },
        'France':{
            'country_name': country_name,
            'intro': 'France is located in Europe',
            'capital': 'Paris',
            'flag': 'https://www.countryflags.io/fr/flat/64.png' 
        },
    }
    return JsonResponse({'data':country_data[country_name]})



def realtimeautocompletebox(request, query):  
    data = ['Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria', 'Bosnia and Herzegovina', 'Barbados', 'Wallis and Futuna', 'Saint Barthelemy', 'Bermuda', 'Brunei', 'Bolivia', 'Bahrain', 'Burundi', 'Benin', 'Bhutan', 'Jamaica', 'Bouvet Island', 'Botswana', 'Samoa', 'Bonaire, Saint Eustatius and Saba ', 'Brazil', 'Bahamas', 'Jersey', 'Belarus', 'Belize', 'Russia', 'Rwanda', 'Serbia', 'East Timor', 'Reunion', 'Turkmenistan', 'Tajikistan', 'Romania', 'Tokelau', 'Guinea-Bissau', 'Guam', 'Guatemala', 'South Georgia and the South Sandwich Islands', 'Greece', 'Equatorial Guinea', 'Guadeloupe', 'Japan', 'Guyana', 'Guernsey', 'French Guiana', 'Georgia', 'Grenada', 'United Kingdom', 'Gabon', 'El Salvador', 'Guinea', 'Gambia', 'Greenland', 'Gibraltar', 'Ghana', 'Oman', 'Tunisia', 'Jordan', 'Croatia', 'Haiti', 'Hungary', 'Hong Kong', 'Honduras', 'Heard Island and McDonald Islands', 'Venezuela', 'Puerto Rico', 'Palestinian Territory', 'Palau', 'Portugal', 'Svalbard and Jan Mayen', 'Paraguay', 'Iraq', 'Panama', 'French Polynesia', 'Papua New Guinea', 'Peru', 'Pakistan', 'Philippines', 'Pitcairn', 'Poland', 'Saint Pierre and Miquelon', 'Zambia', 'Western Sahara', 'Estonia', 'Egypt', 'South Africa', 'Ecuador', 'Italy', 'Vietnam', 'Solomon Islands', 'Ethiopia', 'Somalia', 'Zimbabwe', 'Saudi Arabia', 'Spain', 'Eritrea', 'Montenegro', 'Moldova', 'Madagascar', 'Saint Martin', 'Morocco', 'Monaco', 'Uzbekistan', 'Myanmar', 'Mali', 'Macao', 'Mongolia', 'Marshall Islands', 'Macedonia', 'Mauritius', 'Malta', 'Malawi', 'Maldives', 'Martinique', 'Northern Mariana Islands', 'Montserrat', 'Mauritania', 'Isle of Man', 'Uganda', 'Tanzania', 'Malaysia', 'Mexico', 'Israel', 'France', 'British Indian Ocean Territory', 'Saint Helena', 'Finland', 'Fiji', 'Falkland Islands', 'Micronesia', 'Faroe Islands', 'Nicaragua', 'Netherlands', 'Norway', 'Namibia', 'Vanuatu', 'New Caledonia', 'Niger', 'Norfolk Island', 'Nigeria', 'New Zealand', 'Nepal', 'Nauru', 'Niue', 'Cook Islands', 'Kosovo', 'Ivory Coast', 'Switzerland', 'Colombia', 'China', 'Cameroon', 'Chile', 'Cocos Islands', 'Canada', 'Republic of the Congo', 'Central African Republic', 'Democratic Republic of the Congo', 'Czech Republic', 'Cyprus', 'Christmas Island', 'Costa Rica', 'Curacao', 'Cape Verde', 'Cuba', 'Swaziland', 'Syria', 'Sint Maarten', 'Kyrgyzstan', 'Kenya', 'South Sudan', 'Suriname', 'Kiribati', 'Cambodia', 'Saint Kitts and Nevis', 'Comoros', 'Sao Tome and Principe', 'Slovakia', 'South Korea', 'Slovenia', 'North Korea', 'Kuwait', 'Senegal', 'San Marino', 'Sierra Leone', 'Seychelles', 'Kazakhstan', 'Cayman Islands', 'Singapore', 'Sweden', 'Sudan', 'Dominican Republic', 'Dominica', 'Djibouti', 'Denmark', 'British Virgin Islands', 'Germany', 'Yemen', 'Algeria', 'United States', 'Uruguay', 'Mayotte', 'United States Minor Outlying Islands', 'Lebanon', 'Saint Lucia', 'Laos', 'Tuvalu', 'Taiwan', 'Trinidad and Tobago', 'Turkey', 'Sri Lanka', 'Liechtenstein', 'Latvia', 'Tonga', 'Lithuania', 'Luxembourg', 'Liberia', 'Lesotho', 'Thailand', 'French Southern Territories', 'Togo', 'Chad', 'Turks and Caicos Islands', 'Libya', 'Vatican', 'Saint Vincent and the Grenadines', 'United Arab Emirates', 'Andorra', 'Antigua and Barbuda', 'Afghanistan', 'Anguilla', 'U.S. Virgin Islands', 'Iceland', 'Iran', 'Armenia', 'Albania', 'Angola', 'Antarctica', 'American Samoa', 'Argentina', 'Australia', 'Austria', 'Aruba', 'India', 'Aland Islands', 'Azerbaijan', 'Ireland', 'Indonesia', 'Ukraine', 'Qatar', 'Mozambique']
    data = [x for x in data if x.lower().startswith(query.lower())] 
    return JsonResponse({'data':data})