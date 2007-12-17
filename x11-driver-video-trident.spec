Name: x11-driver-video-trident
Version: 1.2.3
Release: %mkrel 3
Summary: The X.org driver for Trident Cards
Group: System/X11
URL: http://xorg.freedesktop.org

########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-trident  xorg/drivers/xf86-video-trident
# cd xorg/drivers/xf86-video/trident
# git-archive --format=tar --prefix=xf86-video-trident-1.2.3/ master | bzip2 -9 > xf86-video-trident-1.2.3.tar.bz2
########################################################################
Source0: xf86-video-trident-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Trident Cards


%prep
%setup -q -n xf86-video-trident-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/trident_drv.la
%{_libdir}/xorg/modules/drivers/trident_drv.so
%{_mandir}/man4/trident.*

