# rpmbuild --rebuild --with testsuite --without clustering samba.src.rpm
#
# The testsuite is disabled by default. Set --with testsuite or %bcond_without
# to run the Samba torture testsuite.
%bcond_with testsuite
# ctdb is enabled by default, you can disable it with: --without clustering
%bcond_without clustering

%define main_release 1

%define samba_version 4.3.2
%define talloc_version 2.1.3
%define tdb_version 1.3.7
%define tevent_version 0.9.25
%define ldb_version 1.1.21
# This should be rc1 or nil
%define pre_release %nil

%if "x%{?pre_release}" != "x"
%define samba_release 0.%{main_release}.%{pre_release}%{?dist}
%else
%define samba_release %{main_release}%{?dist}
%endif

# This is a network daemon, do a hardened build
# Enables PIE and full RELRO protection
%global _hardened_build 1

%global with_libsmbclient 1
%global with_libwbclient 1

%global with_pam_smbpass 0
%global with_internal_talloc 0
%global with_internal_tevent 0
%global with_internal_tdb 0
%global with_internal_ldb 0

%global with_profiling 1

%global with_vfs_cephfs 1
%if 0%{?rhel}
%global with_vfs_cephfs 0
%endif

%global with_vfs_glusterfs 1
%if 0%{?rhel}
%global with_vfs_glusterfs 0
# Only enable on x86_64
%ifarch x86_64
%global with_vfs_glusterfs 1
%endif
%endif

%global libwbc_alternatives_version 0.12
%global libwbc_alternatives_suffix %nil
%if 0%{?__isa_bits} == 64
%global libwbc_alternatives_suffix -64
%endif

%global with_mitkrb5 1
%global with_dc 0

%if %{with testsuite}
# The testsuite only works with a full build right now.
%global with_mitkrb5 0
%global with_dc 1
%endif

%global with_clustering_support 0

%if %{with clustering}
%global with_clustering_support 1
%endif

%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           samba
Version:        %{samba_version}
Release:        %{samba_release}.3

%if 0%{?rhel}
Epoch:          0
%else
Epoch:          2
%endif

%if 0%{?epoch} > 0
%define samba_depver %{epoch}:%{version}-%{release}
%else
%define samba_depver %{version}-%{release}
%endif

Summary:        Server and Client software to interoperate with Windows machines
License:        GPLv3+ and LGPLv3+
Group:          System Environment/Daemons
URL:            http://www.samba.org/

Source0:        https://download.samba.org/pub/samba/stable/samba-%{version}%{pre_release}.tar.gz

# Red Hat specific replacement-files
Source1: samba.log
Source2: samba.xinetd
Source4: smb.conf.default
Source5: pam_winbind.conf
Source6: samba.pamd

Source200: README.dc
Source201: README.downgrade

Patch0: samba-4.3.3-async_connect_send_test.patch

BuildRoot:                      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires(pre): /usr/sbin/groupadd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires(pre): %{name}-common = %{samba_depver}
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-common-libs = %{samba_depver}
Requires: %{name}-common-tools = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
%endif

Requires: pam

Provides: samba4 = %{samba_depver}
Obsoletes: samba4 < %{samba_depver}

# We don't build it outdated docs anymore
Obsoletes: samba-doc
# Is not supported yet
Obsoletes: samba-domainjoin-gui
# SWAT been deprecated and removed from samba
Obsoletes: samba-swat
Obsoletes: samba4-swat

BuildRequires: cups-devel
BuildRequires: dbus-devel
BuildRequires: docbook-style-xsl
BuildRequires: e2fsprogs-devel
BuildRequires: gawk
BuildRequires: krb5-devel >= 1.10
BuildRequires: libacl-devel
BuildRequires: libaio-devel
BuildRequires: libarchive-devel
BuildRequires: libattr-devel
BuildRequires: libcap-devel
BuildRequires: libuuid-devel
BuildRequires: libxslt
BuildRequires: ncurses-devel
BuildRequires: openldap-devel
BuildRequires: pam-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Parse::Yapp)
BuildRequires: popt-devel
BuildRequires: python-devel
BuildRequires: python-tevent
BuildRequires: quota-devel
BuildRequires: readline-devel
BuildRequires: sed
BuildRequires: xfsprogs-devel
BuildRequires: zlib-devel >= 1.2.3

BuildRequires: pkgconfig(libsystemd-daemon)
BuildRequires: pkgconfig(libsystemd)

%if %{with_vfs_glusterfs}
BuildRequires: glusterfs-api-devel >= 3.4.0.16
BuildRequires: glusterfs-devel >= 3.4.0.16
%endif
%if %{with_vfs_cephfs}
BuildRequires: libcephfs1-devel
%endif
%if %{with_dc}
BuildRequires: gnutls-devel
%endif

# pidl requirements
BuildRequires: perl(Parse::Yapp)

%if ! %with_internal_talloc
%global libtalloc_version 2.1.3

BuildRequires: libtalloc-devel >= %{libtalloc_version}
BuildRequires: pytalloc-devel >= %{libtalloc_version}
%endif

%if ! %with_internal_tevent
%global libtevent_version 0.9.25

BuildRequires: libtevent-devel >= %{libtevent_version}
BuildRequires: python-tevent >= %{libtevent_version}
%endif

%if ! %with_internal_ldb
%global libldb_version 1.1.21

BuildRequires: libldb-devel >= %{libldb_version}
BuildRequires: pyldb-devel >= %{libldb_version}
%endif

%if ! %with_internal_tdb
%global libtdb_version 1.3.7

BuildRequires: libtdb-devel >= %{libtdb_version}
BuildRequires: python-tdb >= %{libtdb_version}
%endif

%if %{with testsuite}
BuildRequires: ldb-tools
%endif

# filter out perl requirements pulled in from examples in the docdir.
#{?filter_setup:
#filter_provides_in %{_docdir}
#filter_requires_in %{_docdir}
#filter_setup
#}

### SAMBA
%description
Samba is the standard Windows interoperability suite of programs for Linux and Unix.

### CLIENT
%package client
Summary: Samba client programs
Group: Applications/System
Requires(pre): %{name}-common = %{samba_depver}
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-common-libs = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}
%if %with_libsmbclient
Requires: libsmbclient = %{samba_depver}
%endif

Provides: samba4-client = %{samba_depver}
Obsoletes: samba4-client < %{samba_depver}

%description client
The %{name}-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

### CLIENT-LIBS
%package client-libs
Summary: Samba client libraries
Group: Applications/System
Requires(pre): %{name}-common = %{samba_depver}
Requires: %{name}-common = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
%endif

%description client-libs
The samba-client-libs package contains internal libraries needed by the
SMB/CIFS clients.

### COMMON
%package common
Summary: Files used by both Samba servers and clients
Group: Applications/System
BuildArch: noarch

Requires(post): systemd
Requires: samba-common-tools = %{samba_depver}

Provides: samba4-common = %{samba_depver}
Obsoletes: samba4-common < %{samba_depver}

%description common
samba-common provides files necessary for both the server and client
packages of Samba.

### COMMON-LIBS
%package common-libs
Summary: Libraries used by both Samba servers and clients
Group: Applications/System
Requires(pre): samba-common = %{samba_depver}
Requires: samba-common = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
%endif

%description common-libs
The samba-common-libs package contains internal libraries needed by the
SMB/CIFS clients.

### COMMON-TOOLS
%package common-tools
Summary: Tools for Samba servers and clients
Group: Applications/System
Requires: samba-common-libs = %{samba_depver}
Requires: samba-client-libs = %{samba_depver}
Requires: samba-libs = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
%endif

%description common-tools
The samba-common-tools package contains tools for Samba servers and
SMB/CIFS clients.

### DC
%package dc
Summary: Samba AD Domain Controller
Group: Applications/System
Requires: %{name}-libs = %{samba_depver}
Requires: %{name}-dc-libs = %{samba_depver}
Requires: %{name}-python = %{samba_depver}

Provides: samba4-dc = %{samba_depver}
Obsoletes: samba4-dc < %{samba_depver}

%description dc
The samba-dc package provides AD Domain Controller functionality

### DC-LIBS
%package dc-libs
Summary: Samba AD Domain Controller Libraries
Group: Applications/System
Requires: %{name}-common-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}

Provides: samba4-dc-libs = %{samba_depver}
Obsoletes: samba4-dc-libs < %{samba_depver}

%description dc-libs
The %{name}-dc-libs package contains the libraries needed by the DC to
link against the SMB, RPC and other protocols.

### DEVEL
%package devel
Summary: Developer tools for Samba libraries
Group: Development/Libraries
Requires: %{name}-libs = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}

Provides: samba4-devel = %{samba_depver}
Obsoletes: samba4-devel < %{samba_depver}

%description devel
The %{name}-devel package contains the header files for the libraries
needed to develop programs that link against the SMB, RPC and other
libraries in the Samba suite.

### CEPH
%if %{with_vfs_cephfs}
%package vfs-cephfs
Summary: Samba VFS module for Ceph distributed storage system
Group: Applications/System
Requires: libcephfs1
Requires: %{name} = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}

%description vfs-cephfs
Samba VFS module for Ceph distributed storage system integration.
%endif

### GLUSTER
%if %{with_vfs_glusterfs}
%package vfs-glusterfs
Summary: Samba VFS module for GlusterFS
Group: Applications/System
Requires: glusterfs-api >= 3.4.0.16
Requires: glusterfs >= 3.4.0.16
Requires: %{name} = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}

Obsoletes: samba-glusterfs
Provides: samba-glusterfs

%description vfs-glusterfs
Samba VFS module for GlusterFS integration.
%endif

