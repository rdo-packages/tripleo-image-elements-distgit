
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-image-elements
Summary:	OpenStack TripleO Image Elements for diskimage-builder
Version:    12.0.2
Release:    1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	https://tarballs.openstack.org/tripleo-image-elements/tripleo-image-elements-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr
BuildRequires:  /usr/bin/pathfix.py

Requires:	diskimage-builder

%description
OpenStack TripleO Image Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images for the TripleO
program.

%prep
%setup -q -n tripleo-image-elements-%{upstream_version}

%build
%{py3_build}

%install
%{py3_install}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

# Fix shebangs for Python 3-only distros
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/tripleo-image-elements/os-svc-install/bin/map-services-tripleo

%files
%doc LICENSE
%doc README.rst
%doc AUTHORS
%doc ChangeLog
%{python3_sitelib}/tripleo_image_elements*
%{_datadir}/tripleo-image-elements

%changelog
* Mon Jun 14 2021 RDO <dev@lists.rdoproject.org> 12.0.2-1
- Update to 12.0.2

* Tue Jul 28 2020 RDO <dev@lists.rdoproject.org> 12.0.1-1
- Update to 12.0.1

* Tue May 26 2020 RDO <dev@lists.rdoproject.org> 12.0.0-1
- Update to 12.0.0

# REMOVEME: error caused by commit https://opendev.org/openstack/tripleo-image-elements/commit/78a9a1cf6e300ac356fecea8ef05e19b61cebf2e
