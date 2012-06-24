#
# NOTE: rat (rat.spec) also contains ucl-common code, sometimes newer
#       than released separately - so check for ucl-common updates
#       when updating rat
#
Summary:	UCL Common Code Library
Summary(pl):	Biblioteka wsp�lnego kodu UCL
Name:		ucl-common
%define	basever	1.2.14
Version:	1.2.16
Release:	4
License:	custom
Group:		Libraries
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/common/common-%{basever}.tar.gz
# Source0-md5:	73f6b1feb2e0223bfcc196657d1979c0
# update from rat-4.2.25
Patch0:		%{name}-%{version}.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-acfix.patch
Patch3:		%{name}-types.patch
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	/usr/include/ucl

%description
Routines common to a number of multimedia tools. The library
originates from work on the RAT project: these are portions that are
not directly related to an audio tool and potentially useful
elsewhere.

%description -l pl
Procedury u�ywane przez kilka narz�dzi multimedialnych. Biblioteka ta
wywodzi si� z prac nad projektem RAT, ale jej cz�ci nie s� zwi�zane
wy��cznie z narz�dziami do d�wi�ku i mog� by� przydatne do innych
cel�w.

%package devel
Summary:	Header files for UCL Common Code Library
Summary(pl):	Pliki nag��wkowe do biblioteki wsp�lnego kodu UCL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for UCL Common Code Library.

%description devel -l pl
Pliki nag��wkowe biblioteki wsp�lnego kodu UCL.

%package static
Summary:	UCL Common Code static library
Summary(pl):	Statyczna biblioteka wsp�lnego kodu UCL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
UCL Common Code static library.

%description static -l pl
Statyczna biblioteka wsp�lnego kodu UCL.

%prep
%setup -qn common-%{basever}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.* .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT
install src/{config_unix,config_win32,uclconf}.h \
	$RPM_BUILD_ROOT%{_includedir}

rm -rf doc/html/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT* MODS* README* src/README.qfdes
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
