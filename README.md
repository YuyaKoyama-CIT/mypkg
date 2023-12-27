# robosys2023
このリポジトリはロボットシステム学のROS 2を学習するために制作したものです。
talkerとlisnerが含まれます

## talker
0.5秒間隔で1ずつカウントアップしたInt16型のデータをパブリッシュしている

rclpy.spin(node)によりプログラムが終了しなくなる

## lisner
ros2 run mypkg listenerで実行

## 実行例
### 別のターミナルから各々立ち上げ確認する方法

```
# ターミナル例,talker実行側←何も表示されない

#ターミナル例,listener実行側
[INFO] [1703666348.319124330] [listener]: Listen: 1
[INFO] [1703666348.818284065] [listener]: Listen: 2
[INFO] [1703666349.318467759] [listener]: Listen: 3
[INFO] [1703666349.818984497] [listener]: Listen: 4
[INFO] [1703666350.319458677] [listener]: Listen: 5
[INFO] [1703666350.818807939] [listener]: Listen: 6
[INFO] [1703666351.319469897] [listener]: Listen: 7
[INFO] [1703666351.819993592] [listener]: Listen: 8

```
### launchファイルを使用し、　てtalkerとlistenerを一つの端末で立ち上げる方法　例
```
[listener-2] [INFO] [1703666241.200523266] [listener]: Listen: 10

```

## 必要なソフトウェア
* ROS 2
* Python

## 開発環境
* Ubuntu 22.04.3 LTS
* ROS 2

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
