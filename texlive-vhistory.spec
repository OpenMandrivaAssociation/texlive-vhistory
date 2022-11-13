Name:		texlive-vhistory
Version:	61719
Release:	1
Summary:	Support for creating a change log
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vhistory
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vhistory.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vhistory.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Vhistory simplifies the creation of a history of versions of a
document. You can easily extract information like the current
version of a list of authors from that history. It helps you to
get consistent documents. The package sets, which is used by
vhistory, allows you to use sets containing text. You can use
the usual operations to create the union of sets or the
intersection of sets etc.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vhistory
%doc %{_texmfdistdir}/doc/latex/vhistory

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
