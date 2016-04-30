#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : memcached
Version  : 1.4.25
Release  : 17
URL      : http://www.memcached.org/files/memcached-1.4.25.tar.gz
Source0  : http://www.memcached.org/files/memcached-1.4.25.tar.gz
Source1  : memcached.service
Summary  : High Performance, Distributed Memory Object Cache
Group    : Development/Tools
License  : BSD-3-Clause
Requires: memcached-bin
Requires: memcached-config
Requires: memcached-doc
BuildRequires : libevent-dev
BuildRequires : libxslt-bin

%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%package bin
Summary: bin components for the memcached package.
Group: Binaries
Requires: memcached-config

%description bin
bin components for the memcached package.


%package config
Summary: config components for the memcached package.
Group: Default

%description config
config components for the memcached package.


%package dev
Summary: dev components for the memcached package.
Group: Development
Requires: memcached-bin
Provides: memcached-devel

%description dev
dev components for the memcached package.


%package doc
Summary: doc components for the memcached package.
Group: Documentation

%description doc
doc components for the memcached package.


%prep
%setup -q -n memcached-1.4.25

%build
%configure --disable-static --sysconfdir=/etc/memcached \
--enable-64bit
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make test

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/memcached.service
## make_install_append content
install -m 0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/memcached
/usr/bin/memcached-tool

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/memcached.service

%files dev
%defattr(-,root,root,-)
/usr/include/memcached/protocol_binary.h

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
