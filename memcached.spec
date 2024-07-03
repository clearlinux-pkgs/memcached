#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
Name     : memcached
Version  : 1.6.29
Release  : 76
URL      : https://memcached.org/files/memcached-1.6.29.tar.gz
Source0  : https://memcached.org/files/memcached-1.6.29.tar.gz
Source1  : memcached.service
Summary  : High Performance, Distributed Memory Object Cache
Group    : Development/Tools
License  : BSD-3-Clause
Requires: memcached-bin = %{version}-%{release}
Requires: memcached-license = %{version}-%{release}
Requires: memcached-man = %{version}-%{release}
Requires: memcached-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : cyrus-sasl-dev
BuildRequires : libevent-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(openssl)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%package bin
Summary: bin components for the memcached package.
Group: Binaries
Requires: memcached-license = %{version}-%{release}
Requires: memcached-services = %{version}-%{release}

%description bin
bin components for the memcached package.


%package dev
Summary: dev components for the memcached package.
Group: Development
Requires: memcached-bin = %{version}-%{release}
Provides: memcached-devel = %{version}-%{release}
Requires: memcached = %{version}-%{release}

%description dev
dev components for the memcached package.


%package extras
Summary: extras components for the memcached package.
Group: Default

%description extras
extras components for the memcached package.


%package license
Summary: license components for the memcached package.
Group: Default

%description license
license components for the memcached package.


%package man
Summary: man components for the memcached package.
Group: Default

%description man
man components for the memcached package.


%package services
Summary: services components for the memcached package.
Group: Systemd services
Requires: systemd

%description services
services components for the memcached package.


%prep
%setup -q -n memcached-1.6.29
cd %{_builddir}/memcached-1.6.29
pushd ..
cp -a memcached-1.6.29 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719977103
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --sysconfdir=/etc/memcached \
--enable-64bit
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --sysconfdir=/etc/memcached \
--enable-64bit
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719977103
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/memcached
cp %{_builddir}/memcached-%{version}/COPYING %{buildroot}/usr/share/package-licenses/memcached/48d3aad525d9acd423ac6021c44fa4d15d4ee9ad || :
cp %{_builddir}/memcached-%{version}/LICENSE.bipbuffer %{buildroot}/usr/share/package-licenses/memcached/7d1d9235b1b589f4347e7e2452db90d57b04fea9 || :
cp %{_builddir}/memcached-%{version}/vendor/mcmc/LICENSE %{buildroot}/usr/share/package-licenses/memcached/4b3f62d5726ced2394f025b2c6febeafdb3c571b || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/memcached.service
## install_append content
install -m 0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/memcached
/usr/bin/memcached

%files dev
%defattr(-,root,root,-)
/usr/include/memcached/protocol_binary.h
/usr/include/memcached/xxhash.h

%files extras
%defattr(-,root,root,-)
/usr/bin/memcached-tool

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/memcached/48d3aad525d9acd423ac6021c44fa4d15d4ee9ad
/usr/share/package-licenses/memcached/4b3f62d5726ced2394f025b2c6febeafdb3c571b
/usr/share/package-licenses/memcached/7d1d9235b1b589f4347e7e2452db90d57b04fea9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/memcached.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/memcached.service
