Name:           perl-YAML-Tiny
Version:	1.69
Release:	3%{?dist}
Summary:        Read/Write YAML files with as little code as possible
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/YAML-Tiny/
Source0:        http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/YAML-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
Requires:       perl(Carp)
Requires:       perl(Exporter)
Requires:       perl(Scalar::Util)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
YAML::Tiny is a Perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and
memory overhead.

%prep
%setup -q -n YAML-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
 AUTOMATED_TESTING=1

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 1.69-3
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.69-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.69-1
- 更新到 1.69

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.51-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.51-6
- 为 Magic 3.0 重建

* Tue Aug 21 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-5
- Add perl(Carp) to requires.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.51-3
- Perl 5.16 rebuild

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 1.51-2
- The POD tests do not run by default

* Wed Mar 14 2012 Petr Šabata <contyk@redhat.com> - 1.51-1
- 1.51 bump
- Remove command macros

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.50-4
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.50-3
- Perl mass rebuild

* Thu Jul 14 2011 Iain Arnell <iarnell@gmail.com> 1.50-2
- drop Test::MinimumVersion BR to avoid circular build deps

* Mon Jun 27 2011 Petr Sabata <contyk@redhat.com> - 1.50-1
- 1.50 bump
- Cleaning the spec file (I assume pre-EPEL6 compatibility is no longer
  essential here)
- Adding Exporter and Scalar::Util (optional but preferred) to BR/Rs

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 18 2010 Steven Pritchard <steve@kspei.com> 1.46-1
- Update to 1.46.

* Tue Dec 07 2010 Steven Pritchard <steve@kspei.com> 1.44-1
- Update to 1.44.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.40-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.40-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.40-1
- auto-update to 1.40 (by cpan-spec-update 0.01)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.39-1
- auto-update to 1.39 (by cpan-spec-update 0.01)
- added a new br on perl(File::Spec) (version 0.80)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Steven Pritchard <steve@kspei.com> 1.36-1
- Update to 1.36.
- BR Test::More.

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 1.32-1
- Update to 1.32.

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.25-2
- rebuild for new perl

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 1.25-1
- Update to 1.25.

* Tue Dec 11 2007 Steven Pritchard <steve@kspei.com> 1.21-1
- Update to 1.21.
- Update License tag.
- BR Test::MinimumVersion.

* Thu Aug 23 2007 Steven Pritchard <steve@kspei.com> 1.14-1
- Update to 1.14.

* Fri Jul 13 2007 Steven Pritchard <steve@kspei.com> 1.13-1
- Update to 1.13.

* Fri Jun 08 2007 Steven Pritchard <steve@kspei.com> 1.12-1
- Update to 1.12.

* Mon May 28 2007 Steven Pritchard <steve@kspei.com> 1.09-1
- Update to 1.09.

* Sat May 19 2007 Steven Pritchard <steve@kspei.com> 1.08-1
- Update to 1.08.
- Update description.

* Tue Mar 13 2007 Steven Pritchard <steve@kspei.com> 1.04-1
- Specfile autogenerated by cpanspec 1.70.
- Drop redundant perl build dependency.
- BR YAML, YAML::Syck, and Test::Pod for better test coverage.
