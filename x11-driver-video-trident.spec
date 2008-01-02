Name: x11-driver-video-trident
Version: 1.2.3
Release: %mkrel 3
Summary: The X.org driver for Trident Cards
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-trident  xorg/drivers/xf86-video-trident
# cd xorg/drivers/xf86-video/trident
# git-archive --format=tar --prefix=xf86-video-trident-1.2.3/ xf86-video-trident-1.2.3 | bzip2 -9 > xf86-video-trident-1.2.3.tar.bz2
########################################################################
Source0: xf86-video-trident-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-trident-1.2.3..origin/mandriva+gpl
Patch1: 0001-Add-doublescan-support-not-tested-on-all-chipsets.patch
Patch2: 0002-Fix-PC98-systems-with-WAITFORVSYNC.patch
Patch3: 0003-Delete-tridentramdac.c-since-all-functions-inside-ar.patch
Patch4: 0004-renamed-.cvsignore-.gitignore.patch
Patch5: 0005-TRIDENT_-_VERSION-using-PACKAGE_VERSION_.patch
Patch6: 0006-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Trident Cards

%prep
%setup -q -n xf86-video-trident-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/trident_drv.so
%{_mandir}/man4/trident.*