### LIBS
%package libs
Summary: Samba libraries
Group: Applications/System
Requires: krb5-libs >= 1.10
Requires: %{name}-client-libs = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
%endif

Provides: samba4-libs = %{samba_depver}
Obsoletes: samba4-libs < %{samba_depver}

%description libs
The %{name}-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

### LIBSMBCLIENT
%if %with_libsmbclient
%package -n libsmbclient
Summary: The SMB client library
Group: Applications/System
Requires(pre): %{name}-common = %{samba_depver}
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}

%description -n libsmbclient
The libsmbclient contains the SMB client library from the Samba suite.

%package -n libsmbclient-devel
Summary: Developer tools for the SMB client library
Group: Development/Libraries
Requires: libsmbclient = %{samba_depver}

%description -n libsmbclient-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.
%endif # with_libsmbclient

### LIBWBCLIENT
%if %with_libwbclient
%package -n libwbclient
Summary: The winbind client library
Group: Applications/System
Requires: %{name}-client-libs = %{samba_depver}

%description -n libwbclient
The libwbclient package contains the winbind client library from the Samba suite.

%package -n libwbclient-devel
Summary: Developer tools for the winbind library
Group: Development/Libraries
Requires: libwbclient = %{samba_depver}
Obsoletes: samba-winbind-devel
Provides: samba-winbind-devel

%description -n libwbclient-devel
The libwbclient-devel package provides developer tools for the wbclient library.
%endif # with_libwbclient

### PYTHON
%package python
Summary: Samba Python libraries
Group: Applications/System
Requires: %{name} = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
Requires: python-tevent
Requires: python-tdb
Requires: pyldb
Requires: pytalloc

Provides: samba4-python = %{samba_depver}
Obsoletes: samba4-python < %{samba_depver}

%description python
The %{name}-python package contains the Python libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python programs.

### PIDL
%package pidl
Summary: Perl IDL compiler
Group: Development/Tools
Requires: perl(Parse::Yapp)
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: noarch

Provides: samba4-pidl = %{samba_depver}
Obsoletes: samba4-pidl < %{samba_depver}

%description pidl
The %{name}-pidl package contains the Perl IDL compiler used by Samba
and Wireshark to parse IDL and similar protocols

### TEST
%package test
Summary: Testing tools for Samba servers and clients
Group: Applications/System
Requires: %{name} = %{samba_depver}
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-winbind = %{samba_depver}

Requires: %{name}-client-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
Requires: %{name}-test-libs = %{samba_depver}
%if %with_dc
Requires: %{name}-dc-libs = %{samba_depver}
%endif
Requires: %{name}-libs = %{samba_depver}
%if %with_libsmbclient
Requires: libsmbclient = %{samba_depver}
%endif
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
%endif

Provides: samba4-test = %{samba_depver}
Obsoletes: samba4-test < %{samba_depver}

%description test
%{name}-test provides testing tools for both the server and client
packages of Samba.

### TEST-LIBS
%package test-libs
Summary: Libraries need by the testing tools for Samba servers and clients
Group: Applications/System
Requires: %{name}-client-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}

%description test-libs
%{name}-test-libs provides libraries required by the testing tools.

### TEST-DEVEL
%package test-devel
Summary: Testing devel files for Samba servers and clients
Group: Applications/System
Requires: %{name}-libs = %{samba_depver}
Requires: %{name}-test-libs = %{samba_depver}

%description test-devel
samba-test-devel provides testing devel files for both the server and client
packages of Samba.

### WINBIND
%package winbind
Summary: Samba winbind
Group: Applications/System
Requires(pre): %{name}-common = %{samba_depver}
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-common-libs = %{samba_depver}
Requires: %{name}-common-tools = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
Requires: %{name}-winbind-modules = %{samba_depver}

Provides: samba4-winbind = %{samba_depver}
Obsoletes: samba4-winbind < %{samba_depver}

%description winbind
The samba-winbind package provides the winbind NSS library, and some
client tools.  Winbind enables Linux to be a full member in Windows
domains and to use Windows user and group accounts on Linux.

### WINBIND-CLIENTS
%package winbind-clients
Summary: Samba winbind clients
Group: Applications/System
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-common-libs = %{samba_depver}
Requires: %{name}-client-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
Requires: %{name}-winbind = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
%endif

Provides: samba4-winbind-clients = %{samba_depver}
Obsoletes: samba4-winbind-clients < %{samba_depver}

%description winbind-clients
The samba-winbind-clients package provides the wbinfo and ntlm_auth
tool.

### WINBIND-KRB5-LOCATOR
%package winbind-krb5-locator
Summary: Samba winbind krb5 locator
Group: Applications/System
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
Requires: %{name}-winbind = %{samba_depver}
%else
Requires: %{name}-libs = %{samba_depver}
%endif

Provides: samba4-winbind-krb5-locator = %{samba_depver}
Obsoletes: samba4-winbind-krb5-locator < %{samba_depver}

# Handle winbind_krb5_locator.so as alternatives to allow
# IPA AD trusts case where it should not be used by libkrb5
# The plugin will be diverted to /dev/null by the FreeIPA
# freeipa-server-trust-ad subpackage due to higher priority
# and restored to the proper one on uninstall
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%description winbind-krb5-locator
The winbind krb5 locator is a plugin for the system kerberos library to allow
the local kerberos library to use the same KDC as samba and winbind use

### WINBIND-MODULES
%package winbind-modules
Summary: Samba winbind modules
Group: Applications/System
Requires: %{name}-client-libs = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient = %{samba_depver}
%endif
Requires: pam

%description winbind-modules
The samba-winbind-modules package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon

### CTDB
%if %with_clustering_support
%package -n ctdb
Summary: A Clustered Database based on Samba's Trivial Database (TDB)
Group: System Environment/Daemons

Requires: %{name}-client-libs = %{samba_depver}

Requires: coreutils
Requires: fileutils
# for ps and killall
Requires: psmisc
Requires: sed
Requires: tdb-tools
Requires: gawk
# for pkill and pidof:
Requires: procps-ng
# for netstat:
Requires: net-tools
Requires: ethtool
# for ip:
Requires: iproute
Requires: iptables
# for flock, getopt, kill:
Requires: util-linux

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description -n ctdb
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.

### CTDB-DEVEL
%package -n ctdb-devel
Summary: CTDB clustered database development package
Group: Development/Libraries

Requires: ctdb = %{samba_depver}
Provides: ctdb-static = %{samba_depver}

%description -n ctdb-devel
Libraries, include files, etc you can use to develop CTDB applications.
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.

### CTDB-TEST
%package -n ctdb-tests
Summary: CTDB clustered database test suite
Group: Development/Tools

Requires: samba-client-libs = %{samba_depver}

Requires: ctdb = %{samba_depver}
Requires: nc

%description -n ctdb-tests
Test suite for CTDB.
CTDB is a cluster implementation of the TDB database used by Samba and other
projects to store temporary data. If an application is already using TDB for
temporary data it is very easy to convert that application to be cluster aware
and use CTDB instead.
%endif # with_clustering_support



%prep
%setup -q -n samba-%{version}%{pre_release}

%patch0 -p1 -b .samba-4.3.3-async_connect_send_test.patch

%build
%global _talloc_lib ,talloc,pytalloc,pytalloc-util
%global _tevent_lib ,tevent,pytevent
%global _tdb_lib ,tdb,pytdb
%global _ldb_lib ,ldb,pyldb,!pyldb-util

%if ! %{with_internal_talloc}
%global _talloc_lib ,!talloc,!pytalloc,!pytalloc-util
%endif

%if ! %{with_internal_tevent}
%global _tevent_lib ,!tevent,!pytevent
%endif

%if ! %{with_internal_tdb}
%global _tdb_lib ,!tdb,!pytdb
%endif

%if ! %{with_internal_ldb}
%global _ldb_lib ,!ldb,!pyldb,!pyldb-util
%endif

%global _samba4_libraries heimdal,!zlib,!popt%{_talloc_lib}%{_tevent_lib}%{_tdb_lib}%{_ldb_lib}

%global _samba4_idmap_modules idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2
%global _samba4_pdb_modules pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
%global _samba4_auth_modules auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4

%global _samba4_modules %{_samba4_idmap_modules},%{_samba4_pdb_modules},%{_samba4_auth_modules}

%global _libsmbclient %nil
%global _libwbclient %nil

%if ! %with_libsmbclient
%global _libsmbclient smbclient,
%endif

%if ! %with_libwbclient
%global _libwbclient wbclient,
%endif

%global _samba4_private_libraries %{_libsmbclient}%{_libwbclient}

%configure \
        --enable-fhs \
        --with-piddir=/run \
        --with-sockets-dir=/run/samba \
        --with-modulesdir=%{_libdir}/samba \
        --with-pammodulesdir=%{_libdir}/security \
        --with-lockdir=/var/lib/samba/lock \
        --with-statedir=/var/lib/samba \
        --with-cachedir=/var/lib/samba \
        --disable-rpath-install \
        --with-shared-modules=%{_samba4_modules} \
        --bundled-libraries=%{_samba4_libraries} \
        --with-pam \
        --with-pie \
        --with-relro \
        --without-fam \
%if (! %with_libsmbclient) || (! %with_libwbclient)
        --private-libraries=%{_samba4_private_libraries} \
%endif
%if %with_mitkrb5
        --with-system-mitkrb5 \
%endif
%if ! %with_dc
        --without-ad-dc \
%endif
%if ! %with_vfs_glusterfs
        --disable-glusterfs \
%endif
%if %with_clustering_support
        --with-cluster-support \
%endif
%if %with_profiling
        --with-profiling-data \
%endif
%if %{with testsuite}
        --enable-selftest \
