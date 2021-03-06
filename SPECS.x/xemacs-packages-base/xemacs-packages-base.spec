%global hgver   3720091d7106
%global pkgdir  %{_datadir}/xemacs
%global xemver  v=$(rpm -q --qf=%%{VERSION} xemacs-nox) ; case $v in 2*) echo $v ;; *) echo 0 ;; esac

Name:           xemacs-packages-base
Version:        20150919
Release:        3%{?dist}
Summary:        Base lisp packages for XEmacs

Group:          Applications/Editors
# dired and efs are GPL+, rest GPLv2+
License:        GPLv2+ and GPL+
URL:            http://www.xemacs.org/Documentation/packageGuide.html
# Tarball created with Source99
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}-checkout.sh

BuildArch:      noarch
BuildRequires:  xemacs-nox
BuildRequires:  texinfo

Requires:       xemacs(bin) >= %(%{xemver})

%description
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains the minimal recommended set of additional lisp
packages for XEmacs: efs, xemacs-base and mule-base from upstream.

%package        el
Summary:        Emacs lisp source files for the base lisp packages for XEmacs
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    el
This package is not needed to run XEmacs; it contains the lisp source
files for the base lisp packages for XEmacs, mainly of interest when
developing or debugging the packages.


%prep
%setup -q
cat << EOF > make.sh
#!/bin/sh
make \\
    XEMACS_BINARY=%{_bindir}/xemacs-nox \\
    XEMACS_INSTALLED_PACKAGES_ROOT=\$RPM_BUILD_ROOT%{pkgdir} \\
    XEMACS_21_5=t \\
    "\$@"
EOF
chmod +x make.sh

%build
apkgs="apel dired efs fsf-compat xemacs-base"
xpkgs="efs xemacs-base"
mpkgs="mule-base"
./make.sh -C xemacs-packages autoloads PACKAGES="$apkgs"
./make.sh -C mule-packages   autoloads PACKAGES="$mpkgs"
./make.sh -C xemacs-packages           PACKAGES="$xpkgs"
./make.sh -C mule-packages             PACKAGES="$mpkgs"


%install
mkdir -p $RPM_BUILD_ROOT%{pkgdir}
./make.sh -C xemacs-packages/xemacs-base install
./make.sh -C xemacs-packages/efs         install
./make.sh -C mule-packages/mule-base     install

# separate files
rm -f *.files
touch base-files el-files

find $RPM_BUILD_ROOT%{pkgdir}/* \
  \( -type f -name '*.el.orig' -exec rm '{}' ';' \) -o \
  \( -type f -not -name '*.el' -fprint base-non-el.files \) -o \
  \( -type d -not -name info -fprintf dir.files "%%%%dir %%p\n" \) -o \
  \( -name '*.el' \( -exec test -e '{}'c \; -fprint el-bytecomped.files -o \
     -fprint base-el-not-bytecomped.files \) \)

sed -i -e "s|$RPM_BUILD_ROOT||" *.files
cat base-*.files dir.files | grep -v /info/ >> base-files
cat el-*.files                              >> el-files

# all info files packaged in xemacs-packages-extra-info for simplicity
rm -rf $RPM_BUILD_ROOT%{pkgdir}/*-packages/info

sed -i -e 's/^\(.*\(\.ja\|-ja\.texi\)\)$/%lang(ja) \1/' base-files


%files -f base-files

%files el -f el-files


%changelog
* Fri Nov 06 2015 Liu Di <liudidi@gmail.com> - 20150919-3
- 为 Magic 3.0 重建

* Thu Oct 22 2015 Liu Di <liudidi@gmail.com> - 20150919-2
- 为 Magic 3.0 重建

* Wed Oct  7 2015 Jerry James <loganjerry@gmail.com> - 20150919-1
- Update to latest package releases

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150413-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Jerry James <loganjerry@gmail.com> - 20150413-1
- Update to latest package releases
- Set the build username for reproducible builds

* Thu Aug  7 2014 Jerry James <loganjerry@gmail.com> - 20140715-1
- Update to latest package releases

* Mon Jul  7 2014 Jerry James <loganjerry@gmail.com> - 20140705-1
- Update to latest package releases
- Drop upstreamed -texi patch
- Update checkout script for mercurial

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130408-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130408-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr  9 2013 Jerry James <loganjerry@gmail.com> - 20130408-1
- Update to latest package releases
- Add -texi patch to fix build with texinfo 5

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121228-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 20121228-1
- Update to latest package releases
- Drop xz BR; it is on the list of exceptions

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110502-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjeryr@gmail.com> - 20110502-2
- Mass rebuild for Fedora 17

* Tue May  3 2011 Jerry James <loganjerry@gmail.com> - 20110502-1
- Update to latest package releases
- Drop BuildRoot tag, clean script, and clean at start of install script

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100727-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 13 2010 Jerry James <loganjerry@gmail.com> - 20100727-1
- Update to new package release.
- New upstream CVS location in checkout script.
- Drop upstreamed patches.
- Use xz instead of lzma to compress.

* Tue Sep  1 2009 Jerry James <loganjerry@gmail.com> - 20090217-4
- Add mule-base patch to fix bz 480845 and hopefully bz 520248.

* Mon Aug 24 2009 Jerry James <loganjerry@gmail.com> - 20090217-3
- Add APEL patch to fix bz 503185 for XEmacs.
- Add dired patch to fix bz 504422.
- Add itimer patch preemptively.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 20090217-1
- Update to 2009-02-17.
- Compress source tarball with lzma.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070427-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 16 2007 Ville Skyttä <ville.skytta at iki.fi> - 20070427-2
- License: GPLv2+ and GPL+

* Fri May 18 2007 Ville Skyttä <ville.skytta at iki.fi> - 20070427-1
- 2007-04-27.
- Require an actual XEmacs editor, not just -common.

* Mon Apr  2 2007 Ville Skyttä <ville.skytta at iki.fi> - 20061221-1
- 2006-12-21.

* Sun Sep 10 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060510-3
- Split minimal set of packages from xemacs-sumo.
- Really build from sources.
