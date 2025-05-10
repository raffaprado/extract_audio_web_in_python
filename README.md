# 🎬 Script para Download de Vídeo e Extração de Áudio

Este script em Python permite baixar vídeos da internet (YouTube, Vimeo, etc.) e extrair seu áudio em formato `.mp3`. Ele utiliza as bibliotecas [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) para o download e [`moviepy`](https://github.com/Zulko/moviepy) para manipulação de mídia.

---

## 📦 Funcionalidades

- Baixa o melhor vídeo e áudio disponíveis até a resolução especificada (ex: 1080p).
- Salva o vídeo no caminho definido.
- Extrai o áudio do vídeo baixado e salva em MP3.

---

## 🧰 Requisitos

- Python 3.6 ou superior
- Bibliotecas:


pip install yt-dlp 
pip install moviepy

Obs: A moviepy também depende de ffmpeg. Você pode instalar via:

    macOS (Homebrew): brew install ffmpeg

    Windows: Baixe em ffmpeg.org e adicione ao PATH