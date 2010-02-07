%define version 0.12.1
%define release %mkrel 2

Summary:	Web page link validation program
Name:		gurlchecker
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Networking/WWW
URL:		http://www.nongnu.org/gurlchecker/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
Source:		http://labs.libre-entreprise.org/download/%{name}/%{name}-%{version}.tar.gz
Patch0:		gurlchecker-0.10.3-tidydir.patch
Patch1:		gurlchecker-0.12-fix-str-fmt.patch
BuildRequires:	libglade2.0-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgnet2-devel
BuildRequires:	imagemagick
BuildRequires:  perl(XML::Parser)
BuildRequires:  gnutls-devel
BuildRequires:  docbook-utils
BuildRequires:  openjade
BuildRequires:  libtidy-devel
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
%patch0 -p0
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

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

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
