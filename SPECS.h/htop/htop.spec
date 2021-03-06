Name:           htop
Version:	1.0.3
Release:        3%{?dist}
Summary:        Interactive process viewer
Summary(zh_CN.UTF-8): 交互式进程查看器

Group:          Applications/System
Group(zh_CN.UTF-8):	应用程序/系统
License:        GPL+
URL:            http://htop.sourceforge.net/
Source0:        http://download.sourceforge.net/htop/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel, python

%description
htop is an interactive text-mode process viewer for Linux, similar to
top(1).

%description -l zh_CN.UTF-8
htop 是一个 Linux 下文本模式的交互式进程查看器，类似 top。


%prep
%setup -q
sed -i s#"INSTALL_DATA = @INSTALL_DATA@"#"INSTALL_DATA = @INSTALL_DATA@ -p"# Makefile.in
#sed -i -e '2,3d' -e '9d' htop.desktop

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --vendor magic \
        --delete-original \
        --remove-category=Application\
        $RPM_BUILD_ROOT%{_datadir}/applications/htop.desktop

#remove empty direcories
rm -rf $RPM_BUILD_ROOT%{prefix}/lib
rm -rf $RPM_BUILD_ROOT%{prefix}/include

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README 
%{_bindir}/htop
%{_datadir}/applications/magic-htop.desktop
%{_datadir}/pixmaps/htop.png
%{_mandir}/man1/htop.1*


%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 1.0.3-3
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 1.0.3-2
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 1.0.3-1
- 更新到 1.0.3

* Tue Apr 15 2014 Liu Di <liudidi@gmail.com> - 1.0.2-2
- 更新到 1.0.2

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 1.0-2
- 为 Magic 3.0 重建


