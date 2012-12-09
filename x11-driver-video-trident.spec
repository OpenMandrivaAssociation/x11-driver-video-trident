Name: x11-driver-video-trident
Version: 1.3.6
Release: 2
Summary: X.org driver for Trident Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-trident-%{version}.tar.bz2
 
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-trident is the X.org driver for Trident Cards.

%prep
%setup -qn xf86-video-trident-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/trident_drv.so
%{_mandir}/man4/trident.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.6-1
+ Revision: 810696
- version update 1.3.6

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.3.5-2
+ Revision: 787286
- Rebuild for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.5-1
+ Revision: 786720
- version update 1.3.5

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.3.4-7
+ Revision: 748475
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.4-6
+ Revision: 703797
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.3.4-5
+ Revision: 683590
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-4
+ Revision: 671182
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.4-3mdv2011.0
+ Revision: 595737
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Jul 20 2010 Thierry Vignaud <tv@mandriva.org> 1.3.4-1mdv2011.0
+ Revision: 555163
- new release

* Wed Aug 05 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.3-1mdv2010.0
+ Revision: 410356
- Use %%configure2_5x

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.2-1mdv2010.0
+ Revision: 391935
- update to new version 1.3.2

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.3.1-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.1-1mdv2009.1
+ Revision: 317853
- New version 1.3.1

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.3.0-3mdv2009.1
+ Revision: 308178
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-2mdv2009.0
+ Revision: 265952
- rebuild early 2009.0 package (before pixel changes)
- improved description
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-1mdv2009.0
+ Revision: 194133
- Update to version 1.3.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.4-1mdv2008.1
+ Revision: 166148
- Revert to use upstream tarball and remove local patches.
  Update to new upstream version 1.2.4.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.3-4mdv2008.1
+ Revision: 156624
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.3-3mdv2008.1
+ Revision: 154790
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
  Also actually apply patches...
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update to generate tarball form tag xf86-video-trident-1.2.3, also
  added several patches as well as sync with existing mandriva branch.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.3-2mdv2008.1
+ Revision: 99058
- minor spec cleanup
- build against new xserver (1.4)

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

