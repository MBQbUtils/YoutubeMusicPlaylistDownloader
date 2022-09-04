#!/usr/bin/python3

"""
Скрипт скачивает плейлисты с YouTube и вырезает аудиодорожки.
Если какие-то видео уже скачаны, они пропускаются.
"""

import json
import os
import re
import sys
import textwrap
import time
import traceback
import yt_dlp


def read_config():
    config_content = """
    {
        /* Путь до каталога с плейлистами */
        "path": "./output/path/", 
        "format": "original", /* Формат звука */
        /* Используйте формат "original", чтобы не менять формат звука
           и не зависеть от наличия ffmpeg
           Форматы:
            "aac", "alac", "flac",
            "m4a", "mp3", "opus",
            "vorbis", "wav"
        */
        "playlists": {
            /*
             * Ссылки на плейлисты с музыкальными клипами
             * в формате "Имя": "Ссылка"
             */
            "Example1": "https://www.youtube.com/playlist?list=PLL_example", /* Пример первый */
            "Example2": "https://www.youtube.com/playlist?list=PLL_example2" /* Пример последний */
        }
    }"""
    config_content = textwrap.dedent(config_content).strip()
    config_path = os.path.abspath('config.json')
    try:
        if not os.path.exists(config_path):
            with open(config_path, 'w', encoding='utf-8') as f:
                f.write(config_content)
            print(f"Edit config at {config_path!r}")
            input("And then press Enter...")
        with open(config_path, encoding='utf-8') as f:
            config_content = f.read()
        config_content = re.sub(pattern=r'\/\*[\s\S]*?\*\/', repl='', string=config_content)
        return json.loads(config_content)
    except:
        print("Error on read config:")
        raise


def output(text):
    print('>>>>>>>>>>>>>>>>', text)


def _main():
    config = read_config()
    playlists_path = os.path.abspath(config['path'])
    audio_format = config['format']
    playlists = config['playlists']
    download_options = dict(
        format='bestaudio',
        windowsfilenames=(sys.platform == 'win32'),
        no_warnings=True,
        compat_opts={
            'no-youtube-unavailable-videos'
        },
        postprocessors=[dict(
            key='FFmpegExtractAudio',
            preferredcodec=audio_format,
        )],
        outtmpl='%(playlist_title)s/%(title)s-%(id)s.%(ext)s'
    )
    if audio_format == 'original':
        del download_options['postprocessors']

    os.makedirs(playlists_path, exist_ok=True)
    os.chdir(playlists_path)
    output('Syncing all playlists')

    for i, name in enumerate(playlists.keys(), 1):
        link = playlists[name]
        download_options['download_archive'] = f'{name}.cache'
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
