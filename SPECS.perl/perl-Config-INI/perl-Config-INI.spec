Name:           perl-Config-INI
Version:        0.019
Release:        6%{?dist}
Summary:        Config::INI Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-INI/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Config-INI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Mixin::Linewise::Readers)
BuildRequires:  perl(Mixin::Linewise::Writers)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Config::INI - simple .ini-file format.

%prep
%setup -q -n Config-INI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes LICENSE README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.019-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.019-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.019-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.019-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.019-2
- 为 Magic 3.0 重建

* Thu Jan 05 2012 Iain Arnell <iarnell@gmail.com> 0.019-1
- update to latest upstream version

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.018-2
- Perl mass rebuild

* Sat Jun 04 2011 Iain Arnell <iarnell@gmail.com> 0.018-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.017-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Dec 14 2010 Iain Arnell <iarnell@gmail.com> 0.017-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Sep 07 2010 Iain Arnell <iarnell@gmail.com> 0.016-1
- update to latest upstream

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.014-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.014-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 19 2009 Iain Arnell 0.014-1
- Specfile autogenerated by cpanspec 1.77.