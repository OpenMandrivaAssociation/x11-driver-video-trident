%define _disable_ld_no_undefined 1

Summary:	X.org driver for Trident Cards
Name:		x11-driver-video-trident
Version:	1.3.6
Release:	5
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-trident-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch
 
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-trident is the X.org driver for Trident Cards.

%prep
%setup -qn xf86-video-trident-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/trident_drv.so
%{_mandir}/man4/trident.*

