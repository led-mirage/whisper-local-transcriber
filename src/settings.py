# Whisper Local Transcriber
#
# Copyright (c) 2025 led-mirage
# このソースコードは MITライセンス の下でライセンスされています。
# ライセンスの詳細については、このプロジェクトのLICENSEファイルを参照してください。

import configparser

class Settings:
    """
    アプリケーション設定を保持するクラス。

    このクラスは、指定された設定ファイルと環境変数から設定情報を取得します。
    """
    
    def __init__(self, config_file:str="settings.ini"):
        """
        設定インスタンスを作成します。

        引数:
            config_file (str): 設定ファイルのパス。デフォルトは"settings.ini"。
        """        
        self.config = configparser.ConfigParser()
        self.config.read(config_file, "UTF-8")


    def get_audio_segment_time(self):
        """
        音声の分割時間を取得します。

        戻り値:
            int: 分割時間（秒）。
        """
        return self.config.get("General", "audio_segment_time")


    def get_whisper_model(self):
        """
        使用するWhisperのモデルを取得します。

        戻り値:
            str: Whisperのモデル。
        """
        return self.config.get("Whisper", "model")

    def get_whisper_prompt(self):
        """
        Whisperのプロンプトを取得します。

        戻り値:
            str: Whisperのプロンプト。
        """
        return self.config.get("Whisper", "prompt")
    
    def get_whisper_newline_after_segment(self):
        """
        セグメント後に改行を挿入するかどうかを取得します。

        戻り値:
            bool: 改行する場合はTrue。それ以外はFalse。
        """
        return self.config.getboolean("Whisper", "newline_after_segment")
    
    def get_whisper_verbose(self):
        """
        Whisperの詳細ログ出力設定を取得します。

        戻り値:
            bool: 詳細ログを出力する場合はTrue。それ以外はFalse。
        """
        return self.config.getboolean("Whisper", "verbose")