Name:           perl-Config-Properties
Version:        1.73
Release:        6%{?dist}
Summary:        Read and write property files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-Properties/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SA/SALVA/Config-Properties-%{version}.tar.gz
Patch1:         perl-Config-Properties-1.70-always_test_PODs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Config::Properties is a near implementation of the java.util.Properties
API. It is designed to allow easy reading, writing and manipulation of Java-
style property files.

%prep
%setup -q -n Config-Properties-%{version}
%patch1 -p0

# Fix files encoding
for i in Changes README; do {
iconv -f iso8859-1 -t utf-8 $i > $i.utf8 \
&& touch -r $i $i.utf8 \
&& mv -f $i.utf8 $i; };
done;


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.73-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.73-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.73-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.73-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Xavier Bachelot <xavier@bachelot.org> 1.73-1
- Update to 1.73.

* Mon Jul 18 2011 Petr Sabata <contyk@redhat.com> - 1.72-2
- Perl mass rebuild

* Sat Jul 16 2011 Xavier Bachelot <xavier@bachelot.org> 1.72-1
- Update to 1.72.

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.71-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.71-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Dec 14 2010 Xavier Bachelot <xavier@bachelot.org> 1.71-1
- Update to 1.71.
- Update Source0 URL.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.70-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.70-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 03 2009 Xavier Bachelot <xavier@bachelot.org> 1.70-2
- Remove useless require perl(Test::More).

* Tue May 26 2009 Xavier Bachelot <xavier@bachelot.org> 1.70-1
- Specfile autogenerated by cpanspec 1.77.
- Fix License:.
- Fix encoding on some files.
- Add patch to always test PODs.