# Created by pyp2rpm-3.3.2
%global pypi_name flake8-polyfill

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Polyfill package for Flake8 plugins

License:        MIT
URL:            https://gitlab.com/pycqa/flake8-polyfill
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(setuptools)

%description
 Polyfill for Flake8 Plugins flake8-polyfill is a package that provides some
compatibility helpers for Flake8 plugins that intend to support Flake8 2.x and
3.x simultaneously. Installation .. code-block:: bash pip install
flake8-polyfillOption Handling One problem area with compatibility with Flake8
2.x and 3.x is the registering options and receiving the parsed values.Flake8
3.0 added extra...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(flake8)
%description -n python3-%{pypi_name}
 Polyfill for Flake8 Plugins flake8-polyfill is a package that provides some
compatibility helpers for Flake8 plugins that intend to support Flake8 2.x and
3.x simultaneously. Installation .. code-block:: bash pip install
flake8-polyfillOption Handling One problem area with compatibility with Flake8
2.x and 3.x is the registering options and receiving the parsed values.Flake8
3.0 added extra...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/flake8_polyfill
%{python3_sitelib}/flake8_polyfill-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 1.0.2-1
- Initial package.