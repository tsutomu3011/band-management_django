# Band Management
<br>
URL：https://bandmanagementd.herokuapp.com/
<br>
<br>
<br>

## このアプリについて
Band Managementは、バンド活動における金銭管理・アーティスト写真管理を実現するアプリです。
<br>
<br>

## 概要
アプリ名：Band Management<br>
使用言語：Python<br>
使用フレームワーク：Django<br>
作業人数：1人<br>
作業期間：10日間
<br>
<br>

## アプリ開発の理由
過去のバンド活動の経験から、バンド活動のマネジメントには多くの労力がかかると実感していました。<br>
その管理業務の中から、金銭管理・写真管理のタスクをアプリ化することで人手による労力の削減を実現しました。
<br>
<br>

## 機能紹介
- ホーム画面

<img width="500" alt="bandmanagement_photo_explain.png" src="https://user-images.githubusercontent.com/57580026/75243706-b902a980-580d-11ea-9272-1b4a77a2a5ea.png">

***

- 金銭管理機能

> ①にて金銭の収支を「5000」「-3000」などと入力<br>
> Current Walletの値、②のbarchartが増減

<img width="500" alt="スクリーンショット 2020-02-25 17.25.07.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/531957/e81747d3-f821-b9b4-3e9d-92058c885036.png">

***

- 写真管理機能

> ①にてファイルを選択、その画像のシチュエーションを設定の上送信<br>
> ②に送信された画像ファイルが登録される

<img width="500" alt="スクリーンショット 2020-02-25 18.53.44.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/531957/c11c810b-bec3-ec27-56b8-1eca518b8929.png">

<br>
<br>

## こだわった機能
金銭管理機能において、残高を棒グラフで表現した機能です。<br>
グループの財政状況を数字でのみ把握するのではなく、ひと目でわかるよう可視化するため実装いたしました。<br>
`Chart.js`というJavaScriptライブラリを使用し、適用する値はデータベースから取得しています。<br>
増減の仕組みは、`views.py`内の関数において、データベースの最後の値に送信された値を加減することで実現しました。<br>

```python:views.py
def wallet(request):
    # データ送信された場合の処理
    if request.method == "POST":
        send_money = request.POST
        total_wallet = Wallet.objects.last().money + int(send_money['money'])
        Wallet.objects.create(money=total_wallet)
        return redirect('top:wallet')
    # 画面表示の場合の処理
    # wallet_bar → 値が正の場合の変数
    # wallet_deficit_bar → 値が負の場合の変数
    else:
        wallet_bar = 0
        wallet_deficit_bar = 0
        if Wallet.objects.last().money >= 0:
            wallet_bar = Wallet.objects.last().money
        else:
            wallet_deficit_bar = Wallet.objects.last().money * -1
        last_wallet = Wallet.objects.last()
        form = WalletForm()
        context = {'last_wallet':last_wallet, 'form':form, 'wallet_bar':wallet_bar, 'wallet_deficit_bar':wallet_deficit_bar}
        return render(request, 'top/wallet.html', context)

```
