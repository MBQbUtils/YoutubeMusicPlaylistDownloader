# [Youtube Music Playlist Downloader](https://github.com/MBQbUtils/YoutubeMusicPlaylistDownloader)
Скрипт скачивает плейлисты с YouTube и вырезает аудиодорожки. Если какие-то видео уже скачаны, они пропускаются.

## Как использовать
После первого запуска создаётся `config.json`
Он имеет следующую структуру: 
```js
{
    // Путь до каталога с плейлистами
    "path": "./output/path/", 
    "format": "original", // Формат звука
    /* Используйте формат "original", чтобы не менять формат звука
       и не зависеть от наличия ffmpeg
       Форматы:
        'aac', 'alac', 'flac',
        'm4a', 'mp3', 'opus',
        'vorbis', 'wav'
    */  
    "playlists": [ // Ссылки на плейлисты с музыкальными клипами
        "https://www.youtube.com/playlist?list=PLL_example",
        "https://www.youtube.com/playlist?list=PLL_example2"
    ]
}
```
Добавьте ссылки на плейлисты в `config.json`
и запустите скрипт заново.
Не удаляйте файл `playlists.cache`.
Он позволяет не скачивать по новой треки при повторном запуске.
`config.json` поддерживает комментарии в стиле `/* комментарий */`.

Чтобы докачать новые видео из плейлиста, просто перезапустите скрипт

## Установка
1. [**Скачайте скрипт**](https://github.com/MBQbUtils/YoutubeMusicPlaylistDownloader/releases/latest/download/main.exe)
2. Запустите его первый раз (он создаст всё необходимое и завершит работу)
3. Следуйте инструкциям выше.

## Благодарности
Проект вдохновлён скриптом [**@SemperSolus0x3d**](https://github.com/SemperSolus0x3d)

[**@Druzai**](https://github.com/Druzai) подсказал популярный аналог `youtube-dl`
