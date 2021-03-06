# IEICE_BC_Article

## 出版された記事のダウンロード先

IEICE B-plus 2022夏号 No.61
<https://www.ieice.org/~cs-edit/magazine/archive.html>

「ブロックチェーン」を学んで，使ってみよう！
藤原明広
<https://www.jstage.jst.go.jp/article/bplus/16/1/16_30/_pdf>



## 動作確認環境

- Ubuntu 20.04.3 LTS

- Python 3.8.10

### 補足

- 永続証明書の発行自体は上述の環境の準備は不要ですが，検証には必要になります．

- MS Windowsでは，wslを使うとUbuntuと同等の環境が構築可能です（未確認）．

- Mac OSでも，brewを使えば環境構築可能だと思います（未確認）．

- 他にもVirtualbox等を使ってUbuntuの仮想環境を構築する方法もあります．



## 環境設定

```
$ sudo apt install poppler-utils jq python3-pip

$ sudo pip3 install pyld
```



## Bloxberg 

- ウェブページ <https://bloxberg.org/>

- Bloxberg Whitepaper 1.1 <https://bloxberg.org/wp-content/uploads/2020/02/bloxberg_whitepaper_1.1.pdf>

- 永続証明発行サイト <https://certify.bloxberg.org/>

- Block explorer <https://blockexplorer.bloxberg.org/>

- Validators <https://validators.bloxberg.org/>



## 永続証明書の発行

- 解説記事6.1節を参照

### 要約の計算

```
$ sha256sum <存在を証明したいデータのファイル名>
```



## 永続証明書の検証

- 解説記事6.2節を参照

### 永続証明書に埋め込まれたJSON形式のテキストファイル(bloxbergJSONCertificate)を抽出

```
$ pdfdetach -saveall <永続証明書のファイル名>

$ cat bloxbergJSONCertificate|jq
```

### 永続証明書とBloxbergブロックチェーンに記録されているMerkle root (= tokenHash)の確認

```
$ python3 check_merkle_root.py bloxbergJSONCertificate

```

