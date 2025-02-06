import os
import re
from urllib import parse
import requests


def download_files(file_url: str, destination_folder: str):
    if not os.path.isdir(destination_folder) and not os.path.exists(destination_folder):
        os.mkdir(f'{destination_folder}')
    while True:
            parsed_url = parse.urlparse(file_url)
            get_data = requests.get(file_url)
            if get_data.status_code == requests.codes.ok:
                with open(f'{destination_folder+parsed_url.path}', 'wb+') as local_file:
                    local_file.write(get_data.content)
                    print(f'Successfully downloaded\n{file_url}\n')
            else:
                print("Finished")
                break
            find_iter = re.findall(r'\d+', parsed_url.path)
            get_path = re.findall(r'\D+', parsed_url.path)

            new_path = f"{get_path[0]}{int(find_iter[0])+1:03}" + get_path[1]
            file_url = parse.urljoin(file_url, new_path)

            



download_files('http://699340.youcanlearnit.net/image050.jpg', './images')
