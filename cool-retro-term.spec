# TODO
# - create and use system package for qmltermwidget?

%define	qtver	5.2
Summary:	A good looking terminal emulator which mimics the old cathode display
Name:		cool-retro-term
Version:	1.0.0
Release:	0.2
License:	GPL-3.0+
Group:		X11/Applications
Source0:	https://github.com/Swordfish90/cool-retro-term/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	06e73fbffcb5fd55695e5ec4034e3ad1
Source1:	https://github.com/Swordfish90/qmltermwidget/archive/490eeaf195cd5764a3798c2a2340ced648db4526/qmltermwidget.tar.gz
# Source1-md5:	64d5f6ee2f8d01512209f211d2533e7d
URL:		https://github.com/Swordfish90/cool-retro-term
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Declarative-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	desktop-file-utils
Requires:	Qt5Quick-controls
Requires:	Qt5Quick-graphicaleffects
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cool-retro-term is a terminal emulator which mimics the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
%setup -q -a1
mv qmltermwidget-*/* qmltermwidget

%build
qmake-qt5
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

desktop-file-install --dir=$RPM_BUILD_ROOT%{_desktopdir} %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/qt5/qml/QMLTermWidget
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*.png
