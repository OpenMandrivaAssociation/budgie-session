%define po_package gnome-session-45

%define _disable_rebuild_configure 1

Summary:	Budgie Session is a softish fork of gnome-session, designed to provide a stable session manager for Budgie 10.x
Name:		budgie-session
Version:	0.9
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Budgie
Url:		https://github.com/BuddiesOfBudgie/budgie-session/
Source0:	https://github.com/BuddiesOfBudgie/budgie-session/releases/download/v%{version}/budgie-session-v%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:	desktop-file-utils
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	xmlto
BuildRequires:	tcp_wrappers-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:  pkgconfig(egl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xtrans)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  pkgconfig(x11)
BuildRequires:	xmlto
BuildRequires:	meson
BuildRequires:  pkgconfig(glesv2)
#BuildRequires:  glesv3-devel

Requires:	desktop-common-data
Requires:	gnome-settings-daemon
Requires:	gsettings-desktop-schemas
Requires:	dconf
Requires:   x11-server-xwayland

%description
Budgie Session is a softish fork of gnome-session, designed to provide a stable session manager for Budgie 10.x

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson                     \
    -Dsystemd=true         \
    -Dsystemd_journal=true
%meson_build

%install
%meson_install
#find_lang %{po_package}

%files
