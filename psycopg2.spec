#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6013BD3AFCF957DE (daniele.varrazzo@gmail.com)
#
Name     : psycopg2
Version  : 2.8.1
Release  : 53
URL      : https://files.pythonhosted.org/packages/52/be/f898e712f5f08131d651a62754fca82a1deb42e4e9889ad01932f770a2be/psycopg2-2.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/be/f898e712f5f08131d651a62754fca82a1deb42e4e9889ad01932f770a2be/psycopg2-2.8.1.tar.gz
Source99 : https://files.pythonhosted.org/packages/52/be/f898e712f5f08131d651a62754fca82a1deb42e4e9889ad01932f770a2be/psycopg2-2.8.1.tar.gz.asc
Summary  : psycopg2 - Python-PostgreSQL Database Adapter
Group    : Development/Tools
License  : LGPL-3.0 ZPL-2.0
Requires: psycopg2-license = %{version}-%{release}
Requires: psycopg2-python = %{version}-%{release}
Requires: psycopg2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : postgresql-dev
BuildRequires : python-dev
BuildRequires : python3-dev

%description
How to build psycopg documentation
----------------------------------
Building the documentation usually requires building the library too for
introspection, so you will need the same prerequisites_.  The only extra
prerequisite is virtualenv_: the packages needed to build the docs will be
installed when building the env.

%package license
Summary: license components for the psycopg2 package.
Group: Default

%description license
license components for the psycopg2 package.


%package python
Summary: python components for the psycopg2 package.
Group: Default
Requires: psycopg2-python3 = %{version}-%{release}

%description python
python components for the psycopg2 package.


%package python3
Summary: python3 components for the psycopg2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the psycopg2 package.


%prep
%setup -q -n psycopg2-2.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554647916
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/psycopg2
cp doc/COPYING.LESSER %{buildroot}/usr/share/package-licenses/psycopg2/doc_COPYING.LESSER
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/psycopg2/doc_COPYING.LESSER

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
