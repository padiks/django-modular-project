# core/views.py
from django.shortcuts import render
from django.http import HttpResponse, Http404
from pathlib import Path
from django.conf import settings
import markdown

def render_markdown_view(request):
    # Static content, you can update this later as per requirement.
    content = "Your markdown content goes here"
    return render(request, 'markdown_renderer.html', {'content': content})

def render_markdown_file(request, filename):
    # Construct the path to the markdown file in static/markdown folder
    markdown_file_path = Path(settings.BASE_DIR) / 'static' / 'markdown' / f'{filename}.md'
    
    # Check if the file exists
    if markdown_file_path.exists():
        # Read the content of the markdown file
        with open(markdown_file_path, 'r') as file:
            content = file.read()
        
        # Convert markdown content to HTML using the markdown library
        html_content = markdown.markdown(content, extensions=['fenced_code', 'codehilite', 'tables'])
        
        # Return the rendered HTML content to the template
        return render(request, 'markdown_renderer.html', {'content': html_content})
    else:
        raise Http404(f"File '{filename}.md' not found.")
