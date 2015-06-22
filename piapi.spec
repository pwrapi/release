Name:		piapi
Version:	2.0.1
Release:	1%{?dist}
Summary:	PowerInsight API communication and extensions

Group:		Development/Libraries
License:	GPLv2+
URL:		http://github.com/pwrapi/release
Source0:	piapi-%{version}.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
The PIAPI is a collection of services that allow remote gathering
of Penguin PowerInsight samples through the use of a one-to-one pairing
between a proxy running on the host and an agent running on the
embedded PowerInsight device.

%prep
%setup -q
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/*
%{_bindir}/*

# devel
%package devel
Summary: PowerInsight API devel package
Group: Development/Libraries
Requires:  piapi
BuildRequires: python-devel
BuildRequires: swig
%description devel
This is a development package of the PowerInsight API.
Users who want to implement their own plugins must install this
package.

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
#end devel


%package doc
Summary: Documentation files for %{name}
Group: Development/Libraries
%description doc
Examples and man for PowerInsight API.
%files doc
%defattr(-,root,root)
%{_mandir}/*/*
%{_datadir}/doc/*/*/*
%docdir %{_defaultdocdir}

%changelog

