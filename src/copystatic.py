import os
import shutil


def copyFilesRecurr(base: str, dst: str):
    contents = os.listdir(base)
    for c in contents:
        base_path = os.path.join(base, c)
        dst_path = os.path.join(dst, c)
        print(f" * {base_path} -> {dst_path}")
        if os.path.isfile(base_path):
            shutil.copy(base_path, dst_path)
        else:
            os.mkdir(dst_path)
            copyFilesRecurr(base_path, dst_path)


def initialCleanUp(dst: str):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
