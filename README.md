# centos7用emacs26.3 RPMの作成

* centos7のemacs24のsrc.rpmからspecを取り出し、26.3でbuildが通るようにした。
  - 起動するかの検証のみ

* buildにはcentos:centos7 のcontainerで実効しており、環境に依存しない作りになっている。

## build用docker imageの作成

```
$ docker build . -t centos7-rpmbuild:latest
```

## build

* emacsのbuildではrandomize_va_spaceを0にする必要がある.
  - [Docker上のEmacsのビルドでハマった話](https://eshamster.hatenablog.com/entry/2016/07/03/125925)を参照。
  - 同じ追記によると不用になったなったとあるが、当方の環境ではまだ必要だった。
  
```
$ sudo sh -c "echo 0 > /proc/sys/kernel/randomize_va_space"
```


* build
  + specファイル名でrpmが作成される想定。
    - 名称が異るばあいはbuild.shを修正するか、その内容を```sh -c "rpmbuild && ..."```のように指定してrunする
```
docker run --rm -v $(pwd):/root/rpmbuild centos7-rpmbuild:latest /root/build.sh emacs
```

* build後、元にもどしておく

```
$ sudo sh -c "echo 2 > /proc/sys/kernel/randomize_va_space"
```