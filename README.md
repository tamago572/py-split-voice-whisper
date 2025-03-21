# py-split-voice

.wav/.mp3の音声ファイルを文字起こしさせ、一節ごとに分割します。

音MAD等にどうぞ。

OpenAIのWhisperを使用していますので、処理はローカルのみで行います。

また、FFmpegがインストールされている必要があります。

音声処理のAIモデルとして、tiny, base, small, medium, largeがありますが、デフォルトでは一番性能が良いlargeを使用しています。マシンスペック等によって調整してください。
