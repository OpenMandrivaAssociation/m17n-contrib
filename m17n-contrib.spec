%define version	1.1.12
%define release	%mkrel 1

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
%setup -qn %{name}-%{version}

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


%changelog
* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 1.1.12-1mdv2011.0
+ Revision: 582860
- 1.1.2 final

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 1.1.12-0.RC.1mdv2011.0
+ Revision: 580651
- 1.1.12 RC

* Wed Mar 31 2010 Funda Wang <fwang@mandriva.org> 1.1.11-1mdv2010.1
+ Revision: 530293
- update to new version 1.1.11

* Wed Jul 29 2009 Funda Wang <fwang@mandriva.org> 1.1.10-1mdv2010.0
+ Revision: 402889
- New version 1.1.10

* Sat Mar 14 2009 Funda Wang <fwang@mandriva.org> 1.1.9-2mdv2009.1
+ Revision: 355013
- should be a noarch package
- update to new version 1.1.9

* Tue Oct 21 2008 Funda Wang <fwang@mandriva.org> 1.1.8-1mdv2009.1
+ Revision: 295991
- New version 1.1.8

* Tue Jul 08 2008 Funda Wang <fwang@mandriva.org> 1.1.7-1mdv2009.0
+ Revision: 232839
- New version 1.1.7

* Wed Feb 13 2008 Funda Wang <fwang@mandriva.org> 1.1.6-1mdv2008.1
+ Revision: 167083
- add back buildroot
- revert noarch, as our build system does not like it
- New version 1.1.6
- It should be noarch pacakge

  + Thierry Vignaud <tv@mandriva.org>
    - fix bogus requires, thus making it installable

* Fri Dec 28 2007 Funda Wang <fwang@mandriva.org> 1.1.5-1mdv2008.1
+ Revision: 138860
- New version 1.1.5

* Fri Dec 28 2007 Funda Wang <fwang@mandriva.org> 1.1.3-1mdv2008.1
+ Revision: 138763
- New version 1.1.4

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 24 2007 Funda Wang <fwang@mandriva.org> 1.1.3-1mdv2008.0
+ Revision: 54906
- do not own /usr/share/m17n dir
- fix file list
- New verison to fix building from source
- New version

* Thu Jul 05 2007 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2008.0
+ Revision: 48501
- from UTUMI Hirosi <utuhiro78@yahoo.co.jp>:
  o new release
  o remove patch0


* Tue Jan 09 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.1.0-1mdv2007.0
+ Revision: 106776
- add patch
- new release

* Wed Oct 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-1.20061013.1mdv2007.1
+ Revision: 66018
- Import m17n-contrib

* Sat Oct 14 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.0.0-1.20061013.1mdv2007.0
- first spec for Mandriva

