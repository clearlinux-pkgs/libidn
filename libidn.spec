#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libidn
Version  : 1.33
Release  : 14
URL      : http://ftp.gnu.org/gnu/libidn/libidn-1.33.tar.gz
Source0  : http://ftp.gnu.org/gnu/libidn/libidn-1.33.tar.gz
Summary  : IETF stringprep, nameprep, punycode, IDNA text processing.
Group    : Development/Tools
License  : Apache-2.0 GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: libidn-bin
Requires: libidn-lib
Requires: libidn-data
Requires: libidn-doc
Requires: libidn-locales
BuildRequires : docbook-xml
BuildRequires : emacs
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : valgrind

%description
See the end for copying conditions.
Libidn is a package for internationalized string handling based on the
Stringprep, Punycode, IDNA and TLD specifications.  Libidn is a GNU
project.  See the file COPYING for licensing information.

%package bin
Summary: bin components for the libidn package.
Group: Binaries
Requires: libidn-data

%description bin
bin components for the libidn package.


%package data
Summary: data components for the libidn package.
Group: Data

%description data
data components for the libidn package.


%package dev
Summary: dev components for the libidn package.
Group: Development
Requires: libidn-lib
Requires: libidn-bin
Requires: libidn-data
Provides: libidn-devel

%description dev
dev components for the libidn package.


%package dev32
Summary: dev32 components for the libidn package.
Group: Default
Requires: libidn-lib32
Requires: libidn-bin
Requires: libidn-data

%description dev32
dev32 components for the libidn package.


%package doc
Summary: doc components for the libidn package.
Group: Documentation

%description doc
doc components for the libidn package.


%package lib
Summary: lib components for the libidn package.
Group: Libraries
Requires: libidn-data

%description lib
lib components for the libidn package.


%package lib32
Summary: lib32 components for the libidn package.
Group: Default
Requires: libidn-data

%description lib32
lib32 components for the libidn package.


%package locales
Summary: locales components for the libidn package.
Group: Default

%description locales
locales components for the libidn package.


%prep
%setup -q -n libidn-1.33
pushd ..
cp -a libidn-1.33 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install
%find_lang libidn

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/idn

%files data
%defattr(-,root,root,-)
/usr/share/emacs/site-lisp/idna.el
/usr/share/emacs/site-lisp/punycode.el

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libidn.so
/usr/lib64/pkgconfig/libidn.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libidn.so
/usr/lib32/pkgconfig/32libidn.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libidn.so.11
/usr/lib64/libidn.so.11.6.16

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libidn.so.11
/usr/lib32/libidn.so.11.6.16

%files locales -f libidn.lang 
%defattr(-,root,root,-)

