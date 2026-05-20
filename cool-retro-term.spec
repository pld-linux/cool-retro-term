# TODO
# - create and use system package for qmltermwidget?

%define	qtver	5.2
Summary:	A good looking terminal emulator which mimics the old cathode display
Name:		cool-retro-term
Version:	1.2.0
Release:	1
License:	GPL-3.0+
Group:		X11/Applications
Source0:	https://github.com/Swordfish90/cool-retro-term/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3e8019a01c619bfd09014bad62bbe432
Source1:	https://github.com/Swordfish90/qmltermwidget/archive/63228027e1f97c24abb907550b22ee91836929c5/qmltermwidget.tar.gz
# Source1-md5:	2e095e89b81b7ab90e7fd53b055fb383
URL:		https://github.com/Swordfish90/cool-retro-term
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	desktop-file-utils
BuildRequires:	libstdc++-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
Requires:	Qt5Gui-platform-xcb-egl >= %{qtver}
Requires:	Qt5Gui-platform-xcb-glx >= %{qtver}
Requires:	Qt5Quick-controls2 >= %{qtver}
Requires:	Qt5Quick-graphicaleffects >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cool-retro-term is a terminal emulator which mimics the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
%setup -q -a1
mv qmltermwidget-*/* qmltermwidget

%build
qmake-qt5 \
	QMAKE_CFLAGS_RELEASE="%{rpmcflags} %{rpmcppflags}" \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags} %{rpmcppflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# qmltermwidget.pro installs QMLTermScrollbar.qml twice (assets + scrollbar) → parallel install races
%{__make} -j1 install \
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
