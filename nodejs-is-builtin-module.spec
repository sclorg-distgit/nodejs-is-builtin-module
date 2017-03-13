%{?scl:%scl_package nodejs-is-builtin-module}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-is-builtin-module

%global npm_name is-builtin-module
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-is-builtin-module
Version:	1.0.0
Release:	3%{?dist}
Summary:	Check if a string matches the name of a Node.js builtin module
Url:		https://github.com/sindresorhus/is-builtin-module
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(ava)
%endif

BuildRequires:	%{?scl_prefix}npm(builtin-modules)

Requires:	%{?scl_prefix}npm(builtin-modules)

%description
Check if a string matches the name of a Node.js builtin module

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
node test.js
%endif

%files
%{nodejs_sitelib}/is-builtin-module

%doc readme.md license

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- Rebuilt with updated metapackage

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- Initial build
