#!/usr/bin/python3

"""
Скрипт скачивает плейлисты с YouTube и вырезает аудиодорожки.
Если какие-то видео уже скачаны, они пропускаются.
"""

import os
import sys
import time
import traceback
import yt_dlp
import json


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
            f.write("[Описание](https://github.com/MBQbUtils/YoutubeMusicPlaylistDownloader)")
    return data


def output(text):
    print('>>>>>>>>>>>>>>>>', text)


def _main():
    config = read_config()
    playlists_path = os.path.abspath(config['path'])
    playlists = config['playlists']
    download_options = dict(
        format='bestaudio',
        windowsfilenames=(sys.platform == 'win32'),
        no_warnings=True,
        lazy_playlist=True,
        compat_opts={
            'no-youtube-unavailable-videos'
        },
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
        retry_count = 0
        success = False
        with yt_dlp.YoutubeDL(download_options) as downloader:
            while not success:
                if retry_count:
                    output(f'Retry sync #{i}, attempt {retry_count}')
                    time.sleep(0.25*retry_count//2)
                try:
                    downloader.download([link])
                    success = True
                except Exception as e:
                    success = False
                    print(e)
                retry_count += 1
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
