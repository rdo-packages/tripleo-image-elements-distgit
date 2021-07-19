%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x4c29ff0e437f3351fd82bdf47c5a3bc787dc7035

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-image-elements
Summary:	OpenStack TripleO Image Elements for diskimage-builder
Version:    13.1.2
Release:    1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	https://tarballs.openstack.org/tripleo-image-elements/tripleo-image-elements-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/tripleo-image-elements/tripleo-image-elements-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:	noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Mon Jul 19 2021 RDO <dev@lists.rdoproject.org> 13.1.2-1
- Update to 13.1.2

* Tue May 18 2021 RDO <dev@lists.rdoproject.org> 13.1.1-1
- Update to 13.1.1

* Thu May 06 2021 RDO <dev@lists.rdoproject.org> 13.1.0-1
- Update to 13.1.0

