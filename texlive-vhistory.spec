# revision 30080
# category Package
# catalog-ctan /macros/latex/contrib/vhistory
# catalog-date 2013-04-21 16:55:16 +0200
# catalog-license lppl1.2
# catalog-version 1.6.1
Name:		texlive-vhistory
Version:	1.6.1
Release:	4
Summary:	Support for creating a change log
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vhistory
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vhistory.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vhistory.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/vhistory/sets.sty
%{_texmfdistdir}/tex/latex/vhistory/vhistory.sty
%doc %{_texmfdistdir}/doc/latex/vhistory/CHANGES
%doc %{_texmfdistdir}/doc/latex/vhistory/README
%doc %{_texmfdistdir}/doc/latex/vhistory/README.doc
%doc %{_texmfdistdir}/doc/latex/vhistory/de_beispiel.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/de_einleitung.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/de_sets.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/de_vhistory.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/en_example.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/en_introduction.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/en_sets.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/en_vhistory.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/hyperref.cfg
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_set_example.pdf
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_set_example.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_sets_de.pdf
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_sets_de.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_sets_en.pdf
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_sets_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
