Summary:	VFolders Menu Generator
Summary(pl):	Generator Menu opartego na VFolders
Name:		vfmg
Version:	0.9.6
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Vendor:		GoTaR <gotar@pld-linux.org>
Source0:	%{name}
Source1:	%{name}-README
Source2:	%{name}-zsh
URL:		http://vfmg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VFolders Menu Generator. Generates window managers menus (for now only
icewm, blackbox, window maker (both old and new style), xfce4 and
afterstep are supported, next coming soon) from desktop files
conforming the freedesktop.org menu specification.

%description -l pl
Generator Menu opartego na VFolders. Generuje menu zarz±dców okien
(jak dot±d wspierane s± tylko icewm, blackbox, window maker (oba
style, stary oraz nowy), xfce4 i afterstep, nastêpne wkrótce) z plików
desktop wype³niaj±cych specyfikacjê menu z freedesktop.org.

%prep
%setup -c -T

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/zsh/site-functions}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} README
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_vfmg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/zsh/site-functions/*
