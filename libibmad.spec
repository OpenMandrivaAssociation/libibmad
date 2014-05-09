Name:    libibmad
Summary: OpenFabrics Alliance InfiniBand MAD library
Version: 1.3.11
Release: 1%{?dist}
License: GPLv2 or BSD

Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
Source1: %{name}.rpmlintrc

BuildRequires: libibumad-devel >= 1.3.9, libtool, glibc-static-devel
ExcludeArch: s390 s390x

%description
libibmad provides low layer IB functions for use by the IB diagnostic
and management programs. These include MAD, SA, SMP, and other basic
IB functions. 

%package devel
Summary: Development files for the libibmad library

Requires: %{name} = %{version}-%{release}, libibumad-devel

%description devel
Development files for the libibmad library.

%package static
Summary: Static version of the libibmad library

Requires: %{name}-devel = %{version}-%{release}

%description static
Static version of the libibmad library

%prep
%setup -q

%build
%configure2_5x
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%{_libdir}/libibmad*.so.*
%doc AUTHORS COPYING ChangeLog

%files devel
%{_libdir}/libibmad.so
%{_includedir}/infiniband/*.h

%files static
%{_libdir}/libibmad.a
