Summary: LHa for UNIX
Name: lha
Version: 1.14i
Release: yoheie.1
License: distributable
Group: Applications/Archiving
Source: https://github.com/yoheie/lha/archive/rpmspec.zip
URL: https://github.com/yoheie/lha/tree/rpmspec
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: make autoconf automake gcc glibc-devel libtool

%description
LHa for UNIX

%prep
%setup -n lha-rpmspec

%build
libtoolize
aclocal
autoheader
automake --force-missing --add-missing
autoconf
./configure --enable-multibyte-filename=utf8 --prefix=/usr --mandir=/usr/share/man
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1

make prefix=$RPM_BUILD_ROOT/usr mandir=$RPM_BUILD_ROOT/usr/share/man install

pushd $RPM_BUILD_ROOT
for n in lha ; do
    chmod 755 ./usr/bin/$n
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/lha
/usr/share/man/man1/lha.1*

%changelog
* Tue Jan 12 2021 Masanao TAGUCHI <mtag@jp.ibm.com>
- update
* Mon Mar 23 2015 Tsuyoshi Sadakata <sadakata@fusic.co.jp>
- first release
