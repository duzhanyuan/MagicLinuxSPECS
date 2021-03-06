Name:           gstreamer-ffmpeg
Version:        0.10.13
Release:        2%{?dist}
Summary:        GStreamer FFmpeg-based plug-ins
Summary(zh_CN.UTF-8): GStreamer FFmpeg 插件
Group:          Applications/Multimedia
Group(zh_CN.UTF-8): 应用程序/多媒体
# the ffmpeg plugin is LGPL, the postproc plugin is GPL
License:        GPLv2+ and LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-ffmpeg/gst-ffmpeg-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gstreamer-devel >= 0.10.0
BuildRequires:  gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:  ffmpeg-devel liboil-devel bzip2-devel

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

This package provides FFmpeg-based GStreamer plug-ins.

%description -l zh_CN.UTF-8
GStreamer FFmpeg 插件。

%prep
%setup -q -n gst-ffmpeg-%{version}


%build
%configure --disable-dependency-tracking --disable-static \
  --with-package-name="gst-plugins-ffmpeg" \
  --with-package-origin="http://www.magiclinux.org/" \
  --with-system-ffmpeg
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/libgst*.la


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/gstreamer-0.10/libgstffmpeg.so
%{_libdir}/gstreamer-0.10/libgstffmpegscale.so
%{_libdir}/gstreamer-0.10/libgstpostproc.so


%changelog
* Fri Apr 11 2014 Liu Di <liudidi@gmail.com> - 0.10.13-2
- 为 Magic 3.0 重建

