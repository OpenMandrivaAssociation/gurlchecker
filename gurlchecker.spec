%define version 0.10.0
%define release %mkrel 4

Summary:	Web page link validation program
Name:		gurlchecker
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/WWW
URL:		http://www.nongnu.org/gurlchecker/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		http://labs.libre-entreprise.org/download/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	libglade2.0-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgnet2-devel
BuildRequires:	ImageMagick
BuildRequires:  perl(XML::Parser)
BuildRequires:  gnutls-devel
BuildRequires:  docbook-utils
BuildRequires:  openjade
BuildRequires:  libtidy-devel
BuildRequires:  libcroco0.6-devel
BuildRequires:	docbook-dtd41-sgml
#BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils
%description
gURLChecker is a graphical web link checker. It can work on a whole
site, a single local page or a browser bookmarks file.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# menu
mkdir -p %{buildroot}%{_menudir}
cat << _EOF_ > %{buildroot}%{_menudir}/%{name}
?package(%{name}): \
 command="%{_bindir}/%{name}" \
 icon="%{name}.png" \
 longtitle="Web page link checker" \
 needs="x11" \
 section="Internet/Other" \
 title="gURLChecker" \
 startup_notify="true" \
 xdg="true"
_EOF_

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Network" \
  --add-category="X-MandrivaLinux-Internet-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}%{_iconsdir} \
	 %{buildroot}%{_liconsdir} \
	 %{buildroot}%{_miconsdir}
convert -geometry 48x48 ui/%{name}_icon.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 ui/%{name}_icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 ui/%{name}_icon.png %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
#%dir %{_datadir}/gtk-doc/html/%{name}
#%{_datadir}/gtk-doc/html/%{name}/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_menudir}/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


