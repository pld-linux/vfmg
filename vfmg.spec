%include	/usr/lib/rpm/macros.perl
Summary:	VFolders Menu Generator
Summary(pl):	Generator Menu opartego na VFolders
Name:		vfmg
Version:	0.9.9a
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Vendor:		GoTaR <gotar@pld-linux.org>
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	2f4450437d963ecb2267c99494f2c60c
URL:		http://vfmg.sourceforge.net/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VFolders Menu Generator. Generates window managers menus (for now only
icewm, blackbox, window maker (both old and new style), xfce4,
afterstep, fvwm2 and olvwm are supported, next coming soon) from
desktop files conforming the freedesktop.org menu specification.

%description -l pl
Generator Menu opartego na VFolders. Generuje menu zarz±dców okien
(jak dot±d wspierane s± tylko icewm, blackbox, window maker (oba
style, stary oraz nowy), xfce4, afterstep, fvwm2 i olvwm, nastêpne
wkrótce) z plików desktop wype³niaj±cych specyfikacjê menu z
freedesktop.org.

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
