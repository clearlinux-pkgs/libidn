#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x08302DB6A2670428 (tim.ruehsen@gmx.de)
#
Name     : libidn
Version  : 1.35
Release  : 24
URL      : http://mirrors.kernel.org/gnu/libidn/libidn-1.35.tar.gz
Source0  : http://mirrors.kernel.org/gnu/libidn/libidn-1.35.tar.gz
Source1 : http://mirrors.kernel.org/gnu/libidn/libidn-1.35.tar.gz.sig
Summary  : IETF stringprep, nameprep, punycode, IDNA text processing.
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: libidn-bin = %{version}-%{release}
Requires: libidn-data = %{version}-%{release}
Requires: libidn-info = %{version}-%{release}
Requires: libidn-lib = %{version}-%{release}
Requires: libidn-license = %{version}-%{release}
Requires: libidn-locales = %{version}-%{release}
Requires: libidn-man = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : emacs
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : valgrind

%description
See the end for copying conditions.
Libidn is a package for internationalized string handling based on the
Stringprep, Punycode, IDNA and TLD specifications.  Libidn is a GNU
project.  See the file COPYING for licensing information.

%package bin
Summary: bin components for the libidn package.
Group: Binaries
Requires: libidn-data = %{version}-%{release}
Requires: libidn-license = %{version}-%{release}

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
Requires: libidn-lib = %{version}-%{release}
Requires: libidn-bin = %{version}-%{release}
Requires: libidn-data = %{version}-%{release}
Provides: libidn-devel = %{version}-%{release}
Requires: libidn = %{version}-%{release}

%description dev
dev components for the libidn package.


%package dev32
Summary: dev32 components for the libidn package.
Group: Default
Requires: libidn-lib32 = %{version}-%{release}
Requires: libidn-bin = %{version}-%{release}
Requires: libidn-data = %{version}-%{release}
Requires: libidn-dev = %{version}-%{release}

%description dev32
dev32 components for the libidn package.


%package info
Summary: info components for the libidn package.
Group: Default

%description info
info components for the libidn package.


%package lib
Summary: lib components for the libidn package.
Group: Libraries
Requires: libidn-data = %{version}-%{release}
Requires: libidn-license = %{version}-%{release}

%description lib
lib components for the libidn package.


%package lib32
Summary: lib32 components for the libidn package.
Group: Default
Requires: libidn-data = %{version}-%{release}
Requires: libidn-license = %{version}-%{release}

%description lib32
lib32 components for the libidn package.


%package license
Summary: license components for the libidn package.
Group: Default

%description license
license components for the libidn package.


%package locales
Summary: locales components for the libidn package.
Group: Default

%description locales
locales components for the libidn package.


%package man
Summary: man components for the libidn package.
Group: Default

%description man
man components for the libidn package.


%prep
%setup -q -n libidn-1.35
cd %{_builddir}/libidn-1.35
pushd ..
cp -a libidn-1.35 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573772923
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1573772923
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libidn
cp %{_builddir}/libidn-1.35/COPYING %{buildroot}/usr/share/package-licenses/libidn/248b64d247f0104e0b86a63358f8310f641a3433
cp %{_builddir}/libidn-1.35/COPYING.LESSERv2 %{buildroot}/usr/share/package-licenses/libidn/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/libidn-1.35/COPYING.LESSERv3 %{buildroot}/usr/share/package-licenses/libidn/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/libidn-1.35/COPYINGv2 %{buildroot}/usr/share/package-licenses/libidn/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/libidn-1.35/COPYINGv3 %{buildroot}/usr/share/package-licenses/libidn/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/libidn-1.35/doc/specifications/COPYING.UCD %{buildroot}/usr/share/package-licenses/libidn/f13a577febd13d4323fb91f99615f194826511fd
cp %{_builddir}/libidn-1.35/java/LICENSE-2.0.txt %{buildroot}/usr/share/package-licenses/libidn/2b8b815229aa8a61e483fb4ba0588b8b6c491890
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
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
/usr/include/idn-free.h
/usr/include/idn-int.h
/usr/include/idna.h
/usr/include/pr29.h
/usr/include/punycode.h
/usr/include/stringprep.h
/usr/include/tld.h
/usr/lib64/libidn.so
/usr/lib64/pkgconfig/libidn.pc
/usr/share/man/man3/idn_free.3
/usr/share/man/man3/idna_strerror.3
/usr/share/man/man3/idna_to_ascii_4i.3
/usr/share/man/man3/idna_to_ascii_4z.3
/usr/share/man/man3/idna_to_ascii_8z.3
/usr/share/man/man3/idna_to_ascii_lz.3
/usr/share/man/man3/idna_to_unicode_44i.3
/usr/share/man/man3/idna_to_unicode_4z4z.3
/usr/share/man/man3/idna_to_unicode_8z4z.3
/usr/share/man/man3/idna_to_unicode_8z8z.3
/usr/share/man/man3/idna_to_unicode_8zlz.3
/usr/share/man/man3/idna_to_unicode_lzlz.3
/usr/share/man/man3/pr29_4.3
/usr/share/man/man3/pr29_4z.3
/usr/share/man/man3/pr29_8z.3
/usr/share/man/man3/pr29_strerror.3
/usr/share/man/man3/punycode_decode.3
/usr/share/man/man3/punycode_encode.3
/usr/share/man/man3/punycode_strerror.3
/usr/share/man/man3/stringprep.3
/usr/share/man/man3/stringprep_4i.3
/usr/share/man/man3/stringprep_4zi.3
/usr/share/man/man3/stringprep_check_version.3
/usr/share/man/man3/stringprep_convert.3
/usr/share/man/man3/stringprep_locale_charset.3
/usr/share/man/man3/stringprep_locale_to_utf8.3
/usr/share/man/man3/stringprep_profile.3
/usr/share/man/man3/stringprep_strerror.3
/usr/share/man/man3/stringprep_ucs4_nfkc_normalize.3
/usr/share/man/man3/stringprep_ucs4_to_utf8.3
/usr/share/man/man3/stringprep_unichar_to_utf8.3
/usr/share/man/man3/stringprep_utf8_nfkc_normalize.3
/usr/share/man/man3/stringprep_utf8_to_locale.3
/usr/share/man/man3/stringprep_utf8_to_ucs4.3
/usr/share/man/man3/stringprep_utf8_to_unichar.3
/usr/share/man/man3/tld_check_4.3
/usr/share/man/man3/tld_check_4t.3
/usr/share/man/man3/tld_check_4tz.3
/usr/share/man/man3/tld_check_4z.3
/usr/share/man/man3/tld_check_8z.3
/usr/share/man/man3/tld_check_lz.3
/usr/share/man/man3/tld_default_table.3
/usr/share/man/man3/tld_get_4.3
/usr/share/man/man3/tld_get_4z.3
/usr/share/man/man3/tld_get_table.3
/usr/share/man/man3/tld_get_z.3
/usr/share/man/man3/tld_strerror.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libidn.so
/usr/lib32/pkgconfig/32libidn.pc
/usr/lib32/pkgconfig/libidn.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libidn-components.png
/usr/share/info/libidn.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libidn.so.12
/usr/lib64/libidn.so.12.6.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libidn.so.12
/usr/lib32/libidn.so.12.6.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libidn/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libidn/248b64d247f0104e0b86a63358f8310f641a3433
/usr/share/package-licenses/libidn/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/libidn/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libidn/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/libidn/f13a577febd13d4323fb91f99615f194826511fd
/usr/share/package-licenses/libidn/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/idn.1

%files locales -f libidn.lang
%defattr(-,root,root,-)

