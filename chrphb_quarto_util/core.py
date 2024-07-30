# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['posts_dir', 'template_dir', 'wbr_template_dir', 'create_post', 'generate_file_content', 'create_post_from_template']

# %% ../nbs/00_core.ipynb 4
import os
from datetime import date
import shutil

# Parent Directory path 
posts_dir = "/home/chris/ws/journal/posts"
# posts_dir = "/home/chris/tmp"
template_dir = "/home/chris/ws/journal/templates/morning"
wbr_template_dir = "/home/chris/ws/journal/templates/wbr"

def create_post(title):
    """
      Creates a new Post entry in the Journal
      The path of the post is based on the current date
    """
    today = date.today()
    name = str(today)+'-'+title
    print(name)
    # Path 
    path = os.path.join(posts_dir, name) 
    os.mkdir(path) 
    print(f"Directory created {name}") 
    src = template_dir + "/index.ipynb"
    dst = posts_dir + "/" + name + "/index.ipynb"
    shutil.copyfile(src, dst)
    print(f"Template copied from {src} to {dst}")

# %% ../nbs/00_core.ipynb 6
def generate_file_content(src, dst):
    """
      Generates the file content
    """
    from locale import setlocale, LC_TIME
    setlocale(LC_TIME, 'fr_FR.UTF-8')
    today = date.today()
    # format the date today in french with full names for week day and month 
    today_fr = today.strftime("%A %d %B %Y")
    # use the french locale for the strftime of today_fr
    #today_fr = today_fr.format(fr_FR)
    print(today_fr)
    # open the file with path src in read mode
    with open(src, "r") as file:
        content = file.read()
        # in the content string, replace $DATE with "hello"
        content = content.replace("$DATE", str(today))
        content = content.replace("$TITLE", today_fr)
        #print(content)
        # open the file with path dst in write mode, encoding utf-8
        with open(dst, "w", encoding="utf-8") as outfile:
            outfile.write(content)

def create_post_from_template(template_dir, posts_dir, title):
    """
      Creates a new Post entry in the Journal
      The path of the post is based on the current date
      Automatically sets the date metadata
    """
    today = date.today()
    name = str(today)+'-'+title
    print(name)
    # Path 
    path = os.path.join(posts_dir, name) 
    os.mkdir(path) 
    print(f"Directory created {name}") 
    src = template_dir + "/index.ipynb"
    dst = posts_dir + "/" + name + "/index.ipynb"
    generate_file_content(src, dst)
