# py-split-voice-whisper

## Overview

.wavの音声ファイルを、whisperによって文字起こしさせ、発話区間ごとにファイルを分割します。

動画編集や音MAD、RVC、so-vits-svcのモデルトレーニングにもどうぞ。

OpenAIのWhisperを使用していますので、処理はローカルのみで行います。

音声処理のAIモデルとして、tiny, base, small, medium, largeがありますが、デフォルトでは一番性能が良いlargeを使用しています。マシンスペック等によって調整してください。

## Requirements

```bash
$ pip install -r requirements.txt
```
によってインストールされるパッケージ。

そしてffmpegがインストールされている必要があります。

venvを作成し環境を分けることをオススメします。

## Usage

```bash
$ python main.py <path_to_audio_file> <path_to_output_folder> <Model>
```
Modelには次のいずれかを指定します。

```
tiny, base, small, medium, large
```

右に行くほど性能が高く、要求されるマシンスペックも高くなります。
