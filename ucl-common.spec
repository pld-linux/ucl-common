
# NOTE that rat.spec also contains ucl-common - sometimes older,
# sometimes newet than this spec

Summary:	UCL Common Code Library
Summary(pl):	Biblioteka wspólnego kodu UCL
Name:		ucl-common
Version:	1.2.14
Release:	1
License:	custom
Group:		Libraries
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/common/common-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-acfix.patch
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
Procedury u¿ywane przez kilka narzêdzi multimedialnych. Biblioteka ta
wywodzi siê z prac nad projektem RAT, ale jej czêsci nie s± zwi±zane
wy³±cznie z narzêdziami do d¼wiêku i mog± byæ przydatne do innych
celów.

%package devel
Summary:	Header files for UCL Common Code Library
Summary(pl):	Pliki nag³ówkowe do biblioteki wspólnego kodu UCL
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for UCL Common Code Library.

%description devel -l pl
Pliki nag³ówkowe biblioteki wspólnego kodu UCL.

%package static
Summary:	UCL Common Code static library
Summary(pl):	Statyczna biblioteka wspólnego kodu UCL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
UCL Common Code static library.

%description static -l pl
Statyczna biblioteka wspólnego kodu UCL.

%prep
%setup -qn common-%{version}
%patch0 -p1
%patch1 -p1

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
