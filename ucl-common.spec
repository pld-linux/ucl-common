
# OBSOLETED by rat.spec, but may be needed again

Summary:	UCL Common Code Library
Summary(pl):	Biblioteka wspólnego kodu UCL
Name:		ucl-common
Version:	1.2.0
Release:	1
License:	custom
Group:		Libraries
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/common/common-%{version}.tar.gz
Patch0:		%{name}-time_h.patch
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Routines common to a number of multimedia tools. This library is
required to build RAT v3.2.7 or later, and may be needed for other UCL
tools.

%description -l pl
Procedury u¿ywane przez kilka narzêdzi multimedialnych. Biblioteka ta
jest wymagana do zbudowania RAT w. 3.2.7 lub nowsza i mo¿e byæ
potrzebna dla innych narzêdzi UCL.

%package devel
Summary:	Development part of UCL Common Code Library
Summary(pl):	Nag³ówki do biblioteki wspólnego kodu UCL
Group:		Development/Libraries

%description devel
Development part of UCL Common Code Library.

%description devel -l pl
Programistyczna czê¶æ biblioteki wspólnego kodu UCL.

%prep
%setup -qn common
%patch0 -p1

%build
%configure2_13 \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/ucl}
install libuclmmbase.a $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}/ucl
rm -f $RPM_BUILD_ROOT%{_includedir}/ucl/test*

gzip -9nf COPYRIGHT MODS README*

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYRIGHT* MODS* README*
%{_includedir}/ucl/*
%{_libdir}/*