%endif
%if ! %with_pam_smbpass
        --without-pam_smbpass \
%endif
        --with-systemd

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

install -d -m 0755 %{buildroot}/usr/{sbin,bin}
install -d -m 0755 %{buildroot}%{_libdir}/security
install -d -m 0755 %{buildroot}/var/lib/samba
install -d -m 0755 %{buildroot}/var/lib/samba/private
install -d -m 0755 %{buildroot}/var/lib/samba/winbindd_privileged
install -d -m 0755 %{buildroot}/var/lib/samba/scripts
install -d -m 0755 %{buildroot}/var/lib/samba/sysvol
install -d -m 0755 %{buildroot}/var/log/samba/old
install -d -m 0755 %{buildroot}/var/spool/samba
install -d -m 0755 %{buildroot}/var/run/samba
install -d -m 0755 %{buildroot}/var/run/winbindd
install -d -m 0755 %{buildroot}/%{_libdir}/samba
install -d -m 0755 %{buildroot}/%{_libdir}/pkgconfig

# Move libwbclient.so* into private directory, it cannot be just libdir/samba
# because samba uses rpath with this directory.
install -d -m 0755 %{buildroot}/%{_libdir}/samba/wbclient
mv %{buildroot}/%{_libdir}/libwbclient.so* %{buildroot}/%{_libdir}/samba/wbclient
if [ ! -f %{buildroot}/%{_libdir}/samba/wbclient/libwbclient.so.%{libwbc_alternatives_version} ]
then
    echo "Expected libwbclient version not found, please check if version has changed."
    exit -1
fi

# Install other stuff
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/samba

install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/samba/smb.conf

install -d -m 0755 %{buildroot}%{_sysconfdir}/security
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/security/pam_winbind.conf

install -d -m 0755 %{buildroot}%{_sysconfdir}/pam.d
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pam.d/samba

echo 127.0.0.1 localhost > %{buildroot}%{_sysconfdir}/samba/lmhosts

# openLDAP database schema
install -d -m 0755 %{buildroot}%{_sysconfdir}/openldap/schema
install -m644 examples/LDAP/samba.schema %{buildroot}%{_sysconfdir}/openldap/schema/samba.schema

install -m 0744 packaging/printing/smbprint %{buildroot}%{_bindir}/smbprint

install -d -m 0755 %{buildroot}%{_prefix}/lib/tmpfiles.d/
install -m644 packaging/systemd/samba.conf.tmp %{buildroot}%{_prefix}/lib/tmpfiles.d/samba.conf
# create /run/samba too.
echo "d /run/samba  755 root root" >> %{buildroot}%{_prefix}/lib/tmpfiles.d/samba.conf
%if %with_clustering_support
echo "d /run/ctdb 755 root root" >> %{buildroot}%{_tmpfilesdir}/ctdb.conf
%endif

install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 packaging/systemd/samba.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/samba
%if %with_clustering_support
install -m 0644 ctdb/config/ctdb.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/ctdb
%endif

install -m 0644 %{SOURCE201} packaging/README.downgrade

%if ! %with_dc
install -m 0644 %{SOURCE200} packaging/README.dc
install -m 0644 %{SOURCE200} packaging/README.dc-libs
%endif

install -d -m 0755 %{buildroot}%{_unitdir}
for i in nmb smb winbind ; do
    cat packaging/systemd/$i.service | sed -e 's@\[Service\]@[Service]\nEnvironment=KRB5CCNAME=FILE:/run/samba/krb5cc_samba@g' >tmp$i.service
    install -m 0644 tmp$i.service %{buildroot}%{_unitdir}/$i.service
done
%if %with_clustering_support
install -m 0755 ctdb/config/ctdb.service %{buildroot}%{_unitdir}
%endif

# NetworkManager online/offline script
install -d -m 0755 %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/
install -m 0755 packaging/NetworkManager/30-winbind-systemd \
            %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/30-winbind

