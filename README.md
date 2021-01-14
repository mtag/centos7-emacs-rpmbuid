# centos7用emacs26.3 RPMの作成

  cenots7のemacsがさすがに古すぎるが、rpm化しないといろいろ面倒なので作成。

* centos7のemacs24のsrc.rpmからspecを取り出し、26.3でbuildが通るようにした。
  - 起動するかの検証のみ

* buildにはcentos:centos7 のcontainerで実行しており、centosのデフォルトの状態でRPM作成・インストールができることを担保している。

  - 用途上必要性はないが、root権限を前提としており、OpenShiftのデフォルト権限設定では動かないはず。

* おまけでlhaのRPM作成specをつけている

## build用docker imageの作成

```
$ docker build . -t centos7-rpmbuild:latest
```

## build

* emacsのDokcerでのbuildではrandomize_va_spaceを0にする必要がある.
  - [Docker上のEmacsのビルドでハマった話](https://eshamster.hatenablog.com/entry/2016/07/03/125925)を参照。ありがとうございます。
    + 追記によると不用になったとあったが、当方の環境ではまだ必要だった。
  
```
$ sudo sh -c "echo 0 > /proc/sys/kernel/randomize_va_space"
```


* build
  + specファイル名でrpmが作成される想定。
    - 名称が異るばあいはbuild.shを修正するか、その内容を```sh -c "rpmbuild && ..."```のように指定してrunする
    - またはsh -c "sleep 36000"などとして、内部でコマンドを実行する。
  * 繰り返し実行する場合、yum-builddepまでの状態のコンテナを作成したほうが時間の節約になる。
    - gccなど最低限をインストール済みのコンテナを作ることも検討
    
```
$ cd rpmbuild
$ docker run --rm -v $(pwd):/root/rpmbuild centos7-rpmbuild:latest /root/build.sh emacs
```

* build後、元にもどしておく

```
$ sudo sh -c "echo 2 > /proc/sys/kernel/randomize_va_space"
```
