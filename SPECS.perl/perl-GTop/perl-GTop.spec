Name:           perl-GTop
Version:        0.18
Release:        5%{?dist}
Summary:        Perl interface to libgtop
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/GTop/
Source0:        http://www.cpan.org/authors/id/M/MJ/MJH/GTop-%{version}.tar.gz
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# core
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
# non-perl
BuildRequires:  libgtop2-devel

%?perl_default_filter

%description
This is a perl interface to the libgtop library, useful for collecting
real-time performance and other system statistics.


%prep
%setup -q -n GTop-%{version}

# rpmlint pacifications...
find . -type f -exec chmod -c -x {} \;
perl -pi -e 's|^#!perl|#!/usr/bin/perl|' examples/*

# thread funkiness on ppc/s390
%ifarch ppc ppc64 s390
mv t/threads.t t/threads.t.disable
%endif

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README TODO examples/ t/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/GTop*
%exclude %{perl_vendorarch}/config.pl
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.18-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.18-2
- Perl 5.16 rebuild

* Tue May 29 2012 Iain Arnell <iarnell@gmail.com> 0.18-1
- update to latest upstream version

* Tue Jan 17 2012 Iain Arnell <iarnell@gmail.com> - 0.17-2
- rebuilt again for F17 mass rebuild

* Sat Jan 14 2012 Iain Arnell <iarnell@gmail.com> 0.17-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use DESTDIR, not PERL_INSTALL_ROOT
- use perl_default_filter

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-15
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-13
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Oct 13 2010 Dan Horák <dan[at]danny.cz> - 0.16-12
- exclude the threads test also on s390

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-11
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.16-10
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 26 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.16-8
- Stripping bad provides of private Perl extension libs

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.16-6
- rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.16-5
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.16-4
- bump

* Mon Apr 30 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.16-3
- disable t/threads.t on ppc

* Mon Apr 30 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.16-2
- bump

* Thu Apr 26 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.16-1
- Specfile autogenerated by cpanspec 1.69.1.