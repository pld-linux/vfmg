%include	/usr/lib/rpm/macros.perl
Summary:	VFolders Menu Generator
Summary(pl):	Generator Menu opartego na VFolders
Name:		vfmg
Version:	0.9.16
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Vendor:		GoTaR <gotar@pld-linux.org>
Source0:	http://ep09.pld-linux.org/~havner/%{name}-%{version}.tar.bz2
# Source0-md5:	2945bbe48efa06123b545883f32f0a69
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/zsh/site-functions,/etc/{rc.d/init.d,sysconfig}}

install vfmg $RPM_BUILD_ROOT%{_bindir}
install vfmg-zsh $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_vfmg
install vfmg.init $RPM_BUILD_ROOT/etc/rc.d/init.d/vfmg
install vfmg.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/vfmg

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add vfmg

%preun
if [ "$1" = "0" ]; then
        /sbin/chkconfig --del vfmg
fi

%files
%defattr(644,root,root,755)
%doc README vfmg.html
%attr(755,root,root) %{_bindir}/*
%attr(754,root,root) /etc/rc.d/init.d/vfmg
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/vfmg
%{_datadir}/zsh/site-functions/*
