Name:           perl-PerlIO-utf8_strict
Version:        0.006
Release:        4%{?dist}
Summary:        Fast and correct UTF-8 I/O
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PerlIO-utf8_strict/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/PerlIO-utf8_strict-%{version}.tar.gz
# Build:
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides a fast and correct UTF-8 PerlIO layer. Unlike perl's
default :utf8 layer it checks the input for correctness.

%prep
%setup -q -n PerlIO-utf8_strict-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/PerlIO/
%{perl_vendorarch}/PerlIO/
%{_mandir}/man3/PerlIO::utf8_strict.3*

%changelog
* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 0.006-4
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-2
- Perl 5.22 rebuild

* Fri May  1 2015 Paul Howarth <paul@city-fan.org> - 0.006-1
- Update to 0.006
  - Move to MakeMaker
- Use %%license

* Wed Nov 12 2014 Petr Pisar <ppisar@redhat.com> - 0.005-1
- 0.005 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-6
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.004-2
- Perl 5.18 rebuild

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 0.004-1
- 0.004 bump

* Thu Feb 21 2013 Petr Pisar <ppisar@redhat.com> - 0.003-1
- 0.003 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 20 2012 Petr Pisar <ppisar@redhat.com> 0.002-1
- Specfile autogenerated by cpanspec 1.78.