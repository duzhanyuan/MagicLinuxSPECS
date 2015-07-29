Name:           perl-ExtUtils-MakeMaker-Coverage
Version:        0.05
Release:        21%{?dist}
Summary:        Allows perl modules to check test coverage with Devel::Cover

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://backpan.perl.org/authors/id/S/SM/SMPETERS/
Source0:        %{url}ExtUtils-MakeMaker-Coverage-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker), perl(Object::Accessor)
BuildRequires:  perl(Test::More), perl(Test::Pod), perl(Test::Pod::Coverage)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# rpm doesn't catch these (BZ 490743)
Requires:       perl(Object::Accessor), perl(Devel::Cover)

%description
This module adds an additional target to the Makefile generated by
ExtUtils::MakeMaker. The target, testcover, calls cover, the
command-line script to generate test coverage statistics, to clean up
any data from a previous run. It then runs the tests, as if make test
was run, then calls cover again to generate the coverage statistics.


%prep
%setup -q -n ExtUtils-MakeMaker-Coverage-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/ExtUtils/MakeMaker/Coverage.pm
%{_mandir}/man3/*.3*
%{_bindir}/testcover

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.05-21
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.05-18
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.05-15
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.05-13
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-11
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-10
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.05-8
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-6
- Add R: perl(Object::Accessor), perl(Devel::Cover) (BZ 490743).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-4
- rebuild for new perl

* Mon Aug 20 2007 Robin Norwood <rnorwood@redhat.com> - 0.05-3
- More BR's: perl(Test::Pod) and perl(Test::Pod::Coverage)

* Fri Aug 17 2007 Robin Norwood <rnorwood@redhat.com> - 0.05-2
- Add missing BuildRequires: perl(Test::More)

* Mon Aug 13 2007 Robin Norwood <rnorwood@redhat.com> - 0.05-1
- Initial build