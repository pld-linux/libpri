Summary:	ISDN PRI channel interface library
Summary(pl):	Biblioteka interfejsu do kana��w PRI ISDN
Name:		libpri
Version:	1.4.0
Release:	0.beta1
License:	GPL
Group:		Libraries
Source0:	http://ftp.digium.com/pub/libpri/releases/libpri-%{version}-beta1.tar.gz
# Source0-md5:	0df4aab74517ff425392cfafc6b97eab
#Patch0:		%{name}-Makefile.patch
URL:		http://www.asterisk.org/
BuildRequires:	zaptel-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISDN PRI channel interface library.

%description -l pl
Biblioteka interfejsu do kana��w PRI ISDN.

%package devel
Summary:	Header files and development documentation for libpri
Summary(pl):	Pliki nag��wkowe i dokumentacja do libpri
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libpri.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do libpri.

%package static
Summary:	libpri static library
Summary(pl):	Statyczna biblioteka libpri
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libpri static library.

%description static -l pl
Statyczna biblioteka libpri.

%prep
%setup -q -n %{name}-%{version}-beta1
#%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
sed -i s,/lib,/%{_lib},g Makefile
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3},%{_includedir},%{_libdir}}

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT \
	LIBDIR=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libpri.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpri.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpri.a
