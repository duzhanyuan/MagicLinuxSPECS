Name:		perl-CPAN-Changes
Summary:	Read and write Changes files
Version:	0.400002
Release:	4%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/CPAN-Changes/
Source0:        http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/CPAN-Changes-%{version}.tar.gz
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildArch:	noarch
BuildRequires:	perl >= 4:5.10.0
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
BuildRequires:	perl(Text::Wrap)
BuildRequires:	perl(version) >= 0.79

%description
It is standard practice to include a Changes file in your distribution. The
purpose of the Changes file is to help a user figure out what has changed
since the last release.

People have devised many ways to write the Changes file. A preliminary
specification has been created (CPAN::Changes::Spec) to encourage module
authors to write clear and concise Changes.

This module will help users programmatically read and write Changes files
that conform to the specification.

%prep
%setup -q -n CPAN-Changes-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check

 TEST_FILES="$(echo $(find xt/ -name '*.t'))"

%files
%doc Changes README
%{perl_vendorlib}/CPAN/
%{perl_vendorlib}/Test/
%{_mandir}/man3/CPAN::Changes.3pm*
%{_mandir}/man3/CPAN::Changes::Release.3pm*
%{_mandir}/man3/CPAN::Changes::Spec.3pm*
%{_mandir}/man3/Test::CPAN::Changes.3pm*
%{_bindir}/tidy_changelog
%{_mandir}/man1/tidy_changelog.1*
%{_mandir}/man3/CPAN::Changes::Group.3pm*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.400002-4
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.400002-3
- 为 Magic 3.0 重建

* Mon Sep 14 2015 Liu Di <liudidi@gmail.com> - 0.400002-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.400002-1
- 更新到 0.400002

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.19-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.19-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.19-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.19-2
- Perl 5.16 rebuild

* Tue May  1 2012 Paul Howarth <paul@city-fan.org> - 0.19-1
- Update to 0.19:
  - Test::CPAN::Changes now accepts version entries ending in '-TRIAL'
    (CPAN RT#76882)
  - releases() in CPAN::Changes also accepts entries ending in '-TRIAL'
- Don't need to remove empty directories from buildroot
- Drop %%defattr, redundant since rpm 4.4

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 0.18-2
- Fedora 17 mass rebuild

* Tue Oct 18 2011 Paul Howarth <paul@city-fan.org> - 0.18-1
- Update to 0.18:
  - Expand changes_file_ok() to accept arguments so that a specific version may
    be checked
  - Add $VERSION to Test::CPAN::Changes so it plays nice with the toolchain
    e.g. Module::Install::AuthorRequires

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.17-2
- Perl mass rebuild

* Thu Apr 21 2011 Paul Howarth <paul@city-fan.org> - 0.17-1
- Update to 0.17:
  - Eliminate extra whitespace when release data is not defined (CPAN RT#67441)
  - Require version.pm 0.79, which introduced the $LAX regexp (CPAN RT#67613)
  - Add the option to sort groups

* Wed Apr 20 2011 Paul Howarth <paul@city-fan.org> - 0.16-1
- Initial RPM version
