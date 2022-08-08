#!/usr/bin/python3

"""
Скрипт скачивает плейлисты с YouTube и вырезает аудиодорожки.
Если какие-то видео уже скачаны, они пропускаются.
"""

import os
import traceback
import yt_dlp
import json
import textwrap


def read_config():
    data = {
        'path': './out/',
        'playlists': []
    }

    try:
        with open('config.json') as f:
            data = json.load(f)
    except:
        with open('config.json', 'w') as f:
            json.dump(data, f, indent=4)
        with open('README.md', 'w') as f:
            f.write(textwrap.dedent("""
            First start creates `config.json`
            Add playlists links like so: 
            ```json
            "playlists": [
                "https://www.youtube.com/playlist?list=PLL_example",
                "https://www.youtube.com/playlist?list=PLL_example2"
            ]
            ```
            Then run this script again
            Don't remove `playlists.cache` file, it contains sync cache
            And allows to skip already downloaded files 
            """).strip())
    return data


def output(text):
    print('>>>>>>>>>>>>>>>>', text)


def _main():
    config = read_config()
    playlists_path = os.path.abspath(config['path'])
    playlists = config['playlists']
    download_options = dict(
        format='bestaudio',
        ignoreerrors=True,
        no_warnings=True,
        postprocessors=[dict(
            key='FFmpegExtractAudio',
            preferredcodec='mp3',
        )],
        download_archive='playlists.cache',
        outtmpl='%(playlist_title)s/%(title)s-%(id)s.%(ext)s'
    )

    os.makedirs(playlists_path, exist_ok=True)
    os.chdir(playlists_path)
    output('Syncing all playlists')

    for i, link in enumerate(playlists, 1):
        output(f'Start sync #{i}. {link!r}')
        with yt_dlp.YoutubeDL(download_options) as downloader:
            downloader.download([link])
        output(f'Synced #{i}!')
    output('Done syncing playlists')


def main():
    try:
        _main()
    except:
        traceback.print_exc()
        input("Error...")
    input("Done...")


if __name__ == '__main__':
    main()
