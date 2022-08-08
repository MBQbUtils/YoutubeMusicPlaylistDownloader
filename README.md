# Youtube Music Playlist Downloader
Скрипт скачивает плейлисты с YouTube и вырезает аудиодорожки. Если какие-то видео уже скачаны, они пропускаются.

## Как использовать
После первого запуска создаётся `config.json`
Он имеет следующую структуру: 
```json
{
    "path": "./output/path/",
    "playlists": [
        "https://www.youtube.com/playlist?list=PLL_example",
        "https://www.youtube.com/playlist?list=PLL_example2"
    ]
}
```
Добавьте ссылки на плейлисты в `config.json`
И запустите скрипт заново
Не удаляйте файл `playlists.cache`
Он позволяет не скачивать по новой треки при повторном запуске

Чтобы докачать новые видео из плейлиста, просто перезапустите скрипт

## Установка
1. [**Скачайте скрипт**](https://github.com/MBQbUtils/YoutubeMusicPlaylistDownloader/releases/latest/download/main.exe)
2. Запустите его первый раз (он создаст всё необходимое и завершит работу)
3. Следуйте инструкциям выше.

## Благодарности
Проект вдохновлён скриптом [**@SemperSolus0x3d**](https://github.com/SemperSolus0x3d)

[**@Druzai**](https://github.com/Druzai) подсказал популярный аналог `youtube-dl`
