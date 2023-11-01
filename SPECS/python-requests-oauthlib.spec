%global distname requests-oauthlib
%global modname requests_oauthlib

Name:               python-requests-oauthlib
Version:            1.3.0
Release:            12%{?dist}
Summary:            OAuthlib authentication support for Requests.

License:            ISC
URL:                http://pypi.python.org/pypi/requests-oauthlib
Source0:            https://github.com/requests/requests-oauthlib/archive/v%{version}.tar.gz
Patch0001:          401.patch
Patch0002:          0002-Don-t-use-SIGNATURE_RSA.patch

BuildArch:          noarch

%description
This project provides first-class OAuth library support for python-request.

%package -n python3-%{distname}
%{?python_provide:%python_provide python3-%{distname}}
Summary:            OAuthlib authentication support for Requests.

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

BuildRequires:      python3-oauthlib >= 0.6.2
BuildRequires:      python3-requests >= 2.0.0

Requires:           python3-oauthlib
Requires:           python3-requests

%description -n python3-%{distname}
This project provides first-class OAuth library support for python-request.

%prep
%autosetup -n %{distname}-%{version} -p1

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info


%build
%py3_build

%install
%py3_install

%files -n python3-%{distname}
%doc README.rst HISTORY.rst requirements.txt AUTHORS.rst
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.0-12
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Sat Jul  3 2021 Jakub Hrozek <jhrozek@redhat.com> - 1.3.0-11
- Don't use SIGNATURE_RSA
- Related: #1935433 - python-oauthlib implements and/or uses the deprecated
                      SHA1 algorithm by default

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.0-10
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb  8 2021 Jakub Hrozek <jhrozek@redhat.com> - 1.3.0-9
- Drop python2 support
- actually run unit tests
- drop unused python3-mock dependency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 27 2020 Kevin Fenzi <kevin@scrye.com> - 1.3.0-7
- Update to 1.3.0. Fixes bug #1769415

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 1.2.0-1
- Update to 1.2.0. Fixes bug #1697439

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018  <jdennis@redhat.com> - 1.0.0-1
- upgrade to new upstream release 1.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018  <jdennis@redhat.com> - 0.8.0-6
- Unify Fedora/RHEL py2/py3 logic

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 John Dennis <jdennis@redhat.com> - 0.8.0-2
- bring spec file for fedora & rhel closer together

* Sat Feb 25 2017 Kevin Fenzi <kevin@scrye.com> - 0.8.0-1
- Update to 0.8.0.
- Make sure to specify package versions required. Fixes bug #1320683

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 0.5.0-5
- Add an explicit python2 subpackage for #1313242.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- new version

* Fri Jan 23 2015 Ralph Bean <rbean@redhat.com> - 0.4.0-7
- Alter egg requirements for epel.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar  3 2014 Jakub Dorňák <jdornak@redhat.com> - 0.4.0-4
- python3 and python version related macros required to build
  python3- subpackage are not available in el6 and el7

* Fri Nov 29 2013 Jakub Dorňák <jdornak@redhat.com> - 0.4.0-3
- added python3 subpackage

* Fri Nov 01 2013 Ralph Bean <rbean@redhat.com> - 0.4.0-2
- Modernized the python2 rpm macros as per review feedback.

* Thu Oct 31 2013 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- Initial package for Fedora
