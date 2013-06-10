Summary:	LMN Domain Name Server Configuration Utilities
Name:		nsc
Version:	4.1
Release:	0
License:	GNU General Public License

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-build
Group:		System/Base
Vendor:		Lastminute.com
Requires:	bind-chroot, m4

%description
NSC is a set of shell and M4 scripts for easy maintenance of DNS zone
files and name server daemon configuration.  It has been designed to
make administration of a DNS server a piece of cake.

%prep
%{__mkdir} -p %{buildroot}/var/named/chroot
# The tar file is created from nsc git repository with command
#git archive --format=tar HEAD > SOURCES/nsc.tar
cd %{buildroot}/var/named/chroot
tar xf %{_sourcedir}/nsc.tar
rm -rf %{buildroot}/var/named/chroot/cf.* %{buildroot}/var/named/chroot/dist
rm -f %{buildroot}/var/named/chroot/custom.conf %{buildroot}/var/named/chroot/.gitignore

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

# List files owned by the package here.
%files
%defattr(-,root,root)
/var/named/chroot

%changelog
* Mon Jun 10 2013  Sami Kerola <sami.kerola@sabre.com>
- First version of this rpm, containing nsc-4.1
