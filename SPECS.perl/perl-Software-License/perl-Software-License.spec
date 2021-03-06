# We need to patch the test suite if we have an old version of Test::More
%global old_test_more %(perl -MTest::More -e 'print (($Test::More::VERSION < 0.88) ? 1 : 0);' 2>/dev/null || echo 0)

Name:           perl-Software-License
Version:	0.103010
Release:	4%{?dist}
Summary:        Package that provides templated software licenses
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Software-License/
# For unknown reasons this module URL is currently missing
#Source0:        http://www.cpan.org/modules/by-module/Software/Software-License-%{version}.tar.gz
Source0:        http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Software-License-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Section)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Software-License contains templates for common open source software licenses.

%prep
%setup -q -n Software-License-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT

%check
 RELEASE_TESTING=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Software/
%{_mandir}/man3/Software::License.3pm*
%{_mandir}/man3/Software::License::*.3pm*
%{_mandir}/man3/Software::LicenseUtils.3pm*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.103010-4
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.103010-3
- 为 Magic 3.0 重建

* Wed Sep 16 2015 Liu Di <liudidi@gmail.com> - 0.103010-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.103010-1
- 更新到 0.103010

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.103004-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.103004-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.103004-3
- Perl 5.16 rebuild

* Wed Mar  7 2012 Paul Howarth <paul@city-fan.org> - 0.103004-2
- Add test suite patch to support building with Test::More < 0.88 so that we
  can build for EPEL-5, only applying the patch when necessary
- Drop redundant versioned requirements of XXX >= 0.000
- Drop BR: perl ≥ 1:5.6.0; even EL-3 could have satisfied that
- BR: perl(base) and perl(Carp), which could be dual-lived
- BR: perl(Test::Pod) for full test coverage
- Run the release tests too
- Don't need to remove empty directories from buildroot
- Don't use macros for commands
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit

* Mon Jan 30 2012 Daniel P. Berrange <berrange@redhat.com> - 0.103004-1
- Update to 0.103004 release (rhbz #750790)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 03 2011 Iain Arnell <iarnell@gmail.com> 0.103002-1
- update to latest upstream version

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.102341-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102341-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.102341-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Dec 17 2010 Daniel P. Berrange <berrange@redhat.com> - 0.102341-1
- Update to 0.102341 release

* Wed Jun 02 2010 Iain Arnell <iarnell@gmail.com> 0.101410-1
- update to 0.101410 release

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.012-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.012-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Daniel P. Berrange <berrange@redhat.com> - 0.012-1
- Update to 0.012 release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep 20 2008 Daniel P. Berrange <berrange@redhat.com> 0.008-3
- Remove explicit requires that duplicate automatic perl deps

* Sat Sep 06 2008 Daniel P. Berrange <berrange@redhat.com> 0.008-2
- Fix description
- Add missing Test::More BR

* Fri Sep 05 2008 Daniel P. Berrange <berrange@redhat.com> 0.008-1
- Specfile autogenerated by cpanspec 1.77.
