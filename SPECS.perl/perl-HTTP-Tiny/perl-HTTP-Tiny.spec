Name:           perl-HTTP-Tiny
Version:	0.056
Release:	3%{?dist}
Summary:        Small, simple, correct HTTP/1.1 client
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Tiny/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/HTTP-Tiny-%{version}.tar.gz
# Check for write failure, bug #1031096, refused by upstream,
# <https://github.com/chansen/p5-http-tiny/issues/32>
Patch0:         HTTP-Tiny-0.042-Croak-on-failed-write-into-a-file.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Socket)
# IO::Socket::IP 0.25 is optional
# IO::Socket::SSL 1.56 is optional
BuildRequires:  perl(MIME::Base64)
# Mozilla::CA is optional
# Net::SSLeay 1.49 is optional
BuildRequires:  perl(Time::Local)
# Tests:
# Data::Dumper not used
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename) 
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::INET)
# IO::Socket::SSL 1.56 not needed
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(List::Util)
# Mozilla::CA not needed
# Net::SSLeay 1.49 not needed
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(bytes)
Requires:       perl(Fcntl)
Requires:       perl(MIME::Base64)
Requires:       perl(Time::Local)

%description
This is a very simple HTTP/1.1 client, designed for doing simple GET requests
without the overhead of a large framework like LWP::UserAgent.

It is more correct and more complete than HTTP::Lite. It supports proxies
(currently only non-authenticating ones) and redirection. It also correctly
resumes after EINTR.

%prep
%setup -q -n HTTP-Tiny-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR='%{buildroot}'
find '%{buildroot}' -type f -name .packlist -exec rm -f {} \;
%{_fixperms} '%{buildroot}'/*

%check
make test

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.056-3
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.056-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.056-1
- 更新到 0.056

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.043-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Petr Pisar <ppisar@redhat.com> - 0.043-1
- 0.043 bump

* Wed Feb 19 2014 Petr Pisar <ppisar@redhat.com> - 0.042-1
- 0.042 bump

* Thu Nov 28 2013 Petr Pisar <ppisar@redhat.com> - 0.039-1
- 0.039 bump

* Wed Nov 27 2013 Petr Pisar <ppisar@redhat.com> - 0.038-2
- Croak on failed write into a file (bug #1031096)
- Do not use already existing temporary files (bug #1031096)

* Tue Nov 19 2013 Petr Pisar <ppisar@redhat.com> - 0.038-1
- 0.038 bump

* Tue Oct 29 2013 Petr Pisar <ppisar@redhat.com> - 0.037-1
- 0.037 bump

* Thu Sep 26 2013 Petr Pisar <ppisar@redhat.com> - 0.036-1
- 0.036 bump

* Wed Sep 11 2013 Petr Pisar <ppisar@redhat.com> - 0.035-1
- 0.035 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.034-2
- Link minimal build-root packages against libperl.so explicitly

* Mon Jul 01 2013 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.034 bump

* Mon Jun 24 2013 Petr Pisar <ppisar@redhat.com> - 0.033-1
- 0.033 bump

* Fri Jun 21 2013 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Thu Jun 20 2013 Petr Pisar <ppisar@redhat.com> - 0.031-1
- 0.031 bump

* Fri Jun 14 2013 Petr Pisar <ppisar@redhat.com> - 0.030-1
- 0.030 bump

* Thu Apr 18 2013 Petr Pisar <ppisar@redhat.com> - 0.029-1
- 0.029 bump

* Fri Mar 15 2013 Petr Pisar <ppisar@redhat.com> 0.028-1
- Specfile autogenerated by cpanspec 1.78.
