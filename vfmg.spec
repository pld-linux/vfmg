%include	/usr/lib/rpm/macros.perl
Summary:	VFolders Menu Generator
Summary(pl):	Generator Menu opartego na VFolders
Name:		vfmg
Version:	0.9.16
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Vendor:		GoTaR <gotar@pld-linux.org>
Source0:	http://ep09.pld-linux.org/~havner/%{name}-%{version}.tar.bz2
# Source0-md5:	ba13c5c5c2516e0b58257c491c69a568
URL:		http://vfmg.sourceforge.net/
BuildRequires:	rpm-perlprov
Requires:	applnk >= 1.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VFolders Menu Generator. Generates window managers menus (for now only
icewm, blackbox, window maker (both old and new style), xfce4, aewm,
afterstep, fvwm2, olvwm, qvwm, enlightenment and fluxbox are
supported, next coming soon) from desktop files conforming the
freedesktop.org menu specification.

%description -l pl
Generator Menu opartego na VFolders. Generuje menu zarz±dców okien
(jak dot±d wspierane s± tylko icewm, blackbox, window maker (oba
style, stary oraz nowy), xfce4, aewm, afterstep, fvwm2, olvwm, qvwm,
enlightenment i fluxbox, nastêpne wkrótce) z plików desktop
wype³niaj±cych specyfikacjê menu z freedesktop.org.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/zsh/site-functions}

install vfmg $RPM_BUILD_ROOT%{_bindir}
install vfmg-zsh $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_vfmg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README vfmg.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/zsh/site-functions/*
