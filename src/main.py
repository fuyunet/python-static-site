from copystatic import initialCleanUp, copyFilesRecurr
from generate_html import generate_page

base = "./static"
dst = "./public"
from_path = "./content/index.md"
template_path = "./template.html"
dest_path = "./public/index.html"


def main():
    print("Deleting public directory...")
    initialCleanUp(dst)

    print("Copying static files to public directory...")
    copyFilesRecurr(base, dst)

    generate_page(from_path, template_path, dest_path)


main()
