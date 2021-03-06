Name:           xarchiver
Version:        0.5.4
Release:        5%{?dist}
Summary:        Archive manager for Xfce
Summary(zh_CN.UTF-8): Xfce 下的归档管理器

Group:          Applications/Archiving
Group(zh_CN.UTF-8): 应用程序/归档
License:        GPLv2+
URL:            http://xarchiver.xfce.org/
Source0:        http://downloads.sourceforge.net/xarchiver/xarchiver-%{version}.tar.bz2

Patch0:         xarchiver-0.5.4-version-fix.patch

BuildRequires:  gtk2-devel, libxml2-devel, gettext, desktop-file-utils
BuildRequires:  xfce4-dev-tools >= 4.3.90.2
BuildRequires:  autoconf >= 2.69
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  intltool

Requires:       arj, binutils, bzip2, cpio, gzip, xdg-utils, tar, unzip, zip

%description
Xarchiver is a lightweight GTK2 only frontend for manipulating 7z, arj, bzip2,
gzip, iso, rar, lha, tar, zip, RPM and deb files. It allows you to create
archives and add, extract, and delete files from them. Password protected
archives in the arj, 7z, rar, and zip formats are supported.

%description -l zh_CN.UTF-8
Xfce 下的归档管理器，支持 arj, bz2, cpio, gzip, tar, zip, 7z 等格式。

%prep
%setup -q
%patch0 -p1
# fix spurious executable permissions of some debug files
chmod -x src/mime.*


%build
autoreconf -vif
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

magic_rpm_clean.sh
%find_lang %{name} || :
desktop-file-install --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category="Compression" \
    --add-mime-type="application/x-xz" \
    --add-mime-type="application/x-xz-compressed-tar" \
    --remove-mime-type="multipart/x-zip" \
    %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora \
    %endif
    %{buildroot}%{_datadir}/applications/%{name}.desktop

# remove duplicate docs
rm %{buildroot}%{_docdir}/%{name}/{AUTHORS,COPYING,ChangeLog,NEWS,README,TODO}


%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &> /dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files 
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}/
%{_libexecdir}/thunar-archive-plugin/


%changelog
* Sat Nov 14 2015 Liu Di <liudidi@gmail.com> - 0.5.4-5
- 为 Magic 3.0 重建

* Fri Nov 06 2015 Liu Di <liudidi@gmail.com> - 0.5.4-4
- 为 Magic 3.0 重建

* Wed Oct 21 2015 Liu Di <liudidi@gmail.com> - 0.5.4-3
- 为 Magic 3.0 重建

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Jaromir Capik <jcapik@redhat.com> - 0.5.4-1
- Update to 0.5.4 (#1147466)

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.5.2-22
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.2-20
- Fix FTBFS with -Werror=format-security (#1037390, #1107209)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-17
- Fix thunar-archive-plugin integration (#961626)
- Conditionalize vendor tag

* Thu Apr 04 2013 Jaromir Capik <jcapik@redhat.com> - 0.5.2-16
- aarch64 support (#926742)
- fixing bogus date in the changelog

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.5.2-15
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 26 2012 Jaromir Capik <jcapik@redhat.com> - 0.5.2-13
- Fix extraction failures when the Drag'n'Drop target path contains spaces (#784075)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.2-11
- Rebuild for new libpng

* Sun Jun 19 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-10
- Fix xz MIME types

* Sat Jun 11 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-9
- Fix xz support. A big thanks to Daniel Hokka Zakrisson (#577480)

* Thu Jun 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-8
- Fix 7zip. Encrypted archives are still not supported.

* Thu Jun 02 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-7
- Add xz support. Thanks to Robby Workman and Daniel Hokka Zakrisson (#577480)
- Remove mime-type multipart/x-zip (#666066)
- Fix crash in IA__gtk_tree_model_get_valist. Thanks to Bastiaan Jacques (#690012)
- Update icon-cache scriptlets

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 22 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-4
- Gui fixes (#491115)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 25 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-2
- Include HTML documentation

* Tue Nov 25 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Sun Nov 09 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1 stable release

* Sun Oct 26 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-0.1.rc1
- Update to 0.5.0rc1
- Fix crash when opening zipped PDF files (#467619)
- Update gtk-icon-cache scriptlets

* Sat Oct 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-0.1.beta2
- Update to 0.5.0beta2

* Sun Aug 31 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-0.1.beta1
- Update to 0.5.0beta1
- Remove xdg-open.patch as xarchiver now uses xdg-open by default

* Sat Apr 19 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.6.20070103svn24249
- Remove additional mime-types from desktop-file-install to make sure we don't break livecds

* Fri Mar 14 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.5.20070103svn24249
- Use xdg-open instead of htmlview (#437554)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.9-0.4.20070103svn24249
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.3.20070103svn24249
- Rebuild for BuildID feature
- Update license tag

* Fri Mar 02 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.2.20070103svn24249
- Downgrade to SVN release 24249 in order to fix #230154 temporarily.

* Sun Jan 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.1.20070128svn24772
- Update to SVN release 24772 of January 28th 2007.

* Wed Jan 03 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.1.20070103svn
- Update to SVN r24249 of January 3rd 2007.
- Add mimetype application/x-deb again since opening of debs now is secure.

* Wed Dec 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.9-0.1.20061213svn
- Update to SVN r24096 of December 13th 2006.

* Wed Dec 06 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6-3
- Add deb.patch to prevent opening of .a files as debs.
- Don't add mimetype for x-ar (archiver can't handle ar archive).

* Wed Nov 29 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6-2
- Add htmlview.patch.

* Tue Nov 28 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6.
- Update %%description.
- Require binutils, cpio and htmlview.
- Add mimetypes application/x-ar, application/x-cd-image and application/x-deb.

* Mon Nov 27 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4.

* Sat Nov 25 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-0.3.rc2
- Install xarchiver.png also in %%{_datadir}/icons/hicolor/48x48/apps/.

* Sat Nov 25 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-0.2.rc2
- Drop subpackage and own %%{_libexecdir}/thunar-archive-plugin/ (#198098).

* Sun Nov 12 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-0.1.rc2
- Update to 0.4.2.RC2.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0.

* Tue Sep 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.9.2-0.beta2
- Initial package.
