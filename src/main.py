from copystatic import initialCleanUp, copyFilesRecurr

base = "./static"
dst = "./public"


def main():
    print("Deleting public directory...")
    initialCleanUp(dst)

    print("Copying static files to public directory...")
    copyFilesRecurr(base, dst)


main()
