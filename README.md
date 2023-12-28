# robosys2023
このリポジトリはロボットシステム学のROS 2を学習するために制作したものです。
talkerとlisner、classifyが含まれます
[![test](https://github.com/YuyaKoyama-CIT/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/YuyaKoyama-CIT/mypkg/actions/workflows/test.yml)

## talker
0.5秒間隔で1ずつカウントアップしたInt16型のデータをパブリッシュしトピックを通じて送信している。
また、rclpy.spin(node)により意図的に終了しない限りプログラムは終了しません

## lisner
subscriberとして設定されており、パブリッシュされトピックを通じて送信されたInt16型のデータを受け取り標準出力する。
また、rclpy.spin(node)により意図的に終了しない限りプログラムは終了しません

## classify
subscriberとして設定されており、パブリッシュされトピックを通じて送信されたInt16型のデータを受け取り、受け取った値が素数が否かを判別して標準入出力に結果を表示する
また、rclpy.spin(node)により意図的に終了しない限りプログラムは終了しません

## 実行例
### 別のターミナルから各々立ち上げ確認する方法

```
# ターミナル例,talker実行側←何も表示されない

$ros2 run mypkg talker


#ターミナル例,listener実行側

$ros2 run mypkg listener
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
Is a prime number?: False
Is a prime number?: False
Is a prime number?: True
Is a prime number?: True
Is a prime number?: False
Is a prime number?: True
Is a prime number?: False
```
### launchファイルを使用し、1つのターミナルからtalkerとlistenerを立ち上げ確認する方法
launchディレクトリ内のtalk_listen.launch.pyを使用します。
```
$ ros2 launch mypkg talk_listen.launch.py
[listener-2] [INFO] [1703667213.087868083] [listener]: Listen: 0
[listener-2] [INFO] [1703667213.577467675] [listener]: Listen: 1
[listener-2] [INFO] [1703667214.077250950] [listener]: Listen: 2
[listener-2] [INFO] [1703667214.577789160] [listener]: Listen: 3
[listener-2] [INFO] [1703667215.077400572] [listener]: Listen: 4
[listener-2] [INFO] [1703667215.577471026] [listener]: Listen: 5
[listener-2] [INFO] [1703667216.077418539] [listener]: Listen: 6
```

## テスト環境
* Ubuntu 22.04
* ROS 2 humble

## 開発環境
* Ubuntu 22.04.3 LTS
* ROS 2
* Python3

## トピックについて
* トピックとはノード間でやり取りするデータのパイプのようなもので、トピックに流れるデータのことをメッセージと言います。
* 送信にはパブリッシャ、受信や読み取りにはサブスクライバを使用します。パブリッシャーがトピックを作成して転送すると、サブスクライバーがそのトピックを受信します。
* 相手の状態に関係なく常にデータを発信しており、不特定多数がデータを受け取ることができるので1対1通信だけでなく1対多数通信を行うことができます。 

## 著作権・ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
    * このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides/robosys_2022/lesson8](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson8.md)
    * [ryuichiueda/my_slides/robosys_2022/lesson9](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson9.md)
    * [ryuichiueda/my_slides/robosys_2022/lesson10](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson10.md)

© 2023 Yuya Koyama
