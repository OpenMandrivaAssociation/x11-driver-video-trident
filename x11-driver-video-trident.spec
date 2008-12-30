Name: x11-driver-video-trident
Version: 1.3.1
Release: %mkrel 2
Summary: X.org driver for Trident Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-trident-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
 
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-trident is the X.org driver for Trident Cards.

%prep
%setup -q -n xf86-video-trident-%{version}

%build
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
