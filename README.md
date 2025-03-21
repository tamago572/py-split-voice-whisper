# py-split-voice-whisper

## Overview

.wavの音声ファイルを、whisperによって文字起こしさせ、一節ごとに分割します。

音MAD等にどうぞ。

OpenAIのWhisperを使用していますので、処理はローカルのみで行います。

音声処理のAIモデルとして、tiny, base, small, medium, largeがありますが、デフォルトでは一番性能が良いlargeを使用しています。マシンスペックやお好みで調整してください。

## Requirements

```bash
$ pip install -r requirements.txt
```
によってインストールされるパッケージ。

そしてffmpegがインストールされている必要があります。

## Usage

```bash
$ python main.py <path_to_audio_file> <path_to_output_folder> <Model>
```
Modelには次のいずれかを指定します。

```
tiny, base, small, medium, large
```

右に行くほど性能が高く、要求されるマシンスペックも高くなります。
