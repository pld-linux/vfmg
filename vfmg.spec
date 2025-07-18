Summary:	VFolders Menu Generator
Summary(pl.UTF-8):	Generator Menu opartego na VFolders
Name:		vfmg
Version:	0.9.95
Release:	8
License:	GPL
Group:		X11/Window Managers/Tools
Vendor:		GoTaR <gotar@pld-linux.org>
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	f73aaacd03bd9b8fe097cac5011f26d9
Patch0:		%{name}-ignore-OnlyUnallocated.patch
Patch1:		%{name}-XDG_MENU_PREFIX.patch
Patch2:		no-xfce4.patch
Patch3:		perl-5.26.patch
URL:		http://vfmg.sourceforge.net/
BuildRequires:	rpm-perlprov
Requires(post,preun):	/sbin/chkconfig
Requires:	xdg-menus
Obsoletes:	wmconfig
Conflicts:	WindowMaker < 0.92.0-0.4
Conflicts:	enlightenment < 0.16.7.2-2
Conflicts:	icewm < 2:1.2.25-0.2
Conflicts:	metisse < 0.3.5-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VFolders Menu Generator. Generates window managers menus (for now only
icewm, blackbox, window maker (both old and new style), xfce4, aewm,
afterstep, fvwm2, olvwm, qvwm, enlightenment and fluxbox are
supported, next coming soon) from desktop files conforming the
freedesktop.org menu specification.

%description -l pl.UTF-8
Generator Menu opartego na VFolders. Generuje menu zarządców okien
(jak dotąd wspierane są tylko icewm, blackbox, window maker (oba
style, stary oraz nowy), xfce4, aewm, afterstep, fvwm2, olvwm, qvwm,
enlightenment i fluxbox, następne wkrótce) z plików desktop
wypełniających specyfikację menu z freedesktop.org.

%package cron
Summary:	Crontab file for VFolders Menu Generator
Summary(pl.UTF-8):	Plik crontaba dla generatora menu opartego na vfolders
Group:		X11/Window Managers/Tools
Requires:	crondaemon

%description cron
This package contains a configuration file that enables window manager
menu generation to be performed regularily at given time.

%description cron -l pl.UTF-8
Pakiet ten zawiera plik konfiguracyjny umożliwiający regularne
generowanie menu dla zarządców okien o określonych godzinach.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_datadir}/zsh/site-functions} \
	$RPM_BUILD_ROOT/etc/{cron.d,rc.d/init.d,sysconfig}

install vfmg $RPM_BUILD_ROOT%{_bindir}
install vfmgrc $RPM_BUILD_ROOT%{_sysconfdir}
install vfmg-zsh $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_vfmg
install vfmg.init $RPM_BUILD_ROOT/etc/rc.d/init.d/vfmg
install vfmg.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/vfmg
install vfmg.cron $RPM_BUILD_ROOT/etc/cron.d/vfmg

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vfmgrc
%attr(754,root,root) /etc/rc.d/init.d/vfmg
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vfmg
%{_datadir}/zsh/site-functions/*

%files cron
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/cron.d/vfmg
