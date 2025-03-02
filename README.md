# Whisper Local Transcriber

Copyright (c) 2025 led-mirage

## 💎 概要

**Whisper Local Transcriber**は、音声または動画ファイルの音声をテキスト化する便利なツールです。ローカルPCで動作するOpenAI Whisperを使用して高精度の音声認識を行い、結果をテキストファイルに出力します。

会議の録音など長時間の音声データをテキストとして保存したいときに便利です。このツールで音声をテキスト化した後で、出力されたテキストをAIに要約してもらうことで、簡単に議事録などを作成できます。

## 💎 主な機能

- **ローカル処理**: すべての処理がお使いのPCで完結するため、セキュリティが高く、コストも電気代だけで済みます。
- **多様なファイル形式**: mp3, m4a, mp4, avi, mov, mkvなど一般的な音声・動画形式に対応しています。
- **動画ファイル対応**: 動画ファイルは自動的にffmpegを使って音声に変換されるので、追加作業は不要です。
- **整理された出力**: 変換されたテキストは`output`ディレクトリに保存され、簡単に見つけることができます。

## 💎 前提条件

### 📦 PyTorch

このアプリケーションはOpenAIのWhisperモデルを使用した音声認識を行うため、PyTorchが必要です。

- **CPU版**: `openai-whisper`パッケージをインストールする際に自動的に導入されるため、特別な操作は不要です。
- **GPU版**: 処理を高速化したい場合は、CUDA Toolkitと互換性のあるGPU版PyTorchをインストールする必要があります（詳細は後述）。

#### 処理速度

Whisperは計算負荷の高いモデルです。長時間の録音を処理する場合、GPU版を利用することで処理時間を大幅に短縮できます（GPUの性能に依存します）。以下は実際のテスト結果です。

5分間の音声データの変換時間（turboモデルを使用）：

| PyTorch | ハードウェア | 処理時間 |
|-|-|-|
| GPU版 | NVIDIA GeForce GTX 1660 SUPER | 1分34秒 |
| CPU版 | Intel Core i5 12600K | 1分53秒 |

### 📦 CUDA Toolkit

GPU版PyTorchを使用するには、NVIDIA製GPUと、NVIDIA CUDA Toolkitが必要です。

#### CUDAがインストールされているか確認する方法

```
nvcc --version
```

上記コマンドを実行して情報が表示されれば、CUDAはインストール済みです。

