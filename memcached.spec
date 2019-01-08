#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : memcached
Version  : 1.5.12
Release  : 30
URL      : http://memcached.org/files/memcached-1.5.12.tar.gz
Source0  : http://memcached.org/files/memcached-1.5.12.tar.gz
Source1  : memcached.service
Summary  : High Performance, Distributed Memory Object Cache
Group    : Development/Tools
License  : BSD-3-Clause
Requires: memcached-bin = %{version}-%{release}
Requires: memcached-license = %{version}-%{release}
Requires: memcached-man = %{version}-%{release}
Requires: memcached-services = %{version}-%{release}
BuildRequires : cyrus-sasl-dev
BuildRequires : libevent-dev
BuildRequires : libxslt-bin

%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%package bin
Summary: bin components for the memcached package.
Group: Binaries
Requires: memcached-license = %{version}-%{release}
Requires: memcached-man = %{version}-%{release}
Requires: memcached-services = %{version}-%{release}

%description bin
bin components for the memcached package.


%package dev
Summary: dev components for the memcached package.
Group: Development
Requires: memcached-bin = %{version}-%{release}
Provides: memcached-devel = %{version}-%{release}

%description dev
dev components for the memcached package.


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

%description services
services components for the memcached package.


%prep
%setup -q -n memcached-1.5.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546947542
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --sysconfdir=/etc/memcached \
--enable-64bit
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1546947542
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/memcached
cp COPYING %{buildroot}/usr/share/package-licenses/memcached/COPYING
cp LICENSE.bipbuffer %{buildroot}/usr/share/package-licenses/memcached/LICENSE.bipbuffer
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/memcached.service
## install_append content
install -m 0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/memcached
/usr/bin/memcached-tool

%files dev
%defattr(-,root,root,-)
/usr/include/memcached/protocol_binary.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/memcached/COPYING
/usr/share/package-licenses/memcached/LICENSE.bipbuffer

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/memcached.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/memcached.service
