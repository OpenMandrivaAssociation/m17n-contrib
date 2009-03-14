%define version	1.1.9
%define release	%mkrel 2

%define m17n_db_version 1.5.0

Name:      m17n-contrib
Summary:   Contributed input methods for m17n library
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   LGPLv2+
URL:       http://www.m17n.org/m17n-lib-en/
Source0:   http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.gz
Requires:        m17n-db >= %{m17n_db_version}
BuildRequires:   m17n-db-devel >= %{m17n_db_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-%{release}-buildroot

%description
Contributed input methods for m17n library.

%prep
%setup -q

%build
[[ ! -x configure ]] && ./bootstrap.sh
%configure2_5x --build=%{_host}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# The file conflicts with m17n-data
rm -f $RPM_BUILD_ROOT%{_datadir}/m17n/bn-itrans.mim

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/m17n/*.mim
%{_datadir}/m17n/icons/*
%{_datadir}/m17n/scripts/*
