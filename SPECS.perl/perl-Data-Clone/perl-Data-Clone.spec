Name:           perl-Data-Clone
Version:        0.004
Release:        6%{?dist}
Summary:        Polymorphic data cloning
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Clone/
Source0:        http://www.cpan.org/authors/id/G/GF/GFUJI/Data-Clone-%{version}.tar.gz
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.18
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(threads)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader) >= 0.1
Requires:       perl(Exporter)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Data::Clone does data cloning, i.e. copies things recursively. This is
smart so that it works with not only non-blessed references, but also
with blessed references (i.e. objects). When clone() finds an object, it
calls a clone method of the object if the object has a clone, otherwise
it makes a surface copy of the object. That is, this module does
polymorphic data cloning.

%prep
%setup -q -n Data-Clone-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 0.004-6
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-1
- 0.004 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.003-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 0.003-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Iain Arnell <iarnell@gmail.com> 0.003-2
- BuildRequire inc::Module::Install, not EU::MM
- additional BuildRequires for tests

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 0.003-1
- Specfile autogenerated by cpanspec 1.79.