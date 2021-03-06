Name:           perl-Import-Into
Version:	1.002005
Release:	3%{?dist}
Summary:        Import packages into other packages
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Import-Into/
Source0:        http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/Import-Into-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Loading Import::Into creates a global method import::into which you can call on
any package to import it into another package.

%prep
%setup -q -n Import-Into-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Import/
%{_mandir}/man3/Import::Into.3pm*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 1.002005-3
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.002005-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.002005-1
- 更新到 1.002005

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1.002002-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May  7 2014 Paul Howarth <paul@city-fan.org> - 1.002002-1
- Update to 1.002002
  - Minor metadata updates
- This release by ETHER -> update source URL
- Classify buildreqs by usage

* Wed Mar 12 2014 Paul Howarth <paul@city-fan.org> - 1.002001-1
- Update to 1.002001
  - Allow specifying by caller level, as well as specifying file, line, and
    version
  - Fix tests and Makefile.PL to support perl 5.6
- This release by HAARG -> update source URL
- Specify all dependencies
- Make %%files list more explicit

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.001001-2
- Perl 5.18 rebuild

* Fri Apr 19 2013 Iain Arnell <iarnell@gmail.com> 1.001001-1
- update to latest upstream version

* Sat Feb 16 2013 Iain Arnell <iarnell@gmail.com> 1.001000-1
- Specfile autogenerated by cpanspec 1.79.
