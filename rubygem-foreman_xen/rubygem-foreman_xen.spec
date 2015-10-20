# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_xen

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    Provision and manage XEN Server from Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.1.5
Release:    1%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman-xen
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman-compute >= 1.8.1
Requires:   %{?scl_prefix}rubygem(deface) < 2.0.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-xen
Provides: foreman-xen

%description
This plugin enables provisioning and managing XEN Server in Foreman.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/lib
%{gem_instdir}/locale
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Mon Sep 21 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- update foreman_xen to 0.1.3 (kvedulv@kvedulv.de)

* Fri Jul 31 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- update foreman_xen to 0.1.2 (kvedulv@kvedulv.de)

* Wed May 27 2015 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- update foreman_xen to 0.1.1 (kvedulv@kvedulv.de)

* Wed May 20 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- update foreman_xen to 0.1.0 (kvedulv@kvedulv.de)

* Wed May 13 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- update foreman_xen to 0.0.6 (kvedulv@kvedulv.de)

* Fri Jan 02 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5.1-1
- Update foreman_xen to 0.0.5.1 (dcleal@redhat.com)

* Thu Dec 18 2014 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Update foreman_xen to 0.0.5 (dcleal@redhat.com)

* Fri Nov 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.4.1-1
- Update to 0.0.4.1 (dcleal@redhat.com)

* Wed Jul 02 2014 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- Update to 0.0.3 (dcleal@redhat.com)

* Mon Jun 16 2014 Dominic Cleal <dcleal@redhat.com> 0.0.2-1
- Update to 0.0.2 (dcleal@redhat.com)

* Wed May 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.1-1
- new package built with tito

