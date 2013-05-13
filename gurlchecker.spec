Summary:	Web page link validation program
Name:		gurlchecker
Version:	0.13.1
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		http://www.nongnu.org/gurlchecker/
Source0:	http://labs.libre-entreprise.org/frs/download.php/857/%{name}-%{version}.tar.gz
Patch0:		gurlchecker-0.13-tidydir.patch
Patch1:		gurlchecker-0.12-fix-str-fmt.patch
BuildRequires:	libglade2.0-devel
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	libgnet2-devel
BuildRequires:	sqlite3-devel
BuildRequires:	libjson-glib-devel
BuildRequires:	imagemagick
BuildRequires:  perl(XML::Parser)
BuildRequires:  gnutls-devel
BuildRequires:  docbook-utils
BuildRequires:  openjade
BuildRequires:  tidy-devel = 1:20090904-7:2013.0
BuildRequires:  libcroco0.6-devel
BuildRequires:	docbook-dtd41-sgml
BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils
BuildRequires:	intltool

%description
gURLChecker is a graphical web link checker. It can work on a whole
site, a single local page or a browser bookmarks file.

%prep
%setup -q
%patch0 -p0 -b .tidy
%patch1 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}%{_iconsdir} \
	 %{buildroot}%{_liconsdir} \
	 %{buildroot}%{_miconsdir}
convert -geometry 48x48 ui/%{name}_icon.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 ui/%{name}_icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 ui/%{name}_icon.png %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%dir %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/%{name}/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Mon Apr 16 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.13.1-1
+ Revision: 791338
- update to 0.13.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13-3mdv2011.0
+ Revision: 611049
- rebuild

* Mon Feb 15 2010 Funda Wang <fwang@mandriva.org> 0.13-2mdv2010.1
+ Revision: 506383
- rework tidy patch
- add more BR
- new version 0.13

* Sun Feb 07 2010 Funda Wang <fwang@mandriva.org> 0.12.1-2mdv2010.1
+ Revision: 501644
- New version 0.12.1

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 0.12-1mdv2010.1
+ Revision: 498524
- New version 0.12

* Tue Nov 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.5-1mdv2010.1
+ Revision: 464297
- Update to new version 0.10.5

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 0.10.3-2mdv2010.0
+ Revision: 382370
- rebuild for gnutls 2.8

* Tue Feb 10 2009 Funda Wang <fwang@mandriva.org> 0.10.3-1mdv2009.1
+ Revision: 339201
- New version 0.10.3

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.10.2-3mdv2009.0
+ Revision: 246729
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Feb 01 2008 Funda Wang <fwang@mandriva.org> 0.10.2-1mdv2008.1
+ Revision: 160977
- drop old category
- tidy does not sit in sub dir
- New version 0.10.2

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue May 22 2007 J√©r√¥me Soyer <saispo@mandriva.org> 0.10.1-1mdv2008.0
+ Revision: 29667
- New release


* Thu Mar 01 2007 Emmanuel Andry <eandry@mandriva.org> 0.10.0-4mdv2007.0
+ Revision: 130363
- buildrequires libtidy-devel
- buildrequires libcroco0.6-devel
- buildrequires docbook-dtd41-sgml
- buildrequires desktop-file-utils
- Import gurlchecker

* Sun Aug 20 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.10.0-3mdv2007.0
- Rebuild against new dbus

* Mon Aug 14 2006 Emmanuel Andry <eandry@mandriva.org> 0.10.0-2mdv2007.0
- xdg menu

* Tue May 30 2006 Jerome Soyer <saispo@mandriva.org> 0.10.0-1mdv2007.0
- New release 0.10.0

* Tue May 16 2006 Jerome Soyer <saispo@mandriva.org> 0.9.2-1mdk
- New release, i decided to upload unstable, more options are present.

* Tue Oct 04 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.8.2-5mdk
- Fix BuildRequires

* Tue Oct 04 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.8.2-4mdk
Fix BuildRequires

* Tue Oct 04 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.8.2-3mdk
Fix BuildRequires

* Tue Oct 04 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.8.2-2mdk
- BuildRequires fix

* Tue May 31 2005 Lenny Cartier <lenny@mandriva.com> 0.8.2-1mdk
- 0.8.2

* Mon Apr 04 2005 Abel Cheung <deaddog@mandrake.org> 0.8.1-1mdk
- 0.8.1

* Tue Jan 04 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.8.0-1mdk
- 0.8.0

* Sun Apr 04 2004 Abel Cheung <deaddog@deaddog.org> 0.6.7-1mdk
- New version

* Sat Mar 13 2004 Abel Cheung <deaddog@deaddog.org> 0.6.6-1mdk
- New version

