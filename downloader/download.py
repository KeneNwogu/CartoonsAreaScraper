import requests
import os
import progressbar


def download(download_link, folder_name):
    """docstring"""
    user = os.path.expanduser('~')
    sp = download_link.split("/")
    name = (sp[len(sp) - 1].replace("%20", " "))
    path = f"{user}\\Desktop\\{folder_name}\\"
    print(path)

    if not os.path.isdir(path):
        os.mkdir(path)

    request = requests.get(download_link, stream=True)
    length = request.headers["Content-length"]
    length_bytes = int(length)
    length = int(length) / (1024 ** 2)
    
    print("Total:", length, "mb")

    start = 0
    chunk_length = 10240

    with open(f"{path + name}", 'wb') as fd:
        with progressbar.ProgressBar(max_value=100) as bar:
            for chunk in request.iter_content(chunk_size=chunk_length):
                start += chunk_length
                percent = int((start / length_bytes) * 100)
                fd.write(chunk)
                bar.update(percent)
            # print(f"downloaded {percent} of 100%")
    print("Finished Downloading...", name)
