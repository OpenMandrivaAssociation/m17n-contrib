%define version	1.1.0
%define release	%mkrel 1

%define m17n-db_version 1.3.4

Name:      m17n-contrib
Summary:   Contributed input methods for m17n library
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   LGPL
URL:       http://www.m17n.org/m17n-lib-en/
Source0:   %{name}-%{version}.tar.bz2

# It will be fixed soon.
Patch0:    m17n-contrib-fix-build.diff

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:        m17n-db >= %{m17n-db_version}
BuildRequires:   m17n-db-devel >= %{m17n-db_version}

%description
Contributed input methods for m17n library.


%prep
%setup -q
%patch0 -p1

%build
[[ ! -x configure ]] && ./bootstrap.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/tbl2mim.awk
%{_datadir}/m17n/*.mim
%{_datadir}/m17n/icons/*.png


