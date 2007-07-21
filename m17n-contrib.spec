%define version	1.1.2
%define release	%mkrel 1

%define m17n-db_version 1.4.0

Name:      m17n-contrib
Summary:   Contributed input methods for m17n library
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   LGPL
URL:       http://www.m17n.org/m17n-lib-en/
Source0:   http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:        m17n-db >= %{m17n-db_version}
BuildRequires:   m17n-db-devel >= %{m17n-db_version}

%description
Contributed input methods for m17n library.

%prep
%setup -q

%build
[[ ! -x configure ]] && ./bootstrap.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# The file conflicts with m17n-data
rm -f $RPM_BUILD_ROOT%{_datadir}/m17n/bn-itrans.mim

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/tbl2mim.awk
%{_datadir}/m17n/*.mim
%{_datadir}/m17n/icons/*.png
