Name:           perl-Apache-DBI-Cache
Version:        0.08
Release:        34%{?dist}
Summary:        Perl DBI connection cache
Summary(zh_CN.UTF-8): Perl DBI 连接缓存
License:        GPL+ or Artistic
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
URL:            http://search.cpan.org/dist/Apache-DBI-Cache/
Source0:        http://www.cpan.org/authors/id/O/OP/OPI/Apache-DBI-Cache-%{version}.tar.gz
Patch0:         0001-DBI-dr-connect-can-clobber-the-arguments.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(DBI) >= 1.37
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(BerkeleyDB)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Deep)
Requires:       perl(DBI) >= 1.37
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^perl(DBI::st)$/d
%filter_from_requires /^perl(DBI::db)$/d
%{?perl_default_filter}
}
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(DBI::st\\)$
%global __requires_exclude %__requires_exclude|^perl\\(DBI::db\\)$

%description
This module is an alternative to Apache::DBI module. As a drop-in
Apache::DBI replacement it provides persistent DBI connections
while overcoming certain limitations. It is compatible with mod_perl,
though it does not require it.

%description -l zh_CN.UTF-8
Perl DBI 连接缓存。

%prep
%setup -q -n Apache-DBI-Cache-%{version}
%patch0 -p1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.08-34
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.08-33
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.08-32
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.08-31
- 为 Magic 3.0 重建

* Thu Apr 23 2015 Liu Di <liudidi@gmail.com> - 0.08-30
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.08-29
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.08-28
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.08-27
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.08-26
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.08-25
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.08-24
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.08-23
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.08-22
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.08-21
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.08-20
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.08-19
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.08-18
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.08-17
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.08-16
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.08-15
- 为 Magic 3.0 重建

* Fri Jan 27 2012 Liu Di <liudidi@gmail.com> - 0.08-14
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 0.08-12
- RPM 4.9 dependency filtering added

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.08-11
- Perl mass rebuild

* Fri Feb 25 2011 Marcela Maslanova <mmaslano@redhat.com> - 0.08-10
- filter useless requires

* Fri Feb 25 2011 Marcela Maslanova <mmaslano@redhat.com> - 0.08-9
- filter useless requires

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.08-6
- Fix a bug which made test suite fail with recent DBI

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.08-1
- Specfile autogenerated by cpanspec 1.77.
- Fixup license and dependencies
