# Youtube Music Playlist Downloader
Скрипт скачивает плейлисты с YouTube и вырезает аудиодорожки. Если какие-то видео уже скачаны, они пропускаются.

## Как использовать
При первом запуске создаётся `config.json`
Он имеет следующую структуру: 

```js
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
}
```
Добавьте ссылки на плейлисты в `config.json`
сохраните изменения и продолжите работу скрипта, нажав `Enter`.

Не удаляйте файл `playlists.cache`.
Он позволяет не скачивать заново треки при повторном запуске.

`config.json` поддерживает комментарии в стиле `/* комментарий */`.

Чтобы докачать новые видео из плейлиста, просто перезапустите скрипт

## Установка
1. [**Скачайте скрипт**](https://github.com/MBQbUtils/YoutubeMusicPlaylistDownloader/releases/latest/download/main.exe)
2. Запустите его, он создаст всё необходимое
3. Следуйте инструкциям выше.

## Благодарности
Проект вдохновлён скриптом [**@SemperSolus0x3d**](https://github.com/SemperSolus0x3d)

[**@Druzai**](https://github.com/Druzai) подсказал популярный аналог `youtube-dl`
