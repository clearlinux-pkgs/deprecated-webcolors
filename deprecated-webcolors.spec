#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D9266A6808FE067 (james@b-list.org)
#
Name     : deprecated-webcolors
Version  : 1.8.1
Release  : 37
URL      : http://pypi.debian.net/webcolors/webcolors-1.8.1.tar.gz
Source0  : http://pypi.debian.net/webcolors/webcolors-1.8.1.tar.gz
Source99 : http://pypi.debian.net/webcolors/webcolors-1.8.1.tar.gz.asc
Summary  : A library for working with color names and color values formats defined by HTML and CSS.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: deprecated-webcolors-license = %{version}-%{release}
Requires: deprecated-webcolors-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3

%description
.. image:: https://travis-ci.org/ubernostrum/webcolors.svg?branch=master
:target: https://travis-ci.org/ubernostrum/webcolors

%package legacypython
Summary: legacypython components for the deprecated-webcolors package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-webcolors package.


%package license
Summary: license components for the deprecated-webcolors package.
Group: Default

%description license
license components for the deprecated-webcolors package.


%package python
Summary: python components for the deprecated-webcolors package.
Group: Default

%description python
python components for the deprecated-webcolors package.


%prep
%setup -q -n webcolors-1.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554330087
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-webcolors
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-webcolors/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-webcolors/LICENSE

%files python
%defattr(-,root,root,-)
