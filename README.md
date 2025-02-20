# 人数集計システムポップアップVer.3
- AIM Commonsでの30分定時集計を知らせるポップアップです。
- TkEasyGUIを使ってUIを構築します。
- PyInstallerを使ってexeにすることで、Pythonの実行環境がないWindowsでも動作します。

## インストール要件
- pythonの```3.13.2```を使っています（他のバージョンでも動くと思いますが未確認）
- モジュールのバージョンは```requirements.txt```をみてください。

## exe化する方法
1. 次のコマンドを実行します  
    ```
    pip install -r requirements.txt
    ```
2. main.pyを変更します。
3. どちらかのコマンドを実行します。
   1. ```
      pyinstaller main.py -F -w --clean
      ```
   2. ```
      pyinstaller main.spec
      ```
4. distフォルダにexeが生成されます。画像を忘れずにdistフォルダにコピーしてください。

## 注意
- PyInstallerは、実行する環境によって、出力するものが異なります
  - win環境ではexeを、mac環境ではappを出力します
  - exeにする作業はかならず、Windowsで行ってください
- Windowsの画面サイズは100%で運用してください
  - 100%以上にすると、見切れてしまいます

