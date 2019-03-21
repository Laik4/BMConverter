# BMConverter
## 概要
'0', '1' で表されたデータを白黒に対応させる変換を行う
ほとんどデバッグしていないので注意

## 使い方
./convert.py inputfile \[-o outputfile\]


| option | description |
| -- | -- |
|inputfile     | 入力ファイル名 (0,1で記述する必要がある。それ以外の文字は無視される) |
|-o outputfile | 出力ファイル名を指定する（省略した場合、変換結果の表示のみ） |
|-r            | 白黒反転する |
|-s size       | サイズを指定する(数値) |

