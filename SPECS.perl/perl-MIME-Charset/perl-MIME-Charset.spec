Name:           perl-MIME-Charset
Version:	1.012
Release:	2%{?dist}
Summary:        Charset Informations for MIME
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MIME-Charset/
Source0:        http://search.cpan.org/CPAN/authors/id/N/NE/NEZUMI/MIME-Charset-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Encode::JIS2K)
BuildRequires:  perl(Encode::HanExtra)
BuildRequires:  perl(Encode::EUCJPASCII)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
MIME::Charset provides informations about character sets used for MIME
messages on Internet.

%prep
%setup -q -n MIME-Charset-%{version}

cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
sed -e '/perl(MIME::Charset)$/d'
EOF

%global __perl_provides %{_builddir}/MIME-Charset-%{version}/%{name}-prov
chmod +x %{__perl_provides}


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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.012-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.012-1
- 更新到 1.012

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.009.1-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.009.1-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.009.1-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.009.1-6
- 为 Magic 3.0 重建

* Fri Jan 06 2012 Xavier Bachelot <xavier@bachelot.org> 1.009.1-5
- Add BR: for perl(Encode::EUCJPASCII) for better test coverage.

* Wed Dec 21 2011 Xavier Bachelot <xavier@bachelot.org> 1.009.1-4
- Add BR: for perl(Encode::JIS2K) and perl(Encode::HanExtra) for better test
  coverage.

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.009.1-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.009.1-2
- Perl mass rebuild

* Fri Jul 08 2011 Xavier Bachelot <xavier@bachelot.org> 1.009.1-1
- Update to 1.009.1.

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.008.2-2
- Perl mass rebuild

* Mon May 30 2011 Xavier Bachelot <xavier@bachelot.org> 1.008.2-1
- Update to 1.008.2.

* Thu May 12 2011 Xavier Bachelot <xavier@bachelot.org> 1.008.1-1
- Update to 1.008.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.008-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Dec 14 2010 Xavier Bachelot <xavier@bachelot.org> 1.008-1
- Update to 1.008.
- Update Source0 URL.
- More BRs for better tests coverage.

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.006.2-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.006.2-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.006.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Xavier Bachelot <xavier@bachelot.org> 1.006.2-2
- Filter duplicate Provides:.

* Fri Apr 24 2009 Xavier Bachelot <xavier@bachelot.org> 1.006.2-1
- Specfile autogenerated by cpanspec 1.77.
- Fix license.
