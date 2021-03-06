Name:           perl-Class-Prototyped
Version:	1.13
Release:	2%{?dist}
Summary:        Fast prototype-based OO programming in Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-Prototyped/
Source0:        http://www.cpan.org/authors/id/T/TE/TEVERETT/Class-Prototyped-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This package provides for efficient and simple prototype-based programming
in Perl. You can provide different subroutines for each object, and also
have objects inherit their behavior and state from another object.

%prep
%setup -q -n Class-Prototyped-%{version}

# RPM 4.8 style
%{?filter_setup:
%filter_from_provides /^perl(My[^)]*Class)$/g
%filter_from_requires /^perl(Class::Prototyped::Graph)$/g
%filter_requires_in %{_docdir}/examples
%filter_setup
}
# RPM 4.9 style
%global __provides_exclude %{?__provides_exclude?__provides_exclude|}^perl\\(My[^\\)]*Class\\)$
%global __requires_exclude %{?__requires_exclude?__requires_exclude|}^perl\\(Class::Prototyped::Graph\\)$
%global __requires_exclude_from %{?__requires_exclude_from?__requires_exclude_from|}%{_docdir}/examples

# Documentation and libraries should not be executable
chmod -x perf/* examples/* Changes lib/Class/*.pm lib/Class/Prototyped/*


%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}

./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README perf/ examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.13-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.13-1
- 更新到 1.13

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.11-21
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.11-20
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.11-19
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.11-18
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.11-17
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.11-16
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.11-15
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.11-14
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.11-13
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 1.11-11
- RPM 4.9 dependency filtering added

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.11-10
- Perl mass rebuild

* Mon Feb 14 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.11-9
- fix broken filter

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.11-7
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.11-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.11-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  9 2009 Lubomir Rintel <lkundrak@v3.sk> 1.11-3
- Fix permissions
- Fix requires/provides

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.11-1
- 1.11

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.10-3
- rebuild for new perl

* Mon Apr 30 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.10-2
- bump

* Mon Apr 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.10-1
- Specfile autogenerated by cpanspec 1.70.
