# mypkg
このリポジトリはロボットシステム学の授業でROS 2を学習するために制作したものです。

talkerとlisner、classifyが含まれます

[![test](https://github.com/YuyaKoyama-CIT/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/YuyaKoyama-CIT/mypkg/actions/workflows/test.yml)

## talker
0.5秒間隔で1ずつカウントアップしたInt16型のデータをトピック(countup)にパブリッシュしている。

## listener　ノード
subscriberとして設定されており、パブリッシュされ送信されたInt16型のメッセージをトピック(countup)を通じて受け取り標準出力する。

## classify　ノード
subscriberとして設定されており、パブリッシュされ送信されたInt16型のメッセージをトピック(countup)を通じて受け取り、受け取った値が素数が否かを判別、結果を標準出力する。

## countup　トピック
talkerから0.5秒ごとにパブリッシュされたメッセージをlistener,classifyにつないでいる
メッセージの型は16ビット符号付き整数である

## 実行例
### 別のターミナルから各々立ち上げ確認する方法

```
# ターミナル例,talker実行側←何も表示されない
$ ros2 run mypkg talker


#ターミナル例,listener実行側
$ ros2 run mypkg listener
[INFO] [1703666348.319124330] [listener]: Listen: 1
[INFO] [1703666348.818284065] [listener]: Listen: 2
[INFO] [1703666349.318467759] [listener]: Listen: 3
[INFO] [1703666349.818984497] [listener]: Listen: 4
[INFO] [1703666350.319458677] [listener]: Listen: 5
[INFO] [1703666350.818807939] [listener]: Listen: 6
[INFO] [1703666351.319469897] [listener]: Listen: 7
[INFO] [1703666351.819993592] [listener]: Listen: 8

#ターミナル例,classify実行側
$ ros2 run mypkg classify
[INFO] [1704032082.623624931] [classify]: 0 is a prime number? :False
[INFO] [1704032083.118168876] [classify]: 1 is a prime number? :False
[INFO] [1704032083.617913377] [classify]: 2 is a prime number? :True
[INFO] [1704032084.117731269] [classify]: 3 is a prime number? :True
[INFO] [1704032084.617721561] [classify]: 4 is a prime number? :False
[INFO] [1704032085.117761120] [classify]: 5 is a prime number? :True
[INFO] [1704032085.618765042] [classify]: 6 is a prime number? :False
```
### launchファイルを使用し、1つのターミナルからtalkerとlistener,classifyを立ち上げ確認する方法
launchディレクトリ内のtalk_listen_classify.launch.pyを使用します。
```
$ ros2 launch mypkg talk_listen_classify.launch.py
[listener-2] [INFO] [1704030541.653069296] [listener]: Listen: 0
[classify-3] [INFO] [1704030541.653065571] [classify]: 0 is a prime number? :False
[listener-2] [INFO] [1704030542.146090180] [listener]: Listen: 1
[classify-3] [INFO] [1704030542.146090943] [classify]: 1 is a prime number? :False
[listener-2] [INFO] [1704030542.645083396] [listener]: Listen: 2
[classify-3] [INFO] [1704030542.645163174] [classify]: 2 is a prime number? :True
[listener-2] [INFO] [1704030543.145358554] [listener]: Listen: 3
[classify-3] [INFO] [1704030543.145283799] [classify]: 3 is a prime number? :True
```

## トピックについて
* トピックとはノード間でやり取りするデータのパイプのようなもので、トピックに流れるデータのことをメッセージと言います。
* 送信にはパブリッシャ、受信や読み取りにはサブスクライバを使用します。パブリッシャーがトピックを作成して転送すると、サブスクライバーがそのトピックを受信します。
* 相手の状態に関係なく常にデータを発信しており、不特定多数がデータを受け取ることができるので1対1通信だけでなく1対多数通信を行うことができます。 

## テスト環境
* Ubuntu 22.04
* ROS 2 humble

## 開発環境
* Ubuntu 22.04.3 LTS
* ROS 2
* Python

## 著作権・ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド群（CC-BY-SA 4.0 by Ryuichi Ueda）上のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides/robosys_2022/lesson8](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson8.md)
    * [ryuichiueda/my_slides/robosys_2022/lesson9](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson9.md)
    * [ryuichiueda/my_slides/robosys_2022/lesson10](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson10.md)
    * [ryuichiueda/my_slides/robosys_2022/lesson11](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson11.md)

© 2023 Yuya Koyama
