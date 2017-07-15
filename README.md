# todo.txt-hidemaru

秀丸エディタで todo.txt を実現します。

![todohidemaru](https://user-images.githubusercontent.com/23325839/28237486-ca166ff0-697b-11e7-940a-c3e7f53f7311.jpg)

todo.txt については拙筆ですが [タスク管理メソッド todo.txt が面白そう - Qiita](http://qiita.com/sta/items/0f72c9c956cf05df8141) をどうぞ。

## 特徴

- 秀丸エディタマクロのみでほぼ完結しています（余計なツールは使いません）
- メニュー項目から選択するだけで各種操作を行えます（手で打つよりも何倍も楽です）

## サポートしている操作

以下の操作をサポートしています。

- タスクの追加 …… 新しくタスク(Todo)を追加します。
- タスクのコピー …… 現在行のタスクと同じ内容のタスクを複製します。
- タスクの編集 …… カーソルを現在行のタスク内容記入部分まで移動させます。
- タスクの終了 …… 現在行のタスクを完了にします。`x` や完了日を手で記入する手間はありません。また完了済タスクに対してこれを行うと未完了に戻すこともできます。
- タスクの検索 …… 指定したキーワードにマッチするタスクを Grep 機能で一覧表示します。
- ソート …… **(Python 2.7 が必要です)** 表示されている全てのタスクを昇順で並び替えます。**開いている todo.txt を書き換えますのでご注意ください**
- 優先度を上げる …… 現在行のタスクの優先度を C → B → A という方向で変更します。
- 優先度を下げる …… 同上、A → B → C という方向で変更します。

## インストール

- (1) todo.txt-hidemaru をダウンロードします
  - Git に慣れてる方なら `git clone https://github.com/stakiran/todo.txt-hidemaru`
  - あるいは [ZIP でダウンロード](https://github.com/stakiran/todo.txt-hidemaru/archive/master.zip) もできます
- (2) [menu.mac](menu.mac) を秀丸エディタにマクロ登録します
- (3) 必要なら menu.mac を簡単に呼び出せるよう、キー割り当てやツールバーへの追加をしておきます
- (4) todo.txt を準備します。空ファイルでも構いません。 [サンプルのtodo.txt](todo.txt) を使っても良いです

## 使い方

todo.txt を秀丸エディタで開いた後、menu.mac を呼び出します。

するとメニューが表示されるので、実行したい操作を選びます。

ちなみにメニュー項目は特定のキー（アンダーラインが引かれている）を押すことで即実行できるようになっています。たとえばタスク追加なら「A」、優先度を上げたいなら「1」を押します。以下の図を見てください。

![todohidemaru_accel](https://user-images.githubusercontent.com/23325839/28237583-ac435856-697d-11e7-9351-149e2a89fbfd.jpg)

なお、何も実行したくない場合は、Esc キーを押すかメニュー外をクリックしてキャンセルしてください。

## (上級者向け)本マクロを改造する

秀丸エディタマクロのわかる方なら、[menu.mac](menu.mac) の中身を見て色々とカスタマイズできるかもしれません。

## Contribution

ご意見、ご要望、バグ報告などありましたら [Issues](https://github.com/stakiran/todo.txt-hidemaru/issues) よりお知らせください（要GitHubアカウント）。

## ライセンス

[MIT License](LICENSE)

## 作者

[stakiran](https://github.com/stakiran)
