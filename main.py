import TkEasyGUI as eg
import pyautogui as pag

scr_w, scr_h = pag.size()

instructions = (
    "・QRコードをスマートフォンで読み取って、集計システムにログインしてください（http://scrs0627.cc.ag.aoyama.ac.jp/）。\n"
    "・ページは学内限定です。agwlanに接続してQRコードを読み取ってください。\n"
    "・ログインには ima.iam.aoyama.ac.jp のGoogleアカウントを使います。\n"
    "・集計が終わったら送信完了ボタンを押してください。"
)

layout = [
    [eg.Text("AIM Commons利用者集計システム Ver.3", font=("Helvetica", 32), pad=((0, 0), (50, 30)))],
    [ 
        eg.Text("",pad=((550, 0), (0, 30))),
        eg.Image("qr.png")
    ],
    [eg.Label(text=instructions, font=("Helvetica", 16), pad=((0, 0), (0, 30)))],
    [eg.Button("送信完了", size=(200, 2), font=("Helvetica", 40))],
]

window = eg.Window(title="AIM Commons利用者集計システム Ver.3", layout=layout, size=(scr_w, scr_h), no_titlebar=True, keep_on_top=True)

while window.is_alive():
    # イベントと値を取得
    event, values = window.read()
    # OKボタンを押した時
    if event == "送信完了":
        window.close()
