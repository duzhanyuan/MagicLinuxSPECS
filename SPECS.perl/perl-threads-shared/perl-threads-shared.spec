Name:           perl-threads-shared
Version:	1.48
Release:	2%{?dist}
Summary:        Perl extension for sharing data structures between threads
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/threads-shared/
Source0:        http://www.cpan.org/authors/id/J/JD/JDHEDDEN/threads-shared-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl(Config)
# Config_m not needed
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(threads) >= 1.73
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
# Win32 not needed
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(threads) >= 1.73
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
By default, variables are private to each thread, and each newly created
thread gets a private copy of each existing variable. This module allows
you to share variables across different threads (and pseudo-forks on
Win32). It is used together with the threads module.

%prep
%setup -q -n threads-shared-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/threads*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.48-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.48-1
- 更新到 1.48

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.46-5
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.46-4
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Petr Pisar <ppisar@redhat.com> - 1.46-2
- Declare optional tests

* Wed Feb 05 2014 Petr Pisar <ppisar@redhat.com> - 1.46-1
- 1.46 bump

* Thu Nov 14 2013 Petr Pisar <ppisar@redhat.com> - 1.45-1
- 1.45 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1.43-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.43-5
- Link minimal build-root packages against libperl.so explicitly

* Tue Jul 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-4
- Remove BR perl(Test)

* Tue Jul 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-3
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Fri Nov 23 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-2
- Add BR perl(File::Spec)
- Replace PERL_INSTALL_ROOT with DESTDIR
- Remove deleting empty directories
- Remove defattr

* Wed Oct 03 2012 Petr Pisar <ppisar@redhat.com> - 1.42-1
- 1.42 bump

* Mon Sep 10 2012 Petr Pisar <ppisar@redhat.com> - 1.41-1
- 1.41 bump

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.40-240
- bump release to override sub-package from perl.spec 

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.40-3
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Petr Pisar <ppisar@redhat.com> - 1.40-1
- 1.40 bump

* Tue Sep 06 2011 Petr Pisar <ppisar@redhat.com> - 1.39-1
- 1.39 bump

* Wed Aug 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.37-3
- change path on vendor, so our debuginfo are not conflicting with
 perl core debuginfos

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.37-2
- Perl mass rebuild

* Tue Apr 26 2011 Petr Pisar <ppisar@redhat.com> - 1.37-1
- 1.37 bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Petr Pisar <ppisar@redhat.com> - 1.36-1
- 1.36 bump

* Mon Oct 11 2010 Petr Pisar <ppisar@redhat.com> - 1.34-1
- 1.34 bump

* Thu Sep 23 2010 Petr Pisar <ppisar@redhat.com> 1.33-1
- Specfile autogenerated by cpanspec 1.78.
- Fix dependencies
- Requires perl(Scalar::Util) is autodetected
- Do not provide private library
- Remove pre-F12 BuildRoot stuff
