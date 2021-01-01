#! /bin/sh
rpmbuild -bs /root/rpmbuild/SPECS/${1}.spec
yum-builddep -y /root/rpmbuild/SRPMS/${1}-*.src.rpm
rpmbuild --rebuild /root/rpmbuild/SRPMS/${1}-*.src.rpm
