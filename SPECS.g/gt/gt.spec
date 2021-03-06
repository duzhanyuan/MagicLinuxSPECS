Name:           gt
Version:        0.4
Release:        19%{?dist}
Summary:        Modified Timidity which supportes enhanced gus format patches
Summary(zh_CN.UTF-8): 带有 gus 格式补丁的增强版 Timidity
Group:          Applications/Multimedia
Group(zh_CN.UTF-8): 应用程序/多媒体
License:        GPLv2+
URL:            http://alsa.opensrc.org/index.php/GusSoundfont
# This is ftp://ling.lll.hawaii.edu/pub/greg/gt-0.4.tar.gz
# with the examples/patch and sfz directories removed as the license of the
# samples in these dirs is unclear. Also the src/ac3* files have been removed
# as these contain patented code.
Source0:        %{name}-%{version}-clean.tar.gz
Patch0:         gt-0.4-noac3.patch
Patch1:         gt-0.4-compile-fix.patch
Patch2:         gt-0.4-optflags.patch
Patch3:         gt-0.4-config-default-velocity-layer.patch
Patch4:         gt-0.4-ppc-compile-fix.patch
Patch5:         gt-0.4-unsf-bigendian-fix.patch
Patch6:         gt-0.4-unsf-tremolo.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  alsa-lib-devel libvorbis-devel flex
Requires:       timidity++-patches

%description
Modified timidity midi player which supportes enhanced gus format patches and
surround audio output.

%description -l zh_CN.UTF-8
带有 gus 格式补丁的增强版 Timidity。

%package -n soundfont-utils
Summary:        Utilities for converting from / to various soundfont formats
Summary(zh_CN.UTF-8): 转换多种 soundfont 格式的工具
Group:          Applications/Multimedia
Group(zh_CN.UTF-8): 应用程序/多媒体

%description -n soundfont-utils
Utilities for converting from / to various soundfont formats and a midi file
disassembler.

%description -n soundfont-utils -l zh_CN.UTF-8 
转换多种 soundfont 格式的工具。

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
cp -p src/README README.timidity


%build
autoreconf -fisv
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# rename somewhat genericly named dim to midi-disasm
mv $RPM_BUILD_ROOT%{_bindir}/dim $RPM_BUILD_ROOT%{_bindir}/midi-disasm
mv $RPM_BUILD_ROOT%{_mandir}/man1/dim.1 \
   $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
sed -i 's/dim/midi-disasm/g' $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
touch -r utils/midifile.c $RPM_BUILD_ROOT%{_mandir}/man1/midi-disasm.1
magic_rpm_clean.sh 

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog FEATURES NEWS README*
%{_bindir}/gt
%{_mandir}/man1/gt.1*

%files -n soundfont-utils
%doc COPYING utils/README* utils/GUSSF2-SPEC
%{_bindir}/*
%exclude %{_bindir}/gt
%{_mandir}/man1/*
%exclude %{_mandir}/man1/gt.1*


%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.4-19
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 0.4-18
- 为 Magic 3.0 重建

* Sat Sep 19 2015 Liu Di <liudidi@gmail.com> - 0.4-17
- 为 Magic 3.0 重建

* Fri Apr 11 2014 Liu Di <liudidi@gmail.com> - 0.4-16
- 为 Magic 3.0 重建

* Thu Dec 06 2012 Liu Di <liudidi@gmail.com> - 0.4-14
- 为 Magic 3.0 重建

* Fri Dec 09 2011 Liu Di <liudidi@gmail.com> - 0.4-13
- 为 Magic 3.0 重建

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Hans de Goede <hdegoede@redhat.com> - 0.4-11
- Add COPYRIGHT file to soundfont-utils

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-9
- Add missing BR flex, fixing FTBFS (#511363)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-7
- Fix an error in unsf's tremolo settings export

* Sat Feb  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-6
- Fix hopefully the last endian issue in unsf

* Fri Feb  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-5
- And fix unsf for char being unsigned on ppc <sigh>

* Fri Feb  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-4
- Fix unsf running on big endian systems

* Wed Jan 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-3
- Correct license field from GPLv2 to GPLv2+

* Wed Jan 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-2
- Fix compilation on big endian archs

* Sun Jan 27 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-1
- Initial Fedora Package