インストール済みの場合は次のように表示されます：
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Nov__3_17:51:05_Pacific_Daylight_Time_2023
Cuda compilation tools, release 12.3, V12.3.103
Build cuda_12.3.r12.3/compiler.33492891_0
```

この例ではCUDA 12.3がインストールされていることが分かります。

#### CUDA未インストールの場合

NVIDIA GPUをお持ちでも、上記コマンドでエラーが出る場合はCUDA Toolkitをインストールする必要があります：

1. [NVIDIA CUDA Toolkit公式サイト](https://developer.nvidia.com/cuda-downloads)からダウンロード
2. お使いのOSやアーキテクチャに適合するバージョンを選択してインストール
3. インストール後、システムを再起動

### 📦 FFmpeg

このアプリケーションでは、音声・動画ファイルの処理にFFmpegが必要です。

#### FFmpegのインストール方法

**Windows**:

1. [FFmpeg公式ダウンロードページ](https://ffmpeg.org/download.html)からWindows用のビルドをダウンロード
2. ダウンロードしたアーカイブを展開し、任意のフォルダに配置
3. 展開したフォルダ内の`bin`ディレクトリをシステム環境変数のPATHに追加
4. コマンドプロンプトを再起動し、`ffmpeg -version`で正常にインストールされたか確認

**💡 どれをダウンロードすればいいのか迷ったら**: Windows builds by BtbN をクリックして、Assetsの中から`ffmpeg-n7.1-latest-win64-gpl-7.1.zip`をダウンロードすればOKです（7.1の部分はバージョン番号）。

**macOS** (Homebrewを使用):
```bash
brew install ffmpeg
```

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### インストール確認
以下のコマンドでFFmpegが正常にインストールされているか確認できます：
```bash
ffmpeg -version
```

### 📦 Python

このアプリケーションを実行するには、Python 3.8以上が必要です。

#### バージョン要件

- **最低要件**: Python 3.8
- **動作確認済み**: Python 3.12.0

**注意**: Python 3.12.0で動作確認していますが、Python 3.8以上であれば基本的に動作します。ただし、最新の機能や修正を利用するには最新のPythonバージョンを使用することをお勧めします。

## 💎 アプリケーションのインストール

1. GitHubからソースを取得します：
    ```bash
    git clone https://github.com/led-mirage/whisper-local-transcriber.git
    ```
2. プロジェクト用ディレクトリに移動します。
    ```bash
    cd whisper-local-transcriber
    ```
3. 仮想環境を作成し、アクティベートします（推奨）：
    ```bash
    # 仮想環境の作成
    python -m venv venv

    # 仮想環境の有効化
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```
4. 必要なパッケージをインストールします：
    ```bash
    pip3 install -r requirements.txt
    ```
5. ご使用の環境にあったPyTorchをインストールします：
    ```bash
    # PyTorch公式サイト(https://pytorch.org/get-started/locally/)で
    # 自分の環境に合ったコマンドを確認してください

    # 例: Windows、Pip、Python、CUDA 12.1の場合のコマンド
    pip3 install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121

    # CPUを使用する場合は、Whisperにバンドルされているためインストールの必要はありません
    ```

**環境に合わせたPyTorchインストールコマンドの取得方法**:
1. [PyTorch公式インストールページ](https://pytorch.org/get-started/locally/)にアクセス
2. ご使用の環境に合わせて以下の選択肢から適切なものを選びます：
    - PyTorch Build (安定版推奨)
    - お使いのOS
    - パッケージマネージャー (通常はPip)
    - 言語 (Python)
    - CUDA バージョン (GPUを使用する場合、互換性のあるバージョン)
    - ※互換性のあるCUDAバージョンが見つからない場合は[previous versions](https://pytorch.org/get-started/previous-versions/)から探してください
3. サイトが自動生成するインストールコマンドをコピーして使用します

**注意**: 必ず自分の環境に合ったコマンドを使用してください。GPUを搭載したマシンでも、適切なCUDAバージョンを選択しないと正常に動作しない場合があります。

## 💎 実行方法

1. 起動します：
    ```
    python src/main.py
    ```
2. テキスト化する音声または動画ファイルのパスを入力してEnterキーを押します：
    ```
    変換元のファイルのパスを入力してください: c:\temp\test.mp3
    ```
3. 出力：  
    結果は`output`ディレクトリ（自動作成）内にテキストファイルとして出力されます。  
    ファイル名は`[元のファイル名（拡張子を除く）].txt`になります。

## 💎 設定ファイル (`settings.ini`)

アプリケーションの設定は`settings.ini`ファイルに書かれています。

### Generalセクション

- **audio_segment_time**: 音声を分割する単位を秒単位で指定します。デフォルトは300秒です。

### Whisperセクション

- **model**: Whisperで使用するモデルの種類を指定します。オプションは、`tiny`, `base`, `small`, `medium`, `large`, `turbo`の中から選択できます。`turbo`は`Large`モデルの最適化バージョンで、処理速度と精度のバランスがとれたモデルです。また、精度が高いほどモデルサイズが大きくなり初回ロード時間が長くなります。詳しくは[Whisperプロジェクト](https://github.com/openai/whisper)のReadmeをご参照ください。

- **prompt**: 変換の際の指示をテキストとして指定します。Whisperの場合、プロンプトの意味が解釈されるわけではないので、出力したいテキストの見本となるような文章を記述します。

- **newline_after_segment**: セグメントごとの出力時に改行を挿入するためのフラグです。`True`に設定すると、各セグメントの出力後に改行が追加されます。

- **verbose**: Whisperの処理中に詳細なログを出力するかどうかを設定します。`True`に設定すると、処理状況が表示されます。

## 💎 使用しているライブラリ

### 🔖 openai-whisper v20240930
ホームページ： https://github.com/openai/whisper  
ライセンス： MIT License

## 💎 ライセンス

© 2025 led-mirage

本アプリケーションは MITライセンス の下で公開されています。詳細については、プロジェクトに含まれる LICENSE ファイルを参照してください。

## 💎 バージョン履歴

### 1.0.0 (2025/03/02)

- ファーストリリース
