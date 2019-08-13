from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about-me/">About me</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contact</a></li>
</ul>

"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + """
        <h2>Home</h2>
        <p>This is the Home</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>About me</h2>
        <p>Me llamo Dany y soy desarrollador web</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portfolio</h2>
        <p>Present my portfolio</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contact</h2>
        <p>Info to my email</p>
        <ul>
            <li><a href="mailto:hola@hektorprofe.net">Email</a></li>
            <li><a href="https://github.com/hcosta">Github</a></li>
            <li><a href="https://youtube.com">Youtube</a></li>
        </ul>
    """)