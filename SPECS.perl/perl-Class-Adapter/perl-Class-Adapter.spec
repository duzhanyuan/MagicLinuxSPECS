Name:           perl-Class-Adapter
Version:        1.08
Release:        9%{?dist}
Summary:        Perl implementation of the "Adapter" Design Pattern
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-Adapter/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Class-Adapter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Scalar::Util) >= 1.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Test::More) >= 0.47
# Tests only:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Class::Adapter class is intended as an abstract base class for creating
any sort of class or object that follows the Adapter pattern.

%prep
%setup -q -n Class-Adapter-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -empty -exec rmdir {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.08-9
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.08-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.08-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.08-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.08-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.08-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.08-2
- Perl mass rebuild

* Thu Mar 24 2011 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump
- Remove BuildRoot stuff

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.07-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun  8 2010 Petr Pisar <ppisar@redhat.com> - 1.07-1
- 1.07 bump (bug #600627)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.06-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.06-2
- rebuild against perl 5.10.1

* Wed Nov 25 2009 Stepan Kasal <skasal@redhat.com> - 1.06-1
- new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 29 2008 Marcela Mašláňová <mmaslano@redhat.com> 1.05-1
- Specfile autogenerated by cpanspec 1.77.