# winbind krb5 locator
install -d -m 0755 %{buildroot}%{_libdir}/krb5/plugins/libkrb5
touch %{buildroot}%{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so

# This makes the right links, as rpmlint requires that
# the ldconfig-created links be recorded in the RPM.
/sbin/ldconfig -N -n %{buildroot}%{_libdir}

%if %{with testsuite}
%check
TDB_NO_FSYNC=1 make %{?_smp_mflags} test
%endif

%post
%systemd_post smb.service
%systemd_post nmb.service

%preun
%systemd_preun smb.service
%systemd_preun nmb.service

%postun
%systemd_postun_with_restart smb.service
%systemd_postun_with_restart nmb.service

%post common
/sbin/ldconfig
/usr/bin/systemd-tmpfiles --create %{_prefix}/lib/tmpfiles.d/samba.conf
if [ -d /var/cache/samba ]; then
    mv /var/cache/samba/netsamlogon_cache.tdb /var/lib/samba/ 2>/dev/null
    mv /var/cache/samba/winbindd_cache.tdb /var/lib/samba/ 2>/dev/null
    rm -rf /var/cache/samba/
    ln -sf /var/cache/samba /var/lib/samba/
fi

%postun common -p /sbin/ldconfig

%if %with_dc
%post dc-libs -p /sbin/ldconfig

%postun dc-libs -p /sbin/ldconfig
%endif # with_dc

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%if %with_libsmbclient
%post -n libsmbclient -p /sbin/ldconfig

%postun -n libsmbclient -p /sbin/ldconfig
%endif # with_libsmbclient

%if %with_libwbclient
%posttrans -n libwbclient
# It has to be posttrans here to make sure all files of a previous version
# without alternatives support are removed
%{_sbindir}/update-alternatives --install %{_libdir}/libwbclient.so.%{libwbc_alternatives_version} \
                                libwbclient.so.%{libwbc_alternatives_version}%{libwbc_alternatives_suffix} %{_libdir}/samba/wbclient/libwbclient.so.%{libwbc_alternatives_version} 10
/sbin/ldconfig

%preun -n libwbclient
%{_sbindir}/update-alternatives --remove libwbclient.so.%{libwbc_alternatives_version}%{libwbc_alternatives_suffix} %{_libdir}/samba/wbclient/libwbclient.so.%{libwbc_alternatives_version}
/sbin/ldconfig

%posttrans -n libwbclient-devel
%{_sbindir}/update-alternatives --install %{_libdir}/libwbclient.so \
                                libwbclient.so%{libwbc_alternatives_suffix} %{_libdir}/samba/wbclient/libwbclient.so 10

%preun -n libwbclient-devel
# alternatives checks if the file which should be removed is a link or not, but
# not if it points to the /etc/alternatives directory or to some other place.
# When downgrading to a version where alternatives is not used and
# libwbclient.so is a link and not a file it will be removed. The following
# check removes the alternatives files manually if that is the case.
if [ "`readlink %{_libdir}/libwbclient.so`" == "libwbclient.so.%{libwbc_alternatives_version}" ]; then
    /bin/rm -f /etc/alternatives/libwbclient.so%{libwbc_alternatives_suffix} /var/lib/alternatives/libwbclient.so%{libwbc_alternatives_suffix} 2> /dev/null
else
    %{_sbindir}/update-alternatives --remove libwbclient.so%{libwbc_alternatives_suffix} %{_libdir}/samba/wbclient/libwbclient.so
fi

%endif # with_libwbclient

%post test -p /sbin/ldconfig

%postun test -p /sbin/ldconfig

%pre winbind
/usr/sbin/groupadd -g 88 wbpriv >/dev/null 2>&1 || :

%post winbind
%systemd_post winbind.service

%preun winbind
%systemd_preun winbind.service

%postun winbind
%systemd_postun_with_restart smb.service
%systemd_postun_with_restart nmb.service

%postun winbind-krb5-locator
if [ "$1" -ge "1" ]; then
        if [ "`readlink %{_sysconfdir}/alternatives/winbind_krb5_locator.so`" == "%{_libdir}/winbind_krb5_locator.so" ]; then
                %{_sbindir}/update-alternatives --set winbind_krb5_locator.so %{_libdir}/winbind_krb5_locator.so
        fi
fi

%post winbind-krb5-locator
%{_sbindir}/update-alternatives --install %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so \
                                winbind_krb5_locator.so %{_libdir}/winbind_krb5_locator.so 10

%preun winbind-krb5-locator
if [ $1 -eq 0 ]; then
        %{_sbindir}/update-alternatives --remove winbind_krb5_locator.so %{_libdir}/winbind_krb5_locator.so
fi

%post winbind-modules -p /sbin/ldconfig

%postun winbind-modules -p /sbin/ldconfig

%if %with_clustering_support
%post -n ctdb
/usr/bin/systemd-tmpfiles --create %{_prefix}/lib/tmpfiles.d/ctdb.conf
%systemd_post ctdb.service

%preun -n ctdb
%systemd_preun ctdb.service

%postun -n ctdb
%systemd_postun_with_restart ctdb.service
%endif


%clean
rm -rf %{buildroot}

### SAMBA
%files
%defattr(-,root,root,-)
%doc COPYING README WHATSNEW.txt
%doc examples/autofs examples/LDAP examples/misc
%doc examples/printer-accounting examples/printing
%doc packaging/README.downgrade
%{_bindir}/smbstatus
%{_bindir}/eventlogadm
%{_sbindir}/nmbd
%{_sbindir}/smbd
%dir %{_libdir}/samba/auth
%{_libdir}/samba/auth/script.so
%{_libdir}/samba/auth/unix.so
%{_libdir}/samba/auth/wbc.so
%dir %{_libdir}/samba/vfs
%{_libdir}/samba/vfs/acl_tdb.so
%{_libdir}/samba/vfs/acl_xattr.so
%{_libdir}/samba/vfs/aio_fork.so
%{_libdir}/samba/vfs/aio_linux.so
%{_libdir}/samba/vfs/aio_posix.so
%{_libdir}/samba/vfs/aio_pthread.so
%{_libdir}/samba/vfs/audit.so
%{_libdir}/samba/vfs/btrfs.so
%{_libdir}/samba/vfs/cap.so
%{_libdir}/samba/vfs/catia.so
%{_libdir}/samba/vfs/commit.so
%{_libdir}/samba/vfs/crossrename.so
%{_libdir}/samba/vfs/default_quota.so
%{_libdir}/samba/vfs/dirsort.so
%{_libdir}/samba/vfs/expand_msdfs.so
%{_libdir}/samba/vfs/extd_audit.so
%{_libdir}/samba/vfs/fake_perms.so
%{_libdir}/samba/vfs/fileid.so
%{_libdir}/samba/vfs/fruit.so
%{_libdir}/samba/vfs/full_audit.so
%{_libdir}/samba/vfs/linux_xfs_sgid.so
%{_libdir}/samba/vfs/media_harmony.so
%{_libdir}/samba/vfs/netatalk.so
%{_libdir}/samba/vfs/preopen.so
%{_libdir}/samba/vfs/readahead.so
%{_libdir}/samba/vfs/readonly.so
%{_libdir}/samba/vfs/recycle.so
%{_libdir}/samba/vfs/scannedonly.so
%{_libdir}/samba/vfs/shadow_copy.so
%{_libdir}/samba/vfs/shadow_copy2.so
%{_libdir}/samba/vfs/shell_snap.so
%{_libdir}/samba/vfs/smb_traffic_analyzer.so
%{_libdir}/samba/vfs/snapper.so
%{_libdir}/samba/vfs/streams_depot.so
%{_libdir}/samba/vfs/streams_xattr.so
%{_libdir}/samba/vfs/syncops.so
%{_libdir}/samba/vfs/time_audit.so
%{_libdir}/samba/vfs/unityed_media.so
%{_libdir}/samba/vfs/worm.so
%{_libdir}/samba/vfs/xattr_tdb.so

%{_unitdir}/nmb.service
%{_unitdir}/smb.service
%attr(1777,root,root) %dir /var/spool/samba
%dir %{_sysconfdir}/openldap/schema
%{_sysconfdir}/openldap/schema/samba.schema
%{_sysconfdir}/pam.d/samba
%{_mandir}/man1/smbstatus.1*
%{_mandir}/man8/eventlogadm.8*
%{_mandir}/man8/smbd.8*
%{_mandir}/man8/nmbd.8*
#%{_mandir}/man8/vfs_*.8*
%{_mandir}/man8/vfs_acl_tdb.8*
%{_mandir}/man8/vfs_acl_xattr.8*
%{_mandir}/man8/vfs_aio_fork.8*
%{_mandir}/man8/vfs_aio_linux.8*
%{_mandir}/man8/vfs_aio_pthread.8*
%{_mandir}/man8/vfs_audit.8*
%{_mandir}/man8/vfs_btrfs.8*
%{_mandir}/man8/vfs_cacheprime.8*
%{_mandir}/man8/vfs_cap.8*
%{_mandir}/man8/vfs_catia.8*
%{_mandir}/man8/vfs_commit.8*
%{_mandir}/man8/vfs_crossrename.8*
%{_mandir}/man8/vfs_default_quota.8*
%{_mandir}/man8/vfs_dirsort.8*
%{_mandir}/man8/vfs_extd_audit.8*
%{_mandir}/man8/vfs_fake_perms.8*
%{_mandir}/man8/vfs_fileid.8*
%{_mandir}/man8/vfs_fruit.8*
%{_mandir}/man8/vfs_full_audit.8*
%{_mandir}/man8/vfs_gpfs.8*
%{_mandir}/man8/vfs_linux_xfs_sgid.8*
%{_mandir}/man8/vfs_media_harmony.8*
%{_mandir}/man8/vfs_netatalk.8*
%{_mandir}/man8/vfs_prealloc.8*
%{_mandir}/man8/vfs_preopen.8*
%{_mandir}/man8/vfs_readahead.8*
%{_mandir}/man8/vfs_readonly.8*
%{_mandir}/man8/vfs_recycle.8*
%{_mandir}/man8/vfs_scannedonly.8*
%{_mandir}/man8/vfs_shadow_copy.8*
%{_mandir}/man8/vfs_shadow_copy2.8*
%{_mandir}/man8/vfs_shell_snap.8*
%{_mandir}/man8/vfs_smb_traffic_analyzer.8*
%{_mandir}/man8/vfs_snapper.8*
%{_mandir}/man8/vfs_streams_depot.8*
%{_mandir}/man8/vfs_streams_xattr.8*
%{_mandir}/man8/vfs_syncops.8*
%{_mandir}/man8/vfs_time_audit.8*
%{_mandir}/man8/vfs_tsmsm.8*
%{_mandir}/man8/vfs_unityed_media.8*
%{_mandir}/man8/vfs_worm.8*
%{_mandir}/man8/vfs_xattr_tdb.8*

%if ! %{with_vfs_glusterfs}
%exclude %{_mandir}/man8/vfs_glusterfs.8*
%endif

%if ! %{with_vfs_cephfs}
%exclude %{_mandir}/man8/vfs_ceph.8*
%endif

### CLIENT
%files client
%defattr(-,root,root)
%{_bindir}/cifsdd
%{_bindir}/dbwrap_tool
%{_bindir}/nmblookup
%{_bindir}/oLschema2ldif
%{_bindir}/regdiff
%{_bindir}/regpatch
%{_bindir}/regshell
%{_bindir}/regtree
%{_bindir}/rpcclient
%{_bindir}/samba-regedit
%{_bindir}/sharesec
%{_bindir}/smbcacls
%{_bindir}/smbclient
%{_bindir}/smbcquotas
%{_bindir}/smbget
#%{_bindir}/smbiconv
%{_bindir}/smbprint
%{_bindir}/smbspool
%{_bindir}/smbta-util
%{_bindir}/smbtar
%{_bindir}/smbtree
%{_mandir}/man1/dbwrap_tool.1*
%{_mandir}/man1/nmblookup.1*
%{_mandir}/man1/oLschema2ldif.1*
%{_mandir}/man1/regdiff.1*
%{_mandir}/man1/regpatch.1*
%{_mandir}/man1/regshell.1*
%{_mandir}/man1/regtree.1*
%exclude %{_mandir}/man1/findsmb.1*
%{_mandir}/man1/log2pcap.1*
%{_mandir}/man1/rpcclient.1*
%{_mandir}/man1/sharesec.1*
%{_mandir}/man1/smbcacls.1*
%{_mandir}/man1/smbclient.1*
%{_mandir}/man1/smbcquotas.1*
%{_mandir}/man1/smbget.1*
%{_mandir}/man5/smbgetrc.5*
%{_mandir}/man1/smbtar.1*
%{_mandir}/man1/smbtree.1*
%{_mandir}/man8/samba-regedit.8*
%{_mandir}/man8/smbspool.8*
%{_mandir}/man8/smbta-util.8*

%if %{with_internal_tdb}
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbrestore
%{_bindir}/tdbtool
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbrestore.8*
%{_mandir}/man8/tdbtool.8*
%endif

%if %with_internal_ldb
%{_bindir}/ldbadd
%{_bindir}/ldbdel
%{_bindir}/ldbedit
%{_bindir}/ldbmodify
%{_bindir}/ldbrename
%{_bindir}/ldbsearch
%{_libdir}/samba/libldb-cmdline.so
%dir %{_libdir}/samba/ldb
%{_libdir}/samba/ldb/asq.so
%{_libdir}/samba/ldb/paged_results.so
%{_libdir}/samba/ldb/paged_searches.so
%{_libdir}/samba/ldb/rdn_name.so
%{_libdir}/samba/ldb/sample.so
%{_libdir}/samba/ldb/server_sort.so
%{_libdir}/samba/ldb/skel.so
%{_libdir}/samba/ldb/tdb.so
%{_mandir}/man1/ldbadd.1.gz
%{_mandir}/man1/ldbdel.1.gz
%{_mandir}/man1/ldbedit.1.gz
%{_mandir}/man1/ldbmodify.1.gz
%{_mandir}/man1/ldbrename.1.gz
%{_mandir}/man1/ldbsearch.1.gz
%endif

### CLIENT-LIBS
%files client-libs
%defattr(-,root,root)
%{_libdir}/libdcerpc-binding.so.*
%{_libdir}/libgensec.so.*
%{_libdir}/libndr.so.*
%{_libdir}/libndr-krb5pac.so.*
%{_libdir}/libndr-nbt.so.*
%{_libdir}/libndr-standard.so.*
%{_libdir}/libnetapi.so.*
%{_libdir}/libsamba-credentials.so.*
%{_libdir}/libsamba-passdb.so.*
%{_libdir}/libsamba-util.so.*
%{_libdir}/libsamba-hostconfig.so.*
%{_libdir}/libsamdb.so.*
%{_libdir}/libsmbconf.so.*
%{_libdir}/libsmbclient-raw.so.*
%{_libdir}/libsmbldap.so.*
%{_libdir}/libtevent-util.so.*
%{_libdir}/libregistry.so.*
%{_libdir}/libdcerpc.so.*

%dir %{_libdir}/samba
%{_libdir}/samba/libCHARSET3-samba4.so
%{_libdir}/samba/libaddns-samba4.so
%{_libdir}/samba/libads-samba4.so
%{_libdir}/samba/libasn1util-samba4.so
%{_libdir}/samba/libauth-sam-reply-samba4.so
%{_libdir}/samba/libauth-samba4.so
%{_libdir}/samba/libauthkrb5-samba4.so
%{_libdir}/samba/libcli-cldap-samba4.so
%{_libdir}/samba/libcli-ldap-common-samba4.so
%{_libdir}/samba/libcli-ldap-samba4.so
%{_libdir}/samba/libcli-nbt-samba4.so
%{_libdir}/samba/libcli-smb-common-samba4.so
%{_libdir}/samba/libcli-spoolss-samba4.so
%{_libdir}/samba/libcliauth-samba4.so
%{_libdir}/samba/libcmdline-credentials-samba4.so
%{_libdir}/samba/libdbwrap-samba4.so
%{_libdir}/samba/libdcerpc-samba-samba4.so
%{_libdir}/samba/liberrors-samba4.so
%{_libdir}/samba/libevents-samba4.so
%{_libdir}/samba/libflag-mapping-samba4.so
%{_libdir}/samba/libgenrand-samba4.so
%{_libdir}/samba/libgpo-samba4.so
%{_libdir}/samba/libgse-samba4.so
%{_libdir}/samba/libhttp-samba4.so
%{_libdir}/samba/libinterfaces-samba4.so
%{_libdir}/samba/libiov-buf-samba4.so
%{_libdir}/samba/libkrb5samba-samba4.so
%{_libdir}/samba/libldbsamba-samba4.so
%{_libdir}/samba/liblibcli-lsa3-samba4.so
%{_libdir}/samba/liblibcli-netlogon3-samba4.so
%{_libdir}/samba/liblibsmb-samba4.so
%{_libdir}/samba/libmessages-dgm-samba4.so
%{_libdir}/samba/libmessages-util-samba4.so
%{_libdir}/samba/libmsghdr-samba4.so
%{_libdir}/samba/libmsrpc3-samba4.so
%{_libdir}/samba/libndr-samba-samba4.so
%{_libdir}/samba/libndr-samba4.so
%{_libdir}/samba/libnet-keytab-samba4.so
%{_libdir}/samba/libnetif-samba4.so
%{_libdir}/samba/libnpa-tstream-samba4.so
%{_libdir}/samba/libprinting-migrate-samba4.so
%{_libdir}/samba/libreplace-samba4.so
%{_libdir}/samba/libsamba-cluster-support-samba4.so
%{_libdir}/samba/libsamba-debug-samba4.so
%{_libdir}/samba/libsamba-modules-samba4.so
%{_libdir}/samba/libsamba-security-samba4.so
%{_libdir}/samba/libsamba-sockets-samba4.so
%{_libdir}/samba/libsamba3-util-samba4.so
%{_libdir}/samba/libsamdb-common-samba4.so
%{_libdir}/samba/libsecrets3-samba4.so
%{_libdir}/samba/libserver-id-db-samba4.so
%{_libdir}/samba/libserver-role-samba4.so
%{_libdir}/samba/libsmb-transport-samba4.so
%{_libdir}/samba/libsmbd-base-samba4.so
%{_libdir}/samba/libsmbd-conn-samba4.so
%{_libdir}/samba/libsmbd-shim-samba4.so
%{_libdir}/samba/libsmbldaphelper-samba4.so
%{_libdir}/samba/libsmbregistry-samba4.so
%{_libdir}/samba/libsys-rw-samba4.so
%{_libdir}/samba/libsocket-blocking-samba4.so
%{_libdir}/samba/libtalloc-report-samba4.so
%{_libdir}/samba/libtdb-wrap-samba4.so
%{_libdir}/samba/libtime-basic-samba4.so
%{_libdir}/samba/libtrusts-util-samba4.so
%{_libdir}/samba/libutil-cmdline-samba4.so
%{_libdir}/samba/libutil-reg-samba4.so
%{_libdir}/samba/libutil-setid-samba4.so
%{_libdir}/samba/libutil-tdb-samba4.so

%if ! %with_libwbclient
%{_libdir}/samba/libwbclient.so.*
%{_libdir}/samba/libwinbind-client-samba4.so
%endif # ! with_libwbclient

%if ! %with_libsmbclient
%{_libdir}/samba/libsmbclient.so.*
%{_mandir}/man7/libsmbclient.7*
%endif # ! with_libsmbclient

%if %{with_internal_talloc}
%{_libdir}/samba/libtalloc.so.2
%{_libdir}/samba/libtalloc.so.%{talloc_version}
%{_libdir}/samba/libpytalloc-util.so.2
%{_libdir}/samba/libpytalloc-util.so.%{talloc_version}
%{_mandir}/man3/talloc.3.gz
%endif

%if %{with_internal_tevent}
%{_libdir}/samba/libtevent.so.0
%{_libdir}/samba/libtevent.so.%{tevent_version}
%endif

%if %{with_internal_tdb}
%{_libdir}/samba/libtdb.so.1
%{_libdir}/samba/libtdb.so.%{tdb_version}
%endif

%if %{with_internal_ldb}
%{_libdir}/samba/libldb.so.1
%{_libdir}/samba/libldb.so.%{ldb_version}
%{_mandir}/man3/ldb.3.gz
%endif

### COMMON
%files common
%defattr(-,root,root)
%{_prefix}/lib/tmpfiles.d/samba.conf
%dir %{_sysconfdir}/logrotate.d/
%config(noreplace) %{_sysconfdir}/logrotate.d/samba
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%ghost %dir /var/run/samba
%ghost %dir /var/run/winbindd
%dir /var/lib/samba
%attr(700,root,root) %dir /var/lib/samba/private
%attr(755,root,root) %dir %{_sysconfdir}/samba
%config(noreplace) %{_sysconfdir}/samba/smb.conf
%config(noreplace) %{_sysconfdir}/samba/lmhosts
%config(noreplace) %{_sysconfdir}/sysconfig/samba
%{_mandir}/man5/lmhosts.5*
%{_mandir}/man5/smb.conf.5*
%{_mandir}/man5/smbpasswd.5*
%{_mandir}/man7/samba.7*

### COMMON-libs
%files common-libs
%defattr(-,root,root)
# common libraries
%{_libdir}/samba/libpopt-samba3-samba4.so

%dir %{_libdir}/samba/pdb
%{_libdir}/samba/pdb/ldapsam.so
%{_libdir}/samba/pdb/smbpasswd.so
%{_libdir}/samba/pdb/tdbsam.so
%{_libdir}/samba/pdb/wbc_sam.so

%if %with_pam_smbpass
%{_libdir}/security/pam_smbpass.so
%endif

%files common-tools
%defattr(-,root,root)
%{_bindir}/net
%{_bindir}/pdbedit
%{_bindir}/profiles
%{_bindir}/smbcontrol
%{_bindir}/smbpasswd
%{_bindir}/testparm
%{_mandir}/man1/profiles.1*
%{_mandir}/man1/smbcontrol.1*
%{_mandir}/man1/testparm.1*
%{_mandir}/man8/net.8*
%{_mandir}/man8/pdbedit.8*
%{_mandir}/man8/smbpasswd.8*

### DC
%files dc
%defattr(-,root,root)

%if %with_dc
%{_bindir}/samba-tool
%{_sbindir}/samba
%{_sbindir}/samba_kcc
%{_sbindir}/samba_dnsupdate
%{_sbindir}/samba_spnupdate
%{_sbindir}/samba_upgradedns
%{_libdir}/samba/auth/samba4.so
%{_libdir}/samba/bind9/dlz_bind9.so
%{_libdir}/samba/bind9/dlz_bind9_10.so
%{_libdir}/samba/libheimntlm-samba4.so.1
%{_libdir}/samba/libheimntlm-samba4.so.1.0.1
%{_libdir}/samba/libkdc-samba4.so.2
%{_libdir}/samba/libkdc-samba4.so.2.0.0
%{_libdir}/samba/libpac-samba4.so
%dir %{_libdir}/samba/gensec
%{_libdir}/samba/gensec/krb5.so
%{_libdir}/samba/ldb/acl.so
%{_libdir}/samba/ldb/aclread.so
%{_libdir}/samba/ldb/anr.so
%{_libdir}/samba/ldb/descriptor.so
%{_libdir}/samba/ldb/dirsync.so
%{_libdir}/samba/ldb/dns_notify.so
%{_libdir}/samba/ldb/extended_dn_in.so
%{_libdir}/samba/ldb/extended_dn_out.so
%{_libdir}/samba/ldb/extended_dn_store.so
%{_libdir}/samba/ldb/ildap.so
%{_libdir}/samba/ldb/instancetype.so
%{_libdir}/samba/ldb/lazy_commit.so
%{_libdir}/samba/ldb/ldbsamba_extensions.so
%{_libdir}/samba/ldb/linked_attributes.so
%{_libdir}/samba/ldb/local_password.so
%{_libdir}/samba/ldb/new_partition.so
%{_libdir}/samba/ldb/objectclass.so
%{_libdir}/samba/ldb/objectclass_attrs.so
%{_libdir}/samba/ldb/objectguid.so
%{_libdir}/samba/ldb/operational.so
%{_libdir}/samba/ldb/partition.so
%{_libdir}/samba/ldb/password_hash.so
%{_libdir}/samba/ldb/ranged_results.so
%{_libdir}/samba/ldb/repl_meta_data.so
%{_libdir}/samba/ldb/resolve_oids.so
%{_libdir}/samba/ldb/rootdse.so
%{_libdir}/samba/ldb/samba3sam.so
%{_libdir}/samba/ldb/samba3sid.so
%{_libdir}/samba/ldb/samba_dsdb.so
%{_libdir}/samba/ldb/samba_secrets.so
%{_libdir}/samba/ldb/samldb.so
%{_libdir}/samba/ldb/schema_data.so
%{_libdir}/samba/ldb/schema_load.so
%{_libdir}/samba/ldb/secrets_tdb_sync.so
%{_libdir}/samba/ldb/show_deleted.so
%{_libdir}/samba/ldb/simple_dn.so
%{_libdir}/samba/ldb/simple_ldap_map.so
%{_libdir}/samba/ldb/subtree_delete.so
%{_libdir}/samba/ldb/subtree_rename.so
%{_libdir}/samba/ldb/tombstone_reanimate.so
%{_libdir}/samba/ldb/update_keytab.so
%{_libdir}/samba/ldb/wins_ldb.so
%{_libdir}/samba/vfs/posix_eadb.so
%dir /var/lib/samba/sysvol
%{_datadir}/samba/setup
%{_mandir}/man8/samba.8*
%{_mandir}/man8/samba-tool.8*
%else # with_dc
%doc packaging/README.dc
%exclude %{_mandir}/man8/samba.8*
%exclude %{_mandir}/man8/samba-tool.8*
%exclude %{_libdir}/samba/ldb/ildap.so
%exclude %{_libdir}/samba/ldb/ldbsamba_extensions.so

%endif # with_dc

### DC-LIBS
%files dc-libs
%defattr(-,root,root)
%if %with_dc
%{_libdir}/samba/libprocess-model-samba4.so
%{_libdir}/samba/libservice-samba4.so
%dir %{_libdir}/samba/process_model
%{_libdir}/samba/process_model/standard.so
%dir %{_libdir}/samba/service
%{_libdir}/samba/service/cldap.so
%{_libdir}/samba/service/dcerpc.so
%{_libdir}/samba/service/dns.so
%{_libdir}/samba/service/dns_update.so
%{_libdir}/samba/service/drepl.so
%{_libdir}/samba/service/kcc.so
%{_libdir}/samba/service/kdc.so
%{_libdir}/samba/service/ldap.so
%{_libdir}/samba/service/nbtd.so
%{_libdir}/samba/service/ntp_signd.so
%{_libdir}/samba/service/s3fs.so
%{_libdir}/samba/service/smb.so
%{_libdir}/samba/service/web.so
%{_libdir}/samba/service/winbindd.so
%{_libdir}/samba/service/wrepl.so
%{_libdir}/libdcerpc-server.so.*
%{_libdir}/samba/libdfs-server-ad-samba4.so
%{_libdir}/samba/libdnsserver-common-samba4.so
%{_libdir}/samba/libdsdb-module-samba4.so
%{_libdir}/samba/libntvfs-samba4.so
%{_libdir}/samba/libposix-eadb-samba4.so
%{_libdir}/samba/bind9/dlz_bind9_9.so
%else
%doc packaging/README.dc-libs
%endif # with_dc

### DEVEL
%files devel
%defattr(-,root,root)
%{_includedir}/samba-4.0/charset.h
%{_includedir}/samba-4.0/core/doserr.h
%{_includedir}/samba-4.0/core/error.h
%{_includedir}/samba-4.0/core/hresult.h
%{_includedir}/samba-4.0/core/ntstatus.h
%{_includedir}/samba-4.0/core/werror.h
%{_includedir}/samba-4.0/credentials.h
%{_includedir}/samba-4.0/dcerpc.h
%{_includedir}/samba-4.0/dlinklist.h
%{_includedir}/samba-4.0/domain_credentials.h
%{_includedir}/samba-4.0/gen_ndr/atsvc.h
%{_includedir}/samba-4.0/gen_ndr/auth.h
%{_includedir}/samba-4.0/gen_ndr/dcerpc.h
%{_includedir}/samba-4.0/gen_ndr/epmapper.h
%{_includedir}/samba-4.0/gen_ndr/krb5pac.h
%{_includedir}/samba-4.0/gen_ndr/lsa.h
%{_includedir}/samba-4.0/gen_ndr/mgmt.h
%{_includedir}/samba-4.0/gen_ndr/misc.h
%{_includedir}/samba-4.0/gen_ndr/nbt.h
%{_includedir}/samba-4.0/gen_ndr/drsblobs.h
%{_includedir}/samba-4.0/gen_ndr/drsuapi.h
%{_includedir}/samba-4.0/gen_ndr/ndr_drsblobs.h
%{_includedir}/samba-4.0/gen_ndr/ndr_drsuapi.h
%{_includedir}/samba-4.0/gen_ndr/ndr_atsvc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_atsvc_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_dcerpc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_epmapper.h
%{_includedir}/samba-4.0/gen_ndr/ndr_epmapper_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_krb5pac.h
%{_includedir}/samba-4.0/gen_ndr/ndr_mgmt.h
%{_includedir}/samba-4.0/gen_ndr/ndr_mgmt_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_misc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_nbt.h
%{_includedir}/samba-4.0/gen_ndr/ndr_samr.h
%{_includedir}/samba-4.0/gen_ndr/ndr_samr_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_svcctl.h
%{_includedir}/samba-4.0/gen_ndr/ndr_svcctl_c.h
%{_includedir}/samba-4.0/gen_ndr/netlogon.h
%{_includedir}/samba-4.0/gen_ndr/samr.h
%{_includedir}/samba-4.0/gen_ndr/security.h
%{_includedir}/samba-4.0/gen_ndr/server_id.h
%{_includedir}/samba-4.0/gen_ndr/svcctl.h
%{_includedir}/samba-4.0/gensec.h
%{_includedir}/samba-4.0/ldap-util.h
%{_includedir}/samba-4.0/ldap_errors.h
%{_includedir}/samba-4.0/ldap_message.h
%{_includedir}/samba-4.0/ldap_ndr.h
%{_includedir}/samba-4.0/ldb_wrap.h
%{_includedir}/samba-4.0/lookup_sid.h
%{_includedir}/samba-4.0/machine_sid.h
%{_includedir}/samba-4.0/ndr.h
%dir %{_includedir}/samba-4.0/ndr
%{_includedir}/samba-4.0/ndr/ndr_dcerpc.h
%{_includedir}/samba-4.0/ndr/ndr_drsblobs.h
%{_includedir}/samba-4.0/ndr/ndr_drsuapi.h
%{_includedir}/samba-4.0/ndr/ndr_svcctl.h
%{_includedir}/samba-4.0/ndr/ndr_nbt.h
%{_includedir}/samba-4.0/netapi.h
%{_includedir}/samba-4.0/param.h
%{_includedir}/samba-4.0/passdb.h
%{_includedir}/samba-4.0/policy.h
%{_includedir}/samba-4.0/read_smb.h
%{_includedir}/samba-4.0/registry.h
%{_includedir}/samba-4.0/roles.h
%{_includedir}/samba-4.0/rpc_common.h
%{_includedir}/samba-4.0/samba/session.h
%{_includedir}/samba-4.0/samba/version.h
%{_includedir}/samba-4.0/share.h
%{_includedir}/samba-4.0/smb2.h
%{_includedir}/samba-4.0/smb2_constants.h
%{_includedir}/samba-4.0/smb2_create_blob.h
%{_includedir}/samba-4.0/smb2_lease.h
%{_includedir}/samba-4.0/smb2_lease_struct.h
%{_includedir}/samba-4.0/smb2_signing.h
%{_includedir}/samba-4.0/smb_cli.h
%{_includedir}/samba-4.0/smb_cliraw.h
%{_includedir}/samba-4.0/smb_common.h
%{_includedir}/samba-4.0/smb_composite.h
%{_includedir}/samba-4.0/smbconf.h
%{_includedir}/samba-4.0/smb_constants.h
%{_includedir}/samba-4.0/smb_ldap.h
%{_includedir}/samba-4.0/smbldap.h
%{_includedir}/samba-4.0/smb_raw.h
%{_includedir}/samba-4.0/smb_raw_interfaces.h
%{_includedir}/samba-4.0/smb_raw_signing.h
%{_includedir}/samba-4.0/smb_raw_trans2.h
%{_includedir}/samba-4.0/smb_request.h
%{_includedir}/samba-4.0/smb_seal.h
%{_includedir}/samba-4.0/smb_signing.h
%{_includedir}/samba-4.0/smb_unix_ext.h
%{_includedir}/samba-4.0/smb_util.h
%{_includedir}/samba-4.0/tdr.h
%{_includedir}/samba-4.0/tsocket.h
%{_includedir}/samba-4.0/tsocket_internal.h
%{_includedir}/samba-4.0/tstream_smbXcli_np.h
%{_includedir}/samba-4.0/samba_util.h
%dir %{_includedir}/samba-4.0/util
%{_includedir}/samba-4.0/util/attr.h
%{_includedir}/samba-4.0/util/blocking.h
%{_includedir}/samba-4.0/util/byteorder.h
%{_includedir}/samba-4.0/util/data_blob.h
%{_includedir}/samba-4.0/util/debug.h
%{_includedir}/samba-4.0/util/fault.h
%{_includedir}/samba-4.0/util/genrand.h
%{_includedir}/samba-4.0/util/idtree.h
%{_includedir}/samba-4.0/util/idtree_random.h
%{_includedir}/samba-4.0/util/memory.h
%{_includedir}/samba-4.0/util/safe_string.h
%{_includedir}/samba-4.0/util/signal.h
%{_includedir}/samba-4.0/util/string_wrappers.h
%{_includedir}/samba-4.0/util/substitute.h
%{_includedir}/samba-4.0/util/talloc_stack.h
%{_includedir}/samba-4.0/util/tevent_ntstatus.h
%{_includedir}/samba-4.0/util/tevent_unix.h
%{_includedir}/samba-4.0/util/tevent_werror.h
%{_includedir}/samba-4.0/util/time.h
%{_includedir}/samba-4.0/util/xfile.h
%{_includedir}/samba-4.0/util_ldb.h
%{_libdir}/libdcerpc-atsvc.so
%{_libdir}/libdcerpc-binding.so
%{_libdir}/libdcerpc-samr.so
%{_libdir}/libdcerpc.so
%{_libdir}/libgensec.so
%{_libdir}/libndr-krb5pac.so
%{_libdir}/libndr-nbt.so
%{_libdir}/libndr-standard.so
%{_libdir}/libndr.so
%{_libdir}/libnetapi.so
%{_libdir}/libregistry.so
%{_libdir}/libsamba-credentials.so
%{_libdir}/libsamba-hostconfig.so
%{_libdir}/libsamba-policy.so
%{_libdir}/libsamba-util.so
%{_libdir}/libsamdb.so
%{_libdir}/libsmbclient-raw.so
%{_libdir}/libsmbconf.so
%{_libdir}/libtevent-util.so
%{_libdir}/pkgconfig/dcerpc.pc
%{_libdir}/pkgconfig/dcerpc_atsvc.pc
%{_libdir}/pkgconfig/dcerpc_samr.pc
%{_libdir}/pkgconfig/gensec.pc
%{_libdir}/pkgconfig/ndr.pc
%{_libdir}/pkgconfig/ndr_krb5pac.pc
%{_libdir}/pkgconfig/ndr_nbt.pc
%{_libdir}/pkgconfig/ndr_standard.pc
%{_libdir}/pkgconfig/netapi.pc
%{_libdir}/pkgconfig/registry.pc
%{_libdir}/pkgconfig/samba-credentials.pc
%{_libdir}/pkgconfig/samba-hostconfig.pc
%{_libdir}/pkgconfig/samba-policy.pc
%{_libdir}/pkgconfig/samba-util.pc
%{_libdir}/pkgconfig/samdb.pc
%{_libdir}/pkgconfig/smbclient-raw.pc
%{_libdir}/libsamba-passdb.so
%{_libdir}/libsmbldap.so

%if %with_dc
%{_includedir}/samba-4.0/dcerpc_server.h
%{_libdir}/libdcerpc-server.so
%{_libdir}/pkgconfig/dcerpc_server.pc
%endif

%if %with_internal_talloc
%{_includedir}/samba-4.0/pytalloc.h
%endif

%if ! %with_libsmbclient
%{_includedir}/samba-4.0/libsmbclient.h
%endif # ! with_libsmbclient

%if ! %with_libwbclient
%{_includedir}/samba-4.0/wbclient.h
%endif # ! with_libwbclient

### VFS-CEPHFS
%if %{with_vfs_cephfs}
%files vfs-cephfs
%{_libdir}/samba/vfs/ceph.so
%{_mandir}/man8/vfs_ceph.8*
%endif

### VFS-GLUSTERFS
%if %{with_vfs_glusterfs}
%files vfs-glusterfs
%{_libdir}/samba/vfs/glusterfs.so
%{_mandir}/man8/vfs_glusterfs.8*
%endif

### LIBS
%files libs
%defattr(-,root,root)
%{_libdir}/libdcerpc-atsvc.so.*
%{_libdir}/libdcerpc-samr.so.*
%{_libdir}/libsamba-policy.so.*

# libraries needed by the public libraries
%{_libdir}/samba/libMESSAGING-samba4.so
%{_libdir}/samba/libLIBWBCLIENT-OLD-samba4.so
%{_libdir}/samba/libauth4-samba4.so
%{_libdir}/samba/libauth-unix-token-samba4.so
%{_libdir}/samba/libcluster-samba4.so
%{_libdir}/samba/libdcerpc-samba4.so
%{_libdir}/samba/libnon-posix-acls-samba4.so
%{_libdir}/samba/libsamba-net-samba4.so
%{_libdir}/samba/libsamba-python-samba4.so
%{_libdir}/samba/libshares-samba4.so
%{_libdir}/samba/libsmbpasswdparser-samba4.so
%{_libdir}/samba/libxattr-tdb-samba4.so

%if %with_dc
%{_libdir}/samba/libdb-glue-samba4.so
%{_libdir}/samba/libHDB-SAMBA4-samba4.so
%{_libdir}/samba/libasn1-samba4.so.8
%{_libdir}/samba/libasn1-samba4.so.8.0.0
%{_libdir}/samba/libgssapi-samba4.so.2
%{_libdir}/samba/libgssapi-samba4.so.2.0.0
%{_libdir}/samba/libhcrypto-samba4.so.5
%{_libdir}/samba/libhcrypto-samba4.so.5.0.1
%{_libdir}/samba/libhdb-samba4.so.11
%{_libdir}/samba/libhdb-samba4.so.11.0.2
%{_libdir}/samba/libheimbase-samba4.so.1
%{_libdir}/samba/libheimbase-samba4.so.1.0.0
%{_libdir}/samba/libhx509-samba4.so.5
%{_libdir}/samba/libhx509-samba4.so.5.0.0
%{_libdir}/samba/libkrb5-samba4.so.26
%{_libdir}/samba/libkrb5-samba4.so.26.0.0
%{_libdir}/samba/libroken-samba4.so.19
%{_libdir}/samba/libroken-samba4.so.19.0.1
%{_libdir}/samba/libwind-samba4.so.0
%{_libdir}/samba/libwind-samba4.so.0.0.0
%endif

### LIBSMBCLIENT
%if %with_libsmbclient
%files -n libsmbclient
%defattr(-,root,root)
%{_libdir}/libsmbclient.so.*

### LIBSMBCLIENT-DEVEL
%files -n libsmbclient-devel
%defattr(-,root,root)
%{_includedir}/samba-4.0/libsmbclient.h
%{_libdir}/libsmbclient.so
%{_libdir}/pkgconfig/smbclient.pc
%{_mandir}/man7/libsmbclient.7*
%endif # with_libsmbclient

### LIBWBCLIENT
%if %with_libwbclient
%files -n libwbclient
%defattr(-,root,root)
%{_libdir}/samba/wbclient/libwbclient.so.*
%{_libdir}/samba/libwinbind-client-samba4.so

### LIBWBCLIENT-DEVEL
%files -n libwbclient-devel
%defattr(-,root,root)
%{_includedir}/samba-4.0/wbclient.h
%{_libdir}/samba/wbclient/libwbclient.so
%{_libdir}/pkgconfig/wbclient.pc
%endif # with_libwbclient

### PIDL
%files pidl
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/pidl
%dir %{perl_vendorlib}/Parse
%{perl_vendorlib}/Parse/Pidl.pm
%dir %{perl_vendorlib}/Parse/Pidl
%{perl_vendorlib}/Parse/Pidl/CUtil.pm
%{perl_vendorlib}/Parse/Pidl/Samba4.pm
%{perl_vendorlib}/Parse/Pidl/Expr.pm
%{perl_vendorlib}/Parse/Pidl/ODL.pm
%{perl_vendorlib}/Parse/Pidl/Typelist.pm
%{perl_vendorlib}/Parse/Pidl/IDL.pm
%{perl_vendorlib}/Parse/Pidl/Compat.pm
%dir %{perl_vendorlib}/Parse/Pidl/Wireshark
%{perl_vendorlib}/Parse/Pidl/Wireshark/Conformance.pm
%{perl_vendorlib}/Parse/Pidl/Wireshark/NDR.pm
%{perl_vendorlib}/Parse/Pidl/Dump.pm
%dir %{perl_vendorlib}/Parse/Pidl/Samba3
%{perl_vendorlib}/Parse/Pidl/Samba3/ServerNDR.pm
%{perl_vendorlib}/Parse/Pidl/Samba3/ClientNDR.pm
%dir %{perl_vendorlib}/Parse/Pidl/Samba4
%{perl_vendorlib}/Parse/Pidl/Samba4/Header.pm
%dir %{perl_vendorlib}/Parse/Pidl/Samba4/COM
%{perl_vendorlib}/Parse/Pidl/Samba4/COM/Header.pm
%{perl_vendorlib}/Parse/Pidl/Samba4/COM/Proxy.pm
%{perl_vendorlib}/Parse/Pidl/Samba4/COM/Stub.pm
%{perl_vendorlib}/Parse/Pidl/Samba4/Python.pm
%{perl_vendorlib}/Parse/Pidl/Samba4/Template.pm
%dir %{perl_vendorlib}/Parse/Pidl/Samba4/NDR
%{perl_vendorlib}/Parse/Pidl/Samba4/NDR/Server.pm
%{perl_vendorlib}/Parse/Pidl/Samba4/NDR/Client.pm
%{perl_vendorlib}/Parse/Pidl/Samba4/NDR/Parser.pm
%{perl_vendorlib}/Parse/Pidl/Samba4/TDR.pm
%{perl_vendorlib}/Parse/Pidl/NDR.pm
%{perl_vendorlib}/Parse/Pidl/Util.pm
%{_mandir}/man1/pidl*
%{_mandir}/man3/Parse::Pidl*

### PYTHON
%files python
%defattr(-,root,root,-)
%{python_sitearch}/*

### TEST
%files test
%defattr(-,root,root)
%{_bindir}/gentest
%{_bindir}/locktest
%{_bindir}/masktest
%{_bindir}/ndrdump
%{_bindir}/smbtorture
%{_mandir}/man1/gentest.1*
%{_mandir}/man1/locktest.1*
%{_mandir}/man1/masktest.1*
%{_mandir}/man1/ndrdump.1*
%{_mandir}/man1/smbtorture.1*
%{_mandir}/man1/vfstest.1*

%if %{with testsuite}
# files to ignore in testsuite mode
%{_libdir}/samba/libnss-wrapper.so
%{_libdir}/samba/libsocket-wrapper.so
%{_libdir}/samba/libuid-wrapper.so
%endif

### TEST-LIBS
%files test-libs
%defattr(-,root,root)
%{_libdir}/libtorture.so.*
%if %with_dc
%{_libdir}/samba/libdlz-bind9-for-torture-samba4.so
%else
%{_libdir}/samba/libdsdb-module-samba4.so
%endif

### TEST-DEVEL
%files test-devel
%defattr(-,root,root)
%{_includedir}/samba-4.0/torture.h
%{_libdir}/libtorture.so
%{_libdir}/pkgconfig/torture.pc

### WINBIND
%files winbind
%defattr(-,root,root)
#%{_bindir}/wbinfo3
%{_libdir}/samba/idmap
%{_libdir}/samba/nss_info
%{_libdir}/samba/libnss-info-samba4.so
%{_libdir}/samba/libidmap-samba4.so
%{_sbindir}/winbindd
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%{_unitdir}/winbind.service
%{_sysconfdir}/NetworkManager/dispatcher.d/30-winbind
%{_mandir}/man8/winbindd.8*
%{_mandir}/man8/idmap_*.8*

### WINBIND-CLIENTS
%files winbind-clients
%defattr(-,root,root)
%{_bindir}/ntlm_auth
%{_bindir}/wbinfo
%{_mandir}/man1/ntlm_auth.1.gz
%{_mandir}/man1/wbinfo.1*

### WINBIND-KRB5-LOCATOR
%files winbind-krb5-locator
%defattr(-,root,root)
%ghost %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so
%{_libdir}/winbind_krb5_locator.so
%{_mandir}/man7/winbind_krb5_locator.7*

### WINBIND-MODULES
%files winbind-modules
%defattr(-,root,root)
%{_libdir}/libnss_winbind.so*
%{_libdir}/libnss_wins.so*
%{_libdir}/security/pam_winbind.so
%config(noreplace) %{_sysconfdir}/security/pam_winbind.conf
%{_mandir}/man5/pam_winbind.conf.5*
%{_mandir}/man8/pam_winbind.8*

%if %with_clustering_support
%files -n ctdb
%defattr(-,root,root)
%doc ctdb/README
%config(noreplace) %{_sysconfdir}/sysconfig/ctdb
%config(noreplace) %{_sysconfdir}/ctdb/notify.sh
%config(noreplace) %{_sysconfdir}/ctdb/debug-hung-script.sh
%config(noreplace) %{_sysconfdir}/ctdb/ctdb-crash-cleanup.sh
%config(noreplace) %{_sysconfdir}/ctdb/gcore_trace.sh
%config(noreplace) %{_sysconfdir}/ctdb/functions
%config(noreplace) %{_sysconfdir}/ctdb/debug_locks.sh
%dir %{_localstatedir}/lib/ctdb/
%{_tmpfilesdir}/%{name}.conf

%{_unitdir}/ctdb.service

%dir %{_sysconfdir}/ctdb
%{_sysconfdir}/ctdb/statd-callout
%dir %{_sysconfdir}/ctdb/nfs-checks.d
%{_sysconfdir}/ctdb/nfs-checks.d/00.portmapper.check
%{_sysconfdir}/ctdb/nfs-checks.d/10.status.check
%{_sysconfdir}/ctdb/nfs-checks.d/20.nfs.check
%{_sysconfdir}/ctdb/nfs-checks.d/30.nlockmgr.check
%{_sysconfdir}/ctdb/nfs-checks.d/40.mountd.check
%{_sysconfdir}/ctdb/nfs-checks.d/50.rquotad.check
%{_sysconfdir}/ctdb/nfs-checks.d/README
%{_sysconfdir}/ctdb/nfs-linux-kernel-callout
%{_sysconfdir}/sudoers.d/ctdb
%dir %{_sysconfdir}/ctdb/events.d
%{_sysconfdir}/ctdb/events.d/00.ctdb
%{_sysconfdir}/ctdb/events.d/01.reclock
%{_sysconfdir}/ctdb/events.d/10.external
%{_sysconfdir}/ctdb/events.d/10.interface
%{_sysconfdir}/ctdb/events.d/11.natgw
%{_sysconfdir}/ctdb/events.d/11.routing
%{_sysconfdir}/ctdb/events.d/13.per_ip_routing
%{_sysconfdir}/ctdb/events.d/20.multipathd
%{_sysconfdir}/ctdb/events.d/31.clamd
%{_sysconfdir}/ctdb/events.d/40.fs_use
%{_sysconfdir}/ctdb/events.d/40.vsftpd
%{_sysconfdir}/ctdb/events.d/41.httpd
%{_sysconfdir}/ctdb/events.d/49.winbind
%{_sysconfdir}/ctdb/events.d/50.samba
%{_sysconfdir}/ctdb/events.d/60.nfs
%{_sysconfdir}/ctdb/events.d/62.cnfs
%{_sysconfdir}/ctdb/events.d/70.iscsi
%{_sysconfdir}/ctdb/events.d/91.lvs
%{_sysconfdir}/ctdb/events.d/99.timeout
%{_sysconfdir}/ctdb/events.d/README
%dir %{_sysconfdir}/ctdb/notify.d
%{_sysconfdir}/ctdb/notify.d/README
%{_prefix}/lib/tmpfiles.d/ctdb.conf
%{_sbindir}/ctdbd
%{_sbindir}/ctdbd_wrapper
%{_bindir}/ctdb
%{_bindir}/smnotify
%{_bindir}/ping_pong
%{_bindir}/ltdbtool
%{_bindir}/ctdb_diagnostics
%{_bindir}/onnode
%{_bindir}/ctdb_lock_helper
%{_bindir}/ctdb_event_helper

%{_mandir}/man1/ctdb.1.gz
%{_mandir}/man1/ctdbd.1.gz
%{_mandir}/man1/onnode.1.gz
%{_mandir}/man1/ltdbtool.1.gz
%{_mandir}/man1/ping_pong.1.gz
%{_mandir}/man1/ctdbd_wrapper.1.gz
%{_mandir}/man5/ctdbd.conf.5.gz
%{_mandir}/man7/ctdb.7.gz
%{_mandir}/man7/ctdb-tunables.7.gz
%{_mandir}/man7/ctdb-statistics.7.gz

%files -n ctdb-devel
%defattr(-,root,root)
%{_includedir}/samba-4.0/ctdb.h
%{_includedir}/samba-4.0/ctdb_client.h
%{_includedir}/samba-4.0/ctdb_protocol.h
%{_includedir}/samba-4.0/ctdb_private.h
%{_includedir}/samba-4.0/ctdb_typesafe_cb.h
%{_includedir}/samba-4.0/ctdb_version.h
%{_libdir}/pkgconfig/ctdb.pc

%files -n ctdb-tests
%defattr(-,root,root)
%dir %{_libdir}/ctdb-tests
%{_libdir}/ctdb-tests/ctdb_bench
%{_libdir}/ctdb-tests/ctdb_fetch
%{_libdir}/ctdb-tests/ctdb_fetch_one
%{_libdir}/ctdb-tests/ctdb_fetch_readonly_loop
%{_libdir}/ctdb-tests/ctdb_fetch_readonly_once
%{_libdir}/ctdb-tests/ctdb_functest
%{_libdir}/ctdb-tests/ctdb_lock_tdb
%{_libdir}/ctdb-tests/ctdb_persistent
%{_libdir}/ctdb-tests/ctdb_porting_tests
%{_libdir}/ctdb-tests/ctdb_randrec
%{_libdir}/ctdb-tests/ctdb_store
%{_libdir}/ctdb-tests/ctdb_stubtest
%{_libdir}/ctdb-tests/ctdb_takeover_tests
%{_libdir}/ctdb-tests/ctdb_trackingdb_test
%{_libdir}/ctdb-tests/ctdb_transaction
%{_libdir}/ctdb-tests/ctdb_traverse
%{_libdir}/ctdb-tests/ctdb_update_record
%{_libdir}/ctdb-tests/ctdb_update_record_persistent
%{_libdir}/ctdb-tests/rb_test
%{_bindir}/ctdb_run_tests
%{_bindir}/ctdb_run_cluster_tests
%dir %{_datadir}/ctdb-tests
%{_datadir}/ctdb-tests/eventscripts/etc-ctdb/events.d
%{_datadir}/ctdb-tests/eventscripts/etc-ctdb/functions
%{_datadir}/ctdb-tests/eventscripts/etc-ctdb/nfs-checks.d
%{_datadir}/ctdb-tests/eventscripts/etc-ctdb/nfs-linux-kernel-callout
%{_datadir}/ctdb-tests/eventscripts/etc-ctdb/statd-callout
%{_datadir}/ctdb-tests/scripts/common.sh
%{_datadir}/ctdb-tests/scripts/integration.bash
%{_datadir}/ctdb-tests/scripts/test_wrap
%{_datadir}/ctdb-tests/scripts/unit.sh
%doc ctdb/tests/README
%endif # with_clustering_support

%changelog
* Sun Feb 14 2016 Liu Di <liudidi@gmail.com> - 2:4.3.2-1.3
- 为 Magic 3.0 重建

* Thu Dec 10 2015 Liu Di <liudidi@gmail.com> - 2:4.3.2-1.2
- 为 Magic 3.0 重建

* Thu Dec 10 2015 Liu Di <liudidi@gmail.com> - 2:4.3.2-1.1
- 为 Magic 3.0 重建


