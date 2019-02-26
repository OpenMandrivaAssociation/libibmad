Summary:	OpenFabrics Alliance InfiniBand MAD library
Name:		libibmad
Version:	1.3.13
Release:	1
License:	GPLv2 or BSD
Url:		http://www.openfabrics.org/
Source:		http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	libibumad-devel

%description
libibmad provides low layer IB functions for use by the IB diagnostic
and management programs. These include MAD, SA, SMP, and other basic
IB functions.

%files
%{_libdir}/libibmad*.so.*
%doc AUTHORS COPYING ChangeLog

#---------------------------------------------------------------------------

%package devel
Summary:	Development files for the libibmad library
Requires:	%{name} = %{version}-%{release}, libibumad-devel

%description devel
Development files for the libibmad library.

%files devel
%{_libdir}/libibmad.so
%{_includedir}/infiniband/*.h

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

