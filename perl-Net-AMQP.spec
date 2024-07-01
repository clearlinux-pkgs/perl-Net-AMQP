#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : perl-Net-AMQP
Version  : 0.06
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHIPS/Net-AMQP-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHIPS/Net-AMQP-0.06.tar.gz
Summary  : 'Advanced Message Queue Protocol (de)serialization and representation'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Net-AMQP-license = %{version}-%{release}
Requires: perl-Net-AMQP-perl = %{version}-%{release}
Requires: perl(Data::Dumper)
Requires: perl(File::Path)
Requires: perl(File::Spec)
Requires: perl(Scalar::Util)
Requires: perl(XML::LibXML)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor)
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(XML::LibXML)
BuildRequires : perl(XML::SAX::Exception)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Net::AMQP - Advanced Message Queue Protocol (de)serialization and
representation

%package dev
Summary: dev components for the perl-Net-AMQP package.
Group: Development
Provides: perl-Net-AMQP-devel = %{version}-%{release}
Requires: perl-Net-AMQP = %{version}-%{release}

%description dev
dev components for the perl-Net-AMQP package.


%package license
Summary: license components for the perl-Net-AMQP package.
Group: Default

%description license
license components for the perl-Net-AMQP package.


%package perl
Summary: perl components for the perl-Net-AMQP package.
Group: Default
Requires: perl-Net-AMQP = %{version}-%{release}

%description perl
perl components for the perl-Net-AMQP package.


%prep
%setup -q -n Net-AMQP-0.06
cd %{_builddir}/Net-AMQP-0.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-AMQP
cp %{_builddir}/Net-AMQP-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-AMQP/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::AMQP.3
/usr/share/man/man3/Net::AMQP::Common.3
/usr/share/man/man3/Net::AMQP::Frame.3
/usr/share/man/man3/Net::AMQP::Frame::Body.3
/usr/share/man/man3/Net::AMQP::Frame::Header.3
/usr/share/man/man3/Net::AMQP::Frame::Heartbeat.3
/usr/share/man/man3/Net::AMQP::Frame::Method.3
/usr/share/man/man3/Net::AMQP::Frame::OOBBody.3
/usr/share/man/man3/Net::AMQP::Frame::OOBHeader.3
/usr/share/man/man3/Net::AMQP::Frame::OOBMethod.3
/usr/share/man/man3/Net::AMQP::Frame::Trace.3
/usr/share/man/man3/Net::AMQP::Protocol.3
/usr/share/man/man3/Net::AMQP::Protocol::Base.3
/usr/share/man/man3/Net::AMQP::Protocol::v0_8.3
/usr/share/man/man3/Net::AMQP::Value.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-AMQP/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
