%global fontname lohit-devanagari
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.5.3
Release:        2%{?dist}
Summary:        Free Devanagari Script Font
Group:          User Interface/X
License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
This package provides a free Devanagari Script TrueType/OpenType font.

%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-0-lohit-devanagari.conf

%build
make %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}



%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README ChangeLog.old


%changelog
* Tue Mar 13 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-2
- Changed fontconf priority

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Nov 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-1
- Upstream release 2.5.2 and spec file cleanup

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-3
- Resoved bug #803308 and #799004

* Mon Apr 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Upstream new release with additional characters from Unicode 6.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Tue Jul 19 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- Resolved: bug 722382

* Wed Jun 22 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- Resolved: bug 715090, patch from Bernard Massot <bmassot@free.fr>

* Tue May 24 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- Resolved: bug 702058, patch from Bernard Massot <bmassot@free.fr>

* Fri Mar 25 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- Upstream release 2.4.5
- Removed hinting instructions bug 682667

* Fri Mar 25 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-4
- Resolved: bug 682667

* Mon Feb 21 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- resolved bug 648423 and bug 670467

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release 2.4.4

* Fri Nov 26 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-8
- added nepali local support
- resolved bugs 648434, 648429, 648424, 648362

* Fri Oct 08 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-7
- fixed bug 641297
- added rupee symbol

* Fri Apr 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-6
- fixed bug 578034

* Thu Feb 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- done changes as per review comments bug 559936 

* Fri Jan 29 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- first release
- decided to keep only one font for all languages using devanagari script
