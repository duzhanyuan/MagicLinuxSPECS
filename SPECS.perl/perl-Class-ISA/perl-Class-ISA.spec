Name:           perl-Class-ISA
Version:        0.36
Release:        1015%{?dist}
Summary:        Report the search path for a class's ISA tree
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-ISA/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/Class-ISA-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This library provides functions that return the list (in order) of names of
(super-)classes Perl would search to find a method, with no duplicates.

%prep
%setup -q -n Class-ISA-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
rm -rf %{buildroot}/%{_mandir}/man3/*
%{_fixperms} %{buildroot}/*

%check


%files
%doc ChangeLog README
%{perl_vendorlib}/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.36-1015
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.36-1014
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.36-1013
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.36-1012
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.36-1011
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.36-1010
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-1009
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.36-1008
- Perl 5.16 rebuild

* Fri Apr 13 2012 Petr Šabata <contyk@redhat.com> - 0.36-1007
- Change description to something more descriptive (#811144)
- Modernize spec

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-1006
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.36-1005
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-1004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Petr Pisar <ppisar@redhat.com> - 0.36-1003
- Increase release number to be higher than Perl core package (bug #651317)

* Mon May 10 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.36-2
- fix of conflicting man pages 

* Mon May 03 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.36-1
- Specfile autogenerated by cpanspec 1.78.
