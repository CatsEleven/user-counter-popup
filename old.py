import requests
import PySimpleGUI as sg
import pyautogui as pag


def postAns(values):
    url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScJ2GFVJMzdpDXefStckDli3ZDlJeiztjbcQ6FXOZFiyadDew/formResponse"
    params = {
    'entry.944232794': values['sofa_A'], 
    'entry.752941540': values["pc"],
    "entry.321313517": values['TTM'],
    'entry.806447966': values['cafe'],
    'entry.1513412249':values['highChair'], 
    'entry.1213218368':values['movable'], 
    'entry.27358015': values['sofa_B'], 
    'entry.884640467':values['sofa_C'],
    'entry.134591070':values['sofa_D'],
    'entry.1895106559':values['Vf_mac'],
    'entry.1819304643' : values['Vf_win'],
    'entry.656878661': values['silent'],
    'entry.253997222': values['comment']
    }
    r = requests.get(url, params=params)
    return r.status_code

def main():
    scr_w,scr_h= pag.size()
    title =  [sg.Text('LC利用者数アンケート Ver2.0', font=('Noto Serif CJK JP',40), pad=((0, 0), (0, 100)))]

    #各収容人数を記載しています
    # ソファー席の人数
    rangeOfSofa = list(range(0, 7, 1))
    #教育研究PC
    rangeOfPc = list(range(0, 8, 1))
    #畳の人数
    rangeOfTatami = list(range(0, 7, 1))
    #カフェ席の人数
    rangeOfCafe = list(range(0, 4, 1))
    #ハイチェアの人数
    rangeOfHighChair = list(range(0, 9, 1))
    #可動席の人数
    rangeOfMovableChair = list(range(0, 12, 1))
    #編集ブース
    Vf = list(range(0, 2, 1))
    #静音環境
    silentEnv = list(range(0, 2, 1))
    
    
    frame_1 = sg.Frame("",[
        [sg.Text("ソファー席", font=('Noto Serif CJK JP',20,"bold"))],
        [sg.Combo(rangeOfSofa, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="sofa_A")]], 
        size=(210, 120), pad=((550, 0), (0, 0)))

    frame_2 = sg.Frame('', layout=[
        [sg.Text("PC席", font=('Noto Serif CJK JP',20,"bold"))],
        [sg.Combo(rangeOfPc, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="pc")]], size=(450, 120))

    frame_3 = sg.Frame('', 
                    layout=[
         [sg.Text("畳", font=('Noto Serif CJK JP',20,"bold"))],
         [sg.Combo(rangeOfTatami, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="TTM")]], size=(210, 120))

    frame_4 = sg.Frame('', [
        [sg.Text("カフェ1人席", font=('Noto Serif CJK JP',20,"bold"))],
        [sg.Combo(rangeOfCafe, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="cafe")]], size=(210, 120), pad=((550, 0), (0, 0)))

    frame_5 = sg.Frame('', [
        [sg.Text("ハイチェア", font=('Noto Serif CJK JP',20,"bold"))],
        [sg.Combo(rangeOfHighChair, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="highChair")]], size=(190, 120), pad=((8, 0), (0, 0)))

    frame_6 = sg.Frame('', [
        [sg.Text("可動席", font=('Noto Serif CJK JP',20,"bold"))],
        [sg.Combo(rangeOfMovableChair, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="movable")]], size=(248, 120), pad=((10, 0), (0, 0)))

    frame_6_1 = sg.Frame('', 
                    layout=[
        [sg.Text("ソファー席", font=('Noto Serif CJK JP',20,"bold"))],
        [sg.Combo(rangeOfSofa, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="sofa_B")], 
        ], size=(210, 120), pad=((10, 0), (0, 0)))

    frame_7 = sg.Frame('', 
                    layout=[[sg.Text("ソファー席", font=('Noto Serif CJK JP',20,"bold"))],
                            [sg.Combo(rangeOfSofa, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="sofa_C")]], 
                        size=(210, 120), pad=((550, 0), (0, 0)))

    frame_8 = sg.Frame('', 
                    layout=[[sg.Text("ソファー席", font=('Noto Serif CJK JP',20,"bold"))],
                            [sg.Combo(rangeOfSofa, default_value=0, font=('Noto Serif CJK JP',30,"bold"), key="sofa_D")]], 
                        pad=((465, 0), (5, 0)),  size=(210, 120))

    frame_9 = sg.Frame('', 
                    layout=[
                             [sg.Text("編集3", font=('Noto Serif CJK JP',20,"bold"))],
                             [sg.Combo(Vf, default_value=0,font=('Noto Serif CJK JP',30,"bold"), key="Vf_mac")]], 
                        pad=((910, 0), (1, 0)),  size=(150, 120))

    frame_9_1 = sg.Frame('', 
                    layout=[
                             [sg.Text("編集2", font=('Noto Serif CJK JP',20,"bold"))],
                             [sg.Combo(Vf, default_value=0,font=('Noto Serif CJK JP',30,"bold"), key="Vf_win")]], 
                        pad=((5, 0), (1, 0)),  size=(150, 120))



    frame_10 = sg.Frame('', 
                    layout=[[sg.Text("静音ブース1", font=('Noto Serif CJK JP',20,"bold"))],
                            [sg.Combo(silentEnv, default_value=0, font=('Noto Serif CJK JP',30,"bold"),key="silent")]], 
                            size=(210, 120), pad=((10, 0), (3, 0)))

    comment =  [sg.Text('気づいたこと・コメントがあれば記入してください！',font=('Noto Serif CJK JP',20,"bold"))]

    freeDescription = [sg.Multiline(size=(200, 5), key='comment')]

    send = [sg.Button("送信", size=(200, 2), font=('Arial', 40))]

    # pad=((left, right), (top, bottom)))],の順番で場所を記述します。
    # デフォルトで数字が入っているようにする

    sg.theme('SystemDefault')

    layout = [
        title,
        [frame_1, frame_2, frame_3],
        [frame_4, frame_5, frame_6,frame_6_1],
        [frame_7,frame_8],
        [frame_9, frame_9_1, frame_10],
        comment,
        freeDescription,
        send
    ]

    # Windowサイズを定義する
    scr_w,scr_h= pag.size()
    window = sg.Window('LC利用者数調査', layout, size=(scr_w, scr_h), finalize=True, no_titlebar=True)

    # ウィンドウの×ボタンを非表示にする
    window.TKroot.overrideredirect(True)



    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '送信':
            ans = postAns(values)
            print(ans)
            break

    # ウィンドウを閉じる
    window.close()


if __name__ == '__main__':
    main()