%define lversion 3.1.11

Summary: Music module player
Summary(zh_CN.UTF-8): 音乐模块播放器
Name: mikmod
Version: 3.2.6
Release: 4%{?dist}
License: GPLv2 and LGPLv2+
Group: Applications/Multimedia
Group(zh_CN.UTF-8): 应用程序/多媒体
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: ncurses-devel libmikmod-devel
URL: http://mikmod.raphnet.net/
Source0: http://downloads.sourceforge.net/project/mikmod/mikmod/%{version}/mikmod-%{version}.tar.gz

%description
MikMod is one of the best and most well known MOD music file players
for UNIX-like systems.  This particular distribution is intended to
compile fairly painlessly in a Linux environment. MikMod uses the OSS
/dev/dsp driver including all recent kernels for output, and will also
write .wav files. Supported file formats include MOD, STM, S3M, MTM,
XM, ULT, and IT.  The player uses ncurses for console output and
supports transparent loading from gzip/pkzip/zoo archives and the
loading/saving of playlists.

Install the mikmod package if you need a MOD music file player.

%description -l zh_CN.UTF-8
MikMod 是类 UNIX 系统上的最好的和几乎最著名的 MOD 音乐文件播放器。

%prep
%setup -q -n %{name}-%{version}


%build
%configure
make CFLAGS="$RPM_OPT_FLAGS `libmikmod-config --cflags`"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_infodir}/dir


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/mikmod
%{_datadir}/mikmod/mikmodrc
%{_mandir}/man1/mikmod*


%changelog
* Sun Nov 01 2015 Liu Di <liudidi@gmail.com> - 3.2.6-4
- 为 Magic 3.0 重建

* Sat Sep 19 2015 Liu Di <liudidi@gmail.com> - 3.2.6-3
- 为 Magic 3.0 重建

* Mon Sep 08 2014 Liu Di <liudidi@gmail.com> - 3.2.6-2
- 为 Magic 3.0 重建

* Mon Sep 08 2014 Liu Di <liudidi@gmail.com> - 3.2.6-1
- 更新到 3.2.6

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 3.2.2-0.beta1.2
- 为 Magic 3.0 重建

* Mon Jan 16 2012 Liu Di <liudidi@gmail.com> - 3.2.2-0.beta1.1
- 为 Magic 3.0 重建


