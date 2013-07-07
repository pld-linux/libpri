Summary:	ISDN PRI channel interface library
Summary(pl.UTF-8):	Biblioteka interfejsu do kanałów PRI ISDN
Name:		libpri
Version:	1.4.14
Release:	3
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.digium.com/pub/libpri/%{name}-%{version}.tar.gz
# Source0-md5:	8c581d8ebeff4c23cc498d71b94ca299
URL:		http://www.asterisk.org/
BuildRequires:	dahdi-tools-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISDN PRI channel interface library.

%description -l pl.UTF-8
Biblioteka interfejsu do kanałów PRI ISDN.

%package devel
Summary:	Header files and development documentation for libpri
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libpri
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libpri.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libpri.

%package static
Summary:	libpri static library
Summary(pl.UTF-8):	Statyczna biblioteka libpri
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libpri static library.

%description static -l pl.UTF-8
Statyczna biblioteka libpri.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	COVERAGE_CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

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
%{_includedir}/libpri.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpri.a
